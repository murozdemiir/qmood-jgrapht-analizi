
# JGraphT v1.5.3 — QMOOD Kalite İncelemesi
*(hazırlayan: Kıdemli Yazılım Mimarisi / Kalite Uzmanı, 2026-06-14)*

| Nitelik | Değer |
|---------|------:|
| Reusability | **310.45** |
| Flexibility | **1.59** |
| Understandability | **-207.89** |
| Functionality | **157.73** |
| Extendibility | **0.49** |
| Effectiveness | **1.12** |

---

## 1. En Zayıf İki Kalite Niteliği

| # | Nitelik | Neden Zayıf? | Sorumlu Metrikler (değerleri) |
|---|----------|--------------|--------------------------------|
| 1 | **Understandability** | En düşük (negatif) skoru gösteriyor. Formülün negatif kısmında büyük **DSC = 618**, yüksek **NOM = 6.32**, **DCC = 3.03** ve **NOP = 3.55** baskın; pozitif taraftaki **DAM = 0.885** ve **CAM = 0.366** bu yükü hafifletemiyor. | DSC 618, NOM 6.32, DCC 3.03, NOP 3.55 |
| 2 | **Extendibility** | Skor **0.49** ile en düşük ikinci. Pozitif terimler (ANA 0.32 + MFA 0.15 + NOP 3.55) toplam **4.02**; fakat **DCC = 3.03** yarım katsayı ile bile ciddi eksi etki yapıyor. Düşük **ANA** ve **MFA** değerleri kalıtım/soyutlama eksikliğini gösteriyor. | DCC 3.03, ANA 0.32, MFA 0.15 |

---

## 2. Köke İninen Bulgular

* **Boyut Büyümesi (DSC)**  
  618 sınıf, önceki sürüme göre +17; Understandability’i doğrudan -0.33 × DSC ile aşağı çekiyor.

* **Yüksek Birim Karmaşıklığı (NOM 6.32, WMC_mean 15.78)**  
  Sınıf başına ortalama 6 yöntem ve 16 karmaşıklık puanı; kavrama maliyeti artıyor.

* **Birbirine Sıkı Bağlılık (DCC 3.03, CBO_mean 3.03)**  
  Modüller arası bağımlılıklar hem Understandability’yi hem Extendibility’yi baltalıyor.

* **Sınırlı Soyutlama & Kalıtım (ANA 0.32, MFA 0.15, DIT_mean 0.32)**  
  Tekrar kullanılabilir davranış ortak üst sınıflara taşınmamış; genişlemeyi zorlaştırıyor.

---

## 3. Refactoring Önerileri

| # | Öneri | Hangi Metrikleri İyileştirir? | Beklenen Etki |
|---|-------|------------------------------|---------------|
| 1 | **Paket Yeniden Yapılanması & Modül Ayırma**<br/>Graf veri yapıları (core), algoritmalar ve yardımcı yapılar net paketlere bölünsün; sıkı bağlı sınıflar arasına arayüz katmanı konulsun. | DSC ↓, DCC ↓, CAM ↑ | Daha düşük boyut, gevşek bağlılık → Understandability ↑, Extendibility ↑ |
| 2 | **Arayüz/Abstract Sınıf Çıkarma**<br/>Algoritma varyantlarını `GraphAlgorithm` arayüzüne taşı, ortak kodu soyut katmanda topla. | ANA ↑, MFA ↑, NOP ↑ (kontrollü), DCC ↓ | Kalıtım & polimorfizm sayesinde yeni algoritma ekleme kolaylaşır → Extendibility ↑ |
| 3 | **Tek Sorumluluk ve Yöntem Ayıklama**<br/>350+ satırlık veya WMC>50 olan sınıfları _(WMC_max = 381)_ parçalayıp yardımcı sınıflara/yöntemlere böl. | WMC ↓, NOM ↓, CAM ↑, LCOM ↓ | Karmaşıklık azalır, kavranabilirlik artar → Understandability ↑, Bakım maliyeti ↓ |

> **Not:** Önerileri önceliklendirirken önce düşük asılı meyveler (paket organizasyonu) ardından soyutlama refactor’ları ele alınmalı ki metrik iyileşmesinin kümülatif etkisi ölçülebilsin.

---

## 4. Sonuç

JGraphT 1.5.3, işlevsel olarak zenginleşse de (Functionality ≈ 158) **anlaşılabilirlik** ve **genişletilebilirlik** alanlarında gerilemiştir. Ölçek büyüdükçe mimari sınırlara çarpmamak için yukarıdaki refactor’ların sürüm 2.0 yol haritasına entegre edilmesi önerilir.
