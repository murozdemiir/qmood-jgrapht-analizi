# JGraphT Sürüm Farkı Analizi: v0.9.0 → v0.9.2

**Hazırlayan:** Kıdemli Yazılım Mimarı / Kalite Uzmanı
**Tarih:** 15 Haziran 2026
**Kapsam:** `jgrapht-core` modülü, v0.9.0'dan v0.9.2'ye geçiş
**Metodoloji:** QMOOD (Bansiya & Davis 2002) Tasarım Metrikleri Yorumlaması

---

## 1. Genel Değerlendirme: Olumlu Bir Evrim Adımı

v0.9.0'dan v0.9.2'ye geçiş, projenin erken döneminde gerçekleşen **olumlu bir mimari evrimi** temsil etmektedir. Bu sürüm farkı, kütüphanenin işlevsel olarak büyürken (yeni sınıflar ve metotlar eklenirken) aynı zamanda soyutlama ve kalıtım gibi temel nesne yönelimli prensipleri daha etkin kullanmaya başladığını göstermektedir.

Bu geçişte **teknik borç birikimine dair net ve güçlü bir işaret bulunmamaktadır.** Ancak uyum (cohesion) metriğindeki düşüş, izlenmesi gereken bir erken uyarı sinyali olarak değerlendirilmelidir.

---

## 2. Metrik Bazında Detaylı Değişim Analizi

### 2.1. Boyut ve Hiyerarşi (DSC, NOH, NOM)

| Metrik | v0.9.0 | v0.9.2 | Değişim | Yorum |
| :--- | :--- | :--- | :--- | :--- |
| **DSC** | 238.0 | 267.0 | +%12.2 | Kütüphaneye yeni sınıflar eklenmiş, kod tabanı büyümüştür. Bu, işlevsellik artışının doğal bir sonucudur. |
| **NOH** | 35.0 | 39.0 | +%11.4 | Sınıf hiyerarşisinin derinliği artmıştır. Yeni alt sınıflar ve arayüzler eklenmektedir. |
| **NOM** | 5.155 | 5.240 | +%1.6 | Metot başına düşen satır sayısında çok hafif bir artış vardır. Bu değişim marjinaldir ve endişe verici değildir. |

**Yorum:** Büyüme (`DSC` ve `NOH`) kontrollü ve orantılı görünmektedir. `NOM`'daki %1.6'lık artış ihmal edilebilir seviyededir ve metotların şişmeye başladığına dair bir kanıt yoktur.

### 2.2. Soyutlama ve Kalıtım (ANA, MFA) — **En Belirgin İyileşme Alanı**

| Metrik | v0.9.0 | v0.9.2 | Değişim | Yorum |
| :--- | :--- | :--- | :--- | :--- |
| **ANA** | 0.618 | 0.670 | +%8.5 | Soyut sınıf ve arayüzlerin oranı belirgin şekilde artmıştır. |
| **MFA** | 0.247 | 0.272 | +%10.2 | Kalıtım yoluyla miras alınan metotların oranı artmıştır. |

**Yorum:** Bu iki metriğin birlikte ve anlamlı oranda artması, **mimari açıdan en değerli pozitif gelişmedir.** Geliştiriciler, yeni işlevselliği somut sınıflara yığmak yerine, soyut temel sınıflar ve arayüzler tanımlayıp bunları genişleterek eklemişlerdir. Bu durum:
- **Genişletilebilirliği (Extendibility)** doğrudan artırır (Denklem: `+0.50*ANA + 0.50*MFA`).
- Açık/Kapalı Prensibi'ne (OCP) uyumu güçlendirir.
- Polimorfizmin (`NOP`) etkin kullanımı için sağlam bir zemin hazırlar.

### 2.3. Kapsülleme ve Kompozisyon (DAM, MOA)

| Metrik | v0.9.0 | v0.9.2 | Değişim | Yorum |
| :--- | :--- | :--- | :--- | :--- |
| **DAM** | 0.899 | 0.894 | -%0.6 | Değişim marjinaldir. Kapsülleme seviyesi neredeyse aynı kalmıştır. |
| **MOA** | 0.374 | 0.405 | +%8.2 | Kompozisyon (bir sınıfın veri üyesi olarak başka sınıfları kullanması) kullanımı artmıştır. |

**Yorum:** `MOA`'daki %8.2'lik artış olumludur. Kalıtıma (`MFA`) ek olarak kompozisyonun da artması, "kalıtım yerine kompozisyonu tercih et" prensibiyle uyumlu, dengeli bir tasarım yaklaşımını gösterir. Bu, **Esnekliği (Flexibility)** artıran bir faktördür (Denklem: `+0.50*MOA`). `DAM`'daki değişim önemsizdir, kapsülleme kalitesi korunmuştur.

