import requests
import numpy as np
from pathlib import Path

OLLAMA = "http://localhost:11434"
EMBED_MODEL = "nomic-embed-text"
CHAT_MODEL= "qwen3:4b-instruct"


def embed(texts):
    r=requests.post(f"{OLLAMA}/api/embed",json={"model":EMBED_MODEL,"input":texts})
    return np.array(r.json()["embeddings"])

def ask_llm(prompt):
    r=requests.post(f"{OLLAMA}/api/chat",json={
        "model":CHAT_MODEL,
        "stream":False,
        "messages": [{"role":"user","content":prompt}],
    })
    return r.json()["message"]["content"]

#print(ask_llm("Türkiyenin başkenti neresi"))

chunks=[]
source_files = Path("Kaynaklar")
for file in [*source_files.glob("*.txt"), *source_files.glob("*.md")]:
    chunks+=[p.strip() for p in file.read_text(encoding="utf-8").split("\n\n") if p.strip()]

chunk_vectors = embed(chunks)
print(f"{len(chunks)} adet chunk indexlendi.")

def retrive(question,k=3):
    q=embed([question])[0]
    scores = chunk_vectors @ q / (np.linalg.norm(chunk_vectors,axis=1) * np.linalg.norm(q))
    return [chunks[i] for i in np.argsort(scores)[::-1][:k]]

while True:
    question = input("Sor: ")
    context ="\n\n".join(retrive(question))
    print(context)
    promt = f"""Bu sorulara SADECE aşağıdaki context'i kullanarak cevap ver 
eğer cevap context içinde değilse "Bilmiyorum" olarak cevap ver

Context:
{context}
Question:
{question}"""
    print("\n Cevap: " + ask_llm(promt) +"\n")