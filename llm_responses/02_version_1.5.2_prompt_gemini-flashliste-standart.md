# JGraphT 1.5.2 Sürümü Teknik Kalite ve Mimari Değerlendirme Raporu

**Rol:** Yazılım Mimarisi ve Kalite Uzmanı
**Analiz Konusu:** JGraphT 1.5.2 (QMOOD ve CK Metrikleri)

---

## 1. Genel Kalite Değerlendirmesi
JGraphT 1.5.2 sürümü, kütüphanenin yüksek bir fonksiyonel (153.10) kapasiteye ulaştığını ancak bu büyümenin beraberinde önemli bir yapısal teknik borç getirdiğini göstermektedir. 601 sınıfın yönetildiği sistemde, özellikle `Understandability` değerindeki dramatik negatiflik, sürdürülebilirlik açısından alarm seviyesindedir.

## 2. En Zayıf 2 Kalite Niteliği ve Sorumlu Metrikler

Sistemin mevcut mimari sağlığı üzerindeki en kritik iki zayıflık şunlardır:

### A. Understandability (Anlaşılabilirlik) | Skoru: -202.26
Sistemin en zayıf halkasıdır. Negatif değer, kodun okunabilirliğinin ve bilişsel yükünün yönetilemez noktaya yaklaştığını gösterir.
* **Sorumlu Metrikler:**
    * **DSC (601.0):** Boyutun büyüklüğü, QMOOD denkleminde negatif katsayı ile ağırlıklandığı için skorun düşüşüne doğrudan neden olmaktadır.
    * **LCOM_max (4371) ve LCOM_mean (30.22):** LCOM değerlerinin bu denli yüksek olması, sınıfların tek bir amaca hizmet etmediğini ve uyumsuz (low cohesion) metodlar içerdiğini kanıtlar.

### B. Extendibility (Genişletilebilirlik) | Skoru: 0.477
Yeni özellik eklemenin maliyetinin, sistemin karmaşıklığı nedeniyle çok yükseldiğini göstermektedir.
* **Sorumlu Metrikler:**
    * **ANA (0.3195):** Soyutlama seviyesinin düşüklüğü, sistemin hiyerarşik esnekliğinin zayıf olduğunu ve somut uygulamalara bağımlılığın arttığını gösterir.
    * **DCC (3.0233):** Sınıflar arası sıkı bağımlılık (coupling), bir parçada yapılacak değişikliğin beklenmedik yan etkilere neden olacağını (ripple effect) kanıtlar.



---

## 3. Somut Refactoring Önerileri

Veri setindeki CK metriklerini baz alarak, sürdürülebilirliği artırmak için şu 3 adım önceliklendirilmelidir:

1.  **"God Class" Ayrıştırma (Split Responsibility):** `WMC_max (381)` ve `LCOM_max (4371)` değerlerine sahip sınıflar, "Tek Sorumluluk İlkesi"ni (SRP) ağır şekilde ihlal etmektedir. Bu sınıfların *Extract Class* tekniği ile, ilgili mantıksal metod gruplarına göre daha küçük, özelleşmiş sınıflara ayrılması şarttır.

2.  **Soyutlama Katmanlarını Güçlendirme (Increase Abstraction):** `ANA (0.3195)` değerini yükseltmek için, somut sınıf bağımlılıkları *Interface* (Arayüz) veya *Abstract Class* yapılarına taşınmalıdır. Bu, `Extendibility` değerini artıracak ve kodun test edilebilirliğini kolaylaştıracaktır.

3.  **Bağımlılıkları Azaltma (Reduce Coupling):** `RFC_max (149)` değeri, sınıfların çok fazla başka sınıfa bağımlı olduğunu gösterir. `DCC` metriğini düşürmek için *Dependency Injection* desenleri gözden geçirilmeli ve sınıf içindeki karmaşık metod çağrı zincirleri "Law of Demeter" prensibine uygun olarak kısaltılmalıdır.

---
*Not: Bu değerlendirme Bansiya & Davis (2002) QMOOD modeli ve Chidamber & Kemerer metrikleri temel alınarak, JGraphT 1.5.2 sürümünün sayısal verileri üzerinden yapılmıştır.*