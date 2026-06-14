# JGraphT (Sürüm 1.5.2 -> 1.5.3) Yapısal Evrim ve Mimari Kalite Analiz Raporu

Bu rapor, `jgrapht-core` modülünün **1.5.2** sürümünden **1.5.3** sürümüne geçiş sürecindeki mimari değişiklikleri, kantitatif tasarım metrikleri ve QMOOD (Quality Model for Object-Oriented Design) denklemleri çerçevesinde inceleyen, kıdemli bir yazılım mimarı gözüyle hazırlanmış kanıt temelli bir kalite değerlendirmesidir.

---

## 1. Tasarım Metriklerindeki Değişimlerin Mimari Anatomisi

Sürüm 1.5.2 ile 1.5.3 arasındaki metrik değişimleri incelendiğinde, projenin oldukça kontrollü, kararlı ve "refactoring odaklı" bir olgunlaşma evresinde olduğu görülmektedir. Metrik gruplarının analizi şu şekildedir:

### A. Kontrollü Hacim Genişlemesi ve Modüler Yapılanma (DSC, NOH, NOM)
* **DSC (Boyut):** Sınıf sayısı %2.8 artarak **601'den 618'e** (17 yeni sınıf) çıkmıştır. Bu, kütüphaneye yeni yetenekler eklendiğini gösteren makul bir dikey büyümedir.
* **NOH (Hiyerarşi):** Hiyerarşi sayısı %4.6 artışla **87'den 91'e** (4 yeni kök sınıf/soyutlama ağacı) yükselmiştir. Hiyerarşideki büyüme oranının (%4.6), sınıf sayısı büyüme oranından (%2.8) fazla olması, yeni işlevlerin mevcut sınıfların içine yığılmadığını; tam aksine yeni, izole mimari ağaçlar kurularak sisteme entegre edildiğini kanıtlar.
* **NOM (Metot Yoğunluğu):** Sınıf başına ortalama metot karmaşıklığı %0.5 gibi çok minimal bir artışla **6.293'ten 6.324'e** çıkmıştır. Bu kararlılık, yeni sınıfların hafif (lightweight) tasarlandığının işaretidir.

### B. Bağımlılık Yönetimi ve Kapsülleme Başarısı (DCC, DAM, CAM)
* **DCC (Coupling/Bağımlılık):** Sisteme 17 yeni sınıf eklenmesine rağmen, sınıflar arası sıkı bağlılık katsayısı sadece %0.3 artarak **3.023'ten 3.032'ye** çıkmıştır. Yeni modüllerin mevcut sisteme spagetti bağlar yerine gevşek bağlı (loosely coupled) entegre edilmesi **çok başarılı bir mimari disiplindir**.
* **DAM (Kapsülleme) & CAM (Cohesion):** Veri gizleme oranı %0.5 artarak **0.881'den 0.885'e** yükselirken; metot bütünlüğü (cohesion) %0.7 artışla **0.363'ten 0.366'ya** çıkmıştır. İki metrikteki pozitif ivme, sınıfların iç kalitesinin ve Single Responsibility (Tek Sorumluluk) uyumunun bu sürümde iyileştirilmeye çalışıldığını doğrular.

### C. Nesne İlişkileri ve Genişleme Kabiliyeti (MOA, NOP, ANA, MFA)
* **MOA (Kompozisyon) & NOP (Polimorfizm):** Nesne kompozisyonu kullanımı %1.0 artarak **0.694'ten 0.701'e** çıkarken; polimorfizm oranı %1.1 yükselerek **3.507'den 3.545'e** ulaşmıştır. Bu artışlar, kütüphanenin nesne yönelimli esneklik mekanizmalarını daha aktif kullanmaya başladığını gösterir.
* **ANA (Soyutlama) & MFA (Kalıtım):** Soyutlama seviyesi (%0.3) ve fonksiyonel kalıtım etkinliği (%0.1) neredeyse tamamen sabit kalmıştır. Tasarımın soyut iskeleti korunmuştur.

---

## 2. QMOOD Kalite Nitelikleri Açısından Değerlendirme

Tasarım metriklerindeki bu değişimlerin QMOOD denklemleri üzerindeki net etkileri olumlu ve olumsuz yönleriyle aşağıda analiz edilmiştir:

### ▲ Olumlu Gelişen Kalite Nitelikleri

* **Functionality (Fonksiyonellik) & Reusability (Yeniden Kullanılabilirlik):**
  * *İlgili Metrikler:* DSC (+%2.8), NOH (+%4.6), NOP (+%1.1), CAM (+%0.7).
  * *Mimari Yorum:* Sistemin fonksiyonel yeteneği (Functionality) ve kütüphane bileşenlerinin yeniden kullanılabilirliği (Reusability) net bir şekilde **olumlu** etkilenmiştir. Formüllerde çarpan ağırlığı yüksek olan sınıf sayısının (DSC) ve polimorfizmin (NOP) artması, kararlı bağımlılık seviyesiyle (DCC %0.3) birleştiğinde kütüphanenin servis kapasitesini güvenli bir şekilde büyütmüştür.
