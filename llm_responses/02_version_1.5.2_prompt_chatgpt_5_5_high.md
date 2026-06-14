# JGraphT `jgrapht-core` 1.5.2 — QMOOD Tabanlı Kalite Değerlendirmesi

## 1. Kapsam ve yorumlama notu

Bu rapor, yalnızca verilen **JGraphT 1.5.2** QMOOD ve CK metriklerine dayanır. Amaç, tek sürüm için tasarım kalitesini eleştirel ve kanıt temelli biçimde değerlendirmek, en zayıf iki kalite niteliğini belirlemek ve metrik-temelli refactoring önerileri üretmektir.

Önemli yorumlama notu: QMOOD kalite nitelikleri aynı ölçeklerde değildir. Örneğin **Reusability = 301.9390** ve **Functionality = 153.1010** değerleri çok yüksek görünür; fakat bu değerler formüllerde **DSC = 601** ve **NOH = 87** gibi boyut/hiyerarşi metriklerinden güçlü biçimde beslenir. Bu nedenle tek sürüm analizinde “en zayıf” nitelikler, sadece ham büyüklüğe değil, formül yönü, negatif/pozitif katkılar ve CK destek metrikleri birlikte okunarak seçilmiştir.

---

## 2. Verilen metriklerin kısa özeti

### 2.1 QMOOD tasarım metrikleri

| Metrik | Değer | Kısa yorum |
|---|---:|---|
| DSC | 601.0000 | Sistem büyük; 601 sınıf var. Boyut, bazı kalite skorlarını yapay olarak yükseltirken anlaşılabilirliği ağır biçimde cezalandırır. |
| NOH | 87.0000 | Hiyerarşi sayısı yüksek; Functionality formülüne pozitif katkı yapar. |
| ANA | 0.3195 | Ortalama soyutlama düşük. Extendibility ve Effectiveness için sınırlı pozitif katkı sağlar. |
| DAM | 0.8806 | Kapsülleme yüksek; Flexibility, Understandability ve Effectiveness için olumlu. |
| DCC / CBO | 3.0233 | Ortalama coupling belirgin; Reusability, Flexibility ve Extendibility’de ceza üretir. |
| CAM | 0.3633 | Cohesion düşük-orta düzeyde; Understandability ve Reusability için pozitif katkısı sınırlı. |
| MOA / DAC | 0.6938 | Kompozisyon kullanımı mevcut; Flexibility ve Effectiveness için olumlu. |
| MFA | 0.1511 | Kalıtım/kalıtımdan gelen davranış kullanımı düşük; Extendibility katkısı zayıf. |
| NOP | 3.5075 | Polimorfizm görece güçlü; Flexibility, Extendibility ve Functionality için olumlu. |
| CIS | 4.2080 | Arayüz/mesajlaşma boyutu orta-yüksek; Reusability ve Functionality için olumlu. |
| NOM | 6.2928 | Ortalama metot sayısı/karmasiklik artmış; Understandability formülünde negatif etki yapar. |

### 2.2 CK metrikleri

| CK metriği | Ortalama | Maksimum | Yorum |
|---|---:|---:|---|
| WMC | 15.7604 | 381 | Ortalama sınıf karmaşıklığı orta-yüksek; maksimum 381 değeri çok büyük “hotspot” sınıflara işaret eder. |
| CBO | 3.0233 | 21 | Ortalama coupling yönetilebilir görünse de maksimum 21, bazı sınıfların aşırı bağımlı olduğunu gösterir. |
| RFC | 17.1265 | 149 | Ortalama response set orta-yüksek; maksimum 149, bazı sınıflarda davranış yüzeyinin büyüdüğünü gösterir. |
| LCOM | 30.2213 | 4371 | Cohesion açısından ciddi risk. Ortalama 30.2213 ve maksimum 4371, bazı sınıflarda sorumluluk dağılması olabileceğini gösterir. |
| NOM | 6.2928 | 95 | Ortalama metot sayısı makul görünse de maksimum 95, “God Class” veya çok görevli sınıf riskini destekler. |
| MPC | 16.7820 | 401 | Mesaj geçişi/çağrı bağımlılığı yüksek; maksimum 401, coupling ve karmaşıklık hotspotlarını destekler. |
| DAC | 0.6938 | 10 | Kompozisyon kullanımı var; fakat maksimum 10 bazı sınıfların çok sayıda veri soyutlamasına bağlı olduğunu gösterir. |

---

## 3. Genel kalite değerlendirmesi

JGraphT 1.5.2 için kalite tablosu şu şekildedir:

