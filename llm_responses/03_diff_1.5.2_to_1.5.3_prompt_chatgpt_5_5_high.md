# JGraphT 1.5.2 → 1.5.3 QMOOD Tasarım Metrikleri Fark Analizi

## 1. Kapsam ve Yöntem

Bu rapor, JGraphT `jgrapht-core` modülünün **1.5.2 → 1.5.3** geçişindeki nesne yönelimli tasarım metriği değişimlerini QMOOD modeli açısından yorumlar. Değerlendirme yalnızca verilen sayısal metriklere dayalıdır.

Önemli not: Bu iki sürüm arasındaki değişimler genel olarak küçüktür. Bu nedenle raporda güçlü mimari dönüşüm iddiası yerine, **küçük fakat yön gösteren kalite sinyalleri** yorumlanmıştır.

---

## 2. Metrik Değişim Özeti

| Metrik | 1.5.2 | 1.5.3 | Değişim | QMOOD Etkisi |
|---|---:|---:|---:|---|
| DSC | 601.000 | 618.000 | +2.8% | Reusability ve Functionality'yi artırır; Understandability'yi düşürür |
| NOH | 87.000 | 91.000 | +4.6% | Functionality'yi artırır |
| ANA | 0.320 | 0.320 | +0.3% | Extendibility ve Effectiveness için küçük olumlu etki |
| DAM | 0.881 | 0.885 | +0.5% | Flexibility, Understandability ve Effectiveness için küçük olumlu etki |
| DCC | 3.023 | 3.032 | +0.3% | Coupling arttığı için Reusability, Flexibility, Understandability ve Extendibility üzerinde olumsuz etki |
| CAM | 0.363 | 0.366 | +0.7% | Cohesion arttığı için Reusability, Understandability ve Functionality için olumlu etki |
| MOA | 0.694 | 0.701 | +1.0% | Flexibility ve Effectiveness için olumlu etki |
| MFA | 0.151 | 0.151 | +0.1% | Extendibility ve Effectiveness için çok küçük olumlu etki |
| NOP | 3.507 | 3.545 | +1.1% | Flexibility, Functionality, Extendibility ve Effectiveness için olumlu; Understandability formülünde negatif |
| CIS | 4.208 | 4.225 | +0.4% | Reusability ve Functionality için olumlu etki |
| NOM | 6.293 | 6.324 | +0.5% | Understandability üzerinde olumsuz etki |

---

## 3. Kalite Açısından Genel Yorum

1.5.3, 1.5.2'ye göre **işlevsel kapsam ve yeniden kullanılabilirlik açısından hafif olumlu**, fakat **anlaşılabilirlik açısından hafif olumsuz** bir değişim göstermektedir.

Bunun temel nedeni, sistem boyutunun artmasıdır. **DSC 601'den 618'e çıkarak %2.8 artmıştır.** QMOOD formüllerinde DSC, Reusability ve Functionality için pozitif katsayıya sahiptir; bu nedenle büyüme bu iki niteliği doğal olarak yukarı iter. Ancak aynı DSC, Understandability formülünde negatif taraftadır. Bu yüzden aynı büyüme, bakım ve anlama maliyeti açısından olumsuz sinyal üretir.

Kalite nitelikleri formüller üzerinden yeniden hesaplandığında yaklaşık değişim şöyledir:

| Kalite Niteliği | 1.5.2 | 1.5.3 | Değişim | Yorum |
|---|---:|---:|---:|---|
| Reusability | 301.9390 | 310.4459 | +8.5069 | Artışın ana nedeni DSC'nin 601 → 618 yükselmesidir |
| Flexibility | 1.5650 | 1.5861 | +0.0211 | MOA, NOP ve DAM artışı olumlu; DCC artışı sınırlı olumsuz etki yapar |
| Understandability | -202.2567 | -207.8903 | -5.6336 | DSC, DCC, NOP ve NOM artışları anlaşılabilirliği düşürür |
| Functionality | 153.1010 | 157.7334 | +4.6324 | DSC 601 → 618 ve NOH 87 → 91 artışı belirleyicidir |
| Extendibility | 0.4774 | 0.4923 | +0.0149 | NOP artışı, DCC artışına rağmen küçük iyileşme sağlar |
| Effectiveness | 1.1105 | 1.1205 | +0.0100 | DAM, MOA ve NOP artışları küçük olumlu etki üretir |

Genel kalite yorumu: **1.5.3 fonksiyonel kapasiteyi ve yeniden kullanılabilirliği artırmış görünür; ancak bu artış büyük ölçüde sistem boyutunun büyümesinden kaynaklandığı için tek başına mimari iyileşme olarak yorumlanmamalıdır.**

---

## 4. Olumlu Değişimler

