# JGraphT `jgrapht-core` QMOOD Kalite Değerlendirmesi

**Rol perspektifi:** Kıdemli yazılım mimarisi ve yazılım kalitesi değerlendirmesi  
**Kapsam:** JGraphT `jgrapht-core` modülünün 0.9.0–1.5.3 sürümleri için verilen QMOOD tasarım metrikleri, QMOOD kalite nitelikleri ve CK ortalamaları  
**Yöntem:** Değerlendirme yalnızca verilen sayısal verilere dayandırılmıştır. Her yorum, ilgili metrik değişimiyle gerekçelendirilmiştir.

---

## 0. Veri ve Yorumlama Notu

Veri 3, “ilk sürüme göre normalize, 1.0=baseline” olarak verilmiş olsa da ham değerlerle birebir oran tutmamaktadır. Örneğin raw Reusability değeri 0.9.0’da **120.4746**, 1.5.3’te **310.4459** olup oran yaklaşık **2.58x**’tir; ancak normalize tabloda 1.5.3 için **1.7392** görünmektedir. Bu nedenle ana değerlendirme **Veri 1, Veri 2 ve Veri 4 raw değerleri** üzerinden yapılmıştır. Normalize tablo yalnızca eğilim kontrolü için temkinli kullanılmıştır.

Ayrıca QMOOD kalite niteliklerinin bir kısmı sistem boyutuna duyarlıdır. Özellikle **DSC**, Reusability ve Functionality formüllerinde pozitif ağırlıkla yer aldığı için sistem büyüdükçe bu iki nitelikte mutlak artış beklenir. Bu nedenle Reusability ve Functionality artışı “salt tasarım iyileşmesi” olarak değil, **büyüme etkisiyle birlikte** yorumlanmalıdır.

---

## 1. Genel Kalite Değerlendirmesi

### 1.1 Genel eğilim

JGraphT `jgrapht-core`, incelenen sürümlerde ciddi biçimde büyümüştür: **DSC 238’den 618’e çıkmıştır**. Bu yaklaşık **+%159.7** artış demektir. Aynı dönemde NOH **35’ten 91’e** yükselmiş, yani hiyerarşi sayısı da yaklaşık **+%160** artmıştır.

Bu büyüme, bazı QMOOD kalite niteliklerini yukarı taşırken bazı mimari kalite sinyallerini zayıflatmıştır. Genel tablo şöyledir:

| Nitelik | 0.9.0 | 1.5.3 | Değişim | Yorum |
|---|---:|---:|---:|---|
| Reusability | 120.4746 | 310.4459 | +189.9713 / +%157.7 | Güçlü artış var; ancak büyük ölçüde DSC ve CIS artışıyla destekleniyor. |
| Functionality | 61.6914 | 157.7334 | +96.0420 / +%155.7 | Güçlü artış var; DSC, CIS, NOH ve NOP katkılı. |
| Flexibility | 1.4611 | 1.5861 | +0.1250 / +%8.6 | Sınırlı artış; 1.2.0’da tepeye çıkıp sonra geriliyor. |
| Effectiveness | 1.0821 | 1.1205 | +0.0384 / +%3.5 | Neredeyse yatay; belirgin kalite sıçraması yok. |
| Extendibility | 0.8944 | 0.4923 | -0.4021 / -%45.0 | Belirgin bozulma; soyutlama ve kalıtım göstergeleri düşerken coupling artıyor. |
| Understandability | -81.8694 | -207.8903 | -126.0209 | Daha negatif hale geliyor; anlaşılabilirlik ciddi biçimde zayıflıyor. |

### 1.2 İyileşen nitelikler

**Reusability** 0.9.0’daki **120.4746** seviyesinden 1.5.3’te **310.4459** seviyesine çıkmıştır. Bu artış ilk bakışta çok olumlu görünür. Ancak formülde **DSC’nin 0.50 katsayıyla** yer alması nedeniyle, sınıf sayısının **238’den 618’e** çıkması bu artışın ana sürücülerinden biridir. CIS de **3.9202’den 4.2249’a** yükselmiştir; bu da arayüz/mesajlaşma kapasitesinin arttığını gösterir. Buna karşılık DCC **2.3487’den 3.0324’e** yükselerek Reusability üzerinde negatif baskı oluşturmuştur. Yani reuse potansiyeli artmıştır; fakat bu artışın bir bölümü gerçek tasarım iyileşmesinden çok sistem büyüklüğünden kaynaklanıyor olabilir.

