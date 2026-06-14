# JGraphT Mimari Kalite ve QMOOD Metrikleri Değerlendirme Raporu

**Hazırlayan:** Kıdemli Yazılım Mimarisi ve Kalite Uzmanı
**İncelenen Sistem:** JGraphT (v0.9.0 - v1.5.3)

Bu rapor, JGraphT kütüphanesinin zaman içindeki mimari evrimini QMOOD (Quality Model for Object-Oriented Design) ve CK (Chidamber & Kemerer) metriklerine dayanarak eleştirel ve kanıt temelli olarak incelemektedir.

---

## 1. GENEL KALİTE DEĞERLENDİRMESİ

Sürümler boyunca sistemin hacmi (DSC - Sınıf Sayısı) **238'den 618'e** çıkarak neredeyse üç katına ulaşmıştır. Bu ciddi büyüme, kalite niteliklerinde kutuplaşmalara yol açmıştır:

* **Gelişen Nitelikler:**
    * **Reusability (Yeniden Kullanılabilirlik) (+%73):** Normalize değere göre 1.0000'dan 1.7392'ye yükselmiştir. Bu artışın ana itici gücü, formüldeki en büyük ağırlığa sahip olan sınıf sayısındaki (DSC) devasa artış ve arayüz/mesajlaşma (CIS) metriklerinin yüksekliğidir.
    * **Functionality (İşlevsellik) (+%72):** Benzer şekilde DSC ve NOP (Polimorfizm) artışından beslenerek 1.0000'dan 1.7266'ya çıkmıştır. Kütüphaneye yeni algoritmalar ve veri yapıları eklendikçe işlevsellik doğal olarak artmıştır.
* **Bozulan Nitelikler:**
    * **Extendibility (Genişletilebilirlik) (-%54):** 1.0000'dan 0.4617'ye keskin bir düşüş yaşamıştır. Formüle baktığımızda ($Extendibility = 0.50 \times (ANA+MFA+NOP) - 0.50 \times DCC$), bu çöküşün temel nedeninin **ANA (Soyutlama)** oranının **0.61'den 0.32'ye** yarı yarıya düşmesi ve **DCC (Coupling/Bağımlılık)** oranının **2.34'ten 3.03'e** çıkması olduğu açıkça görülmektedir.
    * **Understandability (Anlaşılabilirlik) (-%60):** Normalize değer -0.99'dan -1.59'a gerileyerek negatif yönde büyümüştür. Sınıf sayısının (DSC) artması, karmaşıklığın (NOM) **5.15'ten 6.32'ye** çıkması ve soyutlamanın azalması sistemi anlamayı zorlaştırmıştır.

---

## 2. BAKIM YAPILABİLİRLİK (MAINTAINABILITY) ANALİZİ

Bakım yapılabilirlik; sistemin anlaşılabilirliği, esnekliği, modüller arası bağımlılığı (coupling) ve modül içi tutarlılığı (cohesion) ekseninde değerlendirilmelidir. **Metrikler, bakımın giderek zorlaştığını göstermektedir.**

* **Coupling ve Cohesion Çıkmazı:** Sınıflar arası bağımlılık (DCC/CBO) **2.34'ten 3.03'e** yükselirken, sınıfların kendi içindeki tutarlılığını ifade eden CAM (Cohesion Among Methods) metrisi **0.40'tan 0.36'ya** düşmüştür. Yani sınıflar dışarıya daha bağımlı, kendi içlerinde ise daha kopuk hale gelmiştir.
* **Paradigma Kayması ve Flexibility (Esneklik):** Flexibility değerinde bir artış (1.0000 -> 1.4017) gözlemlenmektedir. Bunun temel sebebi, kalıtım (MFA) oranının **0.24'ten 0.15'e** düşerken, kompozisyon (MOA) oranının **0.37'den 0.70'e** çıkmasıdır. Geliştirici ekip *kalıtım yerine kompozisyonu (favor composition over inheritance)* tercih etmiş, bu da esnekliği artırmıştır; ancak azalan cohesion (CAM) bu esnekliğin bakım maliyetini yükseltmektedir.

