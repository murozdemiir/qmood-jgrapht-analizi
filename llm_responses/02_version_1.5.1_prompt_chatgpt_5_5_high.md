# JGraphT 1.5.1 — QMOOD ve CK Metriklerine Dayalı Kalite Değerlendirmesi

**İncelenen modül/sürüm:** JGraphT `jgrapht-core` 1.5.1  
**Analiz kapsamı:** Tek sürüm derin inceleme  
**Temel veri kaynakları:** Verilen QMOOD tasarım metrikleri, CK metrik ortalamaları ve QMOOD kalite nitelikleri

> **Önemli not:** Bu değerlendirme yalnızca verilen sayısal metriklere dayanır. Kodun alan modeli, API tasarım gerekçeleri, algoritmik karmaşıklığı veya test kalitesi ayrıca incelenmediği için sonuçlar “tasarım metriği temelli risk göstergesi” olarak okunmalıdır. Ayrıca QMOOD kalite nitelikleri aynı ölçekte değildir; örneğin `Reusability` ve `Functionality`, formüllerde `DSC` ve `NOH` gibi büyüklük metriklerinden güçlü biçimde etkilenir.

---

## 1. Kısa Sonuç

JGraphT 1.5.1 için metrikler, **geniş ve işlevsel bir kütüphane** izlenimi verir; ancak aynı zamanda **anlaşılabilirlik ve genişletilebilirlik açısından belirgin bakım riski** taşır.

Sayısal özet:

| Kalite Niteliği | Değer | Yorum |
|---|---:|---|
| Reusability | 301.4523 | Yüksek; ancak büyük ölçüde `DSC=600` etkisiyle yükseliyor. |
| Functionality | 152.8887 | Yüksek; `DSC=600` ve `NOH=87` fonksiyonellik formülünü büyütüyor. |
| Flexibility | 1.5703 | Orta/pozitif; `NOP=3.5183` ve `MOA=0.6917` destekliyor, fakat `DCC=3.0183` aşağı çekiyor. |
| Effectiveness | 1.1127 | Sınırlı pozitif; en büyük katkı `NOP=3.5183` üzerinden geliyor. |
| Extendibility | 0.4870 | Zayıf; yüksek coupling ve düşük soyutlama/kalıtım etkili. |
| Understandability | -201.9385 | En zayıf nitelik; özellikle `DSC=600`, `NOM=6.32`, `DCC=3.0183` ve düşük `CAM=0.3641` etkili. |

**En zayıf iki kalite niteliği:**

1. **Understandability = -201.9385**
2. **Extendibility = 0.4870**

---

## 2. Genel Kalite Değerlendirmesi

### 2.1 Güçlü taraf: kapsam ve işlevsellik

`Reusability = 301.4523` ve `Functionality = 152.8887` değerleri yüksektir. Fakat bu değerleri doğrudan “tasarım kalitesi çok iyi” şeklinde yorumlamak yanıltıcı olur; çünkü her iki formülde de sistem büyüklüğü önemli rol oynar.

`Reusability` katkı kırılımı:

```text
Reusability = -0.25*DCC + 0.25*CAM + 0.50*CIS + 0.50*DSC

DCC katkısı = -0.25 * 3.0183 = -0.7546
CAM katkısı =  0.25 * 0.3641 =  0.0910
CIS katkısı =  0.50 * 4.2317 =  2.1159
DSC katkısı =  0.50 * 600    = 300.0000

Toplam = 301.4523
```

Burada `301.4523` değerinin **300 puanı yalnızca DSC=600 büyüklüğünden** gelmektedir. Bu nedenle yüksek `Reusability`, sınıf sayısı yüksek olan büyük bir API yüzeyini gösterir; ancak tek başına düşük coupling, yüksek cohesion veya sade API anlamına gelmez.

`Functionality` için benzer durum vardır:

