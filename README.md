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


## Örnek Çıktılar
17 adet chunk indexlendi.
# Sor: Atatürk nerede doğdu
Atatürk'ün Hayatı
Mustafa Kemal Atatürk (1881-1938)
TÜRKİYE CUMHURİYETİ'NİN KURUCUSU VE İLK CUMHURBAŞKANI
ATATÜRK

Soyadı Kanunu gereğince, 24 Kasım 1934'de TBMM'nce Mustafa Kemal'e "Atatürk" soyadı verildi.

Mustafa Kemal Atatürk 1881 yılında Selânik'te Kocakasım Mahallesi, Islâhhâne Caddesi'ndeki üç katlı pembe evde
doğdu. Babası Ali Rıza Efendi, annesi Zübeyde Hanım'dır. Baba tarafından dedesi Hafız Ahmet Efendi XIV-XV.
yüzyıllarda Konya ve Aydın'dan Makedonya'ya yerleştirilmiş Kocacık Yörüklerindendir. Annesi Zübeyde Hanım
ise Selânik yakınlarındaki Langaza kasabasına yerleşmiş eski bir Türk ailesinin kızıdır. Milis subaylığı, evkaf katipliği
ve kereste ticareti yapan Ali Rıza Efendi, 1871 yılında Zübeyde Hanım'la evlendi. Atatürk'ün beş kardeşinden dördü
küçük yaşlarda öldü, sadece Makbule (Atadan) 1956 yılına değin yaşadı.

*Cevap: Atatürk, Selânik'te Kocakasım Mahallesi, Islâhhâne Caddesi'ndeki üç katlı pembe evde doğdu.*

# Sor: Mareşal ünvanı ne zaman verildi
Mustafa Kemal yönetimindeki Türk Kurtuluş Savaşının önemli aşamaları şunlardır:
Sarıkamış (20 Eylül 1920), Kars (30 Ekim 1920) ve Gümrü'nün (7 Kasım 1920) kurtarılışı.
Çukurova, Gazi Antep, Kahraman Maraş Şanlı Urfa savunmaları (1919- 1921)
I. İnönü Zaferi (6 -10 Ocak 1921)
II. İnönü Zaferi (23 Mart-1 Nisan 1921)
Sakarya Zaferi (23 Ağustos-13 Eylül 1921)
Büyük Taarruz, Başkomutan Meydan Muhaberesi ve Büyük Zafer (26 Ağustos 9 Eylül 1922)

Sakarya Zaferinden sonra 19 Eylül 1921'de Türkiye Büyük Millet Meclisi Mustafa Kemal'e Mareşal rütbesi ve Gazi
unvanını verdi. Kurtuluş Savaşı, 24 Temmuz 1923'te imzalanan Lozan Antlaşması'yla sonuçlandı. Böylece Sevr
Antlaşması'yla paramparça edilen, Türklere 5-6 il büyüklüğünde vatan bırakılan Türkiye toprakları üzerinde ulusal
birliğe dayalı yeni Türk devletinin kurulması için hiçbir engel kalmadı.

Mustafa Kemal Atatürk 1881 yılında Selânik'te Kocakasım Mahallesi, Islâhhâne Caddesi'ndeki üç katlı pembe evde
doğdu. Babası Ali Rıza Efendi, annesi Zübeyde Hanım'dır. Baba tarafından dedesi Hafız Ahmet Efendi XIV-XV.
yüzyıllarda Konya ve Aydın'dan Makedonya'ya yerleştirilmiş Kocacık Yörüklerindendir. Annesi Zübeyde Hanım
ise Selânik yakınlarındaki Langaza kasabasına yerleşmiş eski bir Türk ailesinin kızıdır. Milis subaylığı, evkaf katipliği
ve kereste ticareti yapan Ali Rıza Efendi, 1871 yılında Zübeyde Hanım'la evlendi. Atatürk'ün beş kardeşinden dördü
küçük yaşlarda öldü, sadece Makbule (Atadan) 1956 yılına değin yaşadı.

*Cevap: 19 Eylül 1921'de verildi.*

