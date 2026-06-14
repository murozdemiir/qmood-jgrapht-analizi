# JGraphT 0.9.0 → 0.9.2 – Tasarım Metrik Değişim Analizi

**Analiz Edilen Sürümler:** 0.9.0 → 0.9.2  
**Metrik Modeli:** QMOOD (Bansiya & Davis 2002)  
**Analiz Tarihi:** 2026-06-14

---

## 1. GENEL DEĞİŞİM ÖZETİ

| Metrik Kategorisi | Ortalama Değişim | Yön |
|-------------------|------------------|-----|
| Boyut ve Hiyerarşi (DSC, NOH) | +%11.8 | ⬆️ Büyüme |
| Soyutlama ve Kapsülleme (ANA, DAM) | +%4.0 | ⬆️ İyileşme |
| Bağımlılık ve Uyum (DCC, CAM) | -%2.1 | ⚠️ Karışık |
| Kompozisyon ve Kalıtım (MOA, MFA) | +%9.2 | ⬆️ İyileşme |
| Polimorfizm ve Mesajlaşma (NOP, CIS) | -%1.4 | ➡️ Durağan |
| Karmaşıklık (NOM) | +%1.6 | ⬆️ Hafif artış |

📌 **İlk İzlenim:**  
0.9.0 → 0.9.2 arasında sistem **%12 oranında büyümüş** (29 yeni sınıf). Soyutlama, kompozisyon ve kalıtım metrikleri iyileşmiş, ancak **uyum (cohesion) düşüşü** ve **coupling'deki hafif artış** dikkat çekicidir.

---

## 2. METRİK BAZLI DETAYLI YORUM

### ✅ Olumlu Değişimler (3 metrik)

| Metrik | 0.9.0 | 0.9.2 | Değişim | Yorum |
|--------|-------|-------|---------|-------|
| **ANA (Soyutlama)** | 0.6176 | 0.6704 | **+%8.5** | Kalıtım hiyerarşisi derinleşmiş. DIT_mean 0.6176 → 0.6704, sınıflar daha iyi soyutlanmış. |
| **MOA (Kompozisyon)** | 0.3739 | 0.4045 | **+%8.2** | Nesne kompozisyonu artmış – “favor composition” prensibine uyum iyileşmiş. |
| **MFA (Kalıtım)** | 0.2469 | 0.2721 | **+%10.2** | Kalıtım mekanizmaları daha fazla kullanılmaya başlanmış. |

**Olumlu Yorum:**  
Bu üç metrikteki iyileşme, geliştiricilerin **soyutlama ve nesne ilişkileri konusunda bilinçli çalıştığını** gösterir. ANA (+%8.5) ve MFA (+%10.2) birlikte arttığı için kalıtım hiyerarşisi hem derinleşmiş hem de daha etkin kullanılmıştır.

---

### ⚠️ Olumsuz / Riskli Değişimler (2 metrik)

| Metrik | 0.9.0 | 0.9.2 | Değişim | Yorum |
|--------|-------|-------|---------|-------|
| **CAM (Uyum/Cohesion)** | 0.4070 | 0.3874 | **-%4.8** | Sınıfların iç tutarlılığı azalmış. Metotlar daha dağınık sorumluluklara sahip olmaya başlamış. |
| **DCC (Coupling)** | 2.3487 | 2.3633 | **+%0.6** | Sınıflar arası bağımlılık hafif artmış. Küçük ama yön olarak olumsuz. |

**Olumsuz Yorum:**  
CAM'daki **-%4.8** düşüş, 0.9.0'daki zaten orta seviyedeki uyumun (0.407) daha da bozulduğunu gösterir. Yeni eklenen 29 sınıf, mevcut sınıflarla yeterince uyumlu tasarlanmamış olabilir. DCC'deki +%0.6 artış küçük olsa da, **artan sınıf sayısıyla birlikte coupling'in azalması gerekirken artması** olumsuz bir sinyaldir.

---

### ➡️ Nötr / Durağan Değişimler (4 metrik)