**Functionality** de **61.6914’ten 157.7334’e** yükselmiştir. Bu yaklaşık **+%155.7** artıştır. Formülde DSC, CIS, NOP ve NOH pozitif katkı verdiği için DSC’nin **+%159.7**, NOH’un **+%160**, CIS’in **+%7.8** ve NOP’un **+%8.3** artması Functionality skorunu yukarı çekmiştir. Bu, kütüphanenin işlevsel kapsamının genişlediğini destekler.

**Flexibility** sınırlı düzeyde iyileşmiştir: **1.4611’den 1.5861’e** çıkmıştır. Ancak bu nitelik monoton değildir. En yüksek değer **1.6541 ile 1.2.0** sürümündedir; 1.5.3’te bu değerin altına düşülmüştür. Flexibility artışını destekleyen temel metrik MOA’dır: **0.3739’dan 0.7006’ya** yükselmiştir (**+%87.4**). Buna karşılık DCC’nin **+%29.1** artması esnekliği sınırlamıştır.

### 1.3 Bozulan nitelikler

**Understandability**, en kritik bozulma sinyalidir. Değer **-81.8694’ten -207.8903’e** düşmüştür. QMOOD formülünde Understandability; ANA, DCC, NOP, NOM ve DSC artışlarından negatif etkilenir; DAM ve CAM artışlarından pozitif etkilenir. İncelenen dönemde DSC **+%159.7**, DCC **+%29.1**, NOM **+%22.7**, NOP **+%8.3** artarken; CAM **0.4070’den 0.3660’a** düşmüştür (**-%10.1**). DAM ise **0.8990’dan 0.8850’a** hafif gerilemiştir. Bu kombinasyon anlaşılabilirliğin neden ciddi biçimde bozulduğunu açıklar.

**Extendibility** de belirgin biçimde zayıflamıştır: **0.8944’ten 0.4923’e** düşmüştür (**-%45.0**). Bu düşüşün ana nedenleri ANA’nın **0.6176’dan 0.3204’e** gerilemesi (**-%48.1**), MFA’nın **0.2469’dan 0.1512’ye** düşmesi (**-%38.8**) ve DCC’nin **2.3487’den 3.0324’e** yükselmesidir (**+%29.1**). Yani sistem büyürken yeni davranış ekleme kapasitesi, en azından QMOOD ölçütlerine göre, zayıflamıştır.

---

## 2. Bakım Yapılabilirlik Analizi

Bakım yapılabilirlik açısından sonuç karışıktır; ancak genel risk yönü **bakımın zorlaşmasıdır**.

### 2.1 Understandability bakım riskini artırıyor

Understandability’nin **-81.8694’ten -207.8903’e** gerilemesi, kod tabanını anlamanın sürümler ilerledikçe zorlaştığını gösterir. Burada en güçlü sürücü DSC artışıdır: sınıf sayısı **238’den 618’e** çıkmıştır. Bu büyüme tek başına kötü değildir; ancak aynı anda NOM **5.1555’ten 6.3236’ya**, DCC **2.3487’den 3.0324’e** ve CK tarafında WMC **10.3613’ten 15.7848’e** yükselmiştir. Yani yalnızca daha fazla sınıf yoktur; sınıflar ortalamada daha karmaşık ve daha bağlantılı hale gelmiştir.

### 2.2 Flexibility sınırlı iyileşiyor ama coupling bunu gölgeliyor

Flexibility **1.4611’den 1.5861’e** yükselmiştir; bu yaklaşık **+%8.6**’lık sınırlı bir iyileşmedir. Bu iyileşmenin ana destekçisi MOA/DAC artışıdır: MOA **0.3739’dan 0.7006’ya**, CK tarafında DAC da aynı şekilde **0.3739’dan 0.7006’ya** çıkmıştır. Bu, kompozisyon/veri soyutlama kullanımının arttığını gösterir.

Ancak aynı dönemde DCC/CBO **2.3487’den 3.0324’e** yükselmiştir. Coupling artışı, kompozisyonun sağladığı esneklik kazanımını kısmen tüketmektedir. Bu yüzden Flexibility artışı güçlü değil, sınırlı ve kırılgandır.

### 2.3 Cohesion tarafında zayıflama var

CAM **0.4070’den 0.3660’a** düşmüştür (**-%10.1**). CK tarafında LCOM_mean ise **13.7563’ten 31.2379’a** çıkmıştır (**+%127.1**). Bu iki sinyal birlikte okunduğunda sınıf içi sorumlulukların daha dağınık hale geldiği ve cohesion’ın zayıfladığı görülür.

