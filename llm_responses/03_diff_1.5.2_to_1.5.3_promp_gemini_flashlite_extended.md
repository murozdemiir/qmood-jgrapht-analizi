# JGraphT 1.5.2 -> 1.5.3 Sürüm Farkı Analiz Raporu

**Hazırlayan:** Kıdemli Yazılım Mimarı ve Kalite Uzmanı
**Konu:** JGraphT Sürüm Geçişi (1.5.2 -> 1.5.3) Metrik Tabanlı Kalite Değerlendirmesi
**Tarih:** 14 Haziran 2026

---

## 1. Genel Durum Özeti: "Stabilizasyon ve Bakım Fazı"
JGraphT'nin 1.5.2'den 1.5.3 sürümüne geçişi, mimari bir dönüşümden ziyade **bakım ve küçük iyileştirmeler (patch release)** aşamasında olduğunu kanıtlamaktadır. Tüm metriklerdeki değişimler oldukça sınırlı kalmıştır (%0.1 - %4.6 aralığında). Kütüphane, mevcut mimari yapısını korumuş, radikal bir refactoring veya mimari erozyon (architectural erosion) gerçekleşmemiştir.

---

## 2. Metrik Değişimlerinin Analizi

| Metrik | Değişim | Mimari Yorum |
| :--- | :--- | :--- |
| **DSC (Boyut)** | +2.8% | Sisteme yeni sınıf/özellik eklenmiş ancak bu "hafif" bir büyüme. |
| **NOH (Hiyerarşi)** | +4.6% | Sınıf hiyerarşisi hafif derinleşmiş/genişlemiş. |
| **ANA (Soyutlama)** | +0.3% | Soyutlama seviyesi değişmemiş; mevcut tasarım deseni korunuyor. |
| **CAM (Cohesion)** | +0.7% | Çok küçük bir iyileşme; sınıfların işlevsel odaklanması marjinal düzeyde artmış. |
| **DCC (Coupling)** | +0.3% | Sistemin birbiriyle olan bağımlılığı (coupling) stabil kalmış. |

### Önemli Gözlemler:
* **Stagnasyon (Durgunluk):** `ANA` (0.320) ve `MFA` (0.151) metriklerinin neredeyse sabit kalması (%0.1 - %0.3 değişim), mimari tasarımda soyutlama ve kalıtım seviyelerinin doygunluğa ulaştığını veya bu alanlarda bir geliştirme yapılmadığını gösterir.
* **Cohesion (CAM) Eğilimi:** %0.7'lik artış, sınıfların iç yapısının çok hafif bir şekilde temizlendiğine işaret eder ancak 0.366 gibi düşük bir seviyede kaldığı için sistemin genelinde "kohezyon eksikliği" (LCOM) sorunu varlığını korumaktadır.

---

## 3. Kalite Değerlendirmesi

### Olumlu Yönler:
* **Mimari İstikrar:** Sistemin büyümesine rağmen (DSC +%2.8), `DCC` (Coupling) yalnızca %0.3 artmıştır. Bu, yeni eklenen kodun mevcut sisteme "spagetti" bağımlılıklar eklemediğini, aksine modülerliğin iyi korunduğunu gösterir.
* **Fonksiyonellik Genişlemesi:** `NOP` (Polimorfizm) ve `MOA` (Kompozisyon) oranlarındaki %1'lik artış, kütüphanenin esneklik kapasitesini çok az da olsa destekleyen unsurlardır.

### Olumsuz/Riskli Yönler:
* **İlerleme Eksikliği:** Sistemin "Extendibility" (Genişletilebilirlik) ve "Understandability" (Anlaşılabilirlik) gibi kalite nitelikleri, metrikler değişmediği için aynı kalmıştır. Eğer sistemin bu nitelikleri geçmiş sürümlerde düşükse (ki önceki sürümlerdeki -200'lü Understandability skorları bunu doğrular), bu sürüm mevcut teknik borcu azaltmak yerine olduğu gibi devralmıştır.

---

## 4. Teknik Borç (Technical Debt) Analizi

Bu sürüm geçişinde belirgin bir "yeni" teknik borç birikimi **gözlenmemektedir**. Ancak:

* **Kronik Borç:** `ANA` (Soyutlama) ve `MFA` (Kalıtım) metriklerinin çok düşük seviyede (0.32 ve 0.15) çakılı kalması, sistemin uzun vadeli "Extendibility" (genişletilebilirlik) potansiyelini baskılayan bir **kronik teknik borçtur**.
* **Cohesion (CAM) Sorunu:** `CAM` artışının %0.7'de kalması, sınıfların sorumluluklarının ayrıştırılması (refactoring) noktasında bir "duraksama" olduğunu gösterir.

---

## 5. Mimari Öneriler

Bu sürümde mimari bir bozulma olmadığı için, öneriler "mevcut borcu temizlemeye" odaklanmalıdır:

1. **Soyutlama (ANA) Stratejisi:** Mevcut soyutlama seviyesi (%0.3 değişim ile sabit) genişletilebilirliği kısıtlıyor. Bir sonraki major sürümde, somut sınıfların (`Concrete Classes`) arayüzlere (`Interfaces`) dönüştürülmesi için bir *Interface Segregation* çalışması planlanmalıdır.
2. **Kalıtım (MFA) Kullanımı:** %0.1'lik MFA değişimi, kalıtım hiyerarşisinin kullanılmadığını gösterir. Eğer sistemde kod tekrarı varsa, ortak davranışlar `Abstract Class` yapılarına taşınarak MFA yükseltilmelidir.
3. **Refactoring Odağı:** Sistem stabil olduğu için şu an en iyi zaman: "Küçük, odaklı refactoring". Özellikle düşük `CAM` değerini yükseltmek için, yüksek metot sayısına sahip (WMC/NOM) sınıfların sorumlulukları parçalanmalıdır.

**Sonuç:** 1.5.3 sürümü, mimari açıdan **"statüko"** sürümüdür. Kötüye gidiş yoktur, ancak sistemin genel kalite niteliklerini (Understandability ve Extendibility) bir üst seviyeye taşıyacak mimari iyileştirmeler henüz yapılmamıştır.