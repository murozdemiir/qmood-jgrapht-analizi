# JGraphT Kütüphanesi Mimari ve Yazılım Kalitesi Değerlendirme Raporu
**Odak Modül:** jgrapht-core  
**Analiz Metodolojisi:** QMOOD ve CK Metrikleri Tabanlı Kanıt Temelli Değerlendirme  

---

## 1. Genel Kalite Değerlendirmesi

JGraphT kütüphanesinin v0.9.0 ile v1.5.3 sürümleri arasındaki evrimi, sistem boyutunun doğrusal büyümesiyle birlikte kalite niteliklerinde belirgin bir kutuplaşmaya işaret etmektedir.

### İyileşen Kalite Nitelikleri
* **Reusability (Yeniden Kullanılabilirlik):** v0.9.0'da `120.47` olan ham değer, v1.5.3'te `310.44` değerine ulaşarak baseline sürümüne göre **%73.9** oranında bir artış (`1.7392` normal değer) göstermiştir. Bu artışın temel sebebi formüldeki pozitif ağırlıklı metriklerin büyümesidir: Sistem boyutu (`DSC`: 238'den 618'e) ve sınıf başına arayüz genişliği (`CIS`: 3.92'den 4.22'ye) artarken, negatif ağırlıklı `DCC` (Coupling) artışının bu büyümeyi baskılayamamasıdır.
* **Functionality (Fonksiyonellik):** Fonksiyonellik skoru `61.69` değerinden `157.73` değerine çıkarak **%72.6** artmıştır. Bu durum, kütüphaneye eklenen yeni graf algoritmaları ve veri yapılarının (`DSC` ve `NOP` artışı) doğrudan bir sonucudur.
* **Flexibility (Esneklik):** Esneklik skoru `1.46` değerinden `1.58` değerine (`1.4017` normal değer) yükselmiştir. Bu **%40**'lık artışta en büyük pay, kompozisyonun (`MOA`: 0.37'den 0.70'e) neredeyse iki katına çıkmasıdır.

### Bozulan Kalite Nitelikleri
* **Understandability (Anlaşılabilirlik):** En dramatik çöküş bu nitelikte yaşanmıştır. v0.9.0'da `-81.86` olan ham değer, v1.5.3'te `-207.89` değerine gerilemiştir (Normalleştirilmiş kayıp: **-%59.4**). Negatif katsayılı metriklerin (`DCC`, `NOM`, `DSC`) kontrolsüz büyümesi, anlaşılabilirliği tamamen baltalamıştır.
* **Extendibility (Genişletilebilirlik):** Baseline sürümde `0.89` olan genişletilebilirlik, v1.5.3'te `0.49` seviyesine inerek **%53.8** oranında erimiştir. Bu düşüşün arkasındaki temel neden, soyutlama oranının (`ANA`: 0.61'den 0.32'ye) sert bir şekilde düşmesi ve nesneler arası bağın (`DCC`: 2.34'den 3.03'e) artmasıdır.

---

## 2. Bakım Yapılabilirlik (Maintainability) Analizi

Veriler ışığında JGraphT kütüphanesinin **bakım kolaylığı ciddi ölçüde zorlaşmıştır.**

* **Anlaşılabilirlik ve Karmaşıklık Bariyeri:** Sınıf başına ortalama metot karmaşıklığı (`WMC_mean`) `10.36` seviyesinden `15.78` seviyesine yükselmiştir. Sınıf sayısı (`num_classes`) 238'den 618'e çıkarken metot sayılarının (`NOM`: 5.15 -> 6.32) ve karmaşıklığın eş zamanlı artması, yeni bir geliştiricinin kodu anlamasını zorlaştırmaktadır.
* **Gevşek Bağlılık (Coupling) Kaybı:** Sınıflar arası doğrudan çağrıları gösteren `CBO_mean` değeri `2.34`'ten `3.03`'e çıkmıştır. Benzer şekilde QMOOD `DCC` metriği भी `2.34`'ten `3.03`'e yükselmiştir. Bu durum, sistemdeki bileşenlerin birbirine daha bağımlı hale geldiğini ve bir sınıfta yapılacak değişikliğin beklenmedik yan etkilere (ripple effect) yol açma riskini artırdığını gösterir.
* **Uyum (Cohesion) Erimesi:** QMOOD `CAM` (Cohesion) metriği `0.4070` seviyesinden `0.3660` seviyesine düşmüştür. CK metriği olan `LCOM_mean` (Lack of Cohesion in Methods) ise `13.75` değerinden `31.23` değerine **iki katından fazla** artmıştır. Yüksek LCOM, sınıfların tek bir sorumluluğa odaklanmak yerine, birbiriyle ilişkisiz işleri bir arada barındırmaya başladığının kesin bir kanıtıdır.

