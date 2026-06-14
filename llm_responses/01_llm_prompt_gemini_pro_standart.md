# JGraphT Kütüphanesi QMOOD ve CK Metrikleri Mimari Kalite Değerlendirme Raporu

**Analiz Tarihi:** 14 Haziran 2026
**Değerlendirmeyi Yapan:** Kıdemli Yazılım Mimarisi ve Yazılım Kalitesi Uzmanı
**Kapsam:** JGraphT (jgrapht-core) v0.9.0 - v1.5.3 Sürümleri

---

## 1. GENEL KALİTE DEĞERLENDİRMESİ

Sürümler boyunca (v0.9.0'dan v1.5.3'e) sistemin genel boyutunun (DSC metriği 238'den 618'e) yaklaşık 2.6 kat arttığı görülmektedir. Bu büyüme bazı kalite niteliklerinde iyileşme sağlarken, bazı alanlarda ciddi bozulmalara yol açmıştır:

* **İyileşen Nitelikler:**
    * **Reusability (Yeniden Kullanılabilirlik):** 120.47'den 310.44'e (%157'lik dramatik bir artış) yükselmiştir. Normalize verilere göre temel sürüme kıyasla **1.73** katına çıkmıştır. Bu durum büyük ölçüde sınıf kompozisyonunun (MOA: 0.37'den 0.70'e) ve sistem boyutunun (DSC) artmasından kaynaklanmaktadır.
    * **Functionality (İşlevsellik):** 61.69'dan 157.73'e çıkmıştır. Yeni algoritmalar ve veri yapılarının eklenmesi, hiyerarşideki sınıf sayısını (NOH: 35'ten 91'e) artırarak işlevselliği güçlendirmiştir.
* **Bozulan Nitelikler:**
    * **Understandability (Anlaşılabilirlik):** -81.86'dan -207.89'a gerileyerek ciddi bir kan kaybı yaşamıştır (Normalize: -1.59). Metotların karmaşıklığının (NOM: 5.15'ten 6.32'ye) ve sınıflar arası bağımlılıkların (DCC: 2.34'ten 3.03'e) artması kodun anlaşılmasını matematiksel olarak zorlaştırmıştır.
    * **Extendibility (Genişletilebilirlik):** 0.89'dan 0.49'a (Normalize: 0.46) keskin bir düşüş göstermiştir. Bu düşüşün temel sebebi, sistem büyürken soyutlama oranının (ANA metriği: 0.61'den 0.32'ye) yarı yarıya azalmasıdır.

## 2. BAKIM YAPILABİLİRLİK (MAINTAINABILITY) ANALİZİ

Bakım yapılabilirlik; esneklik, anlaşılabilirlik, kohezyon (uyum) ve kuplaj (bağımlılık) metriklerinin bir fonksiyonudur. JGraphT kütüphanesinde sistem büyüdükçe bakım yapılabilirliğin **zorlaştığı** sayısal verilerle sabittir:

* **Flexibility (Esneklik):** 1.46'dan 1.58'e hafif bir iyileşme (Normalize: 1.40) göstermiştir. Kapsülleme (DAM) 0.89 civarında stabil kalmış, bu da veri gizleme pratiklerinin korunduğunu gösterir. Ancak artan bağımlılık bu esnekliği tehdit etmektedir.
* **Coupling (Bağımlılık) ve Cohesion (Uyum) Paradoksu:** Nesne yönelimli tasarımın altın kuralı olan "Düşük Kuplaj, Yüksek Uyum (Low Coupling, High Cohesion)" prensibi sürümler ilerledikçe ihlal edilmiştir.
    * Sınıflar arası bağımlılık (DCC/CBO) 2.34'ten 3.03'e çıkmıştır.
    * Bunun karşılığında sınıf içi uyum (CAM) 0.40'tan 0.36'ya gerilemiştir.
    * Çok daha kritik olan bulgu: **LCOM_mean** (Lack of Cohesion of Methods) değeri 13.75'ten **31.23'e** fırlamıştır. LCOM'un artması, sınıfların içindeki metotların ortak sınıf değişkenlerini kullanmadığını, yani sınıfların farklı işleri bir arada yapan "parçalı" yapılara dönüştüğünü kanıtlar. Bu durum bakımı ciddi şekilde zorlaştırır.

## 3. TEKNİK BORÇ (TECHNICAL DEBT) TAHMİNİ

Metrik eğilimleri, JGraphT'nin yeni yetenekler kazanırken ciddi bir **tasarımsal teknik borç biriktirdiğine** işaret etmektedir.

1.  **"God Class" (Her Şeyi Yapan Sınıf) Eğilimi:** WMC_mean (Sınıf Başına Karmaşıklık) 10.36'dan 15.78'e, RFC_mean (Sınıfın Tepki Süresi) 11.23'ten 17.25'e çıkmıştır. LCOM'daki %127'lik artışla birleştiğinde, sistemdeki birçok sınıfın çok fazla sorumluluk üstlendiği (Single Responsibility ihlali) ve şiştiği açıktır.
2.  **Soyutlama Borcu:** ANA (Soyutlama Sınıf Sayısı Oranı) 0.61'den 0.32'ye inmiştir. Yeni eklenen özelliklerin arayüzler (interfaces) veya soyut sınıflar (abstract classes) üzerinden değil, doğrudan somut (concrete) sınıflar üzerinden kodlandığı anlaşılmaktadır. Bu, gelecekteki değişikliklerde "Ripple Effect" (dalga etkisi) riskini artırır.

## 4. REFACTORING (YENİDEN YAPILANDIRMA) ÖNERİLERİ

Verilere dayalı olarak acil müdahale gerektiren mimari eylemler şunlardır:

1.  **Büyük Sınıfları Parçalama (Extract Class / Extract Module):**
    * *Kanıt:* LCOM'un 31.23'e ulaşması ve WMC'nin 15.78'e çıkması.
    * *Aksiyon:* Düşük uyuma sahip, LCOM skoru yüksek sınıflar tespit edilmeli ve içerdikleri alt sorumluluklara göre yeni ve daha küçük sınıflara bölünmelidir.
2.  **Soyutlamayı Geri Kazanma (Extract Interface / Extract Superclass):**
    * *Kanıt:* ANA'nın yarı yarıya (0.61 -> 0.32) düşmesi ve Extendibility'nin zayıflaması.
    * *Aksiyon:* Ortak davranışa sahip somut sınıfların üzerine yeni arayüzler tanımlanarak "Program to an interface, not an implementation" (Gerçekleştirmeye değil, arayüze göre programla) prensibi yeniden canlandırılmalıdır.
3.  **Bağımlılıkları Gevşetme (Dependency Injection / Inversion of Control):**
    * *Kanıt:* DCC'nin 3.03'e tırmanması.
    * *Aksiyon:* Doğrudan sınıf örneği (instance) yaratımları yerine bağımlılık enjeksiyonu kullanılarak sınıfların birbiriyle olan sıkı bağları (tight coupling) gevşetilmelidir.

## 5. MİMARİ KALİTE YORUMU (ARCHITECTURAL EROSION)

Veriler, sistem boyutunun (DSC: 238 -> 618) genişlemesiyle birlikte tipik bir **Mimari Aşınma (Architectural Erosion)** sendromunun varlığını kanıtlamaktadır. 

Yazılım, v0.9.0'dan v1.5.3'e geçerken başlangıçtaki iyi soyutlanmış (ANA: 0.61) yapısını kaybetmiş ve kod tabanı genişledikçe somut sınıf yığılmaları oluşmuştur. Artan MOA (Kompozisyon, 0.37 -> 0.70) ve Reusability skorları, kütüphanenin kullanıcılar açısından (dışarıdan) güçlü araçlar sunduğunu gösterse de, kütüphaneyi geliştiren çekirdek ekip için (içeriden) artan LCOM, WMC ve düşen CAM metrikleri kod tabanının yavaş yavaş monolitik, kırılgan ve değiştirilmesi zor bir yapıya (Big Ball of Mud) dönüşmeye başladığının sinyallerini vermektedir. Kütüphane, yeteneklerini artırırken içsel mimari sağlığından taviz vermiştir.