# JGraphT 1.5.3 – Derinlemesine QMOOD Kalite Değerlendirmesi

**Değerlendirilen Modül:** jgrapht-core  
**Metrik Modeli:** QMOOD (Bansiya & Davis 2002)  
**Analiz Tarihi:** 2026-06-14

---

## 1. GENEL KALİTE PROFİLİ (JGraphT 1.5.3)

| Kalite Niteliği | Ham Değer | 0.9.0'a Göre Değişim | Değerlendirme |
|----------------|-----------|----------------------|---------------|
| Reusability     | 310.45    | ↑%157.7              | ✅ Çok İyi    |
| Functionality   | 157.73    | ↑%155.7              | ✅ Çok İyi    |
| Flexibility     | 1.586     | ↑%8.5                | ➖ Orta       |
| Effectiveness   | 1.121     | ↑%3.5                | ➖ Durağan    |
| Extendibility   | 0.492     | ↓%45.0               | ❌ Zayıf      |
| Understandability | -207.89 | ↓%154 (daha negatif) | ❌ Kritik     |

📌 **Özet Değerlendirme:**  
JGraphT 1.5.3, **işlevsellik ve yeniden kullanılabilirlik açısından başarılı** bir büyüme sergilemiştir. Ancak **anlaşılabilirlik ve genişletilebilirlik**, sürdürülebilirliği tehlikeye atan seviyelere gerilemiştir. 618 sınıflık bir sistemde **teknik borç birikimi açıkça görülmektedir**.

---

## 2. EN ZAYIF 2 KALİTE NİTELİĞİ VE SORUMLU METRİKLER

### 🥇 1. Understandability = -207.89 (En Kritik – Felç Seviyesi)

**Formül:** `-0.33*(ANA + DCC + NOP + NOM + DSC) + 0.33*(DAM + CAM)`

#### Metrik Bazlı Hesaplama:

| Terim | Metrik | Değer | Ağırlıklı Katkı |
|-------|--------|-------|-----------------|
| Negatif | ANA | 0.3204 | -0.106 |
| Negatif | DCC | 3.0324 | -1.001 |
| Negatif | NOP | 3.5453 | -1.170 |
| Negatif | NOM | 6.3236 | -2.087 |
| Negatif | DSC | 618.0 | **-203.94** |
| **Negatif Toplam** | - | - | **-208.30** |
| Pozitif | DAM | 0.8850 | +0.292 |
| Pozitif | CAM | 0.3660 | +0.121 |
| **Pozitif Toplam** | - | - | **+0.413** |
| **Sonuç** | - | - | **-207.89** |

#### Sorumlu Metrikler (Etki Sırasına Göre):

| Sıra | Metrik | Değer | Negatif Katkı Payı | Açıklama |
|------|--------|-------|---------------------|----------|
| 1 | **DSC** (Boyut) | 618.0 | **%97.9** | 618 sınıf – sistemin tamamını kavramak neredeyse imkansız |
| 2 | **NOM** (Karmaşıklık) | 6.324 | **%1.00** | Sınıf başına ~6.3 metot, ortalama karmaşıklık yüksek |
| 3 | **NOP** (Polimorfizm) | 3.545 | **%0.56** | Çok sayıda override edilebilir metot – kontrol akışı öngörülemez |
| 4 | **DCC** (Coupling) | 3.032 | **%0.48** | Her sınıf ortalama 3 başka sınıfa bağımlı |

> **Kritik Bulgu:** DSC (618 sınıf), anlaşılabilirliğin **%98'ine yakınını** tek başına olumsuz etkilemektedir. Bu büyüklükte bir sistemde **dokümantasyon ve araç desteği olmadan** yeni bir geliştiricinin kodu anlaması aylar alabilir.

---

### 🥈 2. Extendibility = 0.492 (İkinci En Zayıf – Genişletme Maliyetli)

**Formül:** `0.50*(ANA + MFA + NOP) - 0.50*DCC`

#### Metrik Bazlı Hesaplama:

| Bileşen | Metrik | Değer | Ağırlıklı Katkı |
|---------|--------|-------|-----------------|
| Pozitif | ANA (Soyutlama) | 0.3204 | +0.160 |
| Pozitif | MFA (Kalıtım Kullanımı) | 0.1512 | +0.076 |
| Pozitif | NOP (Polimorfizm) | 3.5453 | +1.773 |
| **Pozitif Toplam** | - | - | **+2.009** |
| Negatif | DCC (Coupling) | 3.0324 | **-1.516** |
| **Sonuç** | - | - | **0.493** |

#### Sorumlu Metrikler:

