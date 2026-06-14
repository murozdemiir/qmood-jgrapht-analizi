# JGraphT Sürüm Farkı Analizi: v1.5.2 → v1.5.3

**Hazırlayan:** Kıdemli Yazılım Mimarı / Kalite Uzmanı
**Tarih:** 15 Haziran 2026
**Kapsam:** `jgrapht-core` modülü, v1.5.2'den v1.5.3'e geçiş
**Metodoloji:** QMOOD (Bansiya & Davis 2002) Tasarım Metrikleri Yorumlaması

---

## 1. Genel Değerlendirme: Marjinal ve Kontrollü Bir Büyüme

v1.5.2'den v1.5.3'e geçiş, projenin olgunluk döneminde gerçekleşen **küçük ölçekli, kontrollü ve genel olarak nötr-pozitif** bir sürüm güncellemesidir. Tüm metriklerdeki değişim oranları %5'in altındadır ve hiçbir metrikte ani bir sıçrama veya düşüş gözlenmemektedir. Bu, projenin istikrarlı bir geliştirme sürecine sahip olduğunu ve bu iki sürüm arasında radikal bir mimari değişiklik yapılmadığını gösterir.

**Bu sürüm geçişinde yeni bir teknik borç birikimine dair net bir kanıt yoktur.** Ancak mevcut yapısal sorunlar (düşük `ANA` ve `MFA`, yüksek `LCOM`) çözülmeden kalmaya devam etmektedir.

---

## 2. Metrik Bazında Detaylı Değişim Analizi

### 2.1. Boyut ve Hiyerarşi (DSC, NOH, NOM)

| Metrik | v1.5.2 | v1.5.3 | Değişim | Yorum |
| :--- | :--- | :--- | :--- | :--- |
| **DSC** | 601.0 | 618.0 | +%2.8 | Kod tabanı büyümeye devam etmektedir. 17 satırlık artış, birkaç yeni sınıf veya mevcut sınıflara küçük eklemeler anlamına gelir. |
| **NOH** | 87.0 | 91.0 | +%4.6 | Sınıf hiyerarşisine 4 yeni seviye eklenmiştir. Yeni soyutlamalar veya derinleşen kalıtım zincirleri söz konusudur. |
| **NOM** | 6.293 | 6.324 | +%0.5 | Metot başına düşen satır sayısındaki değişim ihmal edilebilir düzeydedir. Metot uzunlukları stabildir. |

**Yorum:** Büyüme (`DSC` ve `NOH`) devam etmektedir, ancak bu büyüme orantılıdır. `NOM`'daki %0.5'lik artış (6.293'ten 6.324'e) tamamen marjinaldir ve metotların şişmeye başladığına dair hiçbir kanıt yoktur. `NOH`'taki %4.6'lık artış, hiyerarşi derinliğinin kontrollü bir şekilde arttığını gösterir.

### 2.2. Soyutlama, Kalıtım ve Polimorfizm (ANA, MFA, NOP)

| Metrik | v1.5.2 | v1.5.3 | Değişim | Yorum |
| :--- | :--- | :--- | :--- | :--- |
| **ANA** | 0.320 | 0.320 | +%0.3 | Soyut sınıf ve arayüz oranı neredeyse tamamen aynı kalmıştır. |
| **MFA** | 0.151 | 0.151 | +%0.1 | Kalıtım yoluyla miras alınan metot oranında değişim yoktur. |
| **NOP** | 3.507 | 3.545 | +%1.1 | Polimorfizm kullanımında çok hafif bir artış vardır. |

