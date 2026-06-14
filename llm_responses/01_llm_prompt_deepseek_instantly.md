# JGraphT Kalite Değerlendirmesi (QMOOD, Bansiya & Davis 2002)
**Kapsam:** jgrapht-core, sürüm 0.9.0 → 1.5.3  
**Yöntem:** QMOOD kalite nitelikleri + CK metrikleri + ham metrik trendleri

---

## 1. GENEL KALİTE DEĞERLENDİRMESİ

### İyileşen nitelikler:
- **Reusability (+%73.9):**  
  `0.9.0` → `1.5.3`: 120.47 → 310.44  
  *Ana itici güç:* `CIS` (+%7.8) ve `DSC` (+%159.7) sayesinde, `CAM` (%0.407→0.366) hafif düşse de olumlu etki baskın.

- **Functionality (+%155.7):**  
  61.69 → 157.73  
  *Kaynak:* `NOP`, `CIS`, `DSC`, `NOH` hepsi artmış. `NOH` (+%160) özellikle hiyerarşi derinliğini artırarak işlevselliği desteklemiş.

### Bozulan nitelikler (mutlak değil, göreceli):
- **Extendibility (-%44.9):**  
  0.894 → 0.492  
  *Sebep:* `DCC` (+%29.1) negatif ağırlıklı, `MFA` (-%38.8) ve `ANA` (-%47.9) düşüşü.  
  > Yeni özellik eklemek için gereken soyutlama ve kalıtım mekanizmaları zayıflamış.

- **Understandability (negatif derinleşme, -%154):**  
  -81.87 → -207.89  
  *Kritik metrikler:* `DCC`, `NOM`, `DSC`, `NOP` hepsi artarken `DAM` (kapsülleme) 0.899→0.882 düşmüş. Anlaşılabilirlik ciddi kayıpta.

### Karışık / durağan:
- **Flexibility:** 1.461 → 1.586 (+%8.5)  
  `MOA` (+%87.3) ve `DAM` hafif düşüşe rağmen `NOP` (+%8.3) sayesinde korunmuş.  
  Ancak `DCC` artışı esnekliği sınırlıyor.

- **Effectiveness:** 1.082 → 1.120 (+%3.5)  
  Neredeyse sabit. `ANA` düşüşü, `MOA` ve `MFA` artışıyla dengelenmiş.

📌 **Özet:** Kütüphane **işlevsellik ve yeniden kullanılabilirlik** açısından çok gelişmiş, ancak **anlaşılabilirlik ve genişletilebilirlik** ciddi bedel ödemiş.

---

## 2. BAKIM YAPILABİLİRLİK ANALİZİ  
(Understandability + Flexibility + coupling/cohesion)

### Anlaşılabilirlik düşüşü kanıtları:
- `DCC` (coupling): 2.35 → 3.03 (+%29) → daha fazla bağımlılık, test/local reasoning zorlaşır.
- `CAM` (cohesion): 0.407 → 0.366 (-%10) → sınıflar daha az odaklı hale gelmiş.
- `NOM` (karmaşıklık): 5.16 → 6.32 (+%22.5) → metot başına ortalama iş yükü artmış.
- `DAM` (kapsülleme): 0.899 → 0.882 (-%1.9) → bilgi gizleme zayıflamış.

### Esneklik neden artmadı?
Formül: `Flex = 0.25*DAM - 0.25*DCC + 0.50*MOA + 0.50*NOP`  
- `DAM` azaldığı için esnekliği aşağı çeken bir faktör var.  
- `DCC` artışı da negatif katkı yapıyor.  
- `MOA` ve `NOP`’daki artışlar esnekliği **ancak sabit tutabilmiş**.

📌 **Sonuç:** Bakım zorlaşmıştır. Yeni bir geliştiricinin sistemi anlaması için gereken efor (understandability) %150+ artmış. Esneklik aynı kalmış ama daha yüksek coupling ile bu “sahte bir durağanlık” olabilir.

---

## 3. TEKNİK BORÇ TAHMİNİ  

Aşağıdaki metrik trendleri **biriken teknik borcu** işaret ediyor:

| Metrik | 0.9.0 → 1.5.3 değişim | Anlamı |
|--------|------------------------|---------|
| `DCC` (CBO) | +29% | Bağımlılık borcu – bir sınıfı değiştirmek zincirleme etki yaratır. |
| `WMC_mean` | +52% | Karmaşıklık borcu – metot başına ortalama işlevsellik artmış. |
| `LCOM_mean` | +127% | Uyum borcu – sınıflar birden çok sorumluluk üstleniyor. |
| `CAM` | -10% | Cohesion borcu – iç tutarlılık azalmış. |
| `ANA` (DIT) | -48% | Soyutlama borcu – kalıtım hiyerarşisi sığlaşmış. Derinlik azalınca kod tekrarı artabilir. |

