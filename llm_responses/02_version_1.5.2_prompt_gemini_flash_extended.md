# JGraphT Sürüm 1.5.2 Mimari Tasarım ve Mimari Kalite Değerlendirme Raporu

Bu rapor, `jgrapht-core` modülünün **1.5.2** sürümüne ait QMOOD ve CK metrik verilerini temel alarak hazırlanmış eleştirel, kantitatif ve kanıt temelli bir yazılım kalitesi değerlendirmesidir.

---

## 1. Genel Kalite Durum Analizi

JGraphT 1.5.2 sürümü, **601 adet sınıfa** (DSC) ulaşmış, olgun ancak yapısal büyüme baskısı altında olan büyük ölçekli bir kütüphanedir. Metrikler üzerinden sistem genel hatlarıyla incelendiğinde şu mimari karakteristikler öne çıkmaktadır:

* **Güçlü Kapsülleme ve Kompozisyon:** Sınıf düzeyinde veri gizleme oranı oldukça yüksektir (DAM = 0.8806). Nesne kompozisyonu (MOA = 0.6938 ve DAC_mean = 0.6938), sistemin kalıtım yerine nesne birlikteliğini önceliklendirdiğini göstermektedir.
* **Yanıltıcı Metrik Başarıları:** Reusability (301.939) ve Functionality (153.101) değerlerinin yüksek görünmesi, QMOOD formülasyonundaki toplam sınıf sayısı (DSC = 601.0) çarpanının büyüklüğünden kaynaklanan matematiksel bir illüzyondur. Yapısal tasarımın niteliğinden ziyade kütüphanenin hacmini yansıtmaktadır.
* **Sığ Soyutlama Mimarisi:** Ortalama kalıtım derinliği (ANA / DIT_mean = 0.3195) ve fonksiyonel kalıtım oranı (MFA = 0.1511) oldukça düşüktür. Maksimum kalıtım derinliğinin dahi (DIT_max = 3) olması, kütüphanenin derin, hiyerarşik bir soyutlama yerine geniş ve somut (concrete) tabanlı dikey bir mimariyle genişlediğini doğrulamaktadır.

---

## 2. En Zayıf 2 Kalite Niteliği ve Sorumlu Metrikler

QMOOD denklemleri ve sistem çıktıları analiz edildiğinde, projenin sürdürülebilirliğini tehdit eden en zayıf iki kalite niteliği **Understandability** ve **Extendibility** olarak belirlenmiştir.

### A. Anlaşılabilirlik (Understandability = -202.2567)
Sistemde mutlak değer bazında en kritik negatif skora sahip niteliktir. 
* **Sorumlu Metrikler:** `Understandability = -0.33*(ANA+DCC+NOP+NOM+DSC) + 0.33*(DAM+CAM)`
* **Kritik Gerekçelendirme:** Formülde negatif etkiye sahip olan sınıf sayısı (DSC = 601.0), sınıflar arası sıkı bağlılık (DCC = 3.0233) ve ortalama metot karmaşıklığı (NOM = 6.2928), pozitif etkiye sahip olan kapsülleme (DAM = 0.8806) ve eşbirliktelik (CAM = 0.3633) değerlerini tamamen ezmektedir. 
* **CK Metrik Kanıtları:** Sınıf içi metot odaklılığının düşüklüğü ortalama CAM (0.3633) ile sınırlı değildir; ortalama LCOM_mean (30.2213) ve uç değer olan **LCOM_max = 4371** verisi, sistemde tek bir amaca hizmet etmeyen, birbiriyle alakasız yüzlerce metodu barındıran devasa "Tanrı Sınıfların" (God Classes) varlığını kesin olarak kanıtlamaktadır.

### B. Genişletilebilirlik (Extendibility = 0.4774)
Sistemin yeni gereksinimlere karşı esneme kabiliyetini gösteren, sıfır sınırına yaklaşmış en zayıf pozitif niteliktir.
* **Sorumlu Metrikler:** `Extendibility = 0.50*(ANA+MFA+NOP) - 0.50*DCC`
* **Kritik Gerekçelendirme:** Sistemde soyutlama seviyesi (ANA = 0.3195) ve kalıtım yoluyla metotların yeniden kullanımı (MFA = 0.1511) çok düşüktür. Sınıflar arası doğrudan sıkı bağlılık (DCC = 3.0233), formülün sol tarafındaki zayıf soyutlama katmanını nötralize etmektedir. Sistem, genişletilebilirliğini neredeyse tamamen polimorfizm (NOP = 3.5075) omurgasına borçludur; bu omurganın zarar görmesi sistemin tamamen kilitlenmesine yol açabilir.