* **Flexibility (Esneklik) & Effectiveness (Etkinlik):**
  * *İlgili Metrikler:* DAM (+%0.5), MOA (+%1.0), NOP (+%1.1).
  * *Mimari Yorum:* Değişime direnç göstermeme kabiliyeti (Flexibility) artmıştır. Esnekliğin ana motorları olan kompozisyon (MOA) ve polimorfik metot çeşitliliğinin (NOP) eşzamanlı yükselmesi, kodun sertleşmeden (rigidity) büyümesini sağlamıştır.

### ▼ Olumsuz Gelişen Kalite Nitelikleri

* **Understandability (Anlaşılabilirlik):**
  * *Denklem:* $-0.33 \cdot (ANA+DCC+NOP+NOM+DSC) + 0.33 \cdot (DAM+CAM)$
  * *Mimari Yorum:* Sistemin anlaşılabilirliği bu sürüm geçişinde de **olumsuz** etkilenmeye devam etmiştir. Her ne kadar CAM (+%0.7) ve DAM (+%0.5) pozitif katkı sunsa da, formülün negatif parantezindeki kümülatif büyüme (özellikle DSC'deki %2.8'lik ve NOP'taki %1.1'lik artış) bu kazanımları sıfırlamaktadır. Sınıf sayısı 618'e ulaşan bir sistemde bilişsel yük (cognitive load) kaçınılmaz olarak artmaktadır.

---

## 3. Teknik Borç (Technical Debt) İşaretleri

JGraphT 1.5.3 sürümü genel olarak "temiz" bir büyüme sergilese de, derinlerde biriken kronik mimari borçlanma emareleri barındırmaktadır:

1.  **Düşük Cohesion Temeli (CAM = 0.366):** CAM değerindeki %0.7'lik iyileşme olumludur ancak metriğin absolute değeri (0.366) hala endüstriyel standartların (0.50 ve üzeri) oldukça altındadır. Bu durum, iyileşme çabalarına rağmen sınıfların içindeki metotların heterojen olduğunu ve sistemde hala temizlenmemiş "Çok Sorumluluklu" yapılar bulunduğunu gösterir.
2.  **Statik Soyutlama Blokajı (ANA & MFA = %0):** Soyutlama (ANA) ve Kalıtım (MFA) verilerinin neredeyse hiç değişmemesi, projenin temel mimari sözleşmelerinin (Core Interfaces/Abstract Classes) yeni eklenen 17 sınıfa yön veremediğini gösterir. Geliştiriciler esnekliği üst seviye mimariyi değiştirerek değil, sadece alt uçlarda polimorfik (NOP) metotlar ezerek (overriding) çözmektedir. Bu durum uzun vadede hiyerarşi kırılganlığı riskini sürdürmektedir.

---

## 4. Sonuç ve Yeniden Yapılandırma (Refactoring) Önerileri

**Sonuç Özet:** JGraphT 1.5.2 -> 1.5.3 geçişi, kütüphanenin sağlığı açısından **net bir şekilde OLUMLU** bir adımdır. Boyut büyürken bağımlılıkların (DCC) dizginlenmesi, polimorfizm ve kompozisyonun artırılması sistem olgunluğunun kanıtıdır. `Understandability` kaybı ise kontrolsüz bir erozyondan değil, hacim büyümesinin doğal bir sonucudur.

### Mevcut Yapıyı İyileştirmek İçin 3 Somut Öneri:

1.  **Arayüz İnceltme (Interface Refinement / Role Interfaces):**
    * *Hedef:* `Understandability` değerini düzeltmek ve CAM'i kararlı bir şekilde yükseltmek.
    * *Uygulama:* CAM değeri 0.36 seviyesinde olan çok metotlu sınıfların sunduğu geniş arayüzler (CIS = 4.225), Interface Segregation Principle (Arayüz Ayrımı İlkesi) uyarınca daha spesifik, role özgü küçük arayüzlere bölünmelidir.
2.  **Yatay Soyutlama Katmanlarının Genişletilmesi (Extend Abstraction):**
    * *Hedef:* Sabit kalan ANA (0.320) ve MFA (0.151) metriklerini yukarı çekerek mimari kararlılığı artırmak.
    * *Uygulama:* Yeni eklenen 4 hiyerarşi (NOH) incelenmeli, eğer bu yapılar benzer graf manipülasyonları yapıyorsa, kütüphanenin çekirdeğindeki soyut sınıflardan türetilmeli, mimari şablon kalıpları (Template Method Pattern) kullanılarak kalıtım etkinliği (MFA) artırılmalıdır.
3.  **Metot Gövdesi Optimizasyonu (Extract Method / Inline Method):**
    * *Hedef:* NOM (6.324) metriğinin büyüme hızını durdurmak ve sınıf içi karmaşıklığı azaltmak.
    * *Uygulama:* Sınıf başına metot ortalamasını düşürmek adına, yeni eklenen sınıflardaki aşırı özelleşmiş ve tek bir noktadan çağrılan küçük yardımcı metotlar (private helper methods) gözden geçirilmeli; mantıksal bütünlüğü bozmayacak şekilde ana metot gövdeleriyle birleştirilmeli veya bağımsız strateji sınıflarına (Strategy Pattern) devredilmelidir.