Özellikle 1.0.1’den 1.1.0’a geçişte LCOM_mean **11.8269’dan 24.6991’e** yükselmiştir. Bu tek geçişte yaklaşık **+%108.8** artış anlamına gelir. Bu sıçrama, belirli sürümlerde yeni özellik eklenirken sınıf sorumluluklarının ayrıştırılmadan büyütülmüş olabileceğine işaret eder.

### 2.4 Sonuç

Bakım yapılabilirlik yönünden şu sonuç çıkarılabilir:

- İşlevsel kapsam büyümüştür; bu olumlu bir ürün/kütüphane evrimi sinyalidir.
- Ancak Understandability ciddi biçimde bozulmuştur.
- Coupling artmış, cohesion zayıflamış, WMC/RFC/LCOM yükselmiştir.
- Bu nedenle uzun vadeli bakım maliyetinin azaldığını değil, **arttığını** söylemek daha tutarlıdır.

---

## 3. Teknik Borç Tahmini

Veriler teknik borç birikimine işaret eden birkaç güçlü eğilim göstermektedir.

### 3.1 Coupling artışı

DCC/CBO **2.3487’den 3.0324’e** yükselmiştir (**+%29.1**). Bu, sınıfların ortalamada daha fazla dış sınıfa bağımlı hale geldiğini gösterir. Coupling artışı değişiklik yayılımı riskini artırır: bir sınıftaki değişiklik daha fazla sınıfı etkileyebilir.

Ayrıca MPC_mean **8.6681’den 16.8511’e** çıkmıştır (**+%94.4**). Bu, metot çağrısı/mesajlaşma yoğunluğunun belirgin şekilde arttığını gösterir. DCC ve MPC birlikte değerlendirildiğinde bağımlılık yoğunluğunun yalnızca yapısal değil, davranışsal düzeyde de arttığı söylenebilir.

### 3.2 Complexity artışı

WMC_mean **10.3613’ten 15.7848’e** çıkmıştır (**+%52.3**). RFC_mean ise **11.2353’ten 17.2508’e** yükselmiştir (**+%53.5**). Bu, sınıfların hem daha fazla/karmaşık davranış içerdiğini hem de tetikleyebileceği yanıt kümesinin büyüdüğünü gösterir.

NOM_mean de **5.1555’ten 6.3236’ya** çıkmıştır (**+%22.7**). Bu tek başına büyük bir artış gibi görünmeyebilir; fakat WMC ve RFC artışıyla birlikte düşünüldüğünde, metot sayısı artarken davranış karmaşıklığının da büyüdüğü anlaşılır.

### 3.3 Cohesion zayıflaması

LCOM_mean **13.7563’ten 31.2379’a** yükselmiştir (**+%127.1**). CAM ise **0.4070’den 0.3660’a** düşmüştür (**-%10.1**). Bu, sınıfların daha az odaklı hale geldiğine ve birden fazla sorumluluğu taşımaya başlamış olabileceğine işaret eder.

Bu, teknik borç açısından güçlü bir sinyaldir; çünkü düşük cohesion, değişikliklerin sınıf içinde daha fazla yan etki üretmesine ve test/onarım maliyetinin artmasına neden olur.

### 3.4 Extendibility düşüşü

Extendibility **0.8944’ten 0.4923’e** düşmüştür (**-%45.0**). Bunun arkasında ANA’nın **-%48.1**, MFA’nın **-%38.8** düşmesi ve DCC’nin **+%29.1** artması vardır. Bu, sistemin büyüdükçe daha fazla özellik sunsa da yeni varyasyonları temiz extension point’ler üzerinden ekleme kapasitesinin zayıfladığını düşündürür.

### 3.5 Teknik borç yorumu

Teknik borç sinyali özellikle şu metrik kombinasyonundan gelir:

- **DCC/CBO:** 2.3487 → 3.0324 (**+%29.1**)
- **WMC:** 10.3613 → 15.7848 (**+%52.3**)
- **RFC:** 11.2353 → 17.2508 (**+%53.5**)
- **LCOM:** 13.7563 → 31.2379 (**+%127.1**)
- **CAM:** 0.4070 → 0.3660 (**-%10.1**)
- **Extendibility:** 0.8944 → 0.4923 (**-%45.0**)

Bu tablo, “daha büyük ama daha zor anlaşılır ve daha zor genişletilir” bir evrime işaret etmektedir.

---

## 4. Refactoring Önerileri

Aşağıdaki öneriler doğrudan metrik eğilimlerine dayalıdır.

### 4.1 Coupling azaltma: paket ve bağımlılık sınırlarını yeniden düzenleme