```text
Functionality = 0.12*CAM + 0.22*(NOP + CIS + DSC + NOH)

CAM katkısı       = 0.12 * 0.3641 = 0.0437
NOP+CIS+DSC+NOH   = 3.5183 + 4.2317 + 600 + 87 = 694.75
Ana katkı         = 0.22 * 694.75 = 152.8450

Toplam = 152.8887
```

Bu değer, kütüphanenin geniş kapsamlı olduğunu gösterir; fakat kalite yorumu yapılırken `DSC=600` ve `NOH=87` etkisi ayrıştırılmalıdır.

---

## 3. En Zayıf 2 Kalite Niteliği

## 3.1 Understandability — En zayıf alan

**Değer:** `Understandability = -201.9385`

Formül:

```text
Understandability = -0.33*(ANA + DCC + NOP + NOM + DSC) + 0.33*(DAM + CAM)
```

Katkı kırılımı:

| Metrik | Değer | Formüldeki Katkı | Etki |
|---|---:|---:|---|
| DSC | 600.0000 | -198.0000 | Çok güçlü negatif |
| NOM | 6.3200 | -2.0856 | Negatif |
| NOP | 3.5183 | -1.1610 | Negatif |
| DCC | 3.0183 | -0.9960 | Negatif |
| ANA | 0.3217 | -0.1062 | Küçük negatif |
| DAM | 0.8794 | +0.2902 | Pozitif ama sınırlı |
| CAM | 0.3641 | +0.1202 | Pozitif ama düşük |

Toplam pozitif katkı:

```text
DAM + CAM katkısı = 0.2902 + 0.1202 = 0.4104
```

Toplam negatif katkı:

```text
DSC + NOM + NOP + DCC + ANA katkısı
= -198.0000 -2.0856 -1.1610 -0.9960 -0.1062
= -202.3488
```

Sonuç:

```text
Understandability = -202.3488 + 0.4104 = -201.9385
```

### Yorum

Bu sürümde anlaşılabilirliği düşüren ana unsur **sistem büyüklüğü**dür: `DSC=600`, formüle tek başına `-198.0000` puanlık negatif katkı yapmaktadır. Bu, QMOOD formülünün büyük sistemleri doğal olarak anlaşılması daha zor kabul ettiğini gösterir.

Ancak sorun yalnızca büyüklük değildir. CK metrikleri de bakım/anlama yükünün belirli sınıflarda yoğunlaştığını düşündürür:

| CK Metrik | Ortalama | Maksimum | Risk Yorumu |
|---|---:|---:|---|
| WMC | 15.7767 | 381 | Bazı sınıflar çok yüksek metot/karmaşıklık yükü taşıyor. |
| LCOM | 30.2100 | 4371 | Cohesion problemi belirli sınıflarda çok yüksek olabilir. |
| RFC | 17.1383 | 151 | Bazı sınıfların çağrı/tepki yüzeyi geniş. |
| NOM | 6.3200 | 95 | Bazı sınıflar çok fazla metot içeriyor. |
| MPC | 16.7700 | 403 | Mesajlaşma/çağrı bağımlılığı bazı sınıflarda yoğun. |

Özellikle `LCOM_max=4371`, `WMC_max=381`, `MPC_max=403` ve `NOM_max=95` değerleri, ortalamalar makul görünse bile **hotspot sınıfların** anlaşılabilirliği ciddi biçimde zorlaştırabileceğine işaret eder.

---

## 3.2 Extendibility — İkinci zayıf alan

**Değer:** `Extendibility = 0.4870`

Formül:

```text
Extendibility = 0.50*(ANA + MFA + NOP) - 0.50*DCC
```

Katkı kırılımı:

| Metrik | Değer | Formüldeki Katkı | Etki |
|---|---:|---:|---|
| ANA | 0.3217 | +0.1609 | Düşük pozitif |
| MFA | 0.1523 | +0.0762 | Çok düşük pozitif |
| NOP | 3.5183 | +1.7592 | Güçlü pozitif |
| DCC | 3.0183 | -1.5092 | Güçlü negatif |

