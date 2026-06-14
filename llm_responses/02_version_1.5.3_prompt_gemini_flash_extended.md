# JGraphT Sürüm 1.5.3 Mimari ve Tasarım Kalitesi Değerlendirme Raporu

Bu rapor, `jgrapht-core` modülünün **1.5.3** sürümüne ait yapısal tasarım verilerini nesne yönelimli metrikler (CK Metrikleri) ve QMOOD (Quality Model for Object-Oriented Design) kalite modeli çerçevesinde inceleyen, kıdemli yazılım mimarı perspektifiyle hazırlanmış eleştirel ve kanıt temelli bir teknik analizdir.

---

## 1. Genel Mimari Profil ve Durum Analizi

JGraphT 1.5.3 sürümü, toplam **618 sınıflık** (DSC / num_classes) hacmiyle kütüphanenin evrimindeki en büyük ve en olgun dikey genişleme noktalarından birini temsil etmektedir. Sistem düzeyindeki ortalamalar ve yapısal dağılımlar incelendiğinde şu temel mimari nitelikler tespit edilmiştir:

* **Veri Gizleme ve Kapsülleme Başarısı:** Sistem genelinde kapsülleme seviyesi (DAM = 0.8850) oldukça yüksektir. Sınıflar, içsel durumlarını (internal state) dış dünyadan izole etmeyi büyük ölçüde başarmaktadır.
* **Kalıtım Yerine Kompozisyon Tercihi:** Ortalama kalıtım derinliği (DIT_mean / ANA = 0.3204) ve kalıtım yoluyla metotların yeniden kullanılma oranı (MFA = 0.1512) düşüktür. Buna karşın nesne kompozisyonu (MOA = 0.7006 ve DAC_mean = 0.7006) oldukça yoğundur. Sistem, yapısal genişlemeyi kalıtım hiyerarşileri kurarak değil, nesneleri birbirine agregate ederek çözmeyi gelenek haline getirmiştir.
* **Metrik İllüzyonları (Hacim Baskısı):** Reusability (310.4459) ve Functionality (157.7334) ham skorlarının yüksek görünmesi yapısal kaliteden değil, QMOOD formüllerindeki sınıf sayısı (DSC = 618.0) çarpanının doğrusal büyüklüğünden kaynaklanan matematiksel bir anomalidir.

---

## 2. En Zayıf 2 Kalite Niteliği ve Sorumlu Metrikler

Sayısal veriler derinlemesine incelendiğinde, JGraphT 1.5.3 sürümünün sürdürülebilirliğini ve bakımını en çok tehdit eden iki zayıf kalite alanı **Understandability** ve **Extendibility** olarak öne çıkmaktadır.

### A. Anlaşılabilirlik (Understandability = -207.8903)
Sistemde negatif yönlü mutlak değer olarak en yüksek ve kriz seviyesindeki niteliktir.
* **Formülasyon Analizi:** `Understandability = -0.33*(ANA+DCC+NOP+NOM+DSC) + 0.33*(DAM+CAM)`
* **Sorumlu Metrikler ve Gerekçeler:** Denklemde negatif ağırlığa sahip olan sınıf sayısı (DSC = 618.0), sınıflar arası doğrudan bağımlılık (DCC = 3.0324) ve sınıf başına ortalama metot sayısı (NOM = 6.3236), pozitif etkiye sahip olan kapsülleme (DAM = 0.8850) ve eşbirliktelik (CAM = 0.3660) değerlerini tamamen domine etmektedir.
* **CK Metrik Kanıtları:** Sınıfların iç odaklanmasını gösteren CAM değerinin 0.3660 gibi düşük bir seviyede kalması, koddaki yapısal dağınıklığı doğrulamaktadır. Daha da önemlisi, ortalama metot uyuşmazlığı (LCOM_mean = 31.2379) sistem genelinde metotların aynı değişken setleri üzerinde çalışmadığını göstererek anlaşılabilirliği baltalamaktadır.

### B. Genişletilebilirlik (Extendibility = 0.4923)
Sistemin mimari kırılganlığını en net ortaya koyan, sıfır sınırına hapsolmuş en zayıf pozitif niteliktir.
* **Formülasyon Analizi:** `Extendibility = 0.50*(ANA+MFA+NOP) - 0.50*DCC`
* **Sorumlu Metrikler ve Gerekçeler:** Sistemin soyutlama seviyesi (ANA = 0.3204) ve kalıtım etkinliği (MFA = 0.1512) kritik derecede düşüktür. Sınıflar arası sıkı bağlılık yükü (DCC = 3.0324), formülün sol tarafındaki zayıf soyutlama toplamını tek başına sıfırlamaya yaklaşmaktadır. Sistemin genişletilebilirlik puanını tamamen çöküşten kurtaran yegane unsur polimorfizm (NOP = 3.5453) yoğunluğudur. Soyut mimari zayıf olduğu için, somut sınıflar arasındaki bu DCC baskısı yeni özellik eklemeyi ciddi şekilde zorlaştırmaktadır.

