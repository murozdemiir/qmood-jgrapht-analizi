# JGraphT Yazılım Kalitesi ve Mimari Analiz Raporu

Bu rapor, JGraphT kütüphanesinin 0.9.0 - 1.5.3 sürümleri arasındaki gelişimini QMOOD ve CK metrikleri üzerinden teknik bir perspektifle analiz eder.

---

## 1. Genel Kalite Değerlendirmesi
JGraphT'nin gelişimi, **fonksiyonel genişleme ile beraber yapısal karmaşıklığın arttığı** bir süreçtir.

* **Yeniden Kullanılabilirlik (Reusability):** 120.47’den 310.44’e artış (+%74). API yüzeyinin genişlemesi ve arayüz kullanımının (CIS) bu metriği desteklediği görülmektedir.
* **Anlaşılabilirlik (Understandability):** -81.86’dan -207.89’a düşüş. Bu, sistemin bilişsel yükünün dramatik şekilde arttığını kanıtlar.
* **Genişletilebilirlik (Extendibility):** 1.0.0 sürümündeki 0.77 seviyesinden 0.46 seviyesine düşüş. Sistemin yeni yetenek eklemeye karşı direncinin arttığı sayısal olarak sabittir.

## 2. Bakım Yapılabilirlik (Maintainability) Analizi
Bakım süreçleri, tasarımın sıkılaşan bağımlılıkları nedeniyle zorlaşmıştır:

* **Coupling (Bağımlılık):** DCC (Coupling) metriğinin 2.34'ten 3.03'e çıkması, modüllerin birbirinden ayrışmasının (decoupling) bozulduğunu gösterir.
* **Cohesion (Uyum):** CAM (Cohesion) değerinin 0.40’tan 0.36’ya gerilemesi, sınıfların içsel tutarlılığının azaldığına işarettir.
* **Değerlendirme:** Sıkı bağımlılık ve düşük uyum (high coupling, low cohesion), kod üzerindeki en ufak bir değişikliğin yayılma etkisini (ripple effect) artırmaktadır.

## 3. Teknik Borç (Technical Debt) Tahmini
Aşağıdaki metrik değişimleri, ciddi bir teknik borç birikimine delalet etmektedir:

* **WMC (Weighted Methods per Class):** 10.3'ten 15.7'ye çıkış; sınıfların "God Class" eğilimine girdiğini (tek bir sınıfa çok fazla sorumluluk yüklenmesi) gösterir.
* **ANA (Abstraction):** 0.61'den 0.32'ye düşüş; hiyerarşideki soyutlama katmanlarının azaldığını, sistemin daha az esnek ve daha somut (rigid) hale geldiğini kanıtlar.
* **RFC (Response for Class):** 11.2'den 17.2'ye artış; bir sınıfın içindeki metodların sistemin geneliyle olan karmaşık etkileşimini (test edilebilirlik maliyeti) artırmaktadır.

## 4. Refactoring Önerileri
1.  **Arayüz Ayrıştırma (Interface Segregation):** Yüksek RFC değerini düşürmek için büyük arayüzleri daha küçük, spesifik arayüzlere bölün.
2.  **Sınıf Bölme (Class Splitting):** WMC değeri yüksek sınıfları, "Single Responsibility Principle" (Tek Sorumluluk İlkesi) temelinde alt sınıflara/bileşenlere ayırın.
3.  **Hiyerarşi Optimizasyonu:** DIT (Kalıtım derinliği) düşüşünü tersine çevirmek ve MFA değerini yükseltmek için, kalıtım yerine kompozisyon kullanarak kod tekrarını azaltın.

## 5. Mimari Kalite Yorumu
JGraphT'de **Mimari Erozyon (Architectural Erosion)** belirtileri netleşmiştir. DSC (Sınıf Sayısı) 238'den 618'e çıkarken `Understandability` skorunun bu denli düşmesi, mimarinin ölçeklendikçe yapısal bütünlüğünü koruyamadığını göstermektedir. Sistem, modüler bir yapıdan, birbiriyle yüksek derecede bağımlı (tightly coupled) bir yapıya doğru evrilmiştir.

---
*Analiz Notu: Bu çalışma, Bansiya & Davis (2002) QMOOD modeli referans alınarak JGraphT'nin evrimsel veri setleri üzerinde gerçekleştirilmiştir.*