---

## 3. CK Maksimum (Outlier) Değerlerinin Teknik Borç Analizi

Ortalama (mean) değerler bazı durumlarda sistemin gerçek sağlığını gizleyebilir. Sürüm 1.5.2'deki maksimum (`_max`) CK metrikleri, mimaride ciddi anomali ve teknik borç (Technical Debt) odakları olduğunu doğrulamaktadır:

* **WMC_max = 381:** Ortalama karmaşıklık 15.76 iken, en karmaşık sınıfın ağırlıklı metot karmaşıklığının 381 olması, bu sınıf içinde aşırı yoğun `if-else`, `switch-case` veya iç içe geçmiş döngülerin (nested loops) yer aldığını gösterir. Bu durum kodun test edilebilirliğini ve bakımını imkansızlaştırır.
* **MPC_max = 401 ve RFC_max = 149:** Bir sınıfın dışarıdaki diğer sınıflara 401 farklı mesaj göndermesi (MPC) ve erişebileceği metot kümesinin 149 olması (RFC), bu sınıfın sistem genelinde bir **"Merkezi Bağlantı Noktası" (Hub Class)** haline geldiğini gösterir. Bu sınıf üzerinde yapılacak en ufak bir değişiklik, sistem genelinde domino etkisiyle hatalara yol açma riski taşır.

---

## 4. Somut ve Metrik Temelli 3 Refactoring Önerisi

Tespit edilen mimari erozyonu ve teknik borcu temizlemek adına, doğrudan metrik uç değerlerini hedef alan 3 somut yeniden yapılandırma (refactoring) adımı uygulanmalıdır:

### Öneri 1: Tanrı Sınıfların Bölünmesi (Extract Class / Extract Subclass)
* **Hedef Metrikler:** LCOM_max (4371) ve WMC_max (381) değerlerini düşürmek; CAM (0.3633) değerini yükseltmek.
* **Uygulama:** LCOM ve WMC değerleri zirve yapmış olan uç sınıflar (muhtemelen temel graf algoritma yönetim merkezleri veya veri yapısı sınıfları) analiz edilmelidir. Birbiriyle aynı örnek değişkenleri (instance variables) paylaşmayan metot grupları mantıksal sorumluluklarına göre ayrılmalı ve Tek Sorumluluk İlkesi (SRP) uyarınca yeni, bağımsız sınıflara dönüştürülmelidir. Bu işlem Understandability değerini doğrudan yukarı çekecektir.

### Öneri 2: Koşullu Blokların Polimorfizme Devredilmesi (Replace Conditional with Polymorphism)
* **Hedef Metrikler:** WMC_max (381) ve WMC_mean (15.76) değerlerini düşürmek; ANA (0.3195) ve MFA (0.1511) değerlerini artırmak.
* **Uygulama:** Graf tiplerine veya kenar/düğüm (edge/vertex) varyasyonlarına göre dikey olarak şişmiş ve `if-else`/`switch` bloklarıyla doldurulmuş karmaşık metotlar temizlenmelidir. Ortak davranışlar bir üst soyutlama katmanında (Interface veya Abstract Class) toplanmalı, her bir özel graf varyasyonu bu üst sınıftan türeyen somut alt sınıflara (concrete subclasses) dağıtılmalıdır. Böylece kod karmaşıklığı dikeyden yataya (soyutlamaya) kaydırılacaktır.

### Öneri 3: Bağımlılık İzolasyonu ve Facade Tasarım Kalıbı (Extract Interface / Introduce Facade)
* **Hedef Metrikler:** MPC_max (401), RFC_max (149) ve DCC / CBO_mean (3.0233) bağımlılık trafiğini azaltmak.
* **Uygulama:** Diğer sınıflarla aşırı yüksek etkileşime girerek sistemi sıkı bağlı (tightly coupled) hale getiren hub sınıfların önüne soyut arayüzler (Interfaces) veya bir Facade katmanı yerleştirilmelidir. Sınıfların somut implementasyonlara doğrudan bağımlı olması (CBO) engellenmeli, haberleşme bu arayüzler üzerinden yürütülmelidir. Bu müdahale, sistem üzerindeki bağımlılık baskısını (DCC) azaltarak Extendibility (Genişletilebilirlik) değerini kararlı bir şekilde artıracaktır.