---

## 3. CK Maksimum (Outlier) Değerleri ve Teknik Borç Analizi

Ortalama (mean) metrikler sistem genelini gösterse de, maksimum (`_max`) uç değerler mimarideki yapısal bozulmaları (Architectural Erosion) ve biriken teknik borcu (Technical Debt) açıkça kanıtlamaktadır:

1.  **LCOM_max = 4371 (Kritik Kohezyon Kaybı):** Ortalama LCOM değeri 31.23 iken, uç değerin 4371 olması sistemde en az bir adet devasa **"Tanrı Sınıf" (God Class)** olduğunu gösterir. Bu sınıf, birbiriyle hiçbir ilişkisi olmayan yüzlerce sorumluluğu tek bir çatı altında toplayarak Tek Sorumluluk İlkesini (SRP) tamamen çiğnemiştir.
2.  **WMC_max = 381 (Aşırı Karmaşıklık Katsayısı):** En yüksek ağırlıklı metot karmaşıklığının 381 olması, merkezdeki bir sınıfın içinde yüzlerce dallanma (`if-else`, `switch`, döngü) barındığını gösterir. Bu durum, o sınıfa ait birim testlerinin (unit test) yazılmasını ve doğrulanmasını imkansız hale verir.
3.  **MPC_max = 401 ve RFC_max = 149 (Merkezi Bağımlılık Hub'ı):** Bir sınıfın dış dünyaya 401 farklı mesaj göndermesi (MPC) ve anlık erişebileceği metot havuzunun 149 olması (RFC), bu sınıfın sistemde her şeye dokunan dikey bir monolit (Hub Class) haline geldiğini kanıtlar. Bu düğümde yaşanacak bir hata tüm kütüphaneyi çökertebilecek domino etkisine sahiptir.

---

## 4. Somut ve Metrik Temelli 3 Refactoring Önerisi

Tespit edilen bu anomalileri gidermek ve kütüphanenin sürdürülebilirliğini güvenceye almak için şu 3 somut yeniden yapılandırma (refactoring) adımı atılmalıdır:

### Öneri 1: Tanrı Sınıfların Sorumluluklarına Göre Parçalanması (Extract Class)
* **Hedef Metrikler:** LCOM_max (4371) değerini radikal şekilde düşürmek, CAM (0.3660) değerini yükseltmek ve `Understandability` puanını iyileştirmek.
* **Uygulama:** LCOM değeri binlerin üzerinde olan o uç sınıflar (büyük olasılıkla çekirdek graf yönetim veya genel amaçlı algoritma sınıfları) izole edilmelidir. Sınıf içindeki metotlar ve kullandıkları global değişkenler haritalandırılmalı, birbiriyle ortak durum (state) paylaşmayan işlevler mantıksal sınırlarına göre yeni ve bağımsız küçük sınıflara (Extract Class) aktarılmalıdır.

### Öneri 2: Koşullu Mantık Bloklarının Polimorfizme Devredilmesi (Replace Conditional with Polymorphism)
* **Hedef Metrikler:** WMC_max (381) ve WMC_mean (15.78) değerlerini aşağı çekmek; ANA (0.3204) ve MFA (0.1512) değerlerini artırarak `Extendibility` bariyerini aşmak.
* **Uygulama:** Graf tiplerinin varyasyonlarına (yönlü, yönsüz, ağırlıklı, pseudo vb.) göre metotlar içerisinde dikey olarak büyüyen devasa `if-else` veya `switch-case` blokları temizlenmelidir. Bu varyasyonlar, ortak bir arayüz (Interface) arkasına saklanmalı ve her bir özel davranış biçimi polimorfik alt somut sınıflara (concrete subclasses) dağıtılmalıdır. Karmaşıklık dikey kontrol bloklarından yatay soyutlamaya kaydırılmalıdır.

### Öneri 3: Mesaj Trafiğinin Sınırlandırılması ve Bağımlılık İzolasyonu (Introduce Facade / Dependency Injection)
* **Hedef Metrikler:** MPC_max (401), RFC_max (149) ve DCC / CBO_mean (3.0324) bağımlılık yükünü hafifletmek.
* **Uygulama:** Diğer sınıflara aşırı derecede mesaj gönderen dikey merkez sınıfların önüne bir soyutlama sınır hattı (Interface katmanı veya Facade tasarım kalıbı) kurulmalıdır. Sınıfların birbirlerinin somut iç metot implementasyonlarına doğrudan bağımlı olması (CBO) engellenmeli, haberleşme gevşek bağlı (loosely coupled) arayüz mimarileri üzerinden yürütülerek dikey çağrı trafiği (MPC) kırılmalıdır.