### 4.1. İşlevsel kapasite artmıştır

Functionality değeri yaklaşık **153.1010'dan 157.7334'e** yükselmiştir. Bu artışın en güçlü açıklaması, QMOOD Functionality formülündeki pozitif terimlerdir:

- **DSC:** 601 → 618, **+17 sınıf**, %2.8 artış
- **NOH:** 87 → 91, **+4 hiyerarşi**, %4.6 artış
- **NOP:** 3.507 → 3.545, %1.1 artış
- **CIS:** 4.208 → 4.225, %0.4 artış
- **CAM:** 0.363 → 0.366, %0.7 artış

Bu tablo, 1.5.3'te API/yapı kapsamının genişlediğini ve sistemin daha fazla işlevsel yüzey sunduğunu gösterir.

### 4.2. Flexibility sınırlı şekilde iyileşmiştir

Flexibility yaklaşık **1.5650'dan 1.5861'e** yükselmiştir. Bu artışın sorumlu metrikleri şunlardır:

- **MOA:** 0.694 → 0.701, %1.0 artış
- **NOP:** 3.507 → 3.545, %1.1 artış
- **DAM:** 0.881 → 0.885, %0.5 artış

Bu metrikler kompozisyon, polimorfizm ve kapsülleme tarafında küçük iyileşmeye işaret eder. Ancak **DCC 3.023 → 3.032** yükseldiği için coupling kaynaklı negatif etki tamamen ortadan kalkmamıştır.

### 4.3. Cohesion küçük de olsa iyileşmiştir

**CAM 0.363'ten 0.366'ya** çıkmıştır. Artış yalnızca **%0.7** olduğu için büyük bir tasarım toparlanması iddia edilemez; fakat cohesion yönü olumludur. Bu artış Reusability, Understandability ve Functionality formüllerinde pozitif katkı yapar.

---

## 5. Olumsuz Değişimler

### 5.1. Understandability daha da kötüleşmiştir

Understandability yaklaşık **-202.2567'den -207.8903'e** düşmüştür. Bu, 1.5.3'ün anlaşılabilirlik açısından 1.5.2'ye göre daha maliyetli hale geldiğini gösterir.

Sorumlu metrikler:

- **DSC:** 601 → 618, %2.8 artış
- **DCC:** 3.023 → 3.032, %0.3 artış
- **NOP:** 3.507 → 3.545, %1.1 artış
- **NOM:** 6.293 → 6.324, %0.5 artış

QMOOD Understandability formülünde DSC, DCC, NOP ve NOM negatif tarafta yer alır. Bu nedenle sistem büyüdükçe ve coupling/karmasiklik hafif arttıkça anlaşılabilirlik değeri düşmektedir.

Burada özellikle **DSC artışı** baskındır. 17 yeni sınıf veya sınıf düzeyinde büyüme, sistemin bilişsel yükünü artırmıştır. DAM ve CAM tarafındaki küçük iyileşmeler bu negatif etkiyi dengelemeye yetmemiştir.

### 5.2. Coupling hafif artmıştır

**DCC 3.023'ten 3.032'ye** çıkmıştır. Değişim yalnızca **%0.3** olduğu için dramatik bir coupling bozulması yoktur. Ancak DCC, QMOOD'da birden fazla kalite niteliğini negatif etkiler:

- Reusability: `-0.25 * DCC`
- Flexibility: `-0.25 * DCC`
- Understandability: negatif bileşen içinde
- Extendibility: `-0.50 * DCC`

Bu nedenle küçük artış bile özellikle uzun vadede izlenmelidir.

### 5.3. Karmaşıklık hafif artmıştır

**NOM 6.293'ten 6.324'e** yükselmiştir. Bu yalnızca **%0.5** artıştır; tek başına güçlü teknik borç kanıtı değildir. Fakat Understandability formülünde NOM negatif tarafta olduğundan, sistemin anlaşılabilirlik kaybına katkı yapar.

---

## 6. Teknik Borç Değerlendirmesi

Bu geçişte **zayıf fakat izlenmesi gereken teknik borç sinyali** vardır. Güçlü bir mimari bozulma iddiası için değişimler çok küçük kalmaktadır; ancak bazı yönler risklidir.

### Teknik borç lehine sinyaller

1. **Coupling artmıştır:** DCC 3.023 → 3.032. Artış küçük olsa da DCC birçok kalite niteliğinde negatif katsayıya sahiptir.
2. **Karmaşıklık artmıştır:** NOM 6.293 → 6.324. Bu, sınıf/metot yüzeyinin genişlediğini ve anlama maliyetinin hafif yükseldiğini gösterir.
3. **Anlaşılabilirlik düşmüştür:** Understandability -202.2567 → -207.8903. Bu, en net negatif kalite sinyalidir.
4. **Sistem boyutu büyümüştür:** DSC 601 → 618. Büyüme tek başına borç değildir; fakat coupling ve NOM artışıyla birlikte okununca bakım yükünü artırabilir.