### 2.4. Uyum, Bağımlılık ve Karmaşıklık (CAM, DCC) — **İzlenmesi Gereken Alan**

| Metrik | v0.9.0 | v0.9.2 | Değişim | Yorum |
| :--- | :--- | :--- | :--- | :--- |
| **CAM** | 0.407 | 0.387 | **-%4.8** | Sınıf içi uyum (cohesion) düşmüştür. Metotların ortak veri alanlarını kullanma derecesi azalmıştır. |
| **DCC** | 2.349 | 2.363 | +%0.6 | Sınıflar arası bağımlılıkta çok hafif bir artış vardır. |

**Yorum:** `CAM`'deki %4.8'lik düşüş, bu sürüm farkındaki **tek potansiyel olumsuz sinyaldir.** Yeni eklenen sınıfların veya mevcut sınıflara eklenen metotların, sınıfın temel sorumluluğuyla tam olarak örtüşmeyen işlevler içermeye başlamış olabileceğine işaret eder. Bu, Tek Sorumluluk Prensibi'nin (SRP) ihmal edilmeye başlandığının erken bir göstergesi olabilir. `DCC`'deki %0.6'lık artış ihmal edilebilir düzeydedir ve bağımlılık yönetiminin kontrol altında olduğunu gösterir.

---

## 3. Kalite Niteliklerine Yansıması (Öngörü)

Yukarıdaki metrik değişimlerini QMOOD denklemlerine göre yorumladığımızda, v0.9.2'ye geçişin kalite nitelikleri üzerindeki beklenen etkisi şöyledir:

| Kalite Niteliği | Etkilenen Metrikler | Beklenen Etki | Yorum |
| :--- | :--- | :--- | :--- |
| **Reusability** | CAM↓, DCC↑(çok az), CIS↓(çok az), DSC↑ | **Nötr / Hafif Pozitif** | Artan `DSC` yeniden kullanımı destekler, `CAM`'deki düşüş ise sınırlar. |
| **Flexibility** | MOA↑, DCC↑(çok az), DAM↔, NOP↓ | **Pozitif** | `MOA`'daki artış esnekliği kayda değer şekilde artırır. |
| **Understandability** | ANA↑, DCC↑, NOP↓, NOM↑, DSC↑, CAM↓, DAM↔ | **Hafif Negatif** | Büyüme (`DSC`, `NOM`) ve `CAM` düşüşü anlaşılabilirliği bir miktar azaltabilir. |
| **Functionality** | NOP↓(çok az), CIS↓(çok az), DSC↑, NOH↑, CAM↓ | **Pozitif** | `DSC` ve `NOH`'taki artış işlevsellik algısını güçlü şekilde artırır. |
| **Extendibility** | ANA↑, MFA↑, DCC↑(çok az), NOP↓ | **Pozitif** | `ANA` ve `MFA`'daki güçlü artış, genişletilebilirliği net şekilde iyileştirir. |
| **Effectiveness** | ANA↑, MOA↑, MFA↑, NOP↓, DAM↔ | **Pozitif** | Soyutlama, kompozisyon ve kalıtımdaki ortak artış etkinliği yükseltir. |

---

## 4. Teknik Borç Değerlendirmesi

**Bu sürüm geçişinde anlamlı bir teknik borç birikimi tespit edilmemiştir.**

- **Olumlu Göstergeler:** `ANA` ve `MFA`'daki artışlar, projenin mimari omurgasının güçlendiğini gösterir. Bu, gelecekteki değişikliklerin maliyetini düşüren bir yatırımdır.
- **Tek Erken Uyarı:** `CAM`'deki %4.8'lik düşüş, "sorumluluk kayması" (responsibility creep) eğiliminin başlangıcı olabilir. Yeni işlevsellik eklenirken, bunların mevcut sınıflara uygun olmayan şekilde eklenmesi, ileride `LCOM` (Metot Uyum Eksikliği) değerini yükselterek teknik borca dönüşebilir.
- **Takip Önerisi:** Bir sonraki sürümde `CAM` metriğindeki düşüşün devam edip etmediği izlenmelidir. Eğer düşüş süreklilik kazanırsa, düşük uyumlu sınıfların refactor edilmesi gündeme alınmalıdır.

---

## 5. Sonuç

v0.9.0'dan v0.9.2'ye geçiş, JGraphT projesi için **mimari açıdan net bir başarıdır.** Geliştirme ekibi, kütüphaneyi büyütürken yalnızca yeni kod eklemekle kalmamış, aynı zamanda soyutlama ve kalıtım kullanımını artırarak kod tabanının yapısal kalitesini de yükseltmiştir. Bu, sağlıklı ve sürdürülebilir bir büyüme modelinin göstergesidir. Tek izlenmesi gereken risk, sınıf içi uyumdaki (`CAM`) hafif düşüş eğilimidir.