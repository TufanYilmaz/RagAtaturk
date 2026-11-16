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
for file in Path("Kaynaklar").glob("*.txt"):
    chunks+=[p.strip() for p in file.read_text(encoding="utf-8").split("\n\n") if p.strip()]

chunk_vectors = embed(chunks)
print(f"{len(chunks)} adet chunk indexlendi.")