Toplam:

```text
Pozitif katkı = 0.1609 + 0.0762 + 1.7592 = 1.9962
Negatif katkı = -1.5092

Extendibility = 1.9962 - 1.5092 = 0.4870
```

### Yorum

`NOP=3.5183`, genişletilebilirliği destekleyen en güçlü pozitif metriktir. Bu, polimorfik kullanım veya arayüz/soyut tip kullanımının bir miktar var olduğunu düşündürür.

Ancak `DCC=3.0183`, genişletilebilirliği ciddi biçimde aşağı çeker. `DCC` katkısı `-1.5092` olup, pozitif katkıların yaklaşık %75.6’sını tüketmektedir:

```text
DCC cezası / pozitif katkı = 1.5092 / 1.9962 ≈ %75.6
```

Ayrıca `ANA=0.3217` ve `MFA=0.1523` düşüktür. Bu da soyutlama ve kalıtım üzerinden genişleme noktalarının sınırlı olduğunu gösterir. CK tarafında bu yorumu destekleyen metrikler:

| CK Metrik | Ortalama | Maksimum | Yorum |
|---|---:|---:|---|
| CBO | 3.0183 | 21 | Ortalama coupling orta seviyede; bazı sınıflarda yüksek coupling var. |
| MPC | 16.7700 | 403 | Bazı sınıflar çok yoğun mesajlaşma bağımlılığına sahip. |
| DAC | 0.6917 | 10 | Bazı sınıflar çok sayıda veri/nesne bağımlılığı taşıyor. |
| DIT | 0.3217 | 3 | Kalıtım derinliği genel olarak düşük. |

Burada dikkat edilmesi gereken nokta şudur: Düşük `DIT` veya `MFA` tek başına kötü değildir; kompozisyon tercih eden modern tasarımlarda kalıtımın düşük olması bilinçli bir tercih olabilir. Ancak aynı anda `DCC=3.0183`, `CBO_max=21`, `MPC_max=403` ve `ANA=0.3217` görülüyorsa, genişleme için yeterli soyutlama yerine doğrudan sınıf bağımlılıklarının artmış olma ihtimali güçlenir.

---

## 4. Teknik Borç Göstergeleri

Bu sürümde teknik borç riski özellikle aşağıdaki metrik eğilimlerinde görülmektedir.

### 4.1 Büyük sınıf / karmaşık sınıf riski

- `WMC_mean = 15.7767`
- `WMC_max = 381`
- `NOM_mean = 6.32`
- `NOM_max = 95`

Ortalama değerler yönetilebilir görünse de maksimum değerler çok yüksektir. `WMC_max=381` ve `NOM_max=95`, bazı sınıfların “god class” veya “large class” adayı olabileceğini gösterir.

### 4.2 Düşük cohesion riski

- `CAM = 0.3641`
- `LCOM_mean = 30.2100`
- `LCOM_max = 4371`

`CAM=0.3641`, cohesion’ın çok güçlü olmadığını gösterir. CK tarafında `LCOM_max=4371` ise bazı sınıflarda sorumlulukların aşırı dağılmış olabileceğine işaret eder.

### 4.3 Coupling ve mesajlaşma yoğunluğu

- `DCC = 3.0183`
- `CBO_mean = 3.0183`
- `CBO_max = 21`
- `MPC_mean = 16.7700`
- `MPC_max = 403`
- `RFC_max = 151`

Bu değerler özellikle bazı sınıfların çok fazla dış sınıfa, metoda veya mesajlaşma ilişkisine sahip olduğunu gösterir. Bu durum değişiklik etkisinin yayılmasına, test maliyetinin artmasına ve refactoring riskinin yükselmesine neden olabilir.

---

## 5. Bakım Yapılabilirlik Yorumu

Bakım yapılabilirlik açısından tablo karışıktır:

### Olumlu sinyaller