| Kalite niteliği | Değer | Değerlendirme |
|---|---:|---|
| Reusability | 301.9390 | Ham değer yüksek; ancak bunun ana nedeni `0.50*DSC = 300.5000` katkısıdır. Bu değer doğrudan “tasarım çok yeniden kullanılabilir” şeklinde abartılmamalıdır. |
| Flexibility | 1.5650 | Orta düzey pozitif. `NOP = 3.5075` ve `MOA = 0.6938` destekliyor; `DCC = 3.0233` değeri ise esnekliği aşağı çekiyor. |
| Understandability | -202.2567 | En zayıf alan. Büyük boyut `DSC = 601`, karmaşıklık `NOM = 6.2928`, coupling `DCC = 3.0233` ve polimorfizm `NOP = 3.5075` birlikte negatif etki yapıyor. |
| Functionality | 153.1010 | Ham değer yüksek; fakat ana katkılar `0.22*DSC = 132.2200` ve `0.22*NOH = 19.1400`. Bu, fonksiyonel kapsamın büyüdüğünü gösterir; tasarımın sade olduğu anlamına gelmez. |
| Extendibility | 0.4774 | İkinci zayıf alan. `DCC = 3.0233` genişletilebilirliği `-1.5117` ile cezalandırıyor; düşük `ANA = 0.3195` ve `MFA = 0.1511` bu cezayı telafi edemiyor. |
| Effectiveness | 1.1105 | Pozitif ama sınırlı. `NOP = 3.5075` en büyük katkıyı verirken, düşük `ANA = 0.3195` ve `MFA = 0.1511` etkiyi sınırlıyor. |

### Genel hüküm

1.5.2 sürümü **fonksiyonel kapsam ve yeniden kullanılabilir API yüzeyi açısından güçlü**, fakat **anlaşılabilirlik ve genişletilebilirlik açısından riskli** görünmektedir. Bu sonuç, özellikle şu metriklerle desteklenir:

- **DSC = 601**: sistem büyüklüğü yüksek.
- **Understandability = -202.2567**: QMOOD formülünde açık biçimde negatif.
- **Extendibility = 0.4774**: pozitif ama zayıf; DCC cezası baskın.
- **DCC/CBO_mean = 3.0233, CBO_max = 21**: ortalama coupling yönetilebilir görünse de hotspot sınıflar var.
- **LCOM_mean = 30.2213, LCOM_max = 4371**: cohesion açısından güçlü teknik borç sinyali.
- **WMC_max = 381, NOM_max = 95, MPC_max = 401**: bazı sınıflar aşırı karmaşık ve aşırı bağlantılı olabilir.

---

## 4. En zayıf kalite niteliği 1: Understandability

### 4.1 Neden en zayıf?

**Understandability = -202.2567** değeri, tüm kalite nitelikleri içinde açık ara en problemli skordur. QMOOD formülü şöyledir:

```text
Understandability = -0.33*(ANA + DCC + NOP + NOM + DSC) + 0.33*(DAM + CAM)
```

1.5.2 değerleriyle katkılar:

| Formül katkısı | Değer |
|---|---:|
| `-0.33*ANA` | -0.1054 |
| `-0.33*DCC` | -0.9977 |
| `-0.33*NOP` | -1.1575 |
| `-0.33*NOM` | -2.0766 |
| `-0.33*DSC` | -198.3300 |
| `0.33*DAM` | 0.2906 |
| `0.33*CAM` | 0.1199 |
| **Toplam** | **-202.2567** |

### 4.2 Sorumlu metrikler

Understandability üzerinde en büyük negatif etki **DSC = 601** değerinden gelir:

- `-0.33*DSC = -198.3300`
- Toplam skor: **-202.2567**
- Yani negatif skorun çok büyük kısmı sistem boyutundan kaynaklanır.

Bunun yanında aşağıdaki metrikler de anlaşılabilirliği düşürür:

| Sorumlu metrik | Değer | Etki |
|---|---:|---|
| DSC | 601.0000 | En büyük negatif etki. Sistem büyüdükçe anlamak, test etmek ve zihinsel model kurmak zorlaşır. |
| NOM | 6.2928 | `-0.33*NOM = -2.0766`; sınıf başına davranış sayısı anlaşılabilirliği azaltır. |
| NOP | 3.5075 | `-0.33*NOP = -1.1575`; polimorfizm esneklik getirir ama davranış izlemeyi zorlaştırabilir. |
| DCC | 3.0233 | `-0.33*DCC = -0.9977`; bağımlılıklar arttıkça sınıfları izole anlamak zorlaşır. |
| CAM | 0.3633 | Pozitif ama zayıf katkı: `0.33*CAM = 0.1199`. Cohesion düşük kaldığı için telafi gücü sınırlıdır. |
| DAM | 0.8806 | Güçlü kapsülleme olumlu: `0.33*DAM = 0.2906`; ancak DSC kaynaklı cezayı telafi edemez. |

