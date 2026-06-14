# JGraphT 1.5.1 – Derinlemesine QMOOD Kalite Değerlendirmesi

**Değerlendirilen Modül:** jgrapht-core  
**Metrik Modeli:** QMOOD (Bansiya & Davis 2002)  
**Odak:** Tek sürüm analizi – 1.5.1

---

## 1. GENEL KALİTE PROFİLİ (1.5.1)

| Kalite Niteliği | Ham Değer | Yorum |
|----------------|-----------|-------|
| Reusability     | 301.45    | ✅ Yüksek – geniş API ve çok sayıda sınıf |
| Functionality   | 152.89    | ✅ Yüksek – zengin algoritma ve veri yapısı |
| Flexibility     | 1.57      | ➖ Orta – coupling baskılıyor |
| Effectiveness   | 1.11      | ➖ Orta – soyutlama zayıf |
| Extendibility   | 0.487     | ❌ Düşük – ciddi sorun |
| Understandability | -201.94 | ❌ Çok düşük – kritik seviyede |

📌 **Özet:**  
Kütüphane **işlevsel olarak güçlü** ve **yeniden kullanılabilir**, ancak **anlaşılması çok zor** ve **genişletilmesi maliyetli** bir yapıya sahiptir.

---

## 2. EN ZAYIF 2 KALİTE NİTELİĞİ VE SORUMLU METRİKLER

### 🥇 1. Understandability = -201.94 (en zayıf)

**Formül:**  
`-0.33*(ANA + DCC + NOP + NOM + DSC) + 0.33*(DAM + CAM)`

**Metrik bazlı döküm:**

| Metrik | Değer | Etki | Açıklama |
|--------|-------|------|----------|
| DSC (boyut) | 600 | ➖ Negatif | Çok fazla sınıf (600) – sistem çok büyük |
| DCC (coupling) | 3.018 | ➖ Negatif | Ortalama 3 bağımlılık/sınıf – yüksek |
| NOM (karmaşıklık) | 6.32 | ➖ Negatif | Sınıf başına ~6 metot – orta-yüksek |
| NOP (polimorfizm) | 3.518 | ➖ Negatif | Çok sayıda metot override edilebilir – kontrol güçlüğü |
| ANA (soyutlama) | 0.322 | ➖ Negatif | DIT çok düşük – kalıtım hiyerarşisi sığ |
| DAM (kapsülleme) | 0.879 | ➕ Pozitif | İyi – alanlar büyük oranda private |
| CAM (cohesion) | 0.364 | ➕ Pozitif | Zayıf ama var – sınıflar kısmen odaklı |

**Asıl sorun:**  
Negatif terimlerin toplamı (`ANA+DCC+NOP+NOM+DSC` = 613.18)  
Pozitif terimlerin toplamı (`DAM+CAM` = 1.243)  
→ Negatif etki **~493 kat** daha baskın.

> **Ana neden:** Sistemin **büyüklüğü (DSC)** ve **yüksek bağımlılık (DCC)**, anlaşılabilirliği felç etmiştir.

---

### 🥈 2. Extendibility = 0.487 (ikinci en zayıf)

**Formül:**  
`0.50*(ANA + MFA + NOP) - 0.50*DCC`

| Metrik | Değer | Etki | Açıklama |
|--------|-------|------|----------|
| ANA (soyutlama) | 0.322 | +0.161 | Çok zayıf katkı |
| MFA (kalıtım) | 0.152 | +0.076 | Çok düşük – kalıtım neredeyse yok |
| NOP (polimorfizm) | 3.518 | +1.759 | Orta katkı |
| DCC (coupling) | 3.018 | **-1.509** | Güçlü **negatif** etki |

**Net:** `(0.322+0.152+3.518)*0.5 = 1.996` – `(3.018*0.5)=1.509` → **0.487**

> **Ana neden:** Yeni özellik eklemek için gereken **soyutlama (ANA) ve kalıtım (MFA)** neredeyse yok denecek kadar az. Aşırı kompozisyon (`MOA=0.69`) ve yüksek coupling (`DCC=3.02`), genişletmeyi **pahalı ve riskli** hale getiriyor.

---

## 3. METRİK BAZLI RİSKLER (CK Metriklerle Doğrulama)

