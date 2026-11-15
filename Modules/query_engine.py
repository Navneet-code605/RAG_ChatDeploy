import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from sentence_transformers import SentenceTransformer
import faiss
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from langdetect import detect

# ✅ Load embedding model once
embedder = SentenceTransformer("sentence-transformers/LaBSE")

# ✅ Load Qwen model + tokenizer once
llm_model = "Qwen/Qwen2.5-0.5B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(llm_model, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    llm_model,
    torch_dtype=torch.float16,   # lighter memory footprint
    device_map="cpu",            # runs on CPU (safe for low VRAM)
    trust_remote_code=True
)

def query_engine(query, index, texts, preferred_lang=None):
    # Step 1: Encode query
    query_vec = embedder.encode([query])

    # Step 2: Retrieve top-k chunks (limit to 1 for concise answers)
    D, I = index.search(query_vec, k=1)
    retrieved_chunks = [texts[i] for i in I[0]]

    # Step 3: Detect language if not provided
    user_lang = preferred_lang if preferred_lang else detect(query)

    # Step 4: Construct multilingual prompt with concise instruction
    context = "\n".join(retrieved_chunks)
    prompt = (
        f"Answer in {user_lang}. Keep the answer concise (3-4 sentences). "
        f"Use only this context:\n{context}\n\n"
        f"Question: {query}\nAnswer:"
    )

    # Step 5: Generate shorter answer
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=100, temperature=0.7)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return answer


# ✅ Test block
if __name__ == "__main__":
    from Modules.index_builder import build_index

    # Build FAISS index from all chunks
    index, texts = build_index("Data")

    # Interactive loop
    preferred_lang = input("Enter your preferred language (or press Enter for auto-detect): ")
    while True:
        query = input("Ask a question (or type 'exit'): ")
        if query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        answer = query_engine(query, index, texts, preferred_lang=preferred_lang if preferred_lang else None)
        print("Answer:\n", answer)
