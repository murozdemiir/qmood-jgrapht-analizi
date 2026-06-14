# JGraphT 1.5.2 → 1.5.3 – Sürüm Farkı Analizi (QMOOD)

## 1. GENEL DEĞİŞİM ÖZETİ

### Boyut ve Yapısal Değişim
- **DSC:** 601 → 618 (**+2.8%**)
- **NOH:** 87 → 91 (**+4.6%**)

➡️ Sistem büyümeye devam ediyor, ancak artış oranı düşük (inkremental büyüme).

---

## 2. TASARIM METRİKLERİ YORUMU

### 2.1 Olumlu Değişimler

#### Cohesion ve Kompozisyon
- **CAM:** 0.363 → 0.366 (**+0.7%**)
- **MOA:** 0.694 → 0.701 (**+1.0%**)

➡️ Cohesion hafif artmış, kompozisyon kullanımı artmış → **modülerlik açısından küçük iyileşme**

#### Kapsülleme
- **DAM:** 0.881 → 0.885 (**+0.5%**)

➡️ Encapsulation iyileşmesi → **bakım açısından olumlu**

#### Polymorphism ve Arayüz
- **NOP:** 3.507 → 3.545 (**+1.1%**)
- **CIS:** 4.208 → 4.225 (**+0.4%**)

➡️ Fonksiyonel esneklik ve API kapasitesi artmış

---

### 2.2 Olumsuz Değişimler

#### Coupling
- **DCC:** 3.023 → 3.032 (**+0.3%**)

➡️ Küçük ama negatif yönlü artış → bağımlılıklar büyüyor

#### Karmaşıklık
- **NOM:** 6.293 → 6.324 (**+0.5%**)

➡️ Metod sayısı artıyor → sınıf karmaşıklığı artışı

---

### 2.3 Nötr / Önemsiz Değişimler

- **ANA:** +0.3% (pratikte sabit)
- **MFA:** +0.1% (sabit)

➡️ Soyutlama ve inheritance yapısı değişmemiş

---

## 3. KALİTE ETKİ ANALİZİ

### Pozitif Etkiler:
- CAM ↑ → **Understandability ve Maintainability için hafif iyileşme**
- MOA ↑ → **Flexibility için olumlu**
- DAM ↑ → **Encapsulation iyileşmesi**
- NOP + CIS ↑ → **Functionality artışı**

### Negatif Etkiler:
- DCC ↑ → **Extendibility ve Maintainability üzerinde negatif etki**
- NOM ↑ → **Understandability üzerinde negatif etki**

---

## 4. TEKNİK BORÇ ANALİZİ

### Bulgular:

- **DCC artışı (+0.3%) → coupling artışı**
- **NOM artışı (+0.5%) → karmaşıklık artışı**
- Ancak:
  - CAM ↑ → cohesion iyileşmesi
  - DAM ↑ → kapsülleme iyileşmesi

➡️ Negatif trendler **mevcut ama zayıf**

### Yorum:
- Teknik borç sinyali var (özellikle coupling artışı)
- Ancak:
  - artışlar çok düşük
  - bazı metrikler iyileşiyor

→ **teknik borç artışı kontrol altında**

---

## 5. GENEL DEĞERLENDİRME

### Olumlu:
- Modüler kalite (CAM, MOA) hafif iyileşmiş
- Encapsulation ve polymorphism artmış

### Olumsuz:
- Coupling artışı devam ediyor (DCC ↑)
- Karmaşıklık artışı sürüyor (NOM ↑)

### Net Sonuç:
Bu sürüm geçişi:

➡️ **Küçük ama dengeli bir iyileşme içeriyor**
➡️ Aynı zamanda **mevcut risk trendlerini (coupling, complexity) sürdürüyor**

---

## SONUÇ

- Genel etki: **hafif olumlu**
- Teknik borç: **kontrollü ama artış eğilimi mevcut**
- Kritik risk: **coupling artışı uzun vadede problem yaratabilir**