**Gerekçe:** DCC/CBO **2.3487’den 3.0324’e** çıkmıştır; MPC_mean de **8.6681’den 16.8511’e** yükselmiştir. Bu, sınıflar arası etkileşimin arttığını gösterir.

**Öneri:**

- Algoritma, graph model, traversal, utility ve adapter benzeri sorumlulukları net paket sınırlarıyla ayır.
- Döngüsel veya karşılıklı bağımlılık üreten sınıfları tespit et.
- Yüksek CBO/DCC değerli sınıflarda dependency inversion, interface segregation ve facade kullan.
- Utility/helper sınıflarına aşırı bağımlı merkezi akışlar varsa bunları domain odaklı servislere böl.

**Beklenen metrik etkisi:** DCC/CBO ve MPC düşer; Flexibility ve Understandability üzerindeki negatif baskı azalır.

### 4.2 Cohesion artırma: Extract Class / Move Method / Split Responsibility

**Gerekçe:** LCOM_mean **13.7563’ten 31.2379’a** çıkmıştır; CAM **0.4070’den 0.3660’a** düşmüştür. Bu, sınıf içi sorumlulukların dağıldığını gösterir.

**Öneri:**

- En yüksek LCOM değerli sınıfları önceliklendir.
- Birden fazla algoritmik rol taşıyan sınıfları daha küçük strateji veya yardımcı bileşenlere ayır.
- Sınıfta yalnızca belirli alanları kullanan metot kümeleri varsa bunları ayrı sınıfa taşı.
- State ve behavior kümeleri birlikte hareket etmiyorsa Extract Class uygula.

**Beklenen metrik etkisi:** LCOM düşer, CAM artar, Understandability üzerindeki negatif etki azalır.

### 4.3 Complexity azaltma: büyük metot/sınıf davranışlarını ayrıştırma

**Gerekçe:** WMC_mean **10.3613’ten 15.7848’e** çıkmıştır; RFC_mean **11.2353’ten 17.2508’e** yükselmiştir. Bu, sınıfların davranışsal karmaşıklığının arttığını gösterir.

**Öneri:**

- Yüksek WMC sınıflarında uzun/koşullu algoritmik akışları küçük private metotlara veya ayrı strategy sınıflarına böl.
- Büyük switch/if-else karar yapıları varsa polymorphic dispatch veya strategy pattern değerlendir.
- Algoritma sınıflarında traversal, validation, result construction ve configuration sorumluluklarını ayır.

**Beklenen metrik etkisi:** WMC ve RFC düşer; test edilebilirlik ve lokal anlaşılabilirlik artar.

### 4.4 Arayüz yüzeyini kontrol etme: CIS/NOM büyümesini dengeleme

**Gerekçe:** CIS **3.9202’den 4.2249’a**, NOM **5.1555’ten 6.3236’ya** çıkmıştır. Functionality artışı olumlu olsa da genişleyen public API yüzeyi bakım yükünü artırabilir.

**Öneri:**

- Geniş public sınıflarda interface segregation uygula.
- Kullanıcıya açık API ile iç implementasyon API’lerini ayır.
- Aşırı genel sınıflarda dar ve amaç odaklı facade’lar tanımla.
- Deprecated/legacy API yüzeyleri varsa kontrollü sadeleştirme planı yap.

**Beklenen metrik etkisi:** NOM/CIS artışının bakım maliyeti düşer; Understandability iyileşir.

### 4.5 Extension point tasarımını güçlendirme

**Gerekçe:** Extendibility **0.8944’ten 0.4923’e** düşmüştür; ANA **0.6176’dan 0.3204’e**, MFA **0.2469’dan 0.1512’ye** gerilemiştir. DCC ise artmıştır.

**Öneri:**

- Algoritma aileleri için açık extension point’ler belirle.
- Graph türleri, traversal stratejileri, weighting, path-finding ve matching gibi varyasyon noktalarını interface/strategy üzerinden soyutla.
- Kalıtımı artırmak tek başına hedef olmamalı; amaç kontrollü soyutlama ve düşük coupling olmalıdır.
- Kullanıcıların genişletmesi beklenen sınıflar ile internal sınıflar net ayrılmalıdır.

**Beklenen metrik etkisi:** ANA ve extension-oriented tasarım iyileşir; DCC baskısı azaltılırsa Extendibility toparlanabilir.

---

## 5. Mimari Kalite Yorumu: Architectural Erosion Var mı?

Veriler mimari bozulma, yani **architectural erosion**, için orta-güçlü sinyaller göstermektedir; ancak bu “tam mimari çöküş” olarak yorumlanmamalıdır. Daha doğru ifade şudur: **sistem büyürken işlevsellik ve yeniden kullanılabilirlik artmış, fakat anlaşılabilirlik, cohesion ve genişletilebilirlik belirgin biçimde zayıflamıştır.**

