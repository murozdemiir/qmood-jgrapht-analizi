# JGraphT 1.5.2 – Derinlemesine QMOOD Kalite Değerlendirmesi

**Değerlendirilen Modül:** jgrapht-core  
**Metrik Modeli:** QMOOD (Bansiya & Davis 2002)  
**Analiz Tarihi:** 2026-06-14

---

## 1. GENEL KALİTE PROFİLİ (JGraphT 1.5.2)

| Kalite Niteliği | Ham Değer | Normalize (0.9.0=1.0) | Değerlendirme |
|----------------|-----------|------------------------|---------------|
| Reusability     | 301.94    | 1.701 (↑%70.1)         | ✅ Çok İyi    |
| Functionality   | 153.10    | 1.681 (↑%68.1)         | ✅ Çok İyi    |
| Flexibility     | 1.565     | 1.387 (↑%38.7)         | ➖ Orta       |
| Effectiveness   | 1.111     | 1.007 (↑%0.7)          | ➖ Durağan    |
| Extendibility   | 0.477     | 0.457 (↓%54.3)         | ❌ Zayıf      |
| Understandability | -202.26 | -1.567 (↓%58.3)*       | ❌ Kritik     |

*\*Negatif değerlerde daha düşük (daha negatif) = daha kötü anlaşılabilirlik*

📌 **Özet Değerlendirme:**  
JGraphT 1.5.2, **zengin API ve geniş işlevsellik** sunarken, **anlaşılabilirlik ve genişletilebilirlik** açısından ciddi kalite sorunları taşımaktadır. Sistem büyüdükçe (601 sınıf), bakım maliyeti katlanarak artmıştır.

---

## 2. EN ZAYIF 2 KALİTE NİTELİĞİ VE SORUMLU METRİKLER

### 🥇 1. Understandability = -202.26 (En Kritik)

**Formül:** `-0.33*(ANA + DCC + NOP + NOM + DSC) + 0.33*(DAM + CAM)`

#### Metrik Bazlı Hesaplama:

| Terim | Metrik | Değer | Ağırlıklı Katkı |
|-------|--------|-------|-----------------|
| Negatif | ANA | 0.3195 | -0.105 |
| Negatif | DCC | 3.0233 | -0.998 |
| Negatif | NOP | 3.5075 | -1.157 |
| Negatif | NOM | 6.2928 | -2.077 |
| Negatif | DSC | 601.0 | -198.33 |
| **Negatif Toplam** | - | - | **-202.67** |
| Pozitif | DAM | 0.8806 | +0.291 |
| Pozitif | CAM | 0.3633 | +0.120 |
| **Pozitif Toplam** | - | - | **+0.411** |
| **Sonuç** | - | - | **-202.26** |

#### Sorumlu Metrikler (Sıralı):

| Sıra | Metrik | Değer | Suç Payı | Açıklama |
|------|--------|-------|----------|----------|
| 1 | **DSC** (Boyut) | 601.0 | **%98.0** | 601 sınıf – sistem çok büyük, tek seferde anlaşılamaz |
| 2 | **NOM** (Karmaşıklık) | 6.29 | **%1.03** | Sınıf başına ~6 metot, ortalama karmaşıklık yüksek |
| 3 | **NOP** (Polimorfizm) | 3.51 | **%0.57** | Çok sayıda override edilebilir metot – akış kontrolü zor |
| 4 | **DCC** (Coupling) | 3.02 | **%0.49** | Her sınıf ortalama 3 başka sınıfa bağımlı |

> **Kritik Bulgu:** DSC tek başına anlaşılabilirliğin ~%98'ini olumsuz etkilemektedir. 601 sınıflık bir sistemi anlamak için **ciddi dokümantasyon ve araç desteği** şarttır.

---

### 🥈 2. Extendibility = 0.477 (İkinci En Zayıf)

**Formül:** `0.50*(ANA + MFA + NOP) - 0.50*DCC`

#### Metrik Bazlı Hesaplama:

| Bileşen | Metrik | Değer | Ağırlıklı Katkı |
|---------|--------|-------|-----------------|
| Pozitif | ANA (Soyutlama) | 0.3195 | +0.160 |
| Pozitif | MFA (Kalıtım Kullanımı) | 0.1511 | +0.076 |
| Pozitif | NOP (Polimorfizm) | 3.5075 | +1.754 |
| **Pozitif Toplam** | - | - | **+1.990** |
| Negatif | DCC (Coupling) | 3.0233 | **-1.512** |
| **Sonuç** | - | - | **0.478** |

#### Sorumlu Metrikler:

