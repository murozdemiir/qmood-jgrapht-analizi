# JGraphT 0.9.0 → 0.9.2 — Sürüm Farkı Analizi

> **Kapsam:** jgrapht-core, iki sürüm arası tasarım metriği karşılaştırması  
> **Metodoloji:** QMOOD (Bansiya & Davis, 2002)  
> **Kural:** Her iddia sayısal kanıta dayandırılmıştır.

---

## 1. Metrik Değişimlerinin Özeti

| Metrik | 0.9.0 | 0.9.2 | Değişim | Yön |
|--------|-------|-------|---------|-----|
| DSC (boyut) | 238.000 | 267.000 | **+12.2 %** | Büyüme |
| NOH (hiyerarşi) | 35.000 | 39.000 | **+11.4 %** | Büyüme |
| ANA (soyutlama) | 0.6176 | 0.6704 | **+8.5 %** | ✅ Olumlu |
| DAM (kapsülleme) | 0.8990 | 0.8936 | −0.6 % | ➡ Sabit |
| DCC (coupling) | 2.3487 | 2.3633 | +0.6 % | ➡ Sabit |
| CAM (uyum) | 0.4070 | 0.3874 | **−4.8 %** | ⚠️ Dikkat |
| MOA (kompozisyon) | 0.3739 | 0.4045 | **+8.2 %** | ✅ Olumlu |
| MFA (kalıtım) | 0.2469 | 0.2721 | **+10.2 %** | ✅ Olumlu |
| NOP (polimorfizm) | 3.2731 | 3.1910 | −2.5 % | ➡ Hafif düşüş |
| CIS (arayüz) | 3.9202 | 3.9139 | −0.2 % | ➡ Sabit |
| NOM (karmaşıklık) | 5.1555 | 5.2397 | +1.6 % | ➡ Sabit |

---

## 2. Kalite Nitelikleri — Normalize Karşılaştırma (0.9.0 = 1.00 referans)

| Nitelik | 0.9.0 | 0.9.2 | Δ (normalize) | Yön |
|---------|-------|-------|---------------|-----|
| Reusability | 120.475 | 134.963 | **+12.0 % (+4.65 %n)** | ✅ |
| Flexibility | 1.461 | 1.430 | −2.1 % | ⚠️ Hafif gerileme |
| Understandability | −81.869 | −91.471 | **−11.7 % (kötüleşme)** | ❌ |
| Functionality | 61.691 | 68.930 | **+11.7 %** | ✅ |
| Extendibility | 0.894 | 0.885 | −1.0 % | ➡ Sabit |
| Effectiveness | 1.082 | 1.086 | +0.4 % | ➡ Sabit |

---

## 3. Metrik Değişimlerinin Yorumu

### 3.1 Olumlu Sinyaller

**ANA (soyutlama): +8.5 %** — 0.617 → 0.670  
Yeni eklenen 29 sınıfın (238 → 267) önemli bir bölümü soyut sınıf veya arayüz olarak tasarlanmıştır. Bu, genişletilecek sözleşme noktalarının arttığına ve mimarinin soyutlama katmanını güçlendirdiğine işaret eder. Extendibility ve Effectiveness formüllerinde olumlu katkı sağlar.

**MOA (kompozisyon): +8.2 %** — 0.374 → 0.405  
Sınıfların veri alanı olarak başka sınıf örnekleri tutma oranı artmıştır. Bileşim (composition over inheritance) tercihinin güçlendiği, esneklik açısından olumlu bir tasarım kararıdır. Flexibility formülüne doğrudan pozitif katkı verir.

**MFA (kalıtım faktörü): +10.2 %** — 0.247 → 0.272  
Üst sınıflardan miras alınan metotların oranı artmıştır. Bu, yeni sınıfların mevcut hiyerarşilere entegre edildiğini; rastgele somut sınıf eklenmediğini göstermektedir. NOH'un da +11.4 % artması bu yorumu destekliyor: hiyerarşiler hem daha fazla hem de daha derin/geniş kullanılıyor.

**NOH (hiyerarşi): +11.4 %** — 35 → 39  
DSC +12.2 %, NOH +11.4 % ile neredeyse eş oranda büyümüştür. Yeni sınıfların hiyerarşi dışında değil, mevcut kalıtım ağacına dahil edilerek eklendiği söylenebilir. Bu oran ilerleyen sürümlerde bozulacaktır (1.5.x'te DSC +160 %, NOH +160 %'den çok farklı eğilimler görülmektedir).

---

### 3.2 Dikkat Gerektiren Sinyaller

**CAM (uyum): −4.8 %** — 0.407 → 0.387  
Sınıf içi metotların ortak veri alanlarına birlikte erişim oranı düşmüştür. 29 yeni sınıfın bir kısmının iç uyumu düşük tasarlandığı ya da mevcut sınıflara sorumluluk eklenmesinin bu sınıflar içindeki uyumu azalttığı anlaşılıyor. Understandability formülünde CAM pozitif terimde yer aldığından bu düşüş doğrudan kötüleşmeye katkıda bulunmaktadır.

Bu düşüş −4.8 % ile küçük görünse de CAM'ın zaten 0.407 gibi orta-düşük bir başlangıç noktasında olduğu göz önüne alındığında, trend olarak izlenmesi önerilir.

**Understandability: −81.87 → −91.47 (−11.7 % kötüleşme)**  
Formül: `−0.33 × (ANA + DCC + NOP + NOM + DSC) + 0.33 × (DAM + CAM)`