### Teknik borcu sınırlayan olumlu sinyaller

1. **CAM artmıştır:** 0.363 → 0.366. Cohesion tarafında küçük iyileşme vardır.
2. **DAM artmıştır:** 0.881 → 0.885. Kapsülleme hafif güçlenmiştir.
3. **MOA artmıştır:** 0.694 → 0.701. Kompozisyon kullanımı az da olsa artmıştır.
4. **Extendibility yükselmiştir:** 0.4774 → 0.4923. DCC artışına rağmen NOP ve diğer pozitif terimler küçük iyileşme sağlamıştır.

Sonuç olarak teknik borç değerlendirmesi: **1.5.3'te teknik borç açısından alarm seviyesi yüksek değildir; ancak Understandability düşüşü, DCC artışı ve NOM artışı nedeniyle bakım maliyeti yönünde küçük bir borç birikimi sinyali vardır.**

---

## 7. Kalite Açısından Nihai Karar

**1.5.2 → 1.5.3 geçişi kalite açısından karma fakat hafif olumlu bir sürümdür.**

Olumlu taraf:

- Reusability yaklaşık **301.9390 → 310.4459** yükselmiştir.
- Functionality yaklaşık **153.1010 → 157.7334** yükselmiştir.
- Flexibility yaklaşık **1.5650 → 1.5861** yükselmiştir.
- Extendibility yaklaşık **0.4774 → 0.4923** yükselmiştir.
- CAM, DAM, MOA ve NOP küçük de olsa olumlu yönde değişmiştir.

Olumsuz taraf:

- Understandability yaklaşık **-202.2567 → -207.8903** düşmüştür.
- DCC **3.023 → 3.032** artmıştır.
- NOM **6.293 → 6.324** artmıştır.
- DSC **601 → 618** büyüdüğü için sistemin bilişsel yükü artmıştır.

Bu nedenle nihai yorum:

> JGraphT 1.5.3, 1.5.2'ye göre daha geniş işlevsel kapsama ve hafif daha iyi esneklik/yeniden kullanılabilirlik sinyallerine sahiptir. Ancak bu kazanım, anlaşılabilirlikteki düşüş ve coupling/karmasiklikteki küçük artışlarla birlikte gelmiştir. Dolayısıyla değişim kalite açısından tamamen olumlu değil; **kontrollü büyüme fakat bakım maliyeti riski artan bir geçiş** olarak değerlendirilmelidir.

---

## 8. İzleme ve Refactoring Önerileri

### 8.1. Coupling artışı için bağımlılık azaltma

DCC **3.023 → 3.032** yükseldiği için yeni veya değişen sınıflarda bağımlılık yönleri incelenmelidir. Özellikle çok sayıda sınıfa doğrudan bağımlı servis/algoritma sınıflarında:

- interface üzerinden bağımlılık,
- dependency inversion,
- adapter/facade kullanımı,
- paketler arası bağımlılık yönünün sadeleştirilmesi

uygulanabilir.

### 8.2. NOM artışı için sınıf sorumluluğu ayrıştırma

NOM **6.293 → 6.324** yükselmiştir. Artış küçük olsa da Understandability üzerinde negatif etkilidir. Çok fazla metot barındıran sınıflarda:

- Extract Class,
- Extract Method,
- Strategy ayrıştırması,
- algoritma varyantlarını ayrı sınıflara taşıma

uygulanmalıdır.

### 8.3. Büyüme kaynaklı anlaşılabilirlik kaybını sınırlama

DSC **601 → 618** ve NOH **87 → 91** artmıştır. Bu büyüme Functionality açısından olumlu olsa da Understandability'yi aşağı çekmektedir. Bu nedenle yeni eklenen sınıflar için:

- paket/modül sınırları netleştirilmeli,
- public API yüzeyi sade tutulmalı,
- sınıflar arası kullanım örüntüleri dokümante edilmeli,
- yüksek coupling üreten yeni sınıflar erken aşamada yeniden düzenlenmelidir.

---

## 9. Kısa Sonuç

1.5.3 sürümü, 1.5.2'ye göre **işlevsellik, yeniden kullanılabilirlik, esneklik ve genişletilebilirlik açısından küçük iyileşmeler** göstermektedir. Ancak **Understandability düşmüş**, DCC ve NOM hafif artmıştır. Bu nedenle sürüm, kalite açısından **hafif olumlu fakat bakım maliyeti açısından dikkat gerektiren** bir geçiştir.
