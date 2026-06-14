# JGraphT v1.5.3 Derinlemesine Kalite Değerlendirme Raporu

**Hazırlayan:** Kıdemli Yazılım Mimarı / Kalite Uzmanı
**Tarih:** 14 Haziran 2026
**Kapsam:** `jgrapht-core` modülü, Sürüm 1.5.3
**Metodoloji:** QMOOD (Bansiya & Davis 2002) Tasarım Kalite Modeli

---

## 1. Sürüm Kalitesi Genel Bakış

v1.5.3, `jgrapht-core` kütüphanesinin ulaştığı en yüksek fonksiyonel zenginliği temsil ederken, aynı zamanda **birikmiş yapısal sorunların en belirgin halini** sergilemektedir. 618 sınıflık (`num_classes`) devasa bir kod tabanına ulaşan proje, QMOOD modelinin tüm boyutlarında net bir ödünleşme (trade-off) tablosu çizmektedir.

Proje, **Functionality (İşlevsellik) ve Reusability (Yeniden Kullanılabilirlik)** eksenlerinde zirve yapmıştır. Buna karşılık, **Understandability (Anlaşılabilirlik)** tüm seri boyunca en düşük noktasına gerilemiş ve **Extendibility (Genişletilebilirlik)** kritik seviyede seyretmeye devam etmiştir.

### Kalite Nitelikleri Özet Tablosu

| Kalite Niteliği | Ham Değer | v1.5.1'e Göre Değişim | Durum ve Yorum |
| :--- | :--- | :--- | :--- |
| **Functionality** | 157.73 | +4.84 (↑) | **Çok Yüksek.** Yeni özellikler eklenmeye devam ediyor. |
| **Reusability** | 310.45 | +8.99 (↑) | **Çok Yüksek.** Sınıflar ve arayüzler yeniden kullanım için optimize. |
| **Flexibility** | 1.59 | +0.02 (↑) | **Düşük-Orta.** Kompozisyon güçlü, ancak bağımlılık esnekliği sınırlıyor. |
| **Effectiveness**| 1.12 | +0.01 (↑) | **Düşük-Orta.** Soyutlama ve kapsülleme eksikliği etkinliği baskılıyor. |
| **Extendibility**| 0.49 | +0.01 (↑) | **Çok Düşük (KRİTİK).** Sistem yeni özellik eklemeye hala elverişli değil. |
| **Understandability**| -207.89 | -5.95 (↓) | **Aşırı Düşük (KRİTİK).** Kod tabanı en karmaşık halinde. |

**Genel Sonuç:** v1.5.3, v1.5.1'e kıyasla marjinal iyileşmeler gösterse de, **iki temel yapısal sorun çözülmeden kalmıştır.** En zayıf iki kalite niteliği değişmemiştir: **Understandability (Anlaşılabilirlik)** ve **Extendibility (Genişletilebilirlik).**

---

## 2. En Zayıf 2 Kalite Niteliği ve Sorumlu Metriklerin Analizi

### 2.1. Anlaşılabilirlik (Understandability) — Değer: -207.89 (AŞIRI DÜŞÜK)

Bu değer, tüm sürüm serisindeki en düşük (en negatif) anlaşılabilirlik puanıdır. v1.5.1'deki -201.94'ten bile daha kötüdür. Kod tabanını yeni bir geliştiricinin anlaması için gereken bilişsel yük aşırı derecede yüksektir.

#### Sorumlu Metriklerin Detaylı Analizi:
**Denklem:** `Understandability = -0.33*(ANA + DCC + NOP + NOM + DSC) + 0.33*(DAM + CAM)`

- **`DSC` (Sınıf Başına Düşen Satır): 618.0** *(v1.5.1: 600.0 → +18.0 artış)*
    - **Kanıt:** Ortalama bir sınıf 618 satır uzunluğundadır. Bu, formüldeki en büyük negatif ağırlıklı değişkendir ve doğrudan anlaşılabilirliği aşağı çeker. Sınıf başına 618 satır, bir geliştiricinin tüm sınıf davranışını zihninde canlandırması için aşırı yüksek bir değerdir. `WMC_mean`'in 15.78 olması, bu sınıfların aynı zamanda karmaşık olduğunu da gösterir.
