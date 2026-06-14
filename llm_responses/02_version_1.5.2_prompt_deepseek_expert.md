# JGraphT v1.5.2 Derinlemesine Kalite Değerlendirme Raporu

**Hazırlayan:** Kıdemli Yazılım Mimarı / Kalite Uzmanı
**Tarih:** 15 Haziran 2026
**Kapsam:** `jgrapht-core` modülü, Sürüm 1.5.2
**Metodoloji:** QMOOD (Bansiya & Davis 2002) Tasarım Kalite Modeli

---

## 1. Sürüm Kalitesi Genel Bakış

v1.5.2, 601 sınıflı (`num_classes`) olgun bir sürüm olup, QMOOD modelinin ortaya koyduğu yapısal ödünleşmeleri (trade-off) net bir şekilde sergilemektedir. Proje, **Functionality (İşlevsellik)** ve **Reusability (Yeniden Kullanılabilirlik)** boyutlarında yüksek puanlar alarak bir kütüphane olarak temel görevini başarıyla yerine getirmektedir.

Buna karşılık, **Understandability (Anlaşılabilirlik)** ve **Extendibility (Genişletilebilirlik)** kritik seviyelerde seyretmektedir. Bu durum, kütüphanenin *kullanıcıları* için başarılı, ancak *geliştiricileri* ve *bakımcıları* için giderek zorlaşan bir yapıya dönüştüğünü göstermektedir.

### Kalite Nitelikleri Özet Tablosu

| Kalite Niteliği | Ham Değer | Yorum |
| :--- | :--- | :--- |
| **Functionality** | 153.10 | **Çok Yüksek.** Geniş algoritma ve veri yapısı yelpazesi mevcut. |
| **Reusability** | 301.94 | **Çok Yüksek.** Sınıflar ve arayüzler yeniden kullanıma uygun. |
| **Flexibility** | 1.57 | **Düşük-Orta.** Kompozisyon kullanımı iyi, ancak bağımlılık sınırlayıcı. |
| **Effectiveness**| 1.11 | **Düşük-Orta.** Soyutlama ve kapsülleme oranları düşük. |
| **Extendibility**| 0.48 | **Çok Düşük (KRİTİK).** Sistemi genişletmek mimari olarak zahmetli. |
| **Understandability**| -202.26 | **Aşırı Düşük (KRİTİK).** Kod tabanını anlamak çok yüksek bilişsel yük gerektiriyor. |

**Genel Sonuç:** v1.5.2'de en zayıf iki kalite niteliği, tıpkı v1.5.1 ve v1.5.3'te olduğu gibi, **Understandability (Anlaşılabilirlik)** ve **Extendibility (Genişletilebilirlik)**'tir. Bu iki nitelikteki kritik seviyedeki düşüklük, projenin uzun vadeli sürdürülebilirliği için en büyük riski oluşturmaktadır.

---

## 2. En Zayıf 2 Kalite Niteliği ve Sorumlu Metriklerin Analizi

### 2.1. Anlaşılabilirlik (Understandability) — Değer: -202.26 (AŞIRI DÜŞÜK)

Bu negatif ve yüksek mutlak değer, yeni bir geliştiricinin kodu kavraması için gereken sürenin ve eforun çok fazla olduğunu, değişiklik yapmanın ise yüksek risk taşıdığını gösterir.

**Denklem:** `Understandability = -0.33*(ANA + DCC + NOP + NOM + DSC) + 0.33*(DAM + CAM)`

#### Sorumlu Metriklerin Detaylı Analizi:

- **`DSC` (Sınıf Başına Düşen Satır): 601.0**
    - **Kanıt:** Ortalama bir sınıf 601 satır uzunluğundadır. Bu, formüldeki en büyük negatif ağırlıklı değişkendir. Bir geliştiricinin, bir sınıfın tüm davranışını ve sorumluluklarını zihninde canlandırabilmesi için 601 satırlık kodu okuması ve anlaması gerekir. Bu, Tek Sorumluluk Prensibi'nin (SRP) ihlal edildiğinin güçlü bir göstergesidir.
- **`NOM` (Metot Başına Düşen Satır): 6.29**
    - **Kanıt:** Ortalama metot uzunluğu 6.29 satır ile makul görünse de, bu değer aldatıcıdır. `NOM_max` değerinin **95** olması, en az bir metodun aşırı derecede uzun olduğunu ve bu tür aykırı değerlerin (`outliers`) genel anlaşılabilirliği ciddi şekilde baltaladığını kanıtlar. `WMC_max`'ın 381 olması, bu uzun metodun aynı zamanda çok karmaşık olduğunu teyit eder.
- **`LCOM_mean` (Metot Uyum Eksikliği): 30.22**
    - **Kanıt:** Bu değer, sınıfların iç yapısındaki dağınıklığı gösterir. Bir sınıftaki metotların büyük bir kısmı ortak veri alanlarını paylaşmamakta, yani sınıf aslında birden fazla sınıfın sorumluluğunu üstlenmektedir. `LCOM_max` değerinin **4371** gibi aşırı bir seviyede olması, en az bir "Tanrı Sınıfı"nın (God Class) varlığını neredeyse kesinleştirir ve anlaşılabilirliğin önündeki en büyük yapısal engellerden biridir.

### 2.2. Genişletilebilirlik (Extendibility) — Değer: 0.48 (ÇOK DÜŞÜK)

Bu değer, kütüphaneye yeni bir algoritma veya grafik türü eklemenin, mevcut soyut yapılar üzerinden kolayca yapılamadığını; bunun yerine, muhtemelen somut sınıflarda değişiklik yapmayı gerektirdiğini gösterir. Bu, Açık/Kapalı Prensibi'nin (OCP) ihlalidir.

