# URL Shortener API Dokümantasyonu

## Proje Tanıtımı
Bu proje, kullanıcılardan alınan uzun URL'leri kısaltarak kolay kullanılabilir hale getiren bir RESTful API'dir. Kısaltılmış URL, kullanıcı tarafından kullanıldığında orijinal URL'ye otomatik olarak yönlendirme yapar.

---

## Teknoloji ve Araçlar
- **Programlama Dili:** Python
- **Framework:** Flask
- **Veritabanı:** SQLite
- **Sunucu:** Flask yerel geliştirme sunucusu
- **JSON Formatı:** API istek ve yanıtlarında JSON kullanılır.
- **Araçlar:** Postman (test için)

---

## Kurulum Talimatları

### 1. Gerekli Araçları Kur
Proje için aşağıdaki paketleri yükle:
```bash
pip install flask sqlite3
```

### 2. Proje Yapısı
Proje dizini aşağıdaki gibi olmalıdır:
```
url_shortener/
|-- app.py          # API uygulaması
|-- db.sqlite       # SQLite veritabanı dosyası
```

### 3. Sunucuyu Başlat
Projeyi yerel ortamda çalıştırmak için aşağıdaki komutu kullan:
```bash
python app.py
```
Sunucu, **http://localhost:5000** adresinde çalışır.

---

## API Endpointleri

### 1. **URL Kısaltma**

- **Yöntem:** POST  
- **URL:** `/shorten`  
- **Açıklama:** Uzun bir URL'yi alır ve benzersiz bir kısa ID oluşturarak veritabanına kaydeder. Oluşturulan kısa URL'yi geri döner.

#### İstek
- **Header:** `Content-Type: application/json`
- **Body:**
```json
{
  "url": "https://www.ornek.com/uzun-link"
}
```

#### Yanıt
- **Status Code:** 201
- **Body:**
```json
{
  "short_url": "http://localhost:5000/abc123"
}
```

#### Hata Durumları
- **Eksik URL:**
```json
{
  "error": "URL is required"
}
```
- **Status Code:** 400

---

### 2. **Yönlendirme**

- **Yöntem:** GET  
- **URL:** `/<short_id>`  
- **Açıklama:** Kısaltılmış bir URL ile istekte bulunulduğunda, kullanıcıyı orijinal URL'ye yönlendirir.

#### Örnek
**İstek:**
```
GET http://localhost:5000/abc123
```

**Sonuç:** Kullanıcı tarayıcısında orijinal URL'ye yönlendirilir.

#### Hata Durumları
- **Geçersiz ID:**
```json
{
  "error": "Short URL not found"
}
```
- **Status Code:** 404

---

## Veritabanı Tasarımı
**Tablo Adı:** `urls`
| Alan Adı      | Veri Tipi    | Açıklama                 |
|------------------|-------------|---------------------------|
| id               | INTEGER     | Otomatik artan birincil anahtar |
| short_id         | TEXT UNIQUE | Benzersiz kısa ID          |
| original_url     | TEXT        | Orijinal uzun URL          |

---

## Çalışma Mantığı
1. Kullanıcı **POST /shorten** endpoint'ine uzun URL'yi gönderir.
2. Sistem, rastgele bir **short_id** (6 karakter) oluşturur.
3. Oluşturulan **short_id** ve orijinal URL veritabanına kaydedilir.
4. Kullanıcıya kısaltılmış URL dönülür.
5. Kullanıcı **GET /<short_id>** ile kısaltılmış URL'ye ulaştığında orijinal URL'ye yönlendirilir.

---

## API Testleri
API'yi Postman veya cURL ile test edebilirsin.

### 1. **URL Kısaltma Testi**
```bash
curl -X POST http://localhost:5000/shorten \
-H "Content-Type: application/json" \
-d '{"url": "https://www.ornek.com/uzun-link"}'
```

### 2. **Yönlendirme Testi**
```bash
curl -i http://localhost:5000/abc123
```

---

## Geliştirme Önerileri
- **Validasyon:** Girilen URL formatını kontrol et (regex kullanarak).
- **Kısa ID Çakışma Kontrolü:** Aynı ID'nin oluşmamasını sağla.
- **Rate Limiting:** Kullanıcı başına saniye başına istek sayısını sınırla.
- **Veritabanı:** SQLite yerine PostgreSQL gibi daha performanslı bir veritabanı kullanabilirsin.
- **Caching:** Yönlendirme işleminde Redis kullanarak süreyi hızlandırabilirsin.

---

## İletışim
Sorular veya geliştirme için benimle iletişime geçebilirsin. 😊

