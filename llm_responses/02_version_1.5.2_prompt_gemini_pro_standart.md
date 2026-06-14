# JGraphT v1.5.2 Sürümü Mimari Kalite ve Tasarım Metrikleri Değerlendirme Raporu

**Değerlendirmeyi Yapan:** Kıdemli Yazılım Mimarisi ve Yazılım Kalitesi Uzmanı
**İncelenen Sürüm:** JGraphT v1.5.2 (jgrapht-core)

---

## 1. Genel Kalite Değerlendirmesi

JGraphT v1.5.2 sürümü, sistem boyutu (`DSC = 601.0` sınıf) ve kapsülleme oranının gücü (`DAM = 0.8806`) ile oldukça geniş ve veri gizleme prensiplerine sadık bir kütüphane profili sergilemektedir. Sistemdeki bu hacim ve kompozisyon gücü (`MOA = 0.6938`), sistemin dışarıdan kullanımını cazip kılarak **Reusability (Yeniden Kullanılabilirlik: 301.939)** ve **Functionality (İşlevsellik: 153.101)** metriklerini oldukça yüksek seviyelere taşımıştır.

Ancak ortalama (mean) ve maksimum (max) CK metrikleri arasındaki devasa uçurumlar, mimarinin iç yapısında ciddi bir erozyon olduğunu kanıtlamaktadır. Sınıf başına ortalama metot sayısı (`NOM_mean = 6.29`) kabul edilebilir görünse de, sistemde 95 metodu olan (`NOM_max = 95`) ve metotlar arası uyumsuzluğun ekstrem seviyelere çıktığı (`LCOM_max = 4371`) devasa sınıflar bulunmaktadır. Bu "God Class" (Her Şeyi Yapan Sınıf) antipaterni, kütüphanenin bakımını içeriden giderek zorlaştırmaktadır.

## 2. En Zayıf 2 Kalite Niteliği ve Sorumlu Metrikler

QMOOD modeline göre v1.5.2 sürümünün en kritik iki zayıf noktası şunlardır:

### A. Understandability (Anlaşılabilirlik): -202.2567
Bu değerin ciddi şekilde negatif olması, sistemin bilişsel yükünün (cognitive load) yönetilemez seviyelere ulaştığına işaret eder.
* **Sorumlu Metrikler:** Formüldeki negatif çarpanlı `-0.33*(ANA+DCC+NOP+NOM+DSC)` bloku bu düşüşün ana nedenidir.
    * Kütüphanenin toplam büyüklüğü (`DSC = 601.0`) doğal olarak anlaşılabilirliği zorlaştırır.
    * Sınıflar arası sıkı bağların yüksek olması (`DCC = 3.0233`).
    * Sınıf karmaşıklığının aşırı artışı (`WMC_max = 381` ve `NOM_max = 95`).
* **Yorum:** Negatif etkiyi dengelemesi beklenen sınıf içi uyum (`CAM = 0.3633`) düşük kaldığı için, aşırı karmaşık ve uzun sınıfları okuyup anlamak mimari olarak çok zordur.

### B. Extendibility (Genişletilebilirlik): 0.4774
Sisteme yeni özellikler ekleme kapasitesini gösteren bu metrik oldukça düşüktür ve kod tabanının "kırılgan" (fragile) olduğunu gösterir.
* **Sorumlu Metrikler:** Formül `0.50*(ANA+MFA+NOP) - 0.50*DCC` şeklinde işler.
    * Sistemdeki soyutlama seviyesi yetersizdir (`ANA = 0.3195`). Sınıfların çoğu doğrudan somut gerçekleştirimler barındırmaktadır.
    * Sınıflar arası bağımlılık yüksektir (`DCC = 3.0233`, `CBO_max = 21`).
* **Yorum:** Düşük soyutlama (ANA) ve yüksek kuplaj (DCC) bir araya geldiğinde, mevcut koda dokunmadan yeni özellik eklemek neredeyse imkansız hale gelir. Bir sınıfta yapılacak değişiklik, ona bağlı diğer sınıflarda da (Ripple Effect) zorunlu değişiklikler gerektirecektir.

## 3. Somut ve Metrik-Temelli Refactoring Önerileri

Mimari bozulmayı durdurmak ve iç kaliteyi artırmak için şu 3 hamle acilen uygulanmalıdır:

**1. "God Class" Nesnelerini Parçalama (Extract Class / Single Responsibility)**
* *Kanıt:* `LCOM_mean = 30.22` iken `LCOM_max = 4371` gibi korkunç bir değere ulaşmıştır. Ayrıca `WMC_max = 381` ve `NOM_max = 95` değerleri, sistemde onlarca farklı işi tek başına yapmaya çalışan şişkin sınıflar olduğunu kanıtlar.
* *Aksiyon:* LCOM ve WMC skoru en yüksek olan tepedeki %5'lik sınıf grubu analiz edilmeli. İçerideki metotlar, kullandıkları veri setlerine göre gruplandırılarak yeni ve daha küçük uzman sınıflara (domain classes) bölünmelidir. Bu, doğrudan `CAM` (Uyum) skoru artırarak Anlaşılabilirliği iyileştirecektir.

**2. Soyutlamaları Derinleştirme (Extract Interface / Dependency Inversion)**
* *Kanıt:* Genişletilebilirlik çok düşüktür (`0.4774`) çünkü soyutlama oranı zayıftır (`ANA = 0.3195`) ve bir sınıf 21 farklı sınıfa doğrudan bağlıdır (`CBO_max = 21`).
* *Aksiyon:* Bağımlılığı yüksek olan merkez sınıfların somut referansları (concrete references) incelenmeli. Bu sınıfların üzerine arayüzler (interfaces) inşa edilmeli ve sınıflar arası iletişim doğrudan nesne (instance) üzerinden değil, bu yeni arayüzler üzerinden sağlanmalıdır. Bu hamle `ANA`'yı yükseltip `DCC/CBO`'yu düşürecektir.

**3. Metot Çağrısı Bağımlılığını Azaltma (Move Method / Hide Delegate)**
* *Kanıt:* Sınıfların dışarıya yaptığı metot çağrılarının ortalaması yüksekken (`MPC_mean = 16.78`), maksimumda bir sınıf dışarıya 401 kez çağrı yapmaktadır (`MPC_max = 401`). Bir sınıfın cevap verebildiği küme de aşırı geniştir (`RFC_max = 149`).
* *Aksiyon:* `MPC` değeri çok yüksek sınıflarda, veriyi dışarıdan alıp kendi içinde işleyen (Feature Envy antipaterni) metotlar tespit edilmeli. Bu işlem mantıkları (logic), verinin asıl sahibi olan sınıflara taşınmalı (Move Method). Bu sayede sınıflar arası mesajlaşma trafiği azalacak ve kod daha kapsüllü bir hale gelecektir.