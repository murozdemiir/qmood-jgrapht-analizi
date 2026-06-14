# JGraphT (v1.5.2 -> v1.5.3) Mimari Sürüm Değişim Analizi

**Rol:** Kıdemli Yazılım Mimarisi ve Yazılım Kalitesi Uzmanı
**İncelenen Sürümler:** JGraphT v1.5.2 ve v1.5.3 (jgrapht-core)

Bu rapor, QMOOD nesne yönelimli tasarım metrikleri temel alınarak, JGraphT kütüphanesinin 1.5.2 sürümünden 1.5.3 sürümüne geçişteki (minor/patch) mimari evrimini ve teknik borç durumunu eleştirel bir yaklaşımla değerlendirmektedir.

---

## 1. GENEL DEĞERLENDİRME: OLUMLU MU, OLUMSUZ MU?

İki sürüm arasındaki değişim oranlarının (%5'in altında) dar bir bantta kalması, bu geçişin majör bir mimari refactoring (yeniden yapılandırma) barındırmadığını; daha çok hata düzeltmeleri (bug-fix) ve ufak çaplı özellik eklemelerini (incremental feature additions) içeren **stabil bir bakım sürümü** olduğunu göstermektedir. 

Genel kalite açısından değerlendirdiğimizde; sistemin kontrollü büyüdüğü (bağımlılık patlaması yaşanmadığı) için değişimi **kısmen olumlu ve güvenli** olarak yorumlayabiliriz. Ancak yapısal bir iyileştirme yapılmadığı için, 1.5.x serisinde süregelen kronik mimari sorunlar olduğu gibi bir sonraki sürüme taşınmıştır.

---

## 2. METRİK BAZLI KANITLAR VE KALİTE NİTELİKLERİNE ETKİSİ

Ufak yüzdelik değişimlerin QMOOD denklemleri üzerindeki yansımaları şu şekildedir:

### A. Kontrollü Büyüme ve Bağımlılık Yönetimi (DSC vs DCC)
* **Kanıt:** Sistem boyutu (DSC) **%2.8** artarak 601'den 618'e (17 yeni sınıf) çıkmıştır. Buna karşılık dış bağımlılıkları ölçen DCC (Coupling) metriği sadece **%0.3** (3.023 -> 3.032) oranında çok cüzi bir artış göstermiştir.
* **Yorum:** QMOOD formüllerindeki Reusability (Yeniden Kullanılabilirlik) ve Flexibility (Esneklik) niteliklerini doğrudan tehdit eden DCC'nin, sistem büyürken sabit kalabilmesi mimari açıdan başarılı bir izolasyondur. Eklenen yeni sınıflar, mevcut sistemi daha fazla birbirine kördüğüm (tightly coupled) yapmadan entegre edilmiştir.

### B. Soyutlama Stagnasyonu ve Genişletilebilirlik (ANA, MFA, NOH)
* **Kanıt:** Sistemdeki hiyerarşi ağacı sayısı (NOH) **%4.6** artmıştır (87 -> 91). Ancak Soyutlama (ANA) yalnızca **%0.3** (0.320'de sabit kaldı diyebiliriz) ve Kalıtım (MFA) **%0.1** (0.151) artmıştır.
* **Yorum:** QMOOD'un Extendibility (Genişletilebilirlik) formülü `0.50*(ANA+MFA+NOP) - 0.50*DCC` şeklindedir. NOH artarken ANA ve MFA'nın yerinde sayması, eklenen 4 yeni hiyerarşinin ve 17 yeni sınıfın derin soyutlamalar (abstract sınıflar veya arayüzler) yerine sığ ve **somut (concrete)** sınıflar olarak kodlandığına dair güçlü bir kanıttır. Extendibility niteliğinde belirgin bir iyileşme sağlanamamıştır.

### C. Anlaşılabilirlik (Understandability) Üzerindeki Matematiksel Yük
* **Kanıt:** QMOOD denkleminde Anlaşılabilirlik; DSC (Boyut) ve NOM (Karmaşıklık) parametreleriyle negatif bir korelasyona sahiptir. DSC **%2.8**, sınıf başına ortalama metot sayısı (NOM) ise **%0.5** (6.293 -> 6.324) artmıştır.
* **Yorum:** Sınıf içi metot sayısının artması ve sistemin hacim kazanması, `-(ANA+DCC+NOP+NOM+DSC)` eksi çarpan bloğunu büyüteceği için formülasyon gereği Understandability puanını daha da aşağı çekecektir.

---

## 3. TEKNİK BORÇ (TECHNICAL DEBT) İŞARETLERİ VAR MI?

Bu sürüm geçişinde yeni bir teknik borç **yaratılmamış**, ancak eski sürümlerden devralınan ağır teknik borç **ödenmemiştir.** * **Kronik Sinyal: Sınıf İçi Tutarsızlık (Low Cohesion)**
  * **Kanıt:** CAM (Cohesion) metriği %0.7 gibi önemsiz bir artışla **0.366** gibi çok düşük bir seviyede kalmaya devam etmiştir.
  * **Açıklama:** CAM'in 0.36 bandında olması, JGraphT'nin `core` modülündeki devasa sınıfların (muhtemelen God Class'ların) içindeki metotların birbiriyle veri veya parametre paylaşmadığını, sınıfların tek sorumluluk prensibini (SRP) ihlal etmeye devam ettiğini gösterir.
  * **Risk Durumu:** Bir bakım (patch) sürümü için bu normal karşılansa da, ana (minor/major) sürüm planlamasında bu düşük Cohesion ve düşük Abstraction (ANA: 0.320) seviyeleri, kütüphanenin gelecekteki bakım maliyetini (maintenance effort) ciddi şekilde artıracak temel teknik borçlardır. Geliştirici ekibin `Extract Class` refactoring stratejisini uygulamayı ertelediği görülmektedir.