| CK Metrik | 1.5.1 Değeri | Eşik (genel kabul) | Durum |
|-----------|--------------|--------------------|--------|
| LCOM_mean | 30.21 | <10 iyi, >20 kötü | ❌ **Çok kötü** – uyumsuzluk patlamış |
| CBO_mean (DCC) | 3.018 | <2 iyi, >3 kritik | ⚠️ Kritik seviyede |
| WMC_mean | 15.78 | <10 iyi, >15 riskli | ⚠️ Yüksek karmaşıklık |
| DIT_mean (ANA) | 0.322 | 2-4 ideal | ❌ Çok sığ hiyerarşi |
| RFC_mean | 17.14 | <20 iyi | ✅ Normal |

**Özellikle LCOM (30.21) ve DCC (3.02) birlikte:**  
- Sınıflar hem **düşük iç uyum** (tek sorumluluk ihlali)  
- Hem **yüksek dış bağımlılık**  
→ **Bakım kabusu**

---

## 4. SOMUT REFACTORING ÖNERİLERİ (Metrik bazlı)

### 🔧 Öneri 1 – LCOM düşürmek için “God Class”ları böl
- **Hedef:** `LCOM_mean` 30 → <15
- **Kanıt:** LCOM 30.21, WMC 15.78 → sınıflar çok fazla metoda sahip ve uyumsuz
- **Aksiyon:**  
  `org.jgrapht.alg.shortestpath` içindeki `DijkstraShortestPath` ve benzeri sınıfları:
  - `PathCalculator` (temel algoritma)
  - `PathValidator` (kısıt kontrolü)
  - `PathResultBuilder` (sonuç formatlama)
  olarak ayır.

### 🔧 Öneri 2 – DCC (CBO) azaltmak için “Facade” deseni uygula
- **Hedef:** `DCC` 3.02 → <2.2
- **Kanıt:** CBO_mean 3.018 → her sınıf ortalama 3 başka sınıfa bağımlı
- **Aksiyon:**  
  `org.jgrapht.graph` paketindeki sınıflar için bir `GraphFactory` facade katmanı ekle. Doğrudan `DefaultDirectedGraph`, `SimpleGraph` vb. erişimi azalt.

### 🔧 Öneri 3 – ANA (DIT) artırmak için Template Method deseni geri kazandır
- **Hedef:** `ANA` 0.322 → >0.50
- **Kanıt:** DIT_mean 0.322 → çoğu sınıf doğrudan Object'ten türemiş
- **Aksiyon:**  
  Ortak algoritma iskeletleri (örn. `AbstractGraphIterator`, `BaseGraphAlgorithm`) oluştur. Şu anki somut sınıfların ortak davranışını bu abstract sınıflara taşı.

---

## 5. EK GÖZLEM – Mimari Sinyal

`MOA=0.69` (kompozisyon yüksek) + `MFA=0.152` (kalıtım çok düşük) + `ANA=0.322` →  
**“Favor composition over inheritance” prensibi aşırı uygulanmış.**  
Sonuç: Kod tekrarı artmış, genişletilebilirlik düşmüş, anlaşılabilirlik zarar görmüş.

---

## 6. SONUÇ TABLOSU

| Kalite Niteliği | Değer (1.5.1) | Seviye | Kritik Metrik(ler) |
|----------------|---------------|--------|--------------------|
| Understandability | -201.94 | ❌ Kritik | DSC (600), DCC (3.02) |
| Extendibility | 0.487 | ❌ Zayıf | ANA (0.322), MFA (0.152), DCC (3.02) |
| Flexibility | 1.57 | ➖ Orta | DCC (3.02) baskılıyor |
| Effectiveness | 1.11 | ➖ Orta | ANA (0.322) zayıf |
| Reusability | 301.45 | ✅ İyi | DSC, CIS yüksek |
| Functionality | 152.89 | ✅ İyi | NOP, DSC, NOH yüksek |

**Nihai Karar:**  
JGraphT 1.5.1, **zengin işlevsellik** ve **yüksek yeniden kullanılabilirlik** sunsa da, **anlaşılabilirlik ve genişletilebilirlik açısından ciddi kalite borcu** taşımaktadır.  
Yüksek coupling (`DCC`), düşük uyum (`LCOM`), ve sıfıra yakın soyutlama (`ANA`), sistemin sürdürülebilirliğini tehlikeye atmaktadır.  
**Acil refactoring gereklidir.**