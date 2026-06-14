# JGraphT 0.9.0 → 0.9.2 QMOOD Tasarım Metrikleri Fark Analizi

## 1. Kapsam ve yorumlama notu

Bu rapor, yalnızca verilen QMOOD tasarım metrikleri üzerinden **JGraphT `jgrapht-core` 0.9.0 → 0.9.2** geçişini değerlendirir. Yorumlar sistem düzeyi ortalamalara dayalıdır; sınıf bazlı dağılım, paket bağımlılık grafiği veya değişiklik seti verilmediği için teknik borç yorumu **belirti düzeyinde** yapılmıştır.

QMOOD formüllerinde özellikle **DSC** doğrudan kalite niteliklerine büyük katsayılarla girdiği için, bazı kalite artışları gerçek tasarım iyileşmesinden çok sistemin büyümesinden kaynaklanabilir. Bu nedenle değerlendirmede ham kalite puanının yanında metrik kaynakları da ayrıca yorumlanmıştır.

---

## 2. Genel değişim özeti

| Metrik | 0.9.0 | 0.9.2 | Değişim | Kalite yorumu |
|---|---:|---:|---:|---|
| DSC | 238.000 | 267.000 | +29.000 / +12.2% | Sistem belirgin büyümüş; Reusability ve Functionality puanlarını mekanik olarak yükseltir, ancak Understandability üzerinde negatif baskı oluşturur. |
| NOH | 35.000 | 39.000 | +4.000 / +11.4% | Hiyerarşi genişlemiş; Functionality açısından pozitif katkı verir. |
| ANA | 0.618 | 0.670 | +0.053 / +8.5% | Soyutlama artmış; Extendibility ve Effectiveness için olumlu. |
| DAM | 0.899 | 0.894 | -0.005 / -0.6% | Kapsülleme neredeyse sabit; çok küçük olumsuz sinyal. |
| DCC | 2.349 | 2.363 | +0.015 / +0.6% | Coupling çok hafif artmış; Reusability, Flexibility, Understandability ve Extendibility üzerinde negatif etki yapar. |
| CAM | 0.407 | 0.387 | -0.020 / -4.8% | Cohesion düşmüş; bakım kolaylığı açısından en belirgin olumsuz metriklerden biridir. |
| MOA | 0.374 | 0.405 | +0.031 / +8.2% | Kompozisyon kullanımı artmış; Flexibility ve Effectiveness açısından olumlu. |
| MFA | 0.247 | 0.272 | +0.025 / +10.2% | Kalıtım/yeniden kullanım potansiyeli artmış; Extendibility ve Effectiveness için olumlu. |
| NOP | 3.273 | 3.191 | -0.082 / -2.5% | Polimorfizm azalmış; Flexibility, Extendibility ve Effectiveness için olumsuz. |
| CIS | 3.920 | 3.914 | -0.006 / -0.2% | Arayüz/mesajlaşma boyutu pratikte sabit; Reusability ve Functionality katkısı değişmemiş sayılır. |
| NOM | 5.156 | 5.240 | +0.084 / +1.6% | Ortalama metot sayısı/karmasıklık hafif artmış; Understandability için olumsuz. |

---

## 3. Kalite açısından değişim olumlu mu, olumsuz mu?

Genel tablo **karışık**tır. Sistem 0.9.2'de büyümüş ve bazı tasarım olgunluğu göstergeleri iyileşmiştir; ancak bakım açısından kritik olan cohesion, coupling ve karmaşıklık sinyalleri hafif bozulmuştur.

### 3.1 Olumlu taraflar

**Sistem kapasitesi ve işlevsel kapsam artmıştır.**  
DSC `238 → 267` ile **+29 sınıf / +12.2%**, NOH `35 → 39` ile **+11.4%** artmıştır. QMOOD Functionality formülünde DSC ve NOH pozitif katsayılarla yer aldığı için Functionality yaklaşık `61.6914 → 68.9296`, yani **+7.2382 / +11.7%** yükselir. Ancak bu artışın büyük bölümü tasarım kalitesinden değil, doğrudan büyümeden gelir: Functionality artışına DSC yaklaşık **+6.38**, NOH yaklaşık **+0.88** puan katkı yapar.

**Soyutlama ve kompozisyon yönünde iyileşme vardır.**  
ANA `0.6176 → 0.6704` ile **+8.5%**, MOA `0.3739 → 0.4045` ile **+8.2%**, MFA `0.2469 → 0.2721` ile **+10.2%** artmıştır. Bu üç metrik, tasarımın daha soyut, daha kompozisyon odaklı ve yeniden kullanım potansiyeli daha yüksek hale geldiğine işaret eder. Özellikle ANA artışı Extendibility'ye yaklaşık **+0.0264**, MFA artışı yaklaşık **+0.0126** katkı verir.

### 3.2 Olumsuz taraflar

**Cohesion düşmüştür.**  
CAM `0.4070 → 0.3874` ile **-4.8%** azalmıştır. Bu, sınıfların/metotların sorumluluk bütünlüğünde zayıflama ihtimalini gösterir. CAM, Reusability ve Understandability tarafında pozitif katsayıyla kullanıldığı için düşüşü kalite açısından olumsuzdur.

**Coupling hafif artmıştır.**  
DCC `2.3487 → 2.3633` ile **+0.6%** artmıştır. Mutlak artış küçük olsa da DCC, QMOOD formüllerinde birçok niteliği cezalandırır: Reusability, Flexibility, Understandability ve Extendibility üzerinde negatif etki yapar. Bu sürüm farkında coupling artışı henüz güçlü bir bozulma kanıtı değildir; fakat büyüme ile birlikte izlenmesi gereken bir risktir.