| Metrik | Değer | Etki | Açıklama |
|--------|-------|------|----------|
| **DCC** | 3.0324 | ⚠️ **Güçlü Negatif (-1.516)** | Yüksek coupling, yeni özellik eklemek için birden çok sınıfı değiştirmeyi gerektirir |
| **MFA** | 0.1512 | ❌ Çok Düşük Pozitif | Kalıtım neredeyse hiç kullanılmıyor – kod tekrarı yaygın |
| **ANA** | 0.3204 | ❌ Çok Düşük Pozitif | Soyutlama derinliği çok sığ – ortak davranışlar her sınıfta tekrarlanıyor |

> **Tespit:** `MOA=0.7006` (kompozisyon) çok yüksek, `MFA=0.1512` (kalıtım) çok düşük. "Kompozisyonu tercih edin" prensibi **dogmatik bir şekilde aşırı uygulanmış**. Yeni bir graf tipi eklemek için mevcut sınıfları değiştirmek gerekir → **Open/Closed Principle ihlali**.

---

## 3. DESTEKLEYİCİ CK METRİK ANALİZİ (1.5.3)

| CK Metrik | 1.5.3 Değeri | Sağlıklı Eşik | Durum | Risk Seviyesi |
|-----------|--------------|---------------|-------|---------------|
| **LCOM_mean** | 31.24 | <10 | ❌ Çok Kötü | 🔴 Yüksek |
| **CBO_mean** (DCC) | 3.03 | <2 | ❌ Kötü | 🔴 Yüksek |
| **WMC_mean** | 15.78 | <10 | ⚠️ Riskli | 🟡 Orta |
| **DIT_mean** (ANA) | 0.32 | 2-4 | ❌ Çok Sığ | 🔴 Yüksek |
| **RFC_mean** | 17.25 | <20 | ✅ Normal | 🟢 Düşük |

### Kritik Kombinasyonlar ve Anti-Pattern'ler:

| Kombinasyon | Değerler | Anti-Pattern | Açıklama |
|-------------|----------|--------------|----------|
| LCOM + CBO | 31.24 + 3.03 | **Tanrı Sınıfı** + **Yo-yo Problemi** | Sınıflar çok sorumluluklu ve aşırı bağımlı |
| DIT + WMC | 0.32 + 15.78 | **Lazy Class** + **God Object** | Kalıtım kullanılmamış ama karmaşıklık yüksek – her sınıf kendi başına bir "God" |
| MOA + MFA | 0.70 + 0.15 | **Kompozisyon Takıntısı** | Aşırı kompozisyon, gereksiz delegasyon ve kod şişmesi |

---

## 4. 1.5.x SERİSİ KARŞILAŞTIRMASI (Kötüleşme Trendi)

| Metrik | 1.5.1 | 1.5.2 | 1.5.3 | Değişim (1.5.1→1.5.3) | Yön |
|--------|-------|-------|-------|------------------------|-----|
| DSC | 600 | 601 | 618 | **+18** | ⬆️ Büyüme |
| DCC | 3.018 | 3.023 | 3.032 | **+0.014** | ⬆️ Kötüleşme |
| LCOM | 30.21 | 30.22 | 31.24 | **+1.03** | ⬆️ Kötüleşme |
| CAM | 0.3641 | 0.3633 | 0.3660 | +0.0019 | ➡️ Stabil |
| Extendibility | 0.487 | 0.477 | 0.492 | +0.005 | ➡️ Stabil (kötü) |
| Understandability | -201.94 | -202.26 | -207.89 | **-5.95** | ⬇️ Kötüleşme |

📌 **Trend Analizi:**  
1.5.1 → 1.5.3 arasında:
- **18 yeni sınıf** eklenmiş
- **Coupling artmış** (DCC: 3.018 → 3.032)
- **Uyum bozulmuş** (LCOM: 30.21 → 31.24)
- **Anlaşılabilirlik %3 daha kötüleşmiş**

> **Uyarı:** Eğer bu trend devam ederse, 1.6.0 sürümünde anlaşılabilirlik -220 seviyesini aşabilir. Bu, **sistemin bakımının imkansız hale gelmesi** anlamına gelir.

---

## 5. SOMUT REFACTORING ÖNERİLERİ (Metrik Bazlı)

### 🔧 Öneri 1 – LCOM'u Düşürmek için Sınıfları Sorumluluklarına Göre Böl

| Metrik Hedefi | Mevcut (1.5.3) | Hedef | Gerekçe |
|---------------|----------------|-------|---------|
| LCOM_mean | 31.24 | <15 | LCOM >20, sınıflar "Tanrı Sınıfı" anti-pattern'ine sahip |

**Kanıt:**  
- LCOM 31.24 (en yüksek seviye)
- WMC 15.78 (sınıf başına yüksek metot sayısı)
- NOM 6.32 (çok sayıda metot)

**Aksiyon Planı:**  
`org.jgrapht.alg` paketindeki en büyük 10 sınıfı analiz et:

**Örnek – `GraphMetrics` sınıfı (tahmini WMC >30):**