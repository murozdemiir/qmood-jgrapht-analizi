# JGraphT (v1.5.3) Mimari Kalite Değerlendirmesi

**Rol:** Kıdemli Yazılım Mimarisi ve Yazılım Kalitesi Uzmanı
**İncelenen Sürüm:** JGraphT v1.5.3 (jgrapht-core)

Bu rapor, QMOOD (Quality Model for Object-Oriented Design) kalite nitelik denklemleri ve Chidamber & Kemerer (CK) tasarım metrikleri temel alınarak, JGraphT kütüphanesinin 1.5.3 sürümündeki mimari darboğazları eleştirel ve kanıta dayalı olarak analiz etmektedir.

---

## 1. GENEL KALİTE DEĞERLENDİRMESİ VE EN ZAYIF 2 NİTELİK

Sistemin 1.5.3 sürümü, sınıf sayısı (DSC = 618) açısından kütüphanenin ulaştığı en geniş hacimlerden birini temsil etmektedir. Bu hacimsel büyüme, Functionality (157.73) ve Reusability (310.44) gibi işlevsel nitelikleri yukarı taşısa da, sürdürülebilirlik ekseninde ciddi yapısal bozulmalara yol açmıştır. Sağlanan verilere göre, sistemin en zayıf iki kalite niteliği açıkça **Understandability (Anlaşılabilirlik)** ve **Extendibility (Genişletilebilirlik)** olarak öne çıkmaktadır.

### Zayıf Nitelik 1: Understandability (-207.8903)
Anlaşılabilirlik, QMOOD modelinde negatif yönde en derin çöküşü yaşayan niteliktir.
* **Sorumlu Metrikler:** İlgili denklem olan $-0.33 \times (ANA+DCC+NOP+NOM+DSC) + 0.33 \times (DAM+CAM)$ formülüne bakıldığında, eksi yöndeki en büyük ağırlık DSC (618.0) ve DCC (3.0324) metriklerinden gelmektedir. Ancak esas felaket karmaşıklık tarafındadır. Ortalama sınıf karmaşıklığı (WMC_mean) **15.7848** iken, maksimum karmaşıklık (WMC_max) **381** seviyesine fırlamıştır.
* **Yorum:** Bir sınıfın içinde maksimum **95** metot (NOM_max) barındırması, o sınıfın ne yaptığını anlamayı veya test etmeyi imkansızlaştırır. Formülün pozitif tarafında yer alan modül içi tutarlılık (CAM) metriğinin **0.3660** gibi çok zayıf bir seviyede kalması, bu devasa sınıfların içindeki metotların birbiriyle anlamsal olarak tamamen kopuk çalıştığını kanıtlamaktadır.

### Zayıf Nitelik 2: Extendibility (0.4923)
Mevcut kodu bozmadan yeni yetenekler ekleyebilme kapasitesini ölçen genişletilebilirlik, kritik bir daralma yaşamıştır.
* **Sorumlu Metrikler:** Denklem $0.50 \times (ANA+MFA+NOP) - 0.50 \times DCC$ şeklindedir. Extendibility değerini baskılayan iki temel faktör vardır:
  1. **Soyutlama Eksikliği:** ANA (Soyutlama) **0.3204** ve MFA (Kalıtım) **0.1512** gibi oldukça düşük seviyelerdedir. 618 sınıflık geniş bir ağaçta hiyerarşi derinliğinin (NOH) sadece **91** olması, yeni grafik algoritmalarının arayüzler (interfaces) yerine doğrudan somut (concrete) sınıflar halinde koda eklendiğini göstermektedir.
  2. **Yüksek Bağımlılık Cezası:** Eksi çarpan olan DCC (Coupling) ortalaması **3.0324**'tür. Ancak maksimum bağımlılık (CBO_max) **21**'dir. Bir sınıfın 21 farklı sınıfa doğrudan sıkı sıkıya bağlı (tightly coupled) olması, koda yapılacak herhangi bir yeni eklentinin mevcut sistemi bozma (regression) ihtimalini dramatik ölçüde artırmaktadır.

---

## 2. METRİK-TEMELLİ REFACTORING ÖNERİLERİ

1.5.3 sürümü, mimari yozlaşmanın (architectural erosion) zirve yaptığı noktalardan biridir. Dev sınıfların ve yüksek mesajlaşma trafiğinin getirdiği teknik borcu (technical debt) temizlemek için aşağıdaki 3 somut refactoring adımı acilen uygulanmalıdır:

### Öneri 1: "Extract Class" ile "God Class" Darboğazını Giderme (Hedef: LCOM ve WMC)
* **Kanıt:** Sistemde ortalama metot uyumsuzluğu (LCOM_mean) **31.2379** iken, LCOM_max değeri inanılamayacak bir seviye olan **4371**'e ulaşmıştır. WMC_max **381**, RFC_max ise **149**'dur. Bu istatistikler, kod tabanında aralarında veri paylaşmayan alakasız yüzlerce metodun tek bir çatı altında toplandığı en az bir adet devasa "God Class" olduğunu ispatlar.
* **Aksiyon:** LCOM değeri uç seviyelerde olan bu sınıflar tespit edilmeli ve `Extract Class` yöntemiyle Tek Sorumluluk Prensibine (SRP) uyan mantıksal alt sınıflara bölünmelidir. Bu işlem CAM (Cohesion) değerini yükseltecek ve Understandability erozyonunu durduracaktır.

### Öneri 2: "Move Method" ile Özellik Kıskançlığını (Feature Envy) Çözme (Hedef: MPC ve CBO)
* **Kanıt:** Dış sınıflara yapılan metot çağrısı bağımlılığını ölçen MPC ortalaması **16.8511** iken, MPC_max değeri **401**'dir. Bu, sistemdeki bir sınıfın başka bir sınıfın metotlarını 401 kez çağırdığını gösterir; yani veri bir sınıfta, davranışı işleyen mantık ise bambaşka bir sınıftadır (Feature Envy).
* **Aksiyon:** Dışarıya 401 kez çağrı yapan bu yapı tespit edilip, `Move Method` (Metodu Taşı) refactoring işlemi uygulanmalıdır. İlgili operasyonlar doğrudan verinin bulunduğu asıl sınıfa taşınmalı, böylece sınıflar arası yüksek trafik bağımlılığı (CBO ve DCC) düşürülmelidir.

### Öneri 3: "Extract Interface" ile Soyutlamayı Artırma (Hedef: ANA ve Extendibility)
* **Kanıt:** ANA (**0.3204**) metriğinin diplerde seyretmesi, Açık/Kapalı Prensibinin (Open/Closed Principle) ihlal edildiğini, polimorfizm yerine doğrudan somut sınıf implementasyonlarına bağımlı kalındığını gösterir.
* **Aksiyon:** Ortak davranış sergileyen graf yapıları veya travers algoritmaları için `Extract Interface` veya `Extract Superclass` işlemleriyle soyut katmanlar yaratılmalıdır. Somut bağımlılıklar arayüzlere çevrildiğinde (Dependency Inversion), ANA değeri yükselecek ve Extendibility niteliğindeki pozitif çarpan büyüyecektir.