- `DAM = 0.8794` yüksek sayılabilir; kapsülleme seviyesi iyi görünmektedir.
- `Flexibility = 1.5703` tamamen zayıf değildir; `NOP=3.5183` ve `MOA=0.6917` esneklik değerini destekler.
- `MOA=0.6917`, kompozisyon kullanımının var olduğunu gösterir.

### Olumsuz sinyaller

- `Understandability = -201.9385` çok düşüktür.
- `CAM = 0.3641` cohesion açısından sınırlıdır.
- `DCC = 3.0183` ve `CBO_max=21`, coupling kaynaklı bakım maliyeti riskini artırır.
- `WMC_max=381`, `LCOM_max=4371`, `MPC_max=403` gibi uç değerler belirli sınıflarda ciddi hotspot riski olduğunu gösterir.

**Sonuç:** Bu sürümde bakım yapılabilirlik tamamen kötü değildir; kapsülleme ve polimorfizm bazı olumlu sinyaller verir. Ancak anlaşılabilirlik, cohesion ve hotspot sınıflar bakım maliyetini artırabilecek temel risk alanlarıdır.

---

## 6. Mimari Kalite Yorumu

`DSC=600` ve `NOH=87`, JGraphT 1.5.1’in oldukça geniş bir sınıf ve hiyerarşi yapısına sahip olduğunu gösterir. Bu büyüklük, bir grafik algoritmaları kütüphanesi için doğal olabilir; ancak metrikler mimari erozyon ihtimalini tamamen dışlamaz.

Mimari erozyon açısından kanıtlar:

- `DCC=3.0183`: coupling ortalama olarak belirgin.
- `CBO_max=21`: bazı sınıflar yüksek bağlantılı.
- `MPC_max=403`: bazı sınıflar çok yoğun mesajlaşma yapıyor.
- `LCOM_max=4371`: bazı sınıflarda cohesion çok zayıf olabilir.
- `WMC_max=381`: bazı sınıflar aşırı karmaşık olabilir.
- `ANA=0.3217`, `MFA=0.1523`: soyutlama ve kalıtım katkısı sınırlı.

Bu veriler, tüm sistemin mimari olarak bozulduğunu kesin olarak kanıtlamaz. Ancak **belirli sınıflarda yoğunlaşmış karmaşıklık, coupling ve cohesion bozulması** mimari erozyon açısından incelenmesi gereken hotspot’lara işaret eder.

---

## 7. Somut Refactoring Önerileri

## Öneri 1 — Yüksek WMC/NOM sınıflarını parçala

**Hedef metrikler:**

- `WMC_max = 381`
- `NOM_max = 95`
- `RFC_max = 151`

**Problem:** Bazı sınıflar çok fazla davranış içeriyor olabilir. Bu durum sınıfın anlaşılmasını, test edilmesini ve değiştirilmesini zorlaştırır.

**Refactoring yaklaşımı:**

- `Extract Class`
- `Extract Method`
- `Move Method`
- Algoritma aileleri için `Strategy` ayrıştırması
- Yardımcı hesaplama ve doğrulama mantıklarını ayrı servis/sınıflara taşıma

**Beklenen metrik etkisi:**

- `WMC_max` düşer.
- `NOM_max` düşer.
- `RFC_max` düşer.
- `Understandability` dolaylı olarak iyileşir.

---

## Öneri 2 — Düşük cohesion gösteren sınıflarda sorumluluk ayrımı yap

**Hedef metrikler:**

- `CAM = 0.3641`
- `LCOM_mean = 30.2100`
- `LCOM_max = 4371`

**Problem:** Bazı sınıflar birbiriyle zayıf ilişkili metotlar veya veri alanları içeriyor olabilir. Bu, sınıfın tek sorumluluk ilkesinden uzaklaştığını gösterir.

**Refactoring yaklaşımı:**

- `Extract Class`
- `Split Class by Responsibility`
- Ortak veri kullanan metotları aynı sınıfta grupla
- Az ilişkili yardımcı metotları utility/helper yerine anlamlı domain bileşenlerine ayır