---

## 3. TEKNİK BORÇ (TECHNICAL DEBT) TAHMİNİ

CK metriklerindeki dramatik artışlar, sistemde ciddi bir yapısal teknik borç birikimi olduğuna işaret etmektedir:

* **LCOM (Sınıf İçi Metotların Uyumsuzluğu) Patlaması:** LCOM değeri v0.9.0'da **13.75** iken v1.5.3'te **31.23'e** fırlamıştır. Bu, "God Object" (Her şeyi yapan devasa sınıflar) anti-örüntüsünün oluştuğunun en net kanıtıdır. Sınıflar, aralarında veri paylaşmayan alakasız metotlarla dolmuştur.
* **WMC ve RFC Artışı:** Sınıf başına düşen ortalama karmaşıklık (WMC) **10.36'dan 15.78'e** (%50 artış), bir sınıfın dış dünyaya verdiği tepki kümesi (RFC) ise **11.23'ten 17.25'e** çıkmıştır.
* **Sonuç:** Düşen CAM, artan LCOM ve CBO birleştiğinde; codebase içinde yapılacak bir değişikliğin başka yerleri bozma (regression) ihtimali oldukça artmış, bu da teknik borcun "faizini" yükseltmiştir.

---

## 4. REFACTORING ÖNERİLERİ

Veriler ışığında JGraphT mimarisini rahatlatmak için şu somut adımlar atılmalıdır:

1.  **LCOM ve WMC'yi Düşürmek İçin 'Extract Class':** LCOM'un 31.23'e fırlaması Single Responsibility (Tek Sorumluluk) prensibinin ihlal edildiğini gösterir. Özellik kümesi şişkin sınıflar tespit edilip, alt mantıksal sınıflara bölünmelidir.
2.  **Düşen 'ANA' Metriğini Dengelemek İçin Soyutlamayı Artırmak:** ANA değeri 0.61'den 0.32'ye düşmüştür. Yeni algoritmalar doğrudan somut sınıflar (concrete classes) olarak eklenmiş gibi görünüyor. Ortak graf davranışları için yeni `Interface` veya `Abstract Class` yapıları kurgulanarak Extendibility (Genişletilebilirlik) kurtarılmalıdır.
3.  **Bağımlılıkları Yönetmek (CBO/DCC İyileştirmesi):** RFC'nin 17.25'e çıkması sınıfların birbirinin metotlarını çok fazla çağırdığını gösterir. *Dependency Injection* (Bağımlılık Enjeksiyonu) ve *Facade* tasarım kalıpları kullanılarak sınıflar arası sıkı bağlar (tight coupling) gevşetilebilir.

---

## 5. MİMARİ KALİTE YORUMU (Architectural Erosion)

Sistem hacmi (DSC) büyürken, mimaride belirgin bir **kısmi yozlaşma (architectural erosion)** belirtisi vardır.

Yozlaşmanın en büyük göstergesi **LCOM'daki devasa kontrolsüz büyümedir.** Ancak her metrik değişimi kötüye yorulmamalıdır; DIT (Kalıtım Derinliği) ve MFA (Kalıtım Oranı) düşerken MOA'nın (Kompozisyon) artması, ekibin bilinçli bir mimari karar alarak modern tasarım standartlarına (kompozisyon tabanlı yapı) geçtiğini gösteriyor olabilir.

**Özetle:** JGraphT, sürümler boyunca yetenek ve işlevsellik olarak çok güçlenmiş (Functionality), daha esnek parçalara ayrılmış (MOA artışı); ancak bu büyüme, kodun kendi içindeki odaklılığını kaybetmesine (LCOM ve CAM bozulması) ve soyutlama katmanının zayıflamasına (ANA ve Extendibility çöküşü) neden olarak ciddi bir mimari erozyon ve teknik borç yaratmıştır.