# JGraphT 1.5.3 – QMOOD Derin Kalite Analizi

## 1. GENEL DURUM

- Reusability: **310.45 (yüksek)**
- Functionality: **157.73 (yüksek)**
- Flexibility: **1.586 (orta)**
- Effectiveness: **1.1205 (stabil)**
- Extendibility: **0.4923 (düşük)**
- Understandability: **-207.89 (çok düşük)**

Sistem boyutu artmış: **DSC=618**, karmaşıklık yüksek: **NOM=6.32**, **WMC=15.78**

---

## 2. EN ZAYIF 2 KALİTE NİTELİĞİ

### 2.1 Understandability (En Kritik)

**Değer:** -207.89

#### Sayısal Nedenler:
- **DSC = 618** → negatif katkı (büyük sistem)
- **DCC = 3.0324** → yüksek coupling
- **NOP = 3.5453** → polymorphism karmaşıklığı artırıyor
- **NOM = 6.3236** → metod yoğunluğu

#### CK Kanıtları:
- **LCOM_mean = 31.24 (↑ 1.5.2: 30.22 → 31.24)** → cohesion daha da kötüleşmiş
- **RFC_mean = 17.25 (↑)** → daha fazla çağrı bağımlılığı
- **WMC_mean = 15.78 (stabil yüksek)**

#### Yorum:
Understandability kötüleşmesinin ana nedeni:
- artan boyut (DSC)
- artan coupling (DCC)
- artan cohesion problemi (LCOM)

---

### 2.2 Extendibility

**Değer:** 0.4923

#### Sayısal Nedenler:
- **ANA = 0.3204 (düşük)**
- **MFA = 0.1512 (çok düşük)**
- **DCC = 3.0324 (yüksek)**

#### Yorum:
Extendibility formülünde:
- pozitif katkılar zayıf (ANA, MFA)
- negatif katkı güçlü (DCC)

→ genişletilebilirlik düşük kalıyor

---

## 3. TEKNİK KÖK NEDEN ANALİZİ

### Ortalama CK:
- **CBO_mean = 3.03** → yüksek coupling
- **LCOM_mean = 31.24** → düşük cohesion (kötüleşme var)
- **WMC_mean = 15.78** → karmaşıklık yüksek
- **RFC_mean = 17.25** → geniş API yüzeyi

### Maksimum Değerler:
- **WMC_max = 381**
- **LCOM_max = 4371**
- **RFC_max = 149**

#### Yorum:
Bu değerler:
- God Class
- Blob yapı
- Aşırı bağlı sınıflar

olduğunu güçlü şekilde gösterir.

---

## 4. REFACTORING ÖNERİLERİ

### 1. God Class Parçalama
**Kanıt:** WMC_max=381, LCOM_max=4371  
**Aksiyon:** Sınıflar SRP’ye göre bölünmeli

---

### 2. Coupling Azaltma
**Kanıt:** DCC=3.03, CBO yüksek  
**Aksiyon:**
- interface kullanımı artır
- bağımlılıkları gevşet

---

### 3. Cohesion Artırma
**Kanıt:** CAM=0.366, LCOM yüksek  
**Aksiyon:**
- ilişkili metodlar gruplanmalı
- sınıf sorumlulukları netleştirilmeli

---

## 5. SONUÇ

### Güçlü:
- Reusability ve Functionality artmaya devam ediyor

### Zayıf:
- Understandability daha da kötüleşmiş (-207.89)
- Extendibility düşük kalmış

### Net Değerlendirme:
Sistem:
- büyüdükçe fonksiyonel olarak güçlenmiş
- ancak mimari karmaşıklık artmış

### Kritik Risk:
- teknik borç artışı (LCOM ↑, DCC ↑)
- bakım zorluğu artışı
- mimari erozyon sinyalleri