**Yorum:** Bu üç metrik, bu sürüm geçişinin **en kritik ancak en az değişen** alanını temsil eder. `ANA` (0.320) ve `MFA` (0.151) değerleri, projenin geneli için düşük seviyelerde sabitlenmiş durumdadır. Bu iki metrikte neredeyse hiç değişim olmaması, geliştirme ekibinin yeni özellikleri eklerken soyutlama ve kalıtım mekanizmalarını kullanmak yerine, mevcut somut sınıfları genişletmeye devam ettiğini düşündürmektedir. `NOP`'taki %1.1'lik hafif artış tek başına olumlu ancak yetersizdir; çünkü soyutlama (`ANA`) ve kalıtım (`MFA`) ile desteklenmeyen polimorfizm, genişletilebilirliğe anlamlı bir katkı sağlamaz.

### 2.3. Kapsülleme, Uyum ve Kompozisyon (DAM, CAM, MOA)

| Metrik | v1.5.2 | v1.5.3 | Değişim | Yorum |
| :--- | :--- | :--- | :--- | :--- |
| **DAM** | 0.881 | 0.885 | +%0.5 | Kapsülleme seviyesinde çok hafif bir iyileşme vardır. |
| **CAM** | 0.363 | 0.366 | +%0.7 | Sınıf içi uyumda çok hafif bir iyileşme vardır. |
| **MOA** | 0.694 | 0.701 | +%1.0 | Kompozisyon kullanımı artmaya devam etmektedir. |

**Yorum:** Bu üç metrikteki değişimlerin tamamı pozitif yönlüdür ve bu, sürüm farkının **en olumlu yanını** oluşturur. Özellikle:
- `CAM`'deki %0.7'lik artış: Önceki sürümlerde düşüş eğiliminde olan uyum metriğinde bir duraklama veya hafif toparlanma görülmektedir. Bu, yeni eklenen kodun mevcut sınıfların sorumluluklarıyla daha uyumlu olduğuna işaret eder.
- `MOA`'daki %1.0'lık artış: Kompozisyon kullanımındaki istikrarlı artış devam etmektedir. Bu, "kalıtım yerine kompozisyon" prensibine bağlı kalındığını ve esneklik (`Flexibility`) için olumlu bir zemin oluşturduğunu gösterir.
- `DAM`'daki %0.5'lik artış: Kapsülleme kalitesinde ihmal edilebilir bir iyileşme vardır, ancak bu seviye (0.885) zaten kabul edilebilir bir aralıktadır.

### 2.4. Bağımlılık ve Mesajlaşma (DCC, CIS)

| Metrik | v1.5.2 | v1.5.3 | Değişim | Yorum |
| :--- | :--- | :--- | :--- | :--- |
| **DCC** | 3.023 | 3.032 | +%0.3 | Sınıflar arası bağımlılıkta çok hafif bir artış vardır. |
| **CIS** | 4.208 | 4.225 | +%0.4 | Sınıflar arası mesajlaşma (arayüz kullanımı) çok hafif artmıştır. |

**Yorum:** Her iki metrikteki değişim de marjinaldir. `DCC`'deki %0.3'lük artış (3.023'ten 3.032'ye) endişe verici değildir; bağımlılık yönetimi kontrol altında görünmektedir. `CIS`'teki %0.4'lük artış ise sınıflar arası iletişimin zenginleştiğine dair hafif bir olumlu sinyaldir.

---

## 3. Kalite Niteliklerine Yansıması

Metrik değişimlerini QMOOD denklemlerine göre yorumladığımızda, v1.5.3'e geçişin kalite nitelikleri üzerindeki beklenen etkisi şöyledir:

