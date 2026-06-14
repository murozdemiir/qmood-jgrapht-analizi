# JGraphT Mimari Kalite ve QMOOD Değerlendirme Raporu

Bu rapor, `jgrapht-core` modülünün 0.9.0 ile 1.5.3 sürümleri arasındaki evrimini, sağlanan QMOOD ve CK metrik verilerine dayanarak eleştirel ve kanıt temelli bir yaklaşımla analiz etmektedir.

---

## 1. Genel Kalite Değerlendirmesi

JGraphT kütüphanesi sürümler boyunca ciddi bir yapısal büyüme (DSC: 238.0 -> 618.0) kaydetmiştir. Bu büyüme, kalite niteliklerine doğrusal olmayan şekillerde yansımıştır.

* **İyileşen Nitelikler (Yanıltıcı ve Gerçek Büyüme):**
    * **Reusability (Yeniden Kullanılabilirlik):** %73.92 artış göstermiştir (1.0000 -> 1.7392). Ancak bu artış mimari bir iyileşmeden ziyade, QMOOD formülündeki DSC (+0.50) katsayısının büyüklüğünden kaynaklanmaktadır. Sistem ölçeği büyüdükçe formülasyon gereği bu değer yükselmiştir.
    * **Functionality (Fonksiyonellik):** %72.66 artış göstermiştir (1.0000 -> 1.7266). Sınıf sayısının (DSC) ve hiyerarşi derinliğinin (NOH: 35.0 -> 91.0) artması, kütüphanenin kabiliyetlerinin genişlediğini doğrulamaktadır.
    * **Flexibility (Esneklik):** %40.17 artış yaşamıştır (1.0000 -> 1.4017). Bu durum, kompozisyonun (MOA: 0.3739 -> 0.7006) iki kata yakın artmasıyla desteklenmiştir.

* **Bozulan Nitelikler (Kritik Seviye):**
    * **Extendibility (Genişletilebilirlik):** En dramatik düşüş bu nitelikte yaşanmıştır. %53.83 oranında net bir çöküş söz konusudur (1.0000 -> 0.4617). Bu düşüşün temel sebebi soyutlamanın (ANA: 0.6176 -> 0.3204) ve kalıtımın (MFA: 0.2469 -> 0.1512) hızla azalması, buna karşın bağımlılıkların (DCC: 2.3487 -> 3.0324) artmasıdır.
    * **Understandability (Anlaşılabilirlik):** Başlangıçtaki negatif baseline (-81.8694), sürüm 1.5.3'te -207.8903 seviyesine gerileyerek %59.47 oranında kötüleşmiştir. Artan karmaşıklık (NOM: 5.1555 -> 6.3236) ve büyüyen sınıf hacmi sistemi daha zor anlaşılır kılmıştır.

---

## 2. Bakım Yapılabilirlik (Maintainability) Analizi

Veriler ışığında JGraphT'nin bakımının sürümler ilerledikçe net bir şekilde **zorlaştığı** görülmektedir.

* **Anlaşılabilirlik Bariyeri:** Sınıf başına düşen ortalama metot karmaşıklığı (WMC_mean: 10.3613 -> 15.7848) ve metot sayısı (NOM_mean: 5.1555 -> 6.3236) sürekli yükselmiştir. Bu durum geliştiricilerin kod bloklarını okuma ve anlamlandırma sürelerini uzatmaktadır.
* **Sıkı Bağlılık (Coupling Riskleri):** Sınıflar arası nesne bağımlılığı (CBO_mean / DCC: 2.3487 -> 3.0324) artmıştır. Bir sınıfta yapılacak değişikliğin, diğer sınıfları domino etkisiyle etkileme riski (RFC_mean: 11.2353 -> 17.2508) %53.5 oranında yükselmiştir.
* **Gevşek Birliktelik (Cohesion Deformasyonu):** Sınıf içi odaklanmayı gösteren CAM metriği 0.4070'ten 0.3660'a düşerken, metotların birbiriyle ilişkisizliğini ölçen LCOM_mean metriği **13.7563'ten 31.2379'a (2 katından fazlasına)** fırlamıştır. Sınıflar tek bir sorumluluğa odaklanmaktan uzaklaşmıştır.

---

## 3. Teknik Borç (Technical Debt) Tahmini

JGraphT kod tabanında ciddi bir teknik borç birikimi mevcuttur. Bu durum şu metrik eğilimleriyle sabittir:

