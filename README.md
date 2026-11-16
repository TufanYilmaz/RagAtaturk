# RagAtaturk

Atatürk'ün hayatı ve ilgili kaynaklar üzerine geliştirilmiş basit bir RAG (Retrieval-Augmented Generation) projesi. `Kaynaklar/` klasöründeki metinleri vektörleştirerek Ollama üzerinden ilgili soru-cevap işlemlerini gerçekleştirir.

---

## 📋 Gereksinimler

- **Python** (>= 3.10)
- **UV** paket yöneticisi
- **Ollama** (Yerel LLM ve embedding modellerini çalıştırmak için)

---

## 🚀 Kurulum

### 1. Bağımlılıkların Yüklenmesi

Projeyi klonladıktan sonra gerekli Python kütüphanelerini `uv` ile yükleyin:

```bash
uv add requests numpy
```

*(Alternatif olarak mevcut ortamı senkronize etmek için `uv sync` komutunu da kullanabilirsiniz.)*

### 2. Ollama ve Modellerin Hazırlanması

Ollama'nın sisteminizde kurulu ve çalışır durumda olduğundan emin olun. Projede kullanılan modelleri terminalden indirin:

```bash
# Embedding modeli
ollama pull nomic-embed-text

# LLM Sohbet modeli
ollama pull qwen3:4b-instruct
```

---

## ▶️ Çalıştırma

Ollama servisinin çalıştığından emin olduktan sonra projeyi aşağıdaki komutla başlatabilirsiniz:

```bash
uv run python rag.py
```

Uygulama başladığında `Kaynaklar/` dizinindeki metinler indekslenecek ve terminal üzerinden sorularınızı yöneltebileceğiniz bir komut satırı açılacaktır.