**Polimorfizm azalmıştır.**  
NOP `3.2731 → 3.1910` ile **-2.5%** düşmüştür. NOP, Flexibility, Extendibility ve Effectiveness üzerinde pozitif katsayıya sahiptir. Bu nedenle polimorfizmin azalması, özellikle genişletilebilirlik ve varyasyon yönetimi açısından zayıflatıcıdır.

**Karmaşıklık hafif artmıştır.**  
NOM `5.1555 → 5.2397` ile **+1.6%** artmıştır. Artış küçük olsa da Understandability formülünde NOM negatif taraftadır. Ortalama metot sayısının artması, sınıfların daha fazla davranış taşıdığına ve okunabilirliğin bir miktar zorlaştığına işaret edebilir.

---

## 4. QMOOD kalite niteliklerine formül bazlı etkiler

Aşağıdaki değerler verilen QMOOD formülleriyle yaklaşık olarak hesaplanmıştır.

| Kalite niteliği | 0.9.0 | 0.9.2 | Değişim | Yorum |
|---|---:|---:|---:|---|
| Reusability | 120.4747 | 134.9630 | +14.4883 / +12.0% | Görünürde iyileşir; fakat artışın neredeyse tamamı DSC'nin +29 artışından gelen **+14.5** katkıdır. CAM, CIS ve DCC değişimleri küçük negatif katkı verir. |
| Flexibility | 1.4611 | 1.4303 | -0.0308 / -2.1% | MOA artışı pozitif katkı verir; ancak NOP düşüşü ve DCC artışı bunu bastırır. |
| Understandability | -81.8693 | -91.4705 | -9.6012 | Daha negatif hale gelir. Ana sebep DSC'nin +29 artışıdır; formülde DSC negatif tarafta olduğu için yaklaşık **-9.57** puan baskı yapar. CAM düşüşü ve NOM artışı da küçük olumsuz katkı verir. |
| Functionality | 61.6914 | 68.9296 | +7.2382 / +11.7% | Artışın ana kaynağı DSC ve NOH'dur. Tasarım davranışı açısından CAM, NOP ve CIS küçük negatif katkı yapar. |
| Extendibility | 0.8945 | 0.8851 | -0.0094 / -1.0% | ANA ve MFA artışı olumlu; ancak NOP düşüşü ve DCC artışı nedeniyle toplam sonuç hafif negatiftir. |
| Effectiveness | 1.0821 | 1.0863 | +0.0042 / +0.4% | Çok sınırlı artış vardır; pratikte durağan kabul edilebilir. ANA, MOA, MFA artışı NOP düşüşünü ancak az farkla dengeler. |

---

## 5. Teknik borç işareti var mı?

**Evet, ancak güçlü değil; erken ve hafif düzeyde teknik borç sinyali vardır.**

Teknik borç açısından en dikkat çekici göstergeler şunlardır:

1. **CAM düşüşü:** `0.4070 → 0.3874` (**-4.8%**)  
   Cohesion azalması, sınıfların daha az odaklı hale gelme riskini gösterir. Bu, ileride değişiklik etkisinin daha geniş alana yayılmasına neden olabilir.

2. **DCC artışı:** `2.3487 → 2.3633` (**+0.6%**)  
   Artış çok küçük olsa da sistem büyürken coupling'in düşmemesi, modülerleşmenin büyümeyi tamamen dengelemediğini gösterir.

3. **NOM artışı:** `5.1555 → 5.2397` (**+1.6%**)  
   Ortalama metot sayısı hafif yükselmiştir. Bu, sınıf sorumluluklarının genişleme eğilimine işaret edebilir.

4. **NOP düşüşü:** `3.2731 → 3.1910` (**-2.5%**)  
   Polimorfizmin azalması, varyasyonların soyut arayüzler yerine daha doğrudan veya daha az esnek yapılarla yönetildiği ihtimalini güçlendirir.

Buna karşılık teknik borç yorumunu sınırlayan olumlu göstergeler de vardır: ANA **+8.5%**, MOA **+8.2%**, MFA **+10.2%** artmıştır. Bu metrikler, sistem büyürken soyutlama, kompozisyon ve kalıtım tabanlı yeniden kullanımın da arttığını gösterir. Dolayısıyla 0.9.0 → 0.9.2 geçişi için "mimari bozulma netleşmiştir" demek abartılı olur; daha doğru ifade, **büyümeye eşlik eden hafif bakım riski oluşmuştur** şeklindedir.

---

## 6. Sonuç

0.9.0 → 0.9.2 geçişinde kalite değerlendirmesi **tamamen olumlu değildir**. Sistem büyümüş, daha fazla sınıf ve hiyerarşi içermiş, soyutlama/kompozisyon/kalıtım göstergeleri iyileşmiştir. Bu nedenle Functionality ve Reusability puanları yükselir.

Ancak bakım ve teknik borç açısından dikkat edilmesi gereken metrikler vardır: CAM **-4.8%** düşmüş, DCC **+0.6%** artmış, NOM **+1.6%** yükselmiş ve NOP **-2.5%** azalmıştır. Bu kombinasyon, özellikle cohesion ve esneklik tarafında hafif bir zayıflama olduğunu gösterir.

Kısa karar:  
**0.9.2, 0.9.0'a göre işlevsel kapsam ve soyutlama açısından daha güçlüdür; ancak bakım kolaylığı ve genişletilebilirlik açısından küçük fakat izlenmesi gereken teknik borç sinyalleri üretmiştir.**