| Metrik | 0.9.0 | 0.9.2 | Değişim | Yorum |
|--------|-------|-------|---------|-------|
| **NOP (Polimorfizm)** | 3.2731 | 3.1910 | -%2.5 | Hafif düşüş, istatistiksel olarak anlamlı olmayabilir. |
| **CIS (Mesajlaşma)** | 3.9202 | 3.9139 | -%0.2 | Neredeyse sabit. |
| **NOM (Karmaşıklık)** | 5.1555 | 5.2397 | +%1.6 | Sınıf başına metot sayısı 5.16 → 5.24, önemsiz artış. |
| **DAM (Kapsülleme)** | 0.8990 | 0.8936 | -%0.6 | İhmal edilebilir düşüş, kapsülleme hala çok iyi seviyede (>0.89). |

**Nötr Yorum:**  
Bu metriklerdeki değişimler **%3'ün altında** olduğu için anlamlı bir yorum yapmak zordur. NOP ve CIS'in neredeyse sabit kalması, polimorfizm ve mesajlaşma kalıplarında büyük bir değişiklik yapılmadığını gösterir.

---

## 3. SİSTEM BOYUTU VE BÜYÜME ANALİZİ

| Metrik | 0.9.0 | 0.9.2 | Mutlak Artış | Büyüme Oranı |
|--------|-------|-------|--------------|--------------|
| DSC (Sınıf Sayısı) | 238 | 267 | **+29** | +%12.2 |
| NOH (Hiyerarşi Kökü Sayısı) | 35 | 39 | **+4** | +%11.4 |

**Yorum:**  
Sistem **tek sürümde %12 büyümüş**. Bu hızla büyüyen bir kod tabanında:
- CAM düşüşü **uyum sorunlarını büyütebilir**
- DCC artışı **bağımlılık yönetimini zorlaştırabilir**

> Büyüme hızı (%12) ile uyum düşüşü (-%4.8) arasında **negatif bir korelasyon** vardır. Yeni sınıflar mevcut sınıflarla yeterince uyumlu değildir.

---

## 4. KALİTE AÇISINDAN DEĞERLENDİRME

### Olumlu Kalite Etkileri:

| Etki | Açıklama | Kanıt |
|------|----------|-------|
| Daha iyi soyutlama | Kalıtım hiyerarşisi derinleşmiş, tasarım daha esnek hale gelmiş | ANA +%8.5, MFA +%10.2 |
| Daha fazla kompozisyon | Nesne birleştirme artmış, kod tekrarı azalmış olabilir | MOA +%8.2 |

### Olumsuz Kalite Etkileri:

| Etki | Açıklama | Kanıt |
|------|----------|-------|
| Uyum kaybı | Sınıflar daha az odaklı hale gelmiş – Single Responsibility ihlali riski | CAM -%4.8 |
| Artan bağımlılık | Değişimlerin yan etkisi artabilir – test ve bakım zorlaşır | DCC +%0.6 (küçük ama yön olarak kötü) |

### Genel Kalite Kararı:

| Boyut | Değerlendirme |
|-------|---------------|
| Mimari Sağlık | **Olumlu** – Soyutlama ve kompozisyon iyileşmiş |
| Bakım Kolaylığı | **Olumsuza yakın** – Uyum düşüşü ve coupling artışı endişe verici |
| Sürdürülebilirlik | **Karışık** – İyi soyutlama var ama uyum problemi büyüyor |

📌 **Nihai Karar:**  
0.9.0 → 0.9.2, **kısmen olumlu** bir sürümdür. Soyutlama ve kompozisyon iyileşmiş, ancak uyum kaybı ve coupling artışı **ileride sorun çıkarabilecek sinyallerdir**. Bu hızda büyümeye devam edilirse, CAM düşüşü ciddi bir teknik borç haline gelebilir.

---

## 5. TEKNİK BORÇ İŞARETLERİ

### 🟡 Zayıf İşaretler (Erken Uyarı)

| İşaret | Şiddet | Açıklama |
|--------|--------|----------|
| CAM -%4.8 | Orta | Uyum kaybı erken teknik borç belirtisidir. Şimdiden müdahale edilmezse ileride büyür. |
| DCC +%0.6 | Zayıf | Küçük ama sistem büyüdükçe coupling doğal olarak azalması gerekirken artması alışılmadık. |