- **`NOM` (Metot Başına Düşen Satır): 6.32** *(v1.5.1: 6.32 → değişim yok)*
    - **Kanıt:** Ortalama metot uzunluğu 6.32 satır ile kabul edilebilir görünmektedir. Ancak bu ortalama aldatıcıdır. `NOM_max` değerinin 95 olması, bazı metotların aşırı derecede uzun ve karmaşık olduğunu kanıtlar. Bu aykırı metotlar (`outliers`), kod tabanının genel anlaşılabilirliğini ciddi şekilde düşüren unsurlardır.
- **`DCC` (Sınıflar Arası Bağımlılık): 3.03** *(v1.5.1: 3.02 → +0.01 artış)*
    - **Kanıt:** Ortalama bir sınıf 3'ten fazla başka sınıfa bağımlıdır. `CBO_max` değerinin 21 olması, "Tanrı Sınıfı" (God Class) adaylarının varlığını ve bu sınıfları anlamak için 21 farklı bağlamın bilinmesi gerektiğini ortaya koyar.
- **`LCOM_mean` (Metot Uyum Eksikliği): 31.24** *(v1.5.1: 30.21 → +1.03 artış)*
    - **Kanıt:** Bu, anlaşılabilirliği dolaylı ama güçlü şekilde etkileyen bir metriktir. 31.24 değeri, sınıfların içindeki metotların büyük ölçüde birbirinden kopuk olduğunu, yani bir sınıfın aslında birden fazla sınıfa bölünmesi gerektiğini gösterir. `LCOM_max`'ın 4371 gibi aşırı bir değerde olması, en az bir sınıfın tamamen dağınık bir sorumluluk yapısına sahip olduğunu kanıtlar.

### 2.2. Genişletilebilirlik (Extendibility) — Değer: 0.49 (ÇOK DÜŞÜK)

Bu değer, kütüphaneye yeni bir grafik algoritması veya veri yapısı eklemenin mimari açıdan zahmetli ve riskli olduğunu gösterir. v1.5.1'den bu yana anlamlı bir iyileşme gözlenmemiştir.

#### Sorumlu Metriklerin Detaylı Analizi:
**Denklem:** `Extendibility = 0.50*(ANA + MFA + NOP) - 0.50*DCC`

- **`ANA` (Soyutlama): 0.3204** *(v1.5.1: 0.3217 → -0.0013 azalış)*
    - **Kanıt:** Sınıf hiyerarşisinin yalnızca %32'si soyut sınıf veya arayüzlerden oluşmaktadır. Bu, Açık/Kapalı Prensibi'nin (Open/Closed Principle) sistematik olarak ihlal edildiğini gösterir. Yeni bir davranış eklemek için mevcut bir soyutlamayı genişletmek yerine, büyük olasılıkla somut sınıflar değiştirilmektedir. `DIT_mean`'in 0.32 olması, sınıfların çoğunun `Object`'ten türediğini teyit eder.
- **`MFA` (Kalıtım Faktörü): 0.1512** *(v1.5.1: 0.1523 → -0.0011 azalış)*
    - **Kanıt:** Tüm metotların yalnızca %15'i kalıtım yoluyla yeniden kullanılmaktadır. Bu, polimorfizmin temel mekanizması olan kalıtımın projede neredeyse hiç kullanılmadığını gösterir. Genişletilebilirliğin motoru olan `ANA + MFA` kombinasyonu çok zayıftır.
- **`DCC` (Sınıflar Arası Bağımlılık): 3.03**
    - **Kanıt:** Yüksek bağımlılık, genişletme maliyetini katlayan ikincil ama güçlü bir faktördür. Bir sınıfı genişletmek, onun bağımlı olduğu ortalama 3 (aşırı durumda 21) sınıfı da yönetmeyi gerektirir.

