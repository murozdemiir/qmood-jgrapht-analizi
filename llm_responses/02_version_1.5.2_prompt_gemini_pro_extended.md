# JGraphT (v1.5.2) Mimari Kalite Değerlendirmesi

**Rol:** Kıdemli Yazılım Mimarisi ve Yazılım Kalitesi Uzmanı
**İncelenen Sürüm:** JGraphT v1.5.2 (jgrapht-core)

Bu rapor, QMOOD kalite nitelik denklemleri ve Chidamber & Kemerer (CK) tasarım metrikleri üzerinden JGraphT kütüphanesinin 1.5.2 sürümündeki mimari darboğazları eleştirel ve kanıta dayalı olarak analiz etmektedir.

---

## 1. GENEL KALİTE DEĞERLENDİRMESİ VE EN ZAYIF 2 NİTELİK

Sistemin 1.5.2 sürümündeki genel hacmi (DSC = 601 sınıf), kütüphanenin geniş bir işlevsellik sunduğunu gösterse de, bu büyüme sürdürülebilirlik metriklerinde ciddi tahribata yol açmıştır. Sağlanan verilere göre sistemin en zayıf iki kalite niteliği açıkça **Understandability (Anlaşılabilirlik)** ve **Extendibility (Genişletilebilirlik)** olarak öne çıkmaktadır.

### Zayıf Nitelik 1: Understandability (-202.2567)
Anlaşılabilirlik, QMOOD modelindeki en problemli değerdir ve derin bir negatif eğilim göstermektedir.
* **Sorumlu Metrikler:** İlgili formüldeki cezalandırıcı blok olan $-0.33 \times (ANA+DCC+NOP+NOM+DSC)$ toplamı, özellikle sınıf sayısının (DSC = 601.0) baskınlığı nedeniyle çok yüksektir. Ancak asıl tehlike karmaşıklıkta yatmaktadır. Ortalama sınıf karmaşıklığı (WMC_mean) **15.7604** gibi yüksek bir değerdeyken, maksimum karmaşıklık (WMC_max) **381**'e fırlamıştır.
* **Yorum:** Bir sınıfın içinde maksimum **95** metot (NOM_max) bulunması sistemi anlamayı neredeyse imkansız hale getirmektedir. Formülde pozitif etki yaratması beklenen modül içi tutarlılık (CAM) metriği **0.3633**'te kalarak metotların birbiriyle anlamsal olarak çok kopuk olduğunu (düşük cohesion) kanıtlamaktadır.

### Zayıf Nitelik 2: Extendibility (0.4774)
Mevcut sisteme zarar vermeden yeni yetenekler ekleyebilme kapasitesi kritik seviyede düşüktür.
* **Sorumlu Metrikler:** Formül $0.50 \times (ANA+MFA+NOP) - 0.50 \times DCC$ şeklindedir. Genişletilebilirliği baltalayan iki ana faktör vardır:
  1. **Soyutlama ve Kalıtım Eksikliği:** ANA (Soyutlama) **0.3195** ve MFA (Kalıtım) **0.1511** gibi çok düşük seviyelerdedir. 601 sınıflık bir sistemde hiyerarşi ağacının (NOH) sadece **87** olması, tasarımın arayüzlerden ziyade doğrudan somut (concrete) sınıflar üzerine inşa edildiğini gösterir.
  2. **Yüksek Bağımlılık:** Formüldeki negatif çarpan olan DCC (Coupling) **3.0233** seviyesindedir. Bir sınıfın doğrudan bağlı olduğu sınıf sayısının maksimum **21** (CBO_max) olması, yeni bir özellik eklerken mevcut yapıyı kırma (regression) riskini artırmaktadır.

---

## 2. METRİK-TEMELLİ REFACTORING ÖNERİLERİ

Kod tabanında "God Class" (Her Şeyi Yapan Sınıf) anti-örüntüsü ve kontrolsüz mesajlaşma/bağımlılık problemleri net bir şekilde görülmektedir. Sistemdeki teknik borcu azaltmak için şu 3 somut refactoring adımı uygulanmalıdır:

### Öneri 1: "Extract Class" ile "God Class" Darboğazını Giderme (Hedef: LCOM ve WMC)
* **Kanıt:** Sistemdeki LCOM_mean (Sınıf İçi Metotların Uyumsuzluğu) **30.2213** iken, maksimum değer (LCOM_max) devasa bir seviye olan **4371**'dir. Ayrıca WMC_max **381** ve RFC_max **149**'dur. Bu sayılar, binlerce satırlık ve birbirinden bağımsız işler yapan metotlarla dolu en az bir "God Class" olduğunu kesin olarak kanıtlar.
* **Aksiyon:** LCOM değeri uçuk olan bu istisnai sınıflar tespit edilip `Extract Class` (Sınıf Çıkartma) tekniği ile Tek Sorumluluk Prensibine (SRP) uygun daha küçük sınıflara bölünmelidir. Bu hamle doğrudan CAM (Cohesion) değerini artıracak ve Understandability puanını iyileştirecektir.

### Öneri 2: "Extract Interface" ile Soyutlamayı Artırma (Hedef: ANA ve Extendibility)
* **Kanıt:** ANA (**0.3195**) metriğinin düşüklüğü, algoritmaların ortak bir hiyerarşi yerine doğrudan somut sınıflar içine gömüldüğünü göstermektedir. NOH (Hiyerarşi Sayısı) metrik verisi kütüphane hacmine oranla zayıftır.
* **Aksiyon:** Benzer davranış gösteren graf veri yapıları veya algoritmalar için ortak arayüzler (Interfaces) veya soyut sınıflar (Abstract Classes) oluşturulmalıdır (`Extract Interface` / `Extract Superclass`). Bu refactoring, ANA değerini yukarı çekerek QMOOD denklemindeki Extendibility (Genişletilebilirlik) niteliğine doğrudan pozitif yansıyacaktır.

### Öneri 3: "Move Method" ile Sınıflar Arası Trafiği Düşürme (Hedef: MPC ve CBO)
* **Kanıt:** MPC_max (Metot Çağrısı Bağımlılığı) metriği **401** gibi anormal bir seviyededir. Bu, bir sınıfın başka sınıfların metotlarını dışarıdan tam 401 kez çağırdığını (Feature Envy - Özellik Kıskançlığı) gösterir.
* **Aksiyon:** Dış metotları çok yoğun çağıran yapılar tespit edilip `Move Method` (Metodu Taşı) refactoring işlemi uygulanmalıdır. Davranış, doğrudan verinin (state) bulunduğu sınıfa taşınmalı; böylece sınıflar arası yüksek bağımlılık (CBO ve DCC) düşürülerek sistemin modülerliği artırılmalıdır.