### 5.1 Erosion lehine kanıtlar

Büyüme çok yüksektir: DSC **238’den 618’e** çıkmıştır (**+%159.7**). Bu büyümeye eşlik eden kalite sinyalleri şunlardır:

- DCC/CBO **2.3487’den 3.0324’e** çıkmıştır (**+%29.1**).
- WMC_mean **10.3613’ten 15.7848’e** çıkmıştır (**+%52.3**).
- RFC_mean **11.2353’ten 17.2508’e** çıkmıştır (**+%53.5**).
- LCOM_mean **13.7563’ten 31.2379’a** çıkmıştır (**+%127.1**).
- CAM **0.4070’den 0.3660’a** düşmüştür (**-%10.1**).
- Understandability **-81.8694’ten -207.8903’e** gerilemiştir.
- Extendibility **0.8944’ten 0.4923’e** düşmüştür (**-%45.0**).

Bu kombinasyon, büyümenin yalnızca yeni sınıf ekleme yoluyla değil, aynı zamanda daha karmaşık, daha fazla bağımlı ve daha düşük cohesion’lı sınıflar üretme yönünde ilerlediğini gösterir.

### 5.2 Erosion aleyhine veya dengeleyici kanıtlar

Tamamen negatif bir tablo da yoktur:

- MOA/DAC **0.3739’dan 0.7006’ya** çıkmıştır (**+%87.4**). Bu, kompozisyon/veri soyutlama kullanımının arttığını gösterir.
- Functionality **61.6914’ten 157.7334’e** çıkmıştır (**+%155.7**). Kütüphanenin işlevsel kapsamı belirgin biçimde büyümüştür.
- Reusability **120.4746’dan 310.4459’a** çıkmıştır (**+%157.7**). API ve sınıf çeşitliliği reuse potansiyelini artırmış olabilir.
- Effectiveness **1.0821’den 1.1205’e** yükselmiştir; ancak artış yalnızca **+%3.5** olduğu için güçlü bir mimari iyileşme kanıtı değildir.

### 5.3 Sonuç

Mimari kalite açısından en makul değerlendirme şudur:

> JGraphT `jgrapht-core` incelenen sürümlerde işlevsel olarak büyümüş ve reuse/functionality skorlarını yükseltmiştir; ancak bu büyüme coupling, complexity ve cohesion maliyetiyle gerçekleşmiştir. Özellikle Understandability ve Extendibility düşüşleri, mimari erozyon riskinin arttığını göstermektedir.

Bu nedenle kalite evrimi “genel olarak iyileşti” şeklinde tek boyutlu yorumlanmamalıdır. Daha doğru yorum: **ürün/kapsam kalitesi artarken iç tasarım sürdürülebilirliği zayıflamıştır.**

---

## 6. Kısa Yönetici Özeti

- **En güçlü pozitif eğilim:** Functionality ve Reusability artışı. Functionality **61.6914 → 157.7334**, Reusability **120.4746 → 310.4459**.
- **En güçlü negatif eğilim:** Understandability ve Extendibility bozulması. Understandability **-81.8694 → -207.8903**, Extendibility **0.8944 → 0.4923**.
- **Bakım yapılabilirlik sonucu:** Bakım kolaylaşmamış; büyük olasılıkla zorlaşmıştır. Çünkü DCC, WMC, RFC ve LCOM artarken CAM düşmüştür.
- **Teknik borç sinyali:** LCOM’daki **+%127.1**, WMC’deki **+%52.3**, RFC’deki **+%53.5** ve DCC’deki **+%29.1** artış birlikte güçlü borç göstergesidir.
- **Mimari yorum:** Architectural erosion belirtisi vardır; ancak işlevsel büyüme ve kompozisyon kullanımındaki artış nedeniyle bu durum kontrollü refactoring ile tersine çevrilebilir.

---

## 7. Öncelikli Aksiyon Listesi

1. En yüksek DCC/CBO ve MPC değerlerine sahip sınıflar için bağımlılık azaltma çalışması yap.
2. En yüksek LCOM değerli sınıflarda Extract Class ve Move Method refactoring’i uygula.
3. Yüksek WMC/RFC sınıflarında algoritmik akışları strategy/facade/helper bileşenlerine ayır.
4. Public API yüzeyini gözden geçir; geniş interface ve sınıfları daha dar sorumluluklara böl.
5. Extension point’leri netleştir; yeni graph/algorithm varyasyonlarının düşük coupling ile eklenmesini sağla.

