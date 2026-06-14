# JGraphT v1.5.1 Sürümü Mimari Kalite ve Tasarım Metrikleri Değerlendirme Raporu

## 1. Genel Kalite Değerlendirmesi

JGraphT v1.5.1, `DSC = 600.0` (sistem boyutu) değeriyle oldukça büyük ve kapsamlı bir kütüphane profili çizmektedir. Bu büyüklük, **Functionality (İşlevsellik: 152.88)** ve **Reusability (Yeniden Kullanılabilirlik: 301.45)** skorlarının yüksek olmasını sağlamıştır. Sınıflar arası kompozisyon oranının yüksek olması (`MOA = 0.6917`) ve veri kapsülleme prensiplerine sadık kalınması (`DAM = 0.8794`), kütüphanenin dışarıdan bir bileşen olarak kullanımını kolaylaştırmaktadır. 

Ancak, sistemin iç yapısı CK metriklerindeki ekstrem maksimum (max) değerler üzerinden incelendiğinde, ciddi bir "God Class" (Her Şeyi Yapan Sınıf) yığılmasına ve mimari bozulmaya (architectural erosion) işaret etmektedir. Sınıf ortalamaları makul görünse de, sistemin belli noktalarında bakımı imkansız hale gelmiş devasa yapılar mevcuttur.

## 2. En Zayıf 2 Kalite Niteliği ve Sorumlu Metrikler

QMOOD denklemleri ve sağlanan sayılara göre sistemin en zayıf iki halkası şunlardır:

### A. Understandability (Anlaşılabilirlik): -201.9385
Bu değerin dramatik şekilde negatif olması, sistemin bilişsel karmaşıklığının çok yüksek olduğunu gösterir.
* **Sorumlu Metrikler:** Düşüşün temel kaynağı, formüldeki `-0.33*(ANA+DCC+NOP+NOM+DSC)` bölümüdür.
    * Sistem boyutunun aşırı büyüklüğü (`DSC = 600.0`).
    * Sınıf başına düşen ortalama metot sayısının artışı (`NOM_mean = 6.32`), ancak asıl tehlike tek bir sınıfta 95 metodun bulunmasıdır (`NOM_max = 95`).
    * Sınıflar arası yüksek bağımlılık (`DCC = 3.0183`).
* *Sonuç:* Pozitif etki yapması beklenen sınıf içi uyum ortalama seviyede kaldığı için (`CAM = 0.3641`), artan boyut ve metot karmaşıklığı kodu anlamayı matematiksel olarak zorlaştırmıştır.

### B. Extendibility (Genişletilebilirlik): 0.4870
Bir yazılımın esnekliğini ve yeni özellikler eklenmesine olan uygunluğunu gösteren bu değer kritik derecede düşüktür.
* **Sorumlu Metrikler:** Formül `0.50*(ANA+MFA+NOP) - 0.50*DCC` şeklindedir.
    * Soyutlama oranının zayıflığı (`ANA = 0.3217`). Ortadaki sınıfların çok büyük bir kısmı doğrudan somut (concrete) sınıflardır.
    * Bağımlılığın (Coupling) yüksekliği (`DCC = 3.0183`).
* *Sonuç:* Sistemin genişletilebilirliğini besleyecek olan soyutlama (ANA) düşükken, bunu negatif etkileyen bağımlılık (DCC) yüksek kalmıştır. Bu durum, sisteme yeni bir özellik eklendiğinde mevcut kodlarda değişiklik yapma zorunluluğunu (Ripple Effect) artırır.

## 3. Somut ve Metrik-Temelli Refactoring Önerileri

CK metriklerindeki uç değerleri (max) eritmek ve QMOOD zayıflıklarını gidermek için acil uygulanması gereken 3 mimari hamle:

**1. Sorumlulukların Bölünmesi (Extract Class / Extract Subclass)**
* *Kanıt:* Sistemde metotların birbiriyle uyumsuzluğunu ölçen LCOM değeri ortalama `30.21` iken, `LCOM_max = 4371` gibi akıl almaz bir seviyededir. Ayrıca bir sınıfın karmaşıklığı `WMC_max = 381`'e ulaşmıştır.
* *Aksiyon:* LCOM ve WMC değeri uç noktalarda olan sınıflar tespit edilmelidir. Bu "God Class" yapılarındaki metotların hangi veri gruplarını kullandığı analiz edilerek (Single Responsibility Principle gözetilerek) sınıflar daha küçük, spesifik işler yapan parçalara bölünmelidir. Bu hamle doğrudan `CAM` (Uyum) değerini artırıp, Understandability'yi toparlayacaktır.

**2. Katı Bağımlılıkların Gevşetilmesi (Extract Interface / Dependency Injection)**
* *Kanıt:* Extendibility zayıftır. Bir sınıf 21 farklı sınıfa doğrudan bağımlıdır (`CBO_max = 21`) ve bir sınıftan diğer nesnelere yapılan metot çağrısı muazzam seviyededir (`MPC_max = 403`). Soyutlama ise düşüktür (`ANA = 0.3217`).
* *Aksiyon:* CBO ve MPC değeri yüksek olan merkez (Hub) sınıflar belirlenmeli. Bu sınıfların bağımlı olduğu somut sınıfların üzerine arayüzler (Interfaces) çekilmeli ve nesne yaratımları soyutlamalar üzerinden yapılmalıdır. Bu sayede `ANA` metriği artarken, `DCC/CBO` (Bağımlılık) düşecek ve Extendibility puanı iyileşecektir.

**3. Metot Karmaşıklığını Dağıtma (Replace Conditional with Polymorphism)**
* *Kanıt:* `RFC_max = 151` (Bir sınıfın cevap verebileceği maksimum metot/çağrı seti oldukça geniş) ve `NOM_max = 95`. Polimorfizm kullanım oranı ise geliştirilebilir düzeydedir (`NOP = 3.5183`).
* *Aksiyon:* Çok fazla metot barındıran (`NOM` yüksek) ve karmaşık iş mantıkları içeren (muhtemelen uzun `if/else` veya `switch` blokları barındıran) kodlar tespit edilmelidir. Bu karar yapıları çok biçimlilik (Polymorphism) kullanılarak alt sınıflara devredilmelidir. Bu hamle `NOP` (Polimorfizm) çarpanını artırırken, sınıfların iç karmaşıklığını (`WMC` ve `NOM`) dengeleyecektir.