**Beklenen metrik etkisi:**

- `LCOM_max` ve `LCOM_mean` düşer.
- `CAM` artabilir.
- Sınıf içi tutarlılık arttığı için bakım kolaylaşır.

---

## Öneri 3 — Coupling hotspot’ları için arayüz ve bağımlılık yönünü düzenle

**Hedef metrikler:**

- `DCC = 3.0183`
- `CBO_max = 21`
- `MPC_max = 403`
- `DAC_max = 10`
- `Extendibility = 0.4870`

**Problem:** Bazı sınıflar çok fazla somut sınıfa veya veri tipine doğrudan bağımlı olabilir. Bu durum genişletilebilirliği düşürür ve değişiklik etkisini artırır.

**Refactoring yaklaşımı:**

- Somut sınıf bağımlılıklarını arayüz/soyut tip arkasına al
- `Dependency Inversion Principle` uygula
- Algoritma, graph representation ve traversal davranışlarını daha net soyutlama sınırlarına ayır
- Çok fazla çağrı yapan sınıflarda `Facade` veya `Mediator` ile bağımlılık yüzeyini daralt

**Beklenen metrik etkisi:**

- `DCC` ve `CBO_max` düşebilir.
- `MPC_max` azalabilir.
- `ANA` artabilir.
- `Extendibility` iyileşebilir.

---

## 8. Önceliklendirilmiş Aksiyon Planı

| Öncelik | Aksiyon | Hedef Metrik | Gerekçe |
|---:|---|---|---|
| 1 | `WMC_max`, `LCOM_max`, `MPC_max` değeri yüksek sınıfları listele | WMC, LCOM, MPC | Risk ortalamadan çok uç sınıflarda yoğunlaşıyor. |
| 2 | En yüksek `WMC` ve `NOM` değerli sınıflarda sınıf/metot parçalama yap | WMC, NOM, RFC | Anlaşılabilirlik ve test edilebilirlik artar. |
| 3 | En yüksek `CBO` ve `MPC` değerli sınıflarda bağımlılık yönünü düzenle | DCC, CBO, MPC | Extendibility zayıflığının ana nedeni coupling. |
| 4 | Düşük cohesion sınıflarında sorumluluk ayrımı yap | CAM, LCOM | Bakım yapılabilirlik ve değişiklik izolasyonu iyileşir. |
| 5 | Public API etkisini kontrol ederek refactoring’i küçük adımlarla yap | CIS, NOM, RFC | Kütüphane API uyumluluğu korunmalıdır. |

---

## 9. Son Değerlendirme

JGraphT 1.5.1, metriklere göre **kapsamı geniş ve işlevsel** bir sürümdür. `DSC=600`, `NOH=87`, `Reusability=301.4523` ve `Functionality=152.8887` değerleri, kütüphanenin geniş bir API ve fonksiyon seti sunduğunu gösterir.

Buna karşılık kalite açısından en kritik iki zayıflık şunlardır:

1. **Understandability zayıflığı:**  
   `Understandability=-201.9385`; ana neden `DSC=600`, ayrıca `NOM=6.32`, `DCC=3.0183`, `CAM=0.3641` ve CK tarafında `WMC_max=381`, `LCOM_max=4371`, `MPC_max=403`.

2. **Extendibility zayıflığı:**  
   `Extendibility=0.4870`; ana neden `DCC=3.0183` kaynaklı `-1.5092` ceza, düşük `ANA=0.3217` ve düşük `MFA=0.1523`.

Sonuç olarak bu sürüm için en doğru kalite yorumu şudur:

> JGraphT 1.5.1 fonksiyonel olarak zengin ve yeniden kullanılabilirliği yüksek görünen büyük bir kütüphanedir; ancak belirli sınıflarda yoğunlaşmış karmaşıklık, düşük cohesion ve coupling hotspot’ları nedeniyle anlaşılabilirlik ve genişletilebilirlik bakımından refactoring ihtiyacı taşımaktadır.