| Metrik | Değer | Etki | Açıklama |
|--------|-------|------|----------|
| **DCC** | 3.0233 | ⚠️ **Güçlü Negatif (-1.51)** | Yüksek coupling, yeni özellik eklemeyi riskli ve maliyetli yapar |
| **MFA** | 0.1511 | ❌ Çok Düşük Pozitif | Kalıtım neredeyse kullanılmıyor – kod tekrarı artar |
| **ANA** | 0.3195 | ❌ Çok Düşük Pozitif | Soyutlama derinliği çok sığ – ortak davranışlar tekrarlanır |

> **Tespit:** `MOA=0.6938` (kompozisyon) çok yüksek, `MFA=0.1511` (kalıtım) çok düşük. "Kompozisyonu tercih edin" prensibi **aşırı uygulanmış**. Yeni özellikler eklemek için mevcut sınıfları değiştirmek gerekir → Open/Closed Principle ihlali.

---

## 3. DESTEKLEYİCİ CK METRİK ANALİZİ

| CK Metrik | 1.5.2 Değeri | Sağlıklı Eşik | Durum | Risk Seviyesi |
|-----------|--------------|---------------|-------|---------------|
| **LCOM_mean** | 30.22 | <10 | ❌ Çok Kötü | 🔴 Yüksek |
| **CBO_mean** (DCC) | 3.02 | <2 | ❌ Kötü | 🔴 Yüksek |
| **WMC_mean** | 15.76 | <10 | ⚠️ Riskli | 🟡 Orta |
| **DIT_mean** (ANA) | 0.32 | 2-4 | ❌ Çok Sığ | 🔴 Yüksek |
| **RFC_mean** | 17.13 | <20 | ✅ Normal | 🟢 Düşük |

### Kritik Kombinasyonlar:

1. **LCOM (30.22) + CBO (3.02):**  
   Sınıflar hem düşük iç uyumlu (tek sorumluluk ihlali) hem de yüksek dış bağımlılıklı.  
   → **Bakımı neredeyse imkansız sınıflar**

2. **DIT (0.32) + WMC (15.76):**  
   Sıfıra yakın kalıtım derinliği + yüksek metot başına karmaşıklık  
   → **Her sınıf kendi başına bir "God Object"**

---

## 4. SOMUT REFACTORING ÖNERİLERİ (Metrik Bazlı)

### 🔧 Öneri 1 – LCOM'u Düşürmek için "Low Cohesion" Sınıfları Böl

| Metrik Hedefi | Mevcut | Hedef | Gerekçe |
|---------------|--------|-------|---------|
| LCOM_mean | 30.22 | <15 | LCOM >20, sınıflar birden fazla sorumluluk taşır |

**Kanıt:** LCOM 30.22, WMC 15.76, NOM 6.29 → sınıflar çok metotlu ve uyumsuz.

**Aksiyon:**  
`org.jgrapht.alg` paketindeki sınıfları analiz et. Örneğin:
- `DijkstraShortestPath` → `PathCalculator` (algoritma) + `PathValidator` (kısıtlar) + `PathFormatter` (çıktı)
- `GraphMetrics` → `ConnectivityMetrics` + `CentralityMetrics` + `ClusteringMetrics`

---

### 🔧 Öneri 2 – DCC/CBO Azaltmak için Arayüz ve Soyut Sınıflar Ekle

| Metrik Hedefi | Mevcut | Hedef | Gerekçe |
|---------------|--------|-------|---------|
| DCC (CBO) | 3.02 | <2.2 | CBO >2, bağımlılık yönetilemez seviyede |

**Kanıt:** CBO 3.023 → her sınıf ortalama 3 başka sınıfa doğrudan bağlı.

**Aksiyon:**  
`org.jgrapht.graph` paketi için:
1. `GraphFactory` facade deseni ekle
2. `BaseGraph` abstract sınıfı oluştur, ortak davranışları buraya taşı
3. Somut sınıflar (`DefaultDirectedGraph`, `SimpleGraph`) bu sınıftan türesin

---

### 🔧 Öneri 3 – ANA (DIT) Artırmak için Template Method Deseni Uygula

| Metrik Hedefi | Mevcut | Hedef | Gerekçe |
|---------------|--------|-------|---------|
| ANA (DIT_mean) | 0.32 | >0.50 | DIT <1, neredeyse hiç kalıtım kullanılmıyor |

**Kanıt:** DIT_mean=0.32 → çoğu sınıf doğrudan Object'ten türemiş. MFA=0.151 → kalıtım mekanizmaları neredeyse hiç kullanılmıyor.

**Aksiyon:**  
Algoritma sınıfları için bir iskelet oluştur:
```java
public abstract class BaseGraphAlgorithm<V, E> {
    protected abstract void initialize();
    protected abstract void execute();
    protected abstract void cleanup();
    
    public final void run() {
        initialize();
        execute();
        cleanup();
    }
}