# Sor: Atatürk hangi yıl uzaya çıktı
Atatürk'ün Hayatı
Mustafa Kemal Atatürk (1881-1938)
TÜRKİYE CUMHURİYETİ'NİN KURUCUSU VE İLK CUMHURBAŞKANI
ATATÜRK

Atatürk, 24 Nisan 1920 ve 13 Ağustos 1923 tarihlerinde TBMM Başkanlığına seçildi. Bu başkanlık görevi, DevletHükümet Başkanlığı düzeyindeydi. 29 Ekim 1923 yılında Cumhuriyet ilan edildi ve Atatürk ilk cumhurbaşkanı seçildi.
Anayasa gereğince dört yılda bir cumhurbaşkanlığı seçimleri yenilendi. 1927,1931, 1935 yıllarında TBMM Atatürk'ü
yeniden cumhurbaşkanlığına seçti.
Atatürk sık sık yurt gezilerine çıkarak devlet çalışmalarını yerinde denetledi. İlgililere aksayan yönlerle ilgili emirler
verdi. Cumhurbaşkanı sıfatıyla Türkiye'yi ziyaret eden yabancı ülke devlet başkanlarını, başbakanlarını, bakanlarını
komutanlarını ağırladı.
15-20 Ekim 1927 tarihinde Kurtuluş Savaşı'nı ve Cumhuriyet'in kuruluşunu anlatan büyük nutkunu, 29 Ekim 1933
tarihinde de 10. Yıl Nutku'nu okudu.
Atatürk özel yaşamında sadelik içinde yaşadı. 29 Ocak 1923'de Latife Hanımla evlendi. Birçok yurt gezisine birlikte
çıktılar. Bu evlilik 5 Ağustos 1925 tarihine dek sürdü. Çocukları çok seven Atatürk Afet (İnan), Sabiha (Gökçen),
Fikriye, Ülkü, Nebile, Rukiye, Zehra adlı kızları ve Mustafa adlı çobanı manevi evlat edindi. Abdurrahim ve İhsan adlı
çocukları himayesine aldı. Yaşayanlarına iyi bir gelecek hazırladı.

Atatürk Türkiye'yi "Çağdaş uygarlık düzeyine çıkarmak" amacıyla bir dizi devrim
yaptı. Bu devrimleri beş başlık altında toplayabiliriz:
1. Siyasal Devrimler:
· Saltanatın Kaldırılması (1 Kasım 1922)
· Cumhuriyetin İlanı (29 Ekim 1923)
· Halifeliğin Kaldırılması (3 Mart 1924)
2. Toplumsal Devrimler:
· Kadınlara erkeklerle eşit haklar verilmesi (1926-1934)
· Şapka ve kıyafet devrimi (25 Kasım 1925)
· Tekke zâviye ve türbelerin kapatılması (30 Kasım 1925)
· Soyadı kanunu ( 21 Haziran 1934)
· Lâkap ve unvanların kaldırılması (26 Kasım 1934)
· Uluslararası saat, takvim ve uzunluk ölçülerin kabulü (1925-1931)
3. Hukuk Devrimi:
· Mecellenin kaldırılması (1924-1937)
· Türk Medeni Kanunu ve diğer kanunların çıkarılarak laik hukuk düzenine geçilmesi (1924-1937)
4. Eğitim ve Kültür Alanındaki Devrimler:
· Öğretimin birleştirilmesi (3 Mart 1924)
· Yeni Türk harflerinin kabulü (1 Kasım 1928)
· Türk Dil ve Tarih Kurumlarının kurulması (1931-1932)
· Üniversite öğreniminin düzenlenmesi (31 Mayıs 1933)
· Güzel sanatlarda yenilikler
5. Ekonomi Alanında Devrimler:
· Aşârın kaldırılması
· Çiftçinin özendirilmesi
· Örnek çiftliklerin kurulması
· Sanayiyi Teşvik Kanunu'nun çıkarılarak sanayi kuruluşlarının kurulması
· I. ve II. Kalkınma Planları'nın (1933-1937) uygulamaya konulması, yurdun yeni yollarla donatılması

*Cevap: Bilmiyorum*