---

## 3. Teknik Borç (Technical Debt) Tahmini

JGraphT metriklerindeki eğilimler, kütüphanenin büyürken ciddi bir teknik borç biriktirdiğini doğrulamaktadır:
v0.9.0 [LCOM: 13.75 | CBO: 2.34 | CAM: 0.40]
└── Büyüme ve Mimari Dejenerasyon ──>
v1.5.3 [LCOM: 31.23 | CBO: 3.03 | CAM: 0.36]

* **v1.1.0 Sürümündeki Kırılma Noktası:** Teknik borç birikimi özellikle v1.1.0 sürümünde tepe noktası yapmıştır. Bu sürümde `LCOM_mean` aniden `11.82`'den `24.69`'a fırlamış, `CBO_mean` ise `2.56`'dan `2.87`'ye yükselmiştir. Bu fazda, tasarıma dikkat edilmeden hızlıca özellik eklendiği anlaşılmaktadır.
* **Kapsülleme ve Kalıtım Borcu:** `DAM` (Kapsülleme) metriği `0.89` seviyelerinde stabil kalsa da, kalıtım yoluyla fonksiyonel kazancı gösteren `MFA` metriği `0.24`'ten `0.15`'e gerilemiştir. Geliştiriciler kalıtım yerine kompozisyona (`MOA`: 0.37 -> 0.70) yönelmiştir; ancak bu yönelim doğru yönetilemediği için mesajlaşma karmaşıklığını (`MPC_mean`: 8.66 -> 16.85) iki katına çıkarmıştır.

---

## 4. Refactoring Önerileri

Mevcut teknik borcu azaltmak ve tasarımı stabilize etmek adına şu somut adımlar atılmalıdır:

1.  **LCOM ve CAM Odaklı Sınıf Bölme (Extract Class):** `LCOM_mean` değerinin 31.23'e fırlamış olması, acil müdahale gerektirir. Cohesion (uyum) değeri düşük (`CAM` < 0.35 olan) "Tanrı Sınıflar" (God Classes), **Single Responsibility Principle** uyarınca daha küçük, odaklanmış sınıflara bölünmelidir.
2.  **Bağımlılık Detoksifikasyonu (Reduce Coupling):** `CBO_mean` değerini 3.00 eşiğinin altına indirmek için, sınıflar arası doğrudan bağımlılıklar (tight coupling) azaltılmalıdır. **Dependency Inversion** prensibi uygulanarak somut sınıflar yerine arayüzler (Interfaces) üzerinden iletişim teşvik edilmelidir.
3.  **Metot Seviyesi Refactoring (Extract Method / Decompose Conditional):** Sınıf başına karmaşıklığı belirten `WMC_mean` (15.78) ve metot çağrı sayısını belirten `RFC_mean` (11.23'ten 17.25'e yükseliş) değerlerini düşürmek için, uzun ve yoğun mantıksal kırılmalar içeren metotlar alt metotlara parçalanmalıdır.

---

## 5. Mimari Kalite Yorumu (Architectural Erosion)

Veriler, JGraphT kütüphanesinde net bir **Mimari Bozulma (Architectural Erosion)** olduğunu göstermektedir.

* **Soyutlama Kaybı:** Yazılım büyüdükçe (`DSC`: 238 -> 618, `NOH`: 35 -> 91), mimarinin esnek kalabilmesi için soyutlama oranının korunması veya artması beklenir. Ancak `ANA` (Soyutlama) metriği **0.6176'dan 0.3204'e yarı yarıya düşmüştür.** Benzer şekilde ortalama kalıtım derinliği (`DIT_mean`) de 0.61'den 0.32'ye gerilemiştir. 
* **Sonuç:** Bu durum, kütüphanenin jenerik ve genişletilebilir bir soyut mimari katmanı inşa etmek yerine, sürekli somut (concrete) alt sınıflar ve birbirini doğrudan çağıran yapılar ekleyerek büyüdüğünü kanıtlar. JGraphT, v0.9.0'daki saf ve akademik graf teorisi soyutlamasından, sürümler ilerledikçe daha karmaşık, bakımı zor ve monolitik bir yapıya doğru evrilmiştir.