### 🟢 Teknik Borç Olmayan Durumlar

| Metrik | Neden Borç Sayılmaz |
|--------|---------------------|
| NOP -%2.5 | Değişim çok küçük, istatistiksel gürültü olabilir |
| DAM -%0.6 | Kapsülleme hala çok iyi (>0.89) |
| ANA +%8.5 | İyileşme var, borç azalmış |

### Teknik Borç Değerlendirmesi:

| Seviye | Derece |
|--------|--------|
| Mevcut Teknik Borç | **Düşük** |
| Borç Birikim Hızı | **Orta** (CAM düşüşü hızlı) |
| Acil Müdahale Gerekiyor mu? | **Hayır** – ancak CAM trendi izlenmeli |

> **Uyarı:** Bu sürümde teknik borç **kritik seviyede değildir** ancak CAM'daki -%4.8 düşüş, bir sonraki sürümde de devam ederse **ciddi bir sorun haline gelebilir**.

---

## 6. ÖNERİLER (Metrik Bazlı)

### Öneri 1 – CAM düşüşünü tersine çevir

**Hedef:** 0.9.2'de 0.387'ye düşen CAM, 0.9.3'te >0.41'e çıkarılmalıdır.

**Aksiyon:**  
- Yeni eklenen 29 sınıfın sorumluluklarını gözden geçirin
- Tek sorumluluk prensibini ihlal eden sınıfları bölün
- Mevcut sınıflarla yeni sınıflar arasındaki işlevsel örtüşmeleri azaltın

### Öneri 2 – DCC artışını durdur

**Hedef:** DCC 2.363'ün altına çekilmeli (tercihen 2.30)

**Aksiyon:**  
- Yeni eklenen sınıfların bağımlılık grafiğini analiz edin
- Gereksiz doğrudan bağımlılıkları arayüzlerle soyutlayın
- Dependency Inversion Principle uygulayın

---

## 7. ÖZET TABLO

| Değerlendirme Alanı | Sonuç | Destekleyen Metrik(ler) |
|---------------------|-------|--------------------------|
| En İyi Değişim | ✅ Soyutlama iyileşti | ANA +%8.5, MFA +%10.2 |
| En Kötü Değişim | ⚠️ Uyum bozuldu | CAM -%4.8 |
| Teknik Borç Varlığı | 🟡 Düşük seviyede | CAM, DCC |
| Genel Sürüm Değerlendirmesi | 🟢 **Kısmen Olumlu** | 3 olumlu, 2 olumsuz, 4 nötr değişim |
| İleride Risk | 🔴 Orta – CAM düşüş trendi devam ederse | CAM -%4.8 |

---

## 8. SONUÇ

**JGraphT 0.9.0 → 0.9.2 sürüm farkının kalite değerlendirmesi:**

- **Olumlu yönler:** Soyutlama seviyesi (%8.5), kompozisyon kullanımı (%8.2) ve kalıtım mekanizmaları (%10.2) iyileşmiştir. Geliştiriciler nesne yönelimli tasarım prensiplerine uygun çalışmaktadır.

- **Olumsuz yönler:** Sınıfların iç uyumu (cohesion) %4.8 oranında düşmüş ve sınıflar arası bağımlılık (coupling) artmıştır. 29 yeni sınıf eklenirken uyumun korunamaması endişe vericidir.

- **Teknik borç:** Düşük seviyede teknik borç birikimi vardır. CAM'daki düşüş en belirgin işarettir. Şu an kritik değildir ancak trend devam ederse ilerleyen sürümlerde sorun olabilir.

- **Genel karar:** Bu sürüm **kısmen başarılıdır**. Ancak CAM düşüşüne dikkat edilmeli ve bir sonraki sürümde tersine çevrilmelidir.

---

*Rapor: QMOOD Modeli (Bansiya & Davis 2002) temellidir. Tüm iddialar verilen metrik değerleriyle sayısal olarak kanıtlanmıştır.*

**Analiz Tarihi:** 2026-06-14  
**Uzman:** Kıdemli Yazılım Mimarisi ve Kalite Uzmanı