| Kalite Niteliği | Etkilenen Metrikler | Beklenen Etki | Yorum |
| :--- | :--- | :--- | :--- |
| **Reusability** | DCC↑(çok az), CAM↑, CIS↑, DSC↑ | **Hafif Pozitif** | Tüm bileşenler pozitif yönde hareket etmektedir. |
| **Flexibility** | DAM↑, DCC↑(çok az), MOA↑, NOP↑ | **Hafif Pozitif** | `MOA` ve `DAM`'daki artışlar esnekliği destekler. |
| **Understandability** | ANA↔, DCC↑, NOP↑, NOM↑, DSC↑, DAM↑, CAM↑ | **Nötr / Hafif Negatif** | Büyüme (`DSC`, `NOM`) anlaşılabilirliği hafifçe aşağı çeker. |
| **Functionality** | CAM↑, NOP↑, CIS↑, DSC↑, NOH↑ | **Pozitif** | Tüm bileşenler pozitif yöndedir; en belirgin iyileşme burada beklenir. |
| **Extendibility** | ANA↔, MFA↔, NOP↑, DCC↑(çok az) | **Nötr** | `NOP`'taki artış ile `DCC`'deki artış birbirini dengeler. |
| **Effectiveness** | ANA↔, DAM↑, MOA↑, MFA↔, NOP↑ | **Hafif Pozitif** | `DAM` ve `MOA`'daki artışlar etkinliği bir miktar yükseltir. |

**Özet:** Beklenen etki, tüm kalite niteliklerinde **nötr ile hafif pozitif** arasında değişmektedir. En belirgin kazanım **Functionality**'de, en az değişim ise **Extendibility**'de beklenmektedir.

---

## 4. Teknik Borç Değerlendirmesi

**Bu sürüm geçişinde yeni ve anlamlı bir teknik borç birikimi tespit edilmemiştir.**

Ancak asıl mesele, **mevcut teknik borcun çözülmeden kalmasıdır.** Değişmeyen metrikler, değişenler kadar bilgi vericidir:

| Gösterge | Durum | Yorum |
| :--- | :--- | :--- |
| **ANA (0.320)** | Sabit, Düşük | Soyutlama eksikliği devam ediyor. Yeni kod somut sınıflara ekleniyor. |
| **MFA (0.151)** | Sabit, Düşük | Kalıtım kullanımı yetersiz. Polimorfizm altyapısı zayıf. |
| **CAM (0.366)** | Hafif Artış | Olumlu bir sinyal, ancak değer hala düşük. Uyum sorunu devam ediyor. |
| **DCC (3.032)** | Çok Hafif Artış | Kontrol altında, ancak mutlak değer yüksek sayılabilir. |

**Sonuç:** Geliştirme ekibi, bu sürümde "önce zarar verme" (primum non nocere) prensibine bağlı kalmıştır. Yeni kod eklerken mevcut metrikleri kötüleştirmemeye özen göstermiş, hatta `CAM`, `DAM` ve `MOA`'da marjinal iyileştirmeler sağlamıştır. Bu takdire değerdir. Ancak projenin uzun vadeli sürdürülebilirliği için kritik olan `ANA` ve `MFA` metriklerindeki yapısal düşüklük, çözülmeyi bekleyen kronik bir teknik borç olarak varlığını sürdürmektedir.

---

## 5. Sonuç

v1.5.2'den v1.5.3'e geçiş, JGraphT projesi için **istikrarlı, kontrollü ve genel olarak olumlu bir ara sürümdür.** Tüm metrik değişimleri marjinaldir ve hiçbir alanda ani bir bozulma gözlenmemektedir. Özellikle uyum (`CAM`), kapsülleme (`DAM`) ve kompozisyon (`MOA`) metriklerindeki hafif iyileşmeler, geliştirme ekibinin kod kalitesi konusunda bilinçli olduğunu göstermektedir.

Bununla birlikte, bu sürüm geçişi projenin **en büyük yapısal sorununu çözmek için bir fırsatın kaçırıldığını** da göstermektedir. Soyutlama (`ANA`) ve kalıtım (`MFA`) metriklerinin düşük seviyelerde sabitlenmiş olması, projenin genişletilebilirlik (`Extendibility`) ve anlaşılabilirlik (`Understandability`) sorunlarının devam edeceği anlamına gelmektedir. Bu metrikleri iyileştirmeye yönelik hedefli refactoring çalışmaları (örneğin Strateji deseni enjeksiyonu), gelecek sürümler için önceliklendirilmelidir.