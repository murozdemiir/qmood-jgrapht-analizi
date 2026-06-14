# JGraphT v1.5.3 Sürümü Mimari Kalite ve Tasarım Metrikleri Değerlendirme Raporu

**Değerlendirmeyi Yapan:** Kıdemli Yazılım Mimarisi ve Yazılım Kalitesi Uzmanı
**İncelenen Sürüm:** JGraphT v1.5.3 (jgrapht-core)

---

## 1. Genel Kalite Değerlendirmesi

JGraphT v1.5.3 sürümü, 618 sınıflık sistem boyutu (`DSC = 618.0`) ve güçlü veri kapsülleme oranı (`DAM = 0.885`) ile işlevsel olarak olgunlaşmış bir kütüphane profili sergilemektedir. Sistemin dışarıdan bir bileşen olarak kullanımını kolaylaştıran yüksek kompozisyon gücü (`MOA = 0.7006`), **Reusability (Yeniden Kullanılabilirlik: 310.4459)** ve **Functionality (İşlevsellik: 157.7334)** kalite niteliklerinin yüksek seviyelerde seyretmesini sağlamıştır. 

Ancak, CK metriklerinin ortalama (mean) ve maksimum (max) değerleri arasındaki ekstrem sapmalar incelendiğinde, mimarinin iç yapısında telafisi zorlaşan bir teknik borç birikimi göze çarpmaktadır. Sistem geneline yayılan ortalama metot sayısı makul görünse de (`NOM_mean = 6.32`), 95 metoda sahip (`NOM_max = 95`) ve metotları birbiriyle hiçbir veri paylaşmayan (`LCOM_max = 4371`) monolitik "God Class" yapıları mevcuttur. Bu durum, dışarıdan güçlü görünen kütüphanenin içeriden bakımını ciddi şekilde tehlikeye atmaktadır.

## 2. En Zayıf 2 Kalite Niteliği ve Sorumlu Metrikler

QMOOD denklemlerine göre v1.5.3 sürümünün en kritik ve acil müdahale gerektiren iki zayıf noktası şunlardır:

### A. Understandability (Anlaşılabilirlik): -207.8903
Bu niteliğin bu denli derin bir negatif değere ulaşması, sistemin bilişsel yükünün (cognitive load) yönetilemez seviyelere geldiğinin matematiksel kanıtıdır.
* **Sorumlu Metrikler:** Formüldeki negatif etki yaratan `-0.33*(ANA+DCC+NOP+NOM+DSC)` bloğu ana etkendir.
    * Sistemin devasa boyutu (`DSC = 618.0`) başlı başına anlamayı zorlaştırır.
    * Sınıflar arası bağımlılığın yüksekliği (`DCC = 3.0324`).
    * Maksimum metot sayılarının aşırı uçlarda olması (`NOM_max = 95` ve `WMC_max = 381`).
* **Değerlendirme:** Bu negatif etkiyi dengelemesi beklenen uyum metriği (`CAM = 0.3660`) yetersiz kalmıştır. Sınıflar çok fazla sorumluluk üstlendiği ve karmaşık olduğu için, yeni bir geliştiricinin kodu okuyup güvenli değişiklik yapması çok zordur.

### B. Extendibility (Genişletilebilirlik): 0.4923
Sisteme mevcut yapıyı bozmadan yeni özellikler eklenebilme kapasitesini gösteren bu metrik kritik eşiğin altındadır.
* **Sorumlu Metrikler:** Formül `0.50*(ANA+MFA+NOP) - 0.50*DCC` şeklindedir.
    * Sistemin soyutlama oranı çok zayıftır (`ANA = 0.3204`). Kütüphanedeki sınıfların büyük bir çoğunluğu doğrudan somut (concrete) implementasyonlardır.
    * Bağımlılık (Coupling) çok yüksektir (`DCC = 3.0324`, `CBO_max = 21`).
* **Değerlendirme:** Düşük soyutlama ve yüksek bağımlılığın birleşimi, kodun "kırılgan" (fragile) olmasına yol açar. Arayüzler (interfaces) yerine somut sınıflara sıkı sıkıya bağlı bir mimaride (tight coupling), yeni eklenecek her algoritma eski kodlarda değişiklik yapılmasını (Ripple Effect) zorunlu kılacaktır.

## 3. Somut ve Metrik-Temelli Refactoring Önerileri

Metriklerdeki darboğazları aşmak ve QMOOD kalite niteliklerini iyileştirmek için şu 3 yapısal hamle uygulanmalıdır:

**1. "God Class" Nesnelerini Parçalama (Extract Class / Extract Module)**
* *Kanıt:* Metotların uyumsuzluğunu ölçen `LCOM_mean = 31.23` iken, `LCOM_max = 4371` gibi gerçek dışı bir seviyededir. Sınıf karmaşıklığı `WMC_max = 381` değerindedir.
* *Aksiyon:* LCOM ve WMC skorları tavan yapan tepedeki büyük sınıflar (muhtemelen temel algoritma veya util sınıfları) derhal parçalanmalıdır. İçerideki metotlar, kullandıkları üye değişkenlere göre alt uzmanlık sınıflarına bölünmeli (Single Responsibility Principle), böylece `CAM` (Uyum) artırılmalı ve Understandability puanı toparlanmalıdır.

**2. Katı Bağımlılıkları Soyutlama ile Gevşetme (Extract Interface / Dependency Inversion)**
* *Kanıt:* Genişletilebilirlik zayıftır (`0.4923`). Bir sınıf doğrudan 21 farklı sınıfa bağımlıdır (`CBO_max = 21`) ve kütüphanenin genel soyutlama seviyesi düşüktür (`ANA = 0.3204`).
* *Aksiyon:* Bağımlılığı yüksek merkez (Hub) sınıfların doğrudan nesne yaratımları (concrete instantiation) engellenmelidir. Bu somut sınıfların davranışları yeni arayüzlere (Interfaces) çıkarılmalı ve sistem içi iletişim bu soyutlamalar üzerinden sağlanmalıdır. Bu sayede `ANA` metriği yükselirken, sınıflar arası bağımlılık (`DCC/CBO`) düşecek ve kütüphane yeni eklentilere açılacaktır.

**3. Aşırı Dışa Çağrı Trafiğini Azaltma (Move Method / Replace Conditional with Polymorphism)**
* *Kanıt:* Bir sınıfın dışarıdaki nesnelere yaptığı metot çağrı sayısı çok yüksektir (`MPC_max = 401`). Ayrıca sistemin polimorfizm kullanım oranı geliştirilebilir seviyededir (`NOP = 3.5453`).
* *Aksiyon:* Sınıfların başkalarına ait verileri alıp kendi içinde işlediği "Feature Envy" kokan metotlar (`MPC`'si yüksek olanlar) tespit edilmelidir. Veri ile iş mantığı bir araya getirilerek metotlar asıl ait oldukları sınıflara taşınmalı (Move Method). Karmaşık `if/switch` blokları ise polimorfik yapılara devredilerek `NOP` değeri yükseltilmelidir.