### 4.3 CK metrikleriyle destek

Understandability riskini CK metrikleri de doğrular:

- **LCOM_mean = 30.2213**, **LCOM_max = 4371**: cohesion düşüklüğü veya sorumlulukların dağılması riski.
- **WMC_mean = 15.7604**, **WMC_max = 381**: bazı sınıflarda çok yüksek davranış karmaşıklığı.
- **NOM_mean = 6.2928**, **NOM_max = 95**: bazı sınıfların çok fazla metoda sahip olduğunu gösterir.
- **RFC_max = 149** ve **MPC_max = 401**: bazı sınıflar birçok çağrı/tepki yoluna sahip; bu da davranışın anlaşılmasını zorlaştırır.

### 4.4 Ara hüküm

1.5.2’de anlaşılabilirlik sorunu yalnızca “proje büyük” olduğu için oluşmuyor; **büyük boyutun yanında yüksek LCOM, yüksek WMC hotspotları, yüksek MPC/RFC maksimumları ve düşük CAM** bir araya gelerek bakım ve kavrama maliyetini artırıyor.

---

## 5. En zayıf kalite niteliği 2: Extendibility

### 5.1 Neden ikinci en zayıf?

**Extendibility = 0.4774** pozitif görünse de çok sınırlıdır. Formül şöyledir:

```text
Extendibility = 0.50*(ANA + MFA + NOP) - 0.50*DCC
```

1.5.2 değerleriyle katkılar:

| Formül katkısı | Değer |
|---|---:|
| `0.50*ANA` | 0.1598 |
| `0.50*MFA` | 0.0756 |
| `0.50*NOP` | 1.7537 |
| `-0.50*DCC` | -1.5116 |
| **Toplam** | **0.4774** |

### 5.2 Sorumlu metrikler

| Sorumlu metrik | Değer | Etki |
|---|---:|---|
| DCC | 3.0233 | En kritik negatif faktör. `-0.50*DCC = -1.5117`. |
| ANA | 0.3195 | Soyutlama düşük; `0.50*ANA = 0.1598` katkısı zayıf. |
| MFA | 0.1511 | Kalıtım/yeniden kullanım mirası düşük; `0.50*MFA = 0.0756` katkısı çok düşük. |
| NOP | 3.5075 | En güçlü pozitif faktör; `0.50*NOP = 1.7538`. Ancak DCC cezasını tek başına sınırlı ölçüde aşabiliyor. |

Toplam pozitif Extendibility katkısı:

```text
0.50*(ANA + MFA + NOP) = 1.9890
```

DCC cezası:

```text
0.50*DCC = 1.5116
```

Bu, coupling cezasının pozitif genişletilebilirlik katkılarının yaklaşık **%76.0**’ını tükettiği anlamına gelir. Başka bir ifadeyle, JGraphT 1.5.2’de polimorfizm güçlü olsa da, **coupling ve düşük soyutlama nedeniyle genişletilebilirlik potansiyeli tam kullanılamıyor**.

### 5.3 CK metrikleriyle destek

Extendibility riskini destekleyen CK sinyalleri:

- **CBO_mean = 3.0233**, **CBO_max = 21**: bazı sınıfların yüksek dış bağımlılığı var.
- **MPC_mean = 16.7820**, **MPC_max = 401**: mesaj geçişi/çağrı bağımlılığı yüksek.
- **DAC_mean = 0.6938**, **DAC_max = 10**: bazı sınıflar birçok veri soyutlamasına bağlı olabilir.
- **DIT_mean = 0.3195**, **DIT_max = 3**: derin kalıtım yok; bu iyi olabilir, fakat QMOOD açısından ANA/MFA düşük kaldığı için soyutlama-genişletme desteği sınırlı kalır.

### 5.4 Ara hüküm

Extendibility değerinin düşük olmasının ana nedeni **DCC = 3.0233 coupling cezası** ve **ANA/MFA değerlerinin düşük kalmasıdır**. Sistem genişletilebilir, fakat genişletme noktalarının yeterince soyutlanmadığı ve bazı sınıfların yoğun bağımlılık taşıdığı anlaşılmaktadır.

---

## 6. Güçlü görünen ama dikkatli yorumlanması gereken nitelikler

### 6.1 Reusability

Reusability değeri yüksek görünür:

