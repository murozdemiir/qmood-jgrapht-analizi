
# JGraphT 0.9.0 → 0.9.2 Sürüm Karşılaştırması  
*(Rapor tarihi: 2026-06-14)*

## 1. Ham Metrik Değişimleri

| Metrik | 0.9.0 | 0.9.2 | Δ % |
|--------|------:|------:|----:|
| DSC (Boyut) | 238.0 | 267.0 | **+12.2** |
| NOH (Hiyerarşi Der.) | 35.0 | 39.0 | **+11.4** |
| ANA (Soyutlama) | 0.618 | 0.670 | **+8.5** |
| DAM (Kapsülleme) | 0.899 | 0.894 | **−0.6** |
| DCC (Coupling) | 2.349 | 2.363 | **+0.6** |
| CAM (Cohesion) | 0.407 | 0.387 | **−4.8** |
| MOA (Kompozisyon) | 0.374 | 0.405 | **+8.2** |
| MFA (Kalıtım) | 0.247 | 0.272 | **+10.2** |
| NOP (Polimorfizm) | 3.273 | 3.191 | **−2.5** |
| CIS (Mesajlaşma) | 3.920 | 3.914 | **−0.2** |
| NOM (Yöntem Sayısı) | 5.155 | 5.240 | **+1.6** |

> **Not:** Pozitif yüzde artış = metrik değeri yükseldi.

---

## 2. Metrik Bazlı Yorumlar

| Gözlem | Kanıt | Kalite Etkisi |
|--------|-------|---------------|
| **Kod tabanı %12 büyüdü** | DSC ↑ (+29 sınıf) | Anlaşılabilirlik düşer; yeniden kullanılabilirlik formülde (+) katsayıyla artsa da karmaşıklık artışı teknik borcu besler. |
| **Soyutlama & Kalıtım arttı** | ANA ↑ (+8.5 %), MFA ↑ (+10.2 %) | *Extendibility* ve *Flexibility*’e olumlu; tasarım daha modülerleşiyor. |
| **Birbirine Bağlılık hafif yükseldi** | DCC ↑ (+0.6 %) | Küçük ama olumsuz sinyal; gevşek bağlı mimari için aksi yönde. |
| **Uygulama içi Uyum azaldı** | CAM ↓ (−4.8 %) | Daha düşük kohezyon → sınıfın sorumlulukları dağınık; Understandability ve Reusability negatif etkilenir. |
| **Polimorfizm geriledi** | NOP ↓ (−2.5 %) | Yeni davranış ekleme maliyeti artar; *Extendibility*’de gerçek kazanım sınırlandırılır. |

---

## 3. Kalite Açısından Genel Değerlendirme

| Nitelik | Yön | Gerekçe (formüldeki baskın terimler) |
|---------|-----|--------------------------------------|
| **Reusability** | **Hafif Artı** | DSC ve CIS artışı (pozitif katsayı), DCC artışı düşük kaldı. |
| **Flexibility** | **Hafif Eksi** | DAM hafif düşüş, NOP düşüşü kümülatif olarak skoru aşağı çekti. |
| **Understandability** | **Olumsuz** | DSC, NOM ve DCC artışı (negatif katsayı) > ANA artışı; toplam skor daha negatif. |

Sonuç olarak 0.9.2, bazı mimari iyileştirmeler (soyutlama/kalıtım, kompozisyon) getirirken **anlaşılabilirlik ve iç tutarlılıkta** gerileme sergiliyor.

---

## 4. Teknik Borç İpuçları

1. **Büyüyen Kod Tabanı (DSC ↑)**  
   Sürüm başına %12 hacim artışı kontrolsüz büyüme riskini gösterir.

2. **Kohezyon Düşüşü (CAM ↓)**  
   Tek Sorumluluk İlkesi’nden sapma; bakım maliyetini yükseltir.

3. **Bağlılık Artışı (DCC ↑)**  
   Modüller arası bağımlılıklar refactor/yeniden kullanım zorluğu doğurur.

Bu sinyaller teknik borcun erken göstergeleridir; henüz küçük oranlarda olsa da trend izlenmelidir.

---

## 5. Önerilen Aksiyonlar (Kısa Vadeli)

* **Kohezyon İçin Sınıf İncelemesi** — CAM’i <0.40 altına çeken sınıfları böl veya sorumlulukları yeniden dağıt.  
* **Bağlılığı Azalt** — Yüksek DCC’li modüller arası arayüz tanımla, bağımlılık ters çevir.  
* **Polimorfizmi Teşvik Et** — Strateji/Şablon desenleri ile NOP gerilemesini tersine çevir.

---