---

## 3. Somut Refactoring Önerileri

Aşağıdaki 3 öneri, belirlenen en zayıf kalite niteliklerini (`Understandability` ve `Extendibility`) iyileştirmek için spesifik metrikleri hedef alır.

### Öneri 1: "Tanrı Sınıfı Ayrıştırması" — Sorumlulukları Ayırarak Anlaşılabilirliği Artır
- **Hedef Metrikler:** `LCOM_max` (4371), `CBO_max` (21), `WMC_max` (381), `DCC` (3.03)
- **Tespit:** `LCOM_max` değeri 4371 olan sınıf, neredeyse kesinlikle bir "Tanrı Sınıfı"dır. Aynı sınıf `CBO_max` (21) ve `WMC_max` (381) değerlerine de sahip olabilir (veya bu değerler birkaç sorunlu sınıf arasında dağılmıştır).
- **Eylem:** Bu sınıf(lar)ı statik analiz araçlarıyla tespit edin. Sınıf içindeki, farklı veri alanları üzerinde çalışan metot kümelerini birbirinden ayırın. Her bir kümeyi, tek ve iyi tanımlanmış bir sorumluluğa sahip yeni bir sınıfa taşıyın.
- **Beklenen İyileşme:** `DSC` ve `NOM` ortalamaları düşecek, `CAM` (uyum) artacak, `DCC` (bağımlılık) daha sağlıklı bir yapıya kavuşacaktır. Bu, **Understandability**'yi doğrudan ve güçlü bir şekilde iyileştirecektir.

### Öneri 2: "Strateji Deseni Enjeksiyonu" — Soyutlama Katmanı Oluşturarak Genişletilebilirliği Artır
- **Hedef Metrikler:** `ANA` (0.3204), `MFA` (0.1512), `NOM_max` (95)
- **Tespit:** `ANA` ve `MFA` değerlerinin düşüklüğü ve `NOM_max`'ın (95) varlığı, algoritma seçiminin uzun `if-else` veya `switch-case` bloklarıyla yapıldığı somut sınıflara işaret eder.
- **Eylem:** Farklı grafik gezinme (BFS, DFS, Topolojik Sıralama) veya yol bulma (Dijkstra, A*) algoritmalarını içeren sınıfları tarayın. Her bir algoritma varyantını, ortak bir arayüzden (ör. `GraphIterator<T>`) türeyen somut bir Strateji sınıfına taşıyın.
- **Beklenen İyileşme:** `ANA` (yeni arayüzler) ve `MFA` (arayüzden gelen metotlar) doğrudan artacak, `NOM_max` (uzun metotlar parçalanacak) düşecektir. Bu, **Extendibility**'yi doğrudan ve kalıcı olarak iyileştirecektir.

### Öneri 3: "Aykırı Metot Düzleştirme" — Uzun Metotları Bölerek Karmaşıklığı Azalt
- **Hedef Metrikler:** `NOM_max` (95), `WMC_max` (381)
- **Tespit:** `NOM_max` değeri 95 olan metot, yüksek ihtimalle birden fazla sorumluluğu barındırmakta ve `WMC_max`'a (381) en büyük katkıyı yapmaktadır.
- **Eylem:** Bu metodu tespit edin. İçindeki mantıksal kod bloklarını (bir şeyi hesaplama, bir şeyi dönüştürme, bir şeyi kontrol etme) özel (`private`) yardımcı metotlara çıkarın. Ana metodu, bu yardımcı metotları çağıran bir orkestratör haline getirin.
- **Beklenen İyileşme:** `NOM_max` ve `WMC_max` dramatik şekilde düşecek, böylece `WMC_mean` üzerinde de olumlu bir etki yaratacaktır. Bu, aykırı karmaşıklığı ortadan kaldırarak **Understandability**'yi noktasal olarak iyileştirecektir.