| Formül katkısı | Değer |
|---|---:|
| `-0.25*DCC` | -0.7558 |
| `0.25*CAM` | 0.0908 |
| `0.50*CIS` | 2.1040 |
| `0.50*DSC` | 300.5000 |
| **Toplam** | **301.9390** |

Ancak `0.50*DSC = 300.5000` katkısı toplam değerin neredeyse tamamını oluşturur. Bu nedenle **Reusability = 301.9390** değeri, tek başına “tasarım yeniden kullanım açısından çok sağlıklı” demek için yeterli değildir. Çünkü aynı sürümde:

- **DCC = 3.0233** yeniden kullanımı `-0.7558` ile cezalandırır.
- **CAM = 0.3633** cohesion katkısını yalnızca `0.0908` seviyesinde tutar.
- **LCOM_mean = 30.2213** yeniden kullanılabilir bileşenlerin iç tutarlılığı açısından risklidir.

### 6.2 Functionality

Functionality katkıları:

| Formül katkısı | Değer |
|---|---:|
| `0.12*CAM` | 0.0436 |
| `0.22*NOP` | 0.7716 |
| `0.22*CIS` | 0.9258 |
| `0.22*DSC` | 132.2200 |
| `0.22*NOH` | 19.1400 |
| **Toplam** | **153.1010** |

Functionality = **153.1010** değeri esasen fonksiyonel kapsamın büyük olduğunu gösterir:

- `0.22*DSC = 132.2200`
- `0.22*NOH = 19.1400`

Bu iyi bir kapsam göstergesi olabilir; fakat **tasarımın kolay anlaşılır veya kolay genişletilebilir olduğunu doğrudan kanıtlamaz**.

### 6.3 Flexibility ve Effectiveness

Flexibility katkıları:

| Formül katkısı | Değer |
|---|---:|
| `0.25*DAM` | 0.2202 |
| `-0.25*DCC` | -0.7558 |
| `0.50*MOA` | 0.3469 |
| `0.50*NOP` | 1.7537 |
| **Toplam** | **1.5650** |

Effectiveness katkıları:

| Formül katkısı | Değer |
|---|---:|
| `0.20*ANA` | 0.0639 |
| `0.20*DAM` | 0.1761 |
| `0.20*MOA` | 0.1388 |
| `0.20*MFA` | 0.0302 |
| `0.20*NOP` | 0.7015 |
| **Toplam** | **1.1105** |

Flexibility = **1.5650** değerini özellikle **NOP = 3.5075** ve **MOA = 0.6938** destekler. Ancak **DCC = 3.0233** esnekliği `-0.7558` ile aşağı çeker.

Effectiveness = **1.1105** pozitif ama sınırlıdır. En büyük katkı `0.20*NOP = 0.7015`; buna karşın düşük **ANA = 0.3195** ve **MFA = 0.1511** etkiyi sınırlamaktadır.

---

## 7. 3 somut refactoring önerisi

### Öneri 1 — Yüksek LCOM/WMC/NOM sınıflarında sorumluluk ayrıştırma

**Hedef metrikler:** LCOM, WMC, NOM, RFC, Understandability  
**Kanıt:**

- **LCOM_mean = 30.2213**, **LCOM_max = 4371**
- **WMC_mean = 15.7604**, **WMC_max = 381**
- **NOM_mean = 6.2928**, **NOM_max = 95**
- **RFC_max = 149**

Bu değerler, bazı sınıfların çok fazla sorumluluk ve davranış taşıdığını gösterir. Özellikle maksimum değerler ortalamadan çok yüksek olduğu için problem sistem geneline homojen dağılmamış; belirli “hotspot” sınıflarda yoğunlaşmış olabilir.

**Somut aksiyonlar:**

- WMC, NOM ve LCOM maksimumlarına sahip sınıflar listelenmeli.
- Bu sınıflarda `Extract Class`, `Extract Method`, `Move Method` ve `Introduce Parameter Object` uygulanmalı.
- Algoritma sınıflarında veri hazırlama, algoritma yürütme, sonuç üretme ve doğrulama sorumlulukları ayrılmalı.
- Bir sınıfın metotları ortak alanları kullanmıyorsa, ilgili metot grupları ayrı sınıflara taşınmalı.

**Beklenen metrik etkisi:**

- LCOM düşer.
- WMC ve NOM hotspotları azalır.
- CAM/cohesion artabilir.
- Understandability üzerindeki `NOM`, `DCC` ve dolaylı karmaşıklık baskısı azalır.

---

### Öneri 2 — Coupling hotspotları için arayüz/adapter/facade katmanı kullanımı

**Hedef metrikler:** DCC/CBO, MPC, RFC, Extendibility, Flexibility  
**Kanıt:**

