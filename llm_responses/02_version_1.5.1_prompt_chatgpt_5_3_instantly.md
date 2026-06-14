# JGraphT 1.5.1 – QMOOD Derin Kalite Analizi

## 1. GENEL DURUM

- Reusability: **301.45 (yüksek)**
- Functionality: **152.88 (yüksek)**
- Flexibility: **1.57 (orta)**
- Effectiveness: **1.11 (stabil)**
- Extendibility: **0.487 (düşük)**
- Understandability: **-201.93 (çok düşük)**

Sistem büyük (**DSC=600**) ve karmaşık (**NOM=6.32, WMC=15.77**).

---

## 2. EN ZAYIF 2 KALİTE NİTELİĞİ

### 2.1 Understandability (En Kritik Zayıflık)

**Değer:** -201.93

#### Sebepler:
- DSC = 600 → denklemde negatif etkili (büyük sistem)
- DCC = 3.0183 → yüksek coupling → karmaşıklık artışı
- NOM = 6.32 → metod sayısı yüksek
- CK:
  - LCOM_mean = 30.21 → düşük cohesion
  - RFC_mean = 17.13 → yüksek çağrı zinciri

#### Yorum:
- Büyük + bağlı + parçalanmış yapı → okunabilirlik ciddi düşmüş

---

### 2.2 Extendibility

**Değer:** 0.487

#### Sebepler:
- ANA = 0.3217 → düşük soyutlama
- MFA = 0.1523 → inheritance kullanımı düşük
- DCC = 3.0183 → genişletmeyi zorlaştırıyor

#### Yorum:
- Yeni özellik eklemek zor çünkü:
  - bağımlılıklar yüksek
  - soyutlama düşük

---

## 3. TEKNİK KÖK NEDEN ANALİZİ

- CBO_mean = 3.0183 → coupling yüksek
- LCOM_mean = 30.21 → cohesion düşük
- WMC_mean = 15.77 → kompleks sınıflar
- Maks değerler:
  - WMC_max = 381 → aşırı karmaşık sınıf
  - RFC_max = 151 → aşırı bağımlı sınıf
  - LCOM_max = 4371 → çok kötü cohesion

Bu değerler lokal "god class" veya "blob" yapıları işaret ediyor.

---

## 4. REFACTORING ÖNERİLERİ

### 1. God Class Parçalama
- Kanıt: WMC_max=381, LCOM_max=4371
- Aksiyon: Büyük sınıflar sorumluluklarına göre bölünmeli

---

### 2. Coupling Azaltma (Dependency Inversion)
- Kanıt: DCC=3.0183, CBO yüksek
- Aksiyon:
  - Interface kullanımı artırılmalı
  - bağımlılıklar soyutlanmalı

---

### 3. Cohesion Artırma
- Kanıt: CAM=0.3641 düşük, LCOM yüksek
- Aksiyon:
  - metodlar ilgili veriyle gruplanmalı
  - SRP uygulanmalı

---

## 5. SONUÇ

- Güçlü yön: yüksek functionality ve reusability
- Zayıf yön: anlaşılabilirlik ve genişletilebilirlik

### Net Değerlendirme:
Sistem **feature-rich ama mimari olarak zor yönetilebilir**.

- Teknik borç: yüksek
- Maintainability: düşük
- Refactoring ihtiyacı: kritik seviyede