1.  **"God Class" (Tanrı Sınıf) Eğilimi:** LCOM_mean değerinin 31.23'e fırlaması ve CAM'in düşmesi, sürümler içinde büyüyen bazı sınıfların bölünmediğini, aksine yapısal olarak şişmeye bırakıldığını gösterir.
2.  **Soyutlama Erezyonu:** Ortalama kalıtım derinliğinin (DIT_mean / ANA: 0.6176 -> 0.3204) yarı yarıya düşmesi, yeni özellikler eklenirken interface veya abstract sınıflar üzerinden genişleme yerine, mevcut somut sınıflara doğrudan kod eklendiğini (Spaghetti Code riski) doğrulamaktadır.
3.  **Metot Şişmesi:** Sınıf başına ağırlıklı karmaşıklığın (WMC) %52.3 artması, metotların çok fazla kontrol ifadesi (if-else, döngüler) içermeye başladığına ve dolayısıyla birim test yazımının zorlaştığına işaret eder.

---

## 4. Refactoring Önerileri

Mevcut teknik borcu azaltmak ve Extendibility çöküşünü durdurmak amacıyla şu somut mimari müdahaleler yapılmalıdır:

* **Öneri 1: Sınıf Bölme (Extract Class) ve SRP Uyumu**
    * *Gerekçe:* LCOM_mean metriğinin 13.75'ten 31.23'e yükselmesi ve CAM değerinin 0.3660'a düşmesi.
    * *Aksiyon:* Eşbirlikteliği (cohesion) düşük olan, birden fazla amaca hizmet eden büyük sınıflar tespit edilerek Tek Sorumluluk İlkesi (SRP) doğrultusunda alt sınıflara parçalanmalıdır.
* **Öneri 2: Metotların Parçalanması (Extract Method)**
    * *Gerekçe:* WMC_mean değerinin 15.78'e ve NOM_mean değerinin 6.32'ye çıkması.
    * *Aksiyon:* Sınıf içerisindeki yoğun mantıksal kırılmalara sahip uzun metotlar, daha küçük ve isimlendirilmiş alt metotlara bölünerek karmaşıklık aşağı çekilmelidir.
* **Öneri 3: Soyutlama Katmanının Güçlendirilmesi (Extract Interface / Superclass)**
    * *Gerekçe:* ANA/DIT_mean değerinin 0.6176'dan 0.3204'e düşmesi ve Extendibility'nin yarı yarıya erimesi.
    * *Aksiyon:* Doğrudan somut sınıflara olan bağımlılığı azaltmak için graf algoritmaları ve veri yapıları arayüzler (interface) arkasına alınmalı, polymorphism (NOP) etkinleştirilmelidir.
* **Öneri 4: Bağımlılık Yönetimi ve Gevşek Bağlılık (Loose Coupling)**
    * *Gerekçe:* CBO_mean (DCC) değerinin 2.34'ten 3.03'e çıkması ve RFC_mean değerinin 17.25'e yükselmesi.
    * *Aksiyon:* Sınıfların birbirini doğrudan çağırması yerine, Dependency Injection veya Facade tasarım kalıpları kullanılarak sınıflar arası doğrudan çağrı trafiği (MPC_mean: 8.66 -> 16.85) dizginlenmelidir.

---

## 5. Mimari Kalite Yorumu (Architectural Erosion)

JGraphT projesinde net bir **Mimari Erozyon (Architectural Erosion)** semptomu gözlenmektedir. 

Yazılım sistemleri büyürken (DSC: 238 -> 618), bu büyümeyi yönetebilmek için soyutlama (ANA) ve kalıtım mimarisinin (MFA) kararlı kalması veya güçlenmesi beklenir. JGraphT modelinde ise tam tersi bir seyir gerçekleşmiştir: Graf teorisi gibi doğası gereği hiyerarşik ve soyutlamaya çok uygun bir alanda, DIT_mean (0.61 -> 0.32) ve MFA (0.24 -> 0.15) hızla düşmüştür.

Sistem, büyüme baskısını soyut tasarımlarla çözmek yerine, nesne kompozisyonunu (MOA/DAC: 0.37 -> 0.70) kontrolsüzce artırarak çözmeye çalışmıştır. Bu durum, sınıfların iç içe geçmesine (CBO/DCC artışı) ve sistemin esnekliğini kaybetmesine yol açmıştır. Sonuç olarak; yazılım büyüdükçe ilk baştaki temiz mimari plan zayıflamış ve sistem her sürümde yapısal olarak daha kırılgan hale gelmiştir.