# JGraphT (v1.5.1) Mimari Kalite Değerlendirmesi

**Rol:** Kıdemli Yazılım Mimarisi ve Yazılım Kalitesi Uzmanı
**İncelenen Sürüm:** JGraphT v1.5.1 (jgrapht-core)

Bu rapor, QMOOD kalite nitelik denklemleri ve Chidamber & Kemerer (CK) tasarım metrikleri üzerinden JGraphT kütüphanesinin 1.5.1 sürümündeki mimari darboğazları eleştirel ve kanıta dayalı olarak analiz etmektedir.

---

## 1. GENEL KALİTE DEĞERLENDİRMESİ VE EN ZAYIF 2 NİTELİK

Sistemin mevcut boyutunun (DSC=600) getirdiği yük altında, sistemin işlevselliği ve yeniden kullanılabilirliği (hacimsel olarak) yüksek görünse de, kodun sürdürülebilirliği ciddi şekilde yara almıştır. Denklem sonuçlarına ve ham verilere baktığımızda en zayıf 2 kalite niteliği açıkça **Understandability (Anlaşılabilirlik)** ve **Extendibility (Genişletilebilirlik)** olarak öne çıkmaktadır.

### Zayıf Nitelik 1: Understandability (-201.9385)
Anlaşılabilirlik niteliği derin bir negatif değere çakılmıştır. 
* **Sorumlu Metrikler:** Formüldeki cezalandırıcı etken olan `(ANA+DCC+NOP+NOM+DSC)` toplamı çok yüksektir. DSC'nin (600) baskınlığı bir yana, asıl problem karmaşıklık ve bağımlılıktır. Ortalama DCC (Coupling) **3.0183**, sınıf başına düşen metot sayısı (NOM) ortalama **6.32**'dir. Ancak maksimum değerler felakettir: NOM_max **95**, WMC_max (sınıf karmaşıklığı) **381**. 
* **Yorum:** Bir sınıfın içinde 95 metot bulunması ve karmaşıklığının 381 olması, o sınıfın (ve dolayısıyla sistemin) anlaşılabilirliğini imkânsız hale getirir. Pozitif etki yaratması beklenen CAM (Cohesion - Sınıf içi tutarlılık) metriğinin **0.3641** gibi düşük bir seviyede kalması, metotların birbiriyle alakasız işlemler yaptığını kanıtlamaktadır.

### Zayıf Nitelik 2: Extendibility (0.4870)
Genişletilebilirlik, mevcut kod tabanına zarar vermeden yeni özelliklerin eklenebilme kapasitesidir ve bu sürümde kritik seviyede düşüktür.
* **Sorumlu Metrikler:** Formül `0.50*(ANA+MFA+NOP) - 0.50*DCC` şeklindedir. Burada Extendibility'yi aşağı çeken iki ana faktör vardır: 
  1. Soyutlama eksikliği: ANA (Soyutlama) **0.3217** ve MFA (Kalıtım) **0.1523** seviyesindedir. 
  2. Yüksek bağımlılık: DCC **3.0183** ile ciddi bir eksi puan getirmektedir. CBO_max'ın **21** olması (bir sınıfın 21 farklı sınıfa doğrudan bağlı olması), koda yeni bir ekleme yaparken mevcudu bozma ihtimalini devasa ölçüde artırmaktadır.

---

## 2. METRİK-TEMELLİ REFACTORING ÖNERİLERİ

Sayısal verilere baktığımızda, kod tabanında açıkça "God Class" (Her Şeyi Yapan Sınıf) anti-örüntüsü ve sıkı bağımlılık (tight coupling) problemleri birikmiş bir teknik borç (technical debt) oluşturmaktadır. Aşağıdaki 3 somut refactoring adımı acilen uygulanmalıdır:

### Öneri 1: "Extract Class" ile "God Class"ları Parçalayın (Hedef: LCOM ve WMC)
* **Kanıt:** Sistemde LCOM_mean (Metotların Uyumsuzluğu) **30.21** iken, LCOM_max değeri inanılmaz bir seviye olan **4371**'e fırlamıştır. WMC_max **381**, RFC_max **151**'dir. Bu sayılar, binlerce satırlık, içinde ortak bir state (durum/değişken) paylaşmayan onlarca metodun bulunduğu devasa sınıfların olduğunu gösterir.
* **Aksiyon:** LCOM değeri yüksek olan bu sınıflar tespit edilip `Extract Class` (Sınıf Çıkartma) yöntemiyle tek sorumluluk prensibine (SRP) uygun alt mantıksal sınıflara bölünmelidir. Bu işlem CAM'ı (Cohesion) artıracak, WMC'yi düşürecek ve Understandability puanını ciddi şekilde iyileştirecektir.

### Öneri 2: "Extract Interface / Superclass" ile Soyutlamayı Artırın (Hedef: ANA ve Extendibility)
* **Kanıt:** ANA (Soyutlama seviyesi) sadece **0.3217**. NOH (Hiyerarşi sayısı) 600 sınıflık bir yapı için sadece **87**'dir. Bu da algoritmaların veya graf yapılarının yüksek oranda somut (concrete) sınıflara yazıldığını gösteriyor.
* **Aksiyon:** Benzer davranış gösteren sınıflar (örneğin farklı shortest-path algoritmaları veya graf tipleri) için `Extract Interface` veya ortak metotları yukarı çekmek için `Extract Superclass` / `Pull Up Method` uygulanmalıdır. Bu işlem ANA'yı yükseltecek, dolayısıyla Extendibility (Genişletilebilirlik) formülündeki pozitif çarpanı büyütecektir.

### Öneri 3: "Dependency Inversion" Uygulayarak Bağımlılıkları Gevşetin (Hedef: DCC ve CBO)
* **Kanıt:** DCC ortalaması **3.0183**, CBO_max **21**, MPC_max (Metot Çağrısı Bağımlılığı) **403**. Özellikle MPC'nin bu kadar yüksek olması, bazı sınıfların dışarıdaki sınıflara ait metotları durmaksızın çağırdığını, yani yoğun bir veri/davranış trafiği olduğunu gösterir.
* **Aksiyon:** Bağımlılıklar somut sınıflar üzerinden değil, arayüzler (Interfaces) üzerinden yapılmalıdır. Ayrıca, başka bir sınıfın metotlarını 403 kez çağıran (MPC_max) sınıf için `Move Method` (Metodu Taşı) refactoring işlemi uygulanarak, davranış verinin bulunduğu yere taşınmalı ve sınıflar arası trafik (coupling) azaltılmalıdır.