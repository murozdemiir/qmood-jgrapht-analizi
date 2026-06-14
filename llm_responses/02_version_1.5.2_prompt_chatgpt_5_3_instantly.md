# JGraphT 1.5.2 – QMOOD Derin Kalite Analizi

## 1. GENEL DURUM

- Reusability: **301.94 (yüksek)**
- Functionality: **153.10 (yüksek)**
- Flexibility: **1.565 (orta)**
- Effectiveness: **1.1105 (stabil)**
- Extendibility: **0.4774 (düşük)**
- Understandability: **-202.26 (çok düşük)**

Sistem boyutu yüksek: **DSC=601**, karmaşıklık artmış: **NOM=6.29**, **WMC=15.76**

---

## 2. EN ZAYIF 2 KALİTE NİTELİĞİ

### 2.1 Understandability (En Kritik Zayıflık)

**Değer:** -202.26

#### Sayısal Nedenler:
- **DSC = 601** → denklemde negatif etkili (büyük sistem)
- **DCC = 3.0233** → yüksek coupling → zihinsel yük artışı
- **NOP = 3.5075** → polymorphism karmaşıklığı artırıyor
- **NOM = 6.29** → sınıf başına metod sayısı yüksek

#### CK Kanıtları:
- **LCOM_mean = 30.22** → düşük cohesion (yüksek parçalanma)
- **RFC_mean = 17.13** → yüksek metod çağrı zinciri
- **WMC_mean = 15.76** → sınıflar kompleks

#### Yorum:
Understandability düşüşü doğrudan:
- artan sistem boyutu (DSC)
- artan coupling (DCC)
- düşük cohesion (LCOM)
kombinasyonundan kaynaklanıyor.

---

### 2.2 Extendibility

**Değer:** 0.4774

#### Sayısal Nedenler:
- **ANA = 0.3195 (düşük)** → soyutlama zayıf
- **MFA = 0.1511 (çok düşük)** → inheritance kullanımı sınırlı
- **DCC = 3.0233 (yüksek)** → bağımlılıklar genişletmeyi zorlaştırıyor

#### Yorum:
Extendibility formülü:
- pozitif: ANA + MFA + NOP
- negatif: DCC

Burada:
- pozitif katkılar düşük (ANA, MFA)
- negatif katkı yüksek (DCC)

→ sonuç: genişletilebilirlik düşük

---

## 3. TEKNİK KÖK NEDEN ANALİZİ

### Kritik CK Metrikleri:
- **CBO_mean = 3.0233** → coupling yüksek
- **LCOM_mean = 30.22** → cohesion düşük
- **WMC_mean = 15.76** → karmaşık sınıflar
- **RFC_mean = 17.13** → geniş çağrı yüzeyi

### Maksimum Değerler (Risk Göstergesi):
- **WMC_max = 381** → aşırı kompleks sınıf
- **RFC_max = 149** → aşırı bağımlı sınıf
- **LCOM_max = 4371** → çok düşük cohesion

### Yorum:
Bu değerler lokal olarak:
- God Class
- Blob sınıflar
- Yoğun bağımlı modüller

olduğunu güçlü şekilde işaret eder.

---

## 4. REFACTORING ÖNERİLERİ

### 1. God Class Parçalama
**Kanıt:**
- WMC_max = 381
- LCOM_max = 4371

**Aksiyon:**
- Büyük sınıflar sorumluluklarına göre ayrılmalı (SRP)

---

### 2. Coupling Azaltma (Dependency Inversion)
**Kanıt:**
- DCC = 3.0233
- CBO_mean yüksek

**Aksiyon:**
- Interface tabanlı tasarım artırılmalı
- doğrudan bağımlılıklar azaltılmalı

---

### 3. Cohesion Artırma
**Kanıt:**
- CAM = 0.3633 (düşük)
- LCOM_mean = 30.22 (yüksek)

**Aksiyon:**
- ilişkili metod ve veriler gruplanmalı
- sınıf içi sorumluluklar sadeleştirilmeli

---

## 5. SONUÇ

### Güçlü Yönler:
- Reusability yüksek (DSC=601 ve CIS=4.208 katkısı)
- Functionality yüksek (NOP, CIS, DSC artışı)

### Zayıf Yönler:
- Understandability ciddi düşük
- Extendibility düşük

### Net Değerlendirme:
Sistem:
- fonksiyonel olarak güçlü
- ancak mimari olarak karmaşık ve zor yönetilebilir

### Risk:
- yüksek teknik borç
- düşük bakım yapılabilirlik
- refactoring ihtiyacı kritik seviyede