📌 **Özellikle vurgu:**  
`LCOM_mean` 13.8 → 31.2 (**+%126**) en tehlikeli sinyaldir.  
Bu kadar düşük uyum, sınıfların “birden çok iş yapan tanrı sınıflarına” dönüştüğünü gösterir.  
Teknik borç **özellikle 1.1.0 ve sonrasında** hızlanmıştır.

---

## 4. REFACTORING ÖNERİLERİ (metrik bazlı, somut)

1. **Yüksek LCOM’lu sınıfları böl**  
   - Hedef: `LCOM_mean` 31 → <20  
   - Örnek: Graf algoritma sınıflarını (Dijkstra, BFS, vb.) ayrı sorumluluklara ayır.

2. **DCC (CBO) düşürmek için arayüzler ekle**  
   - `DCC` 3.03 → <2.5  
   - Özellikle `Graph` interface’i altındaki somut sınıflar arası doğrudan bağımlılıkları azalt.

3. **CAM (cohesion) artırmak için metot gruplarını yeniden düzenle**  
   - `CAM` 0.366 → >0.45  
   - `org.jgrapht.alg` paketindeki yardımcı metotları ilgili sınıflara taşı.

4. **Düşen ANA (DIT) sebebiyle ortak davranışı abstract sınıfta topla**  
   - `ANA` 0.62 → 0.32 → ortak algoritma iskeletleri (template method) yeniden kazandırılmalı.

5. **NOM (WMC) fazla olan sınıflarda metot sayısını azalt**  
   - WMC_mean 15.8 → <12  
   - Büyük sınıfları (örn. `GraphTests`, `GraphMetrics`) işlevsel olarak parçala.

---

## 5. MİMARİ KALİTE YORUMU – Architectural Erosion?

**Evet, belirgin mimari bozulma var.**

| Gösterge | 0.9.0 → 1.5.3 | Erozyon işareti |
|----------|----------------|------------------|
| `DSC` (sınıf sayısı) | 238 → 618 (+%160) | Sistem büyümüş. |
| `MOA` (kompozisyon) | 0.37 → 0.70 (+%89) | Daha fazla nesne birleştirme – iyi. |
| `MFA` (kalıtım) | 0.25 → 0.15 (-%38) | **Kötü** – kalıtım yerine kompozisyon aşırı tercih edilmiş olabilir. |
| `DAM` (kapsülleme) | 0.899 → 0.882 | Bilgi gizleme azalmış. |
| `ANA` (DIT) | 0.62 → 0.32 | Hiyerarşi düzleşmiş – ortak soyutlama kaybı. |

📌 **Yorum:**  
Başlangıçta iyi tanımlanmış bir soyutlama hiyerarşisi varken, büyüdükçe **yeni sınıflar mevcut hiyerarşiye entegre olmak yerine doğrudan somut sınıflara eklenmiş**.  
Bu durum:  
- Tekrar eden kod (düşük ANA)  
- Zayıf kapsülleme (düşük DAM)  
- Yüksek coupling (yüksek DCC)  
- Düşük genişletilebilirlik (Extendibility)  

ile sonuçlanmıştır.  
Mimari erozyon **1.1.0 sürümünden itibaren** hızlanmıştır (LCOM, DCC, WMC sıçraması).

---

## Özet Tablo – Kalite Nitelikleri Trendi

| Kalite Niteliği | 0.9.0 → 1.5.3 değişim (%) | Yön |
|----------------|----------------------------|------|
| Reusability    | +157.7%                    | ✅ İyi |
| Functionality  | +155.7%                    | ✅ İyi |
| Flexibility    | +8.5%                      | ➖ Durağan |
| Effectiveness  | +3.5%                      | ➖ Durağan |
| Extendibility  | -44.9%                     | ❌ Kötü |
| Understandability | -154% (negatif derinleşme) | ❌ Çok kötü |

**Nihai Karar:**  
JGraphT **işlevsel olarak zenginleşmiş**, ancak **bakım maliyeti ve anlaşılabilirlik açısından ciddi teknik borç biriktirmiştir**. Mimari erozyon mevcuttur.  
Refactoring önceliği: **LCOM azaltma + DCC düşürme + ANA artırma**.