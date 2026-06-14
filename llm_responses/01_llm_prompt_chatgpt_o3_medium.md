
# JGraphT QMOOD Kalite Değerlendirmesi (v0.9.0 – v1.5.3)

## 1. Genel Kalite Eğilimi

| Kalite Niteliği | 0.9.0 (baseline) | 1.5.3 | Değişim (%) | Yorum |
|-----------------|------------------|-------|-------------|-------|
| Reusability | 1.000 | 1.739 | **+74%** | Güçlü artış – özellikle CIS (+27%) ve DSC (+160%) artışıyla destekleniyor. |
| Flexibility | 1.000 | 1.402 | **+40%** | DAM hafif gerilerken MOA (+86%) ve NOP (+8%) yükselişi esneklik kazandırdı. |
| Understandability | -0.990 | -1.595 | **−61%** | DCC (+29%), NOP (+8%) ve özellikle DSC büyümesi (-) etkili. |
| Functionality | 1.000 | 1.727 | **+73%** | NOP, CIS ve DSC artışları işlevselliği yükseltti. |
| Extendibility | 1.000 | 0.462 | **−54%** | ANA (–44%) ve artan DCC nedeniyle genişletilebilirlik düştü. |
| Effectiveness | 1.000 | 1.015 | **+1.5%** | Büyük değişim yok – denge korunuyor. |

**Özet:** Reusability, Flexibility ve Functionality belirgin biçimde iyileşirken, Understandability ve Extendibility ciddi oranda bozuldu. Effectiveness neredeyse sabit kaldı.

## 2. Bakım Yapılabilirlik Analizi

| Metrik | 0.9.0 | 1.5.3 | Değişim (%) |
|--------|-------|-------|-------------|
| DCC (Coupling) | 2.35 | 3.03 | **+29%** |
| CAM (Cohesion) | 0.407 | 0.366 | **−10%** |
| WMC (Complexity) | 10.36 | 15.78 | **+52%** |
| LCOM (Lack of Cohesion) | 13.76 | 31.24 | **+127%** |
| Understandability index | -0.99 | -1.60 | **−61%** |

**Yorum:** Coupling ve kompleksite artarken cohesion azaldı; Understandability metriği %61 kötüleşti. Flexibility artışı (+40%) bazı bakım senaryolarını kolaylaştırsa da genel bakım maliyeti yükselmiştir.

## 3. Teknik Borç Göstergeleri

* **Yükselen Coupling (DCC +29%, CBO +29%)** – Modüller arası bağımlılıklar artıyor.  
* **Artan Sınıf Kompleksitesi (WMC +52%) ve Çağrı Yayılımı (RFC ≈ x2,8)** – Test ve değişiklik maliyeti büyüyor.  
* **Düşen Cohesion (CAM −10%, LCOM +127%)** – Tek sorumluluk prensibinden sapma.  
* **Zayıflayan Extendibility (−54%)** – Gelecekteki yeni özellik maliyeti artacak.

Bu birleşik eğilimler artan teknik borca işaret eder.

## 4. Refactoring Önerileri

1. **Modülerleştirme & Arabirim Ayırma**  
   *Hedef:* DCC & CBO’yu %15 düşürmek.  
   *Eylem:* Yüksek bağımlı paketlerde Service/Repository arabirimleri tanımla, Observer veya Strategy desenleri ile ters bağımlılık oluştur.

2. **Sınıf Boyutu Küçültme (Extract Class / Extract Method)**  
   *Hedef:* WMC < 12, LCOM’yi yarıya indirmek.  
   *Eylem:* 100+ satırlık ya da 10+ sorumluluk gösteren sınıfları böl.

3. **Kohesyon Artırıcı Yeniden Düzenleme**  
   *Hedef:* CAM ≥ 0.45.  
   *Eylem:* İlgisiz alanları/işlemleri ayrı domain nesnelerine taşı, Data Class’ları zenginleştir.

4. **Soyutlama Oranı Yükseltme**  
   *Hedef:* ANA’yı 0.45’e çekmek, Extendibility’yi %20 artırmak.  
   *Eylem:* Ortak davranışları abstract üst sınıflara veya arabirimlere al; Template Method kullan.

5. **Aşırı Karmaşık İşlevleri Bölme**  
   *Hedef:* En yüksek WMC’li 5 sınıfta %30 karmaşıklık azaltmak.  
   *Eylem:* Uzun algoritmaları küçük, tek sorumlu metotlara ayır; erken çıkış ve guard clause kullan.

## 5. Mimari Kalite Yorumu

* **Sistem Boyutu (DSC) %160 büyüdü** (238 → 618 sınıf).  
* Coupling (DCC/CBO) ve RFC aynı dönemde ~%29–50 arttı; bu, sınırlar arası bağımlılıkların ölçekle büyüdüğünü gösterir.  
* **DIT derinliği azalması (0.62 → 0.32)** kalıtımın yüzeysel kaldığını, yeniden kullanım yerine kopyalama eğilimi olabileceğini düşündürür.  
* Bu kombinasyonlar **mimari erozyon** sinyali verir: ölçekle orantılı olmayan bağımlılık artışı ve azalan soyutlama.  
* Öneri: Katman sınırlarını gözden geçir, bağımsız modüller için “clean/hexagonal architecture” prensiplerine göre package refactoring yap.

---