- **DCC/CBO_mean = 3.0233**
- **CBO_max = 21**
- **MPC_mean = 16.7820**, **MPC_max = 401**
- **RFC_max = 149**
- Extendibility formülünde `-0.50*DCC = -1.5117`

Extendibility skoru **0.4774** düzeyinde kalmaktadır; coupling cezası pozitif genişletilebilirlik katkılarının yaklaşık **%76.0**’ını tüketmektedir.

**Somut aksiyonlar:**

- CBO ve MPC maksimumlarına sahip sınıflarda doğrudan somut sınıf bağımlılıkları tespit edilmeli.
- Çok kullanılan alt sistemler için `Facade` uygulanmalı.
- Algoritmaların veri yapılarıyla doğrudan sıkı bağ kurduğu yerlerde `interface` veya `strategy` tabanlı ayrıştırma yapılmalı.
- Dış bağımlılık üreten yardımcı sınıflar için `Adapter` veya `Port/Adapter` yaklaşımı kullanılmalı.

**Beklenen metrik etkisi:**

- DCC/CBO ve MPC düşer.
- RFC düşebilir.
- Extendibility artar; çünkü `-0.50*DCC` cezası azalır.
- Flexibility artar; çünkü `-0.25*DCC` cezası azalır.

---

### Öneri 3 — Soyutlama ve genişletme noktalarını bilinçli artırma

**Hedef metrikler:** ANA, MFA, NOP, Extendibility, Effectiveness  
**Kanıt:**

- **ANA = 0.3195** düşük.
- **MFA = 0.1511** düşük.
- **NOP = 3.5075** pozitif ve güçlü; ancak DCC cezasını sınırlı ölçüde telafi ediyor.
- Extendibility katkıları:
  - `0.50*ANA = 0.1598`
  - `0.50*MFA = 0.0756`
  - `0.50*NOP = 1.7538`
  - `-0.50*DCC = -1.5117`

Sistemde polimorfizm var; fakat soyutlama ve yeniden kullanılabilir soyut üst yapı desteği görece düşük kalıyor.

**Somut aksiyonlar:**

- Sık değişen algoritma varyasyonları için `Strategy` veya `Template Method` kullanılmalı.
- Grafik algoritmalarında ortak işlem adımları soyut taban sınıf veya arayüzlere alınmalı.
- Sadece gerçekten varyasyon noktası olan alanlarda soyutlama artırılmalı; gereksiz interface üretiminden kaçınılmalı.
- Public API yüzeyi ile iç implementasyon sınıfları net ayrılmalı.

**Beklenen metrik etkisi:**

- ANA artabilir.
- NOP korunur veya kontrollü biçimde artar.
- DCC düşerse Extendibility belirgin iyileşir.
- Effectiveness, `ANA`, `MFA` ve `NOP` katkıları üzerinden artabilir.

---

## 8. Sonuç

JGraphT 1.5.2 için genel kalite yorumu şöyledir:

- Sistem **büyük ve fonksiyonel olarak zengin** görünmektedir: **DSC = 601**, **NOH = 87**, **Functionality = 153.1010**.
- Ham **Reusability = 301.9390** yüksek görünür; fakat bu değerin ana nedeni **`0.50*DSC = 300.5000`** katkısıdır. Bu nedenle yeniden kullanılabilirlik yorumu dikkatli yapılmalıdır.
- En zayıf kalite niteliği açık biçimde **Understandability = -202.2567** değeridir. Bunun ana nedeni **DSC = 601** olmakla birlikte, **NOM = 6.2928**, **DCC = 3.0233**, **CAM = 0.3633**, **LCOM_mean = 30.2213** ve **WMC_max = 381** gibi metrikler de bakım/anlama riskini destekler.
- İkinci zayıf kalite niteliği **Extendibility = 0.4774** olarak değerlendirilmiştir. Ana sorun **DCC = 3.0233** coupling cezasıdır; düşük **ANA = 0.3195** ve **MFA = 0.1511** bu cezayı yeterince dengeleyememektedir.
- Refactoring önceliği; önce **LCOM/WMC/NOM hotspotlarının ayrıştırılması**, sonra **coupling hotspotlarının interface/facade/adapter ile gevşetilmesi**, ardından **bilinçli soyutlama ve genişletme noktalarının güçlendirilmesi** olmalıdır.

Kısa hüküm: **JGraphT 1.5.2 kapsam ve fonksiyonellik açısından güçlü, fakat anlaşılabilirlik ve genişletilebilirlik açısından teknik borç sinyalleri taşıyan bir tasarıma sahiptir.**