**Denklem:** `Extendibility = 0.50*(ANA + MFA + NOP) - 0.50*DCC`

#### Sorumlu Metriklerin Detaylı Analizi:

- **`ANA` (Soyutlama): 0.3195**
    - **Kanıt:** Sınıf hiyerarşisinin yalnızca %32'si soyut sınıf veya arayüzlerden oluşur. Bu, projenin ağırlıklı olarak somut sınıflar üzerine kurulu olduğu anlamına gelir. Yeni bir davranış eklemek için bir arayüzü genişletip yeni bir somut sınıf eklemek (genişletme) yerine, mevcut somut bir sınıfın içine yeni metotlar eklemek (değiştirme) gerekir. `DIT_mean` değerinin 0.32 olması, çoğu sınıfın `Object`'ten türediğini teyit eder.
- **`MFA` (Kalıtım Faktörü): 0.1511**
    - **Kanıt:** Tüm metotların yalnızca %15'i kalıtım yoluyla yeniden kullanılır. Bu, polimorfizmin temel mekanizması olan kalıtımın projede çok az kullanıldığını gösterir. `NOP` değeri (3.51) nispeten yüksek olsa da, bu polimorfizm soyut sınıflar/arayüzler yerine somut sınıflar üzerinden sağlanıyor olabilir, bu da genişletilebilirliğe katkı sağlamaz.
- **`DCC` (Sınıflar Arası Bağımlılık): 3.02**
    - **Kanıt:** Yüksek bağımlılık, genişletmenin maliyetini katlar. Bir sınıfı genişletmek için, onun bağımlı olduğu ortalama 3 diğer sınıfı (ve `CBO_max`'ın 21 olduğu düşünülürse, aşırı durumda 21 sınıfı) da anlamak ve yönetmek gerekir. Bu, genişletmeyi riskli ve maliyetli hale getirir.

---

## 3. Somut Refactoring Önerileri

Aşağıdaki 3 öneri, belirlenen en zayıf iki kalite niteliğini (`Understandability` ve `Extendibility`) iyileştirmek için spesifik metrikleri hedef alır.

### Öneri 1: "Tanrı Sınıfı ve Düşük Uyum" Operasyonu — Sorumlulukları Ayrıştır
- **Hedef Metrikler:** `LCOM_max` (4371), `CBO_max` (21), `WMC_max` (381), `DSC` (601)
- **Tespit:** `LCOM_max` değeri 4371 olan sınıf, neredeyse kesinlikle bir "Tanrı Sınıfı"dır. Bu sınıf, birbiriyle ilgisiz birçok sorumluluğu üstlenmiş durumdadır.
- **Eylem:** Statik analiz araçlarıyla bu sınıfı tespit edin. Sınıfın metotlarını ve kullandıkları veri alanlarını analiz ederek, birbiriyle yüksek uyumlu metot gruplarını (doğal kümeleri) yeni, daha küçük ve odaklı sınıflara taşıyın (Extract Class).
- **Beklenen İyileşme:** `DSC` ve `NOM` ortalamaları düşecek, `CAM` (uyum) artacak, `DCC` daha sağlıklı bir dağılıma kavuşacak. Bu, **Understandability**'yi doğrudan ve güçlü bir şekilde iyileştirecektir.

### Öneri 2: "Strateji Deseni Enjeksiyonu" — Soyutlama Katmanı Oluştur
- **Hedef Metrikler:** `ANA` (0.3195), `MFA` (0.1511), `NOM_max` (95)
- **Tespit:** Düşük `ANA` ve `MFA` değerleri ile birlikte `NOM_max`'ın (95) varlığı, farklı algoritmaların uzun `if-else` veya `switch-case` bloklarıyla yönetildiği somut sınıflara işaret eder.
- **Eylem:** Farklı grafik gezinme (BFS, DFS) veya yol bulma (Dijkstra, A*) algoritmalarını içeren sınıfları tarayın. Her bir algoritma varyantını, ortak bir arayüzden (ör. `ShortestPathAlgorithm<T>`) türeyen somut bir Strateji sınıfına taşıyın.
- **Beklenen İyileşme:** `ANA` (yeni arayüz) ve `MFA` (arayüzden gelen metotlar) doğrudan artacak, `NOM_max` (uzun metotlar parçalanacak) düşecektir. Bu, **Extendibility**'yi doğrudan ve kalıcı olarak iyileştirecektir.

### Öneri 3: "Aykırı Metot Düzleştirme" — Uzun Metotları Böl
- **Hedef Metrikler:** `NOM_max` (95), `WMC_max` (381)
- **Tespit:** `NOM_max` değeri 95 olan metot, yüksek ihtimalle `WMC_max`'a (381) en büyük katkıyı yapan metottur ve birden fazla sorumluluğu barındırmaktadır.
- **Eylem:** Bu metodu tespit edin. İçindeki mantıksal kod bloklarını (doğrulama, dönüştürme, hesaplama) `private` yardımcı metotlara çıkarın (Extract Method). Ana metodu, bu yardımcı metotları sırayla çağıran bir orkestratör haline getirin.
- **Beklenen İyileşme:** `NOM_max` ve `WMC_max` dramatik şekilde düşecek, `WMC_mean` üzerinde de olumlu bir etki yaratacaktır. Bu, aykırı karmaşıklığı ortadan kaldırarak **Understandability**'yi noktasal olarak iyileştirecektir.