Kötüleşmenin kaynağı:
- DSC: 238 → 267 (+29) → formüle −9.57 ek negatif katkı
- CAM: 0.407 → 0.387 → pozitif katkı 0.134'ten 0.128'e düştü (−0.006)
- ANA: +0.052 → pozitif terime 0.017 ek katkı (ancak negatif etkileri dengelemeye yetmez)

**Sonuç:** Understandability kötüleşmesinin %98'inden fazlası DSC büyümesinden kaynaklanmaktadır. Bu, QMOOD formülünün yapısal özelliği olmakla birlikte, büyüyen sistemlerde anlaşılırlık yönetiminin daha dikkatli yapılması gerektiğini de doğru biçimde yansıtmaktadır.

**NOP (polimorfizm): −2.5 %** — 3.273 → 3.191  
Hafif düşüş; sınıf başına polimorfik metot sayısı azalmıştır. 29 yeni sınıfın bir bölümünün geride kalan polimorfik metot ortalamasını seyrelttiği düşünülebilir. Extendibility ve Flexibility üzerindeki etkisi marjinaldir (−0.041 puan civarı).

**Flexibility: 1.461 → 1.430 (−2.1 %)**  
MOA +8.2 % ve DAM sabit kalmasına karşın NOP'taki düşüş Flexibility'yi hafifçe geriletmiştir. NOP formüle 0.50 katsayısıyla giriyor; −0.082 × 0.50 = −0.041 puan kayıp. Anlamlı bir bozulma değildir ancak NOP eğilimi izlenmelidir.

---

## 4. Teknik Borç İşaretleri

### 4.1 Mevcut: CAM düşüşü

**Kanıt:** CAM 0.407 → 0.387 (−4.8 %).  
Bu sürümde henüz küçük bir sinyal, ancak cohesion düşüşleri kronikleştiğinde geri döndürmesi maliyetli hale gelir. Sonraki sürümlerde CAM 0.366'ya kadar düşecektir (1.5.x verileri); bu düşüşün 0.9.2'de başladığı görülmektedir.

**Risk:** Düşük cohesion → sınıf içindeki sorumluluklar dağıtık → değişiklik etkisi tahmin edilmesi güç → bakım maliyeti artar.

### 4.2 Potansiyel: NOP düşüşü

**Kanıt:** NOP 3.273 → 3.191 (−2.5 %).  
Polimorfik metot ortalamasının DSC büyümesiyle seyrelmesi, yeni sınıfların ortak arayüzlere tam olarak bağlanmadan eklendiğinin erken sinyali olabilir. 0.9.2'de bu etki sınırlıdır; ilerleyen sürümlerde ANA düşüşüyle birleştiğinde Extendibility üzerinde baskı oluşturacaktır.

### 4.3 Borç yok: DCC kontrolde

**Kanıt:** DCC 2.349 → 2.363 (+0.6 %).  
Coupling artışı bu geçişte ihmal edilebilir düzeydedir. 29 yeni sınıf eklenmiş olmasına karşın bağımlılık yoğunluğunun sabit kalması, bu sürümde yeni sınıfların görece izole tasarlandığına işaret eder. Olumlu bir işarettir.

---

## 5. Genel Değerlendirme

| Boyut | Yargı | Gerekçe |
|-------|-------|---------|
| Büyüme kalitesi | ✅ Kontrollü | ANA ve MFA artışı; hiyerarşiler kullanılıyor |
| Soyutlama | ✅ İyileşiyor | ANA +8.5 %, yeni sınıfların önemli bölümü soyut |
| Kompozisyon | ✅ İyileşiyor | MOA +8.2 %; bileşim tercihli tasarım |
| Coupling | ✅ Sabit | DCC +0.6 %; büyümeye oranla başarılı |
| Uyum (Cohesion) | ⚠️ Erken uyarı | CAM −4.8 %; küçük ama tersine eğilim başladı |
| Anlaşılırlık | ❌ Boyut etkisiyle kötüleşiyor | DSC +12.2 % → Understandability −11.7 % |
| Teknik borç | Düşük-orta | CAM düşüşü izlenmeli; DCC şimdilik kontrollü |

> **Özet:** 0.9.0 → 0.9.2 geçişi genel olarak **sağlıklı bir büyüme** sergilemektedir. ANA, MOA ve MFA'daki eş zamanlı artış, yeni sınıfların mimariye düşünerek entegre edildiğine işaret etmektedir. Bununla birlikte CAM'daki erken düşüş, sonraki sürümlerde kronikleşecek bir cohesion sorununu başlatmaktadır. DCC bu sürümde kontrol altındadır; ancak ilerleyen sürümlerdeki artışın bu iyi başlangıcı erodeedeceği verilerden görülmektedir.

---

## 6. Belirsizlikler

- **CAM düşüşünün kaynağı netleştirilmeli:** Yeni sınıfların mı yoksa mevcut sınıflara eklenen metotların mı uyumu düşürdüğü sınıf düzeyi veri olmadan ayrıştırılamaz.
- **NOP seyrelmesi:** Polimorfizm düşüşünün bilinçli bir tasarım kararı mı yoksa sızıntı mı olduğu commit geçmişi incelenmeden belirlenemez.

---

*Rapor QMOOD (Bansiya & Davis, 2002) temel alınarak hazırlanmıştır.*
