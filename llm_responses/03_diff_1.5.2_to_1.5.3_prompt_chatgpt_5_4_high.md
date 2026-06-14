# JGraphT 1.5.2 -> 1.5.3 Sürüm Farkı Analizi

## Kısa sonuç

1.5.2'den 1.5.3'e geçiş **genel olarak hafif olumlu**, ancak **stratejik bir kalite sıçraması değil**.  
Verilen metriklerin çoğu çok küçük oranlarda iyileşmiştir: `DAM +%0.5`, `CAM +%0.7`, `MOA +%1.0`, `NOP +%1.1`, `CIS +%0.4`. Buna karşılık **coupling** de az da olsa artmıştır: `DCC 3.023 -> 3.032` (`+%0.3`).  
Bu nedenle tablo, **kontrollü evrim** izlenimi verir; belirgin bir bozulma yoktur, fakat **teknik borcu azalttığını söylemek için de veri zayıftır**.

---

## 1) Tasarım metriklerindeki değişimin yorumu

### Boyut ve yapı büyümesi
- `DSC 601 -> 618` (`+%2.8`)
- `NOH 87 -> 91` (`+%4.6`)

Sistem hem sınıf sayısı hem de hiyerarşi açısından büyümüştür. Bu tek başına olumsuz değildir; fakat büyüme, bakım maliyetini doğal olarak artırır. Özellikle QMOOD'da `DSC`, bazı kalite niteliklerini yukarı çekerken anlaşılabilirliği aşağı çeken çok güçlü bir terimdir.

### Kapsülleme ve iç bütünlük
- `DAM 0.8806 -> 0.8850` (`+%0.5`)
- `CAM 0.3633 -> 0.3660` (`+%0.7`)

Bu iki artış **olumlu** sinyaldir.  
`DAM` artışı veri gizleme/kapsülleme tarafında hafif güçlenme; `CAM` artışı ise sınıf içi uyumda küçük iyileşme anlamına gelir. Ancak büyüklükleri çok küçüktür; bu yüzden bunlar **mikro iyileşme** olarak görülmelidir.

### Bağımlılık ve kompozisyon
- `DCC 3.0233 -> 3.0324` (`+%0.3`)
- `MOA 0.6938 -> 0.7006` (`+%1.0`)

`MOA` artışı kompozisyon kullanımının biraz güçlendiğini gösterir; bu normalde esneklik için olumlu kabul edilir.  
Ancak `DCC` de artmıştır. Coupling artışı küçük olsa da, özellikle büyük bir kod tabanında ters yönde bir sinyaldir; çünkü modüller arası bağımlılıkların hafifçe arttığını gösterir.

### Polimorfizm / arayüz kullanımı / yöntem karmaşıklığı
- `NOP 3.5075 -> 3.5453` (`+%1.1`)
- `CIS 4.2080 -> 4.2249` (`+%0.4`)
- `NOM 6.2928 -> 6.3236` (`+%0.5`)

`NOP` ve `CIS` artışı, esneklik ve işlevsellik açısından olumlu okunabilir.  
Buna karşılık `NOM` da artmıştır. Artış küçük olsa da, ortalama metodik karmaşıklığın/operasyonel yüzeyin biraz daha genişlediğini düşündürür. Bu yüzden kazanım vardır ama “ücretsiz” değildir.

---

## 2) QMOOD kalite etkisi: olumlu mu, olumsuz mu?

Aşağıdaki kalite değerleri, verilen QMOOD denklemleriyle doğrudan hesaplanmıştır.

| Kalite niteliği | 1.5.2 | 1.5.3 | Değişim |
|---|---:|---:|---:|
| Reusability | 301.9390 | 310.4459 | +8.5069 |
| Flexibility | 1.5650 | 1.5861 | +0.0211 |
| Understandability | -202.2567 | -207.8903 | -5.6336 |
| Functionality | 153.1010 | 157.7334 | +4.6324 |
| Extendibility | 0.4774 | 0.4923 | +0.0149 |
| Effectiveness | 1.1105 | 1.1205 | +0.0100 |

### Olumlu taraf
- **Reusability artıyor**: `301.9390 -> 310.4459`
- **Functionality artıyor**: `153.1010 -> 157.7334`
- **Flexibility artıyor**: `1.5650 -> 1.5861`
- **Extendibility artıyor**: `0.4774 -> 0.4923`
- **Effectiveness artıyor**: `1.1105 -> 1.1205`

Bu nedenle **genel kalite etkisi hafif olumlu** denebilir.

### Olumsuz taraf
- **Understandability daha da kötüleşiyor**: `-202.2567 -> -207.8903`

Bu bozulmanın ana nedeni doğrudan büyümedir.  
QMOOD formülünde:
- negatif blok: `-0.33*(ANA + DCC + NOP + NOM + DSC)`
- pozitif blok: `+0.33*(DAM + CAM)`

1.5.2 -> 1.5.3 geçişinde:
- negatif bloğun katkısı **-5.6359** kadar kötüleşiyor
- pozitif bloğun telafisi yalnızca **+0.0023**

Yani anlaşılabilirlikteki bozulma neredeyse tamamen `DSC`, `DCC`, `NOP` ve `NOM` artışlarının birleşik etkisinden geliyor; `DAM` ve `CAM` artışı bunu pratikte telafi edemiyor.

---

## 3) Hangi metrik kaliteyi neden etkiledi?

### Reusability neden arttı?
Formül:
`Reusability = -0.25*DCC + 0.25*CAM + 0.50*CIS + 0.50*DSC`

1.5.2 -> 1.5.3 katkı farkı:
- `-0.25*DCC = -0.0023`
- `+0.25*CAM = +0.0007`
- `+0.50*CIS = +0.0084`
- `+0.50*DSC = +8.5000`

Bu niteliği **esas olarak `DSC` artışı** yükseltmiştir.  
Dolayısıyla burada görülen iyileşme, yeniden kullanılabilirliğin “tasarımsal olarak daha temiz olduğu” anlamına gelmeyebilir; **ölçek artışının formüle mekanik etkisi** baskındır.

### Functionality neden arttı?
Formül:
`Functionality = 0.12*CAM + 0.22*(NOP + CIS + DSC + NOH)`

Katkı farkı:
- `+0.12*CAM = +0.0003`
- `+0.22*(NOP + CIS + DSC + NOH) = +4.6320`

Burada da artışın temel sürücüleri:
- `DSC +17`
- `NOH +4`
- `NOP +0.0378`
- `CIS +0.0169`

Yani sistem daha fazla yapı/hiyerarşi/arayüz kapasitesi taşıdığı için işlevsellik puanı yükselmiştir.

### Flexibility ve Extendibility neden az da olsa arttı?
- `DAM`, `MOA` ve `NOP` artışı olumlu etki yaptı.
- Fakat `DCC` de arttığı için kazancın bir kısmı geri alındı.

Örnek:
`Flexibility` için toplam artış `+0.0211`; bunun içinde:
- `+0.25*DAM = +0.0011`
- `+0.50*MOA = +0.0034`
- `+0.50*NOP = +0.0189`
- `-0.25*DCC = -0.0023`

Bu, esneklik artışının var olduğunu ama **dar marjlı** olduğunu gösterir.

---

## 4) Teknik borç işareti var mı?

## Kısa hüküm
**Güçlü bir yeni teknik borç sıçraması görünmüyor; ancak teknik borcun azaldığını da söylemek zor.**  
En doğru ifade: **“stabil ama borç nötr / hafif borç biriktiren”** bir geçiş.

### Teknik borç lehine olmayan sinyaller
1. **Coupling artıyor**
   - `DCC 3.0233 -> 3.0324` (`+%0.3`)
   - Küçük de olsa, büyük sistemlerde coupling genelde azaltılmak istenir.

2. **Yöntemsel yüzey büyüyor**
   - `NOM 6.2928 -> 6.3236` (`+%0.5`)
   - Daha fazla operasyon yüzeyi, bakım ve test maliyetini artırabilir.

3. **Anlaşılabilirlik kötüleşiyor**
   - `Understandability -202.2567 -> -207.8903`
   - Özellikle `DSC` artışı burada belirleyici.

### Teknik borç lehine olumlu sinyaller
1. **Cohesion düşmüyor, aksine hafif artıyor**
   - `CAM 0.3633 -> 0.3660`
2. **Encapsulation hafif artıyor**
   - `DAM 0.8806 -> 0.8850`
3. **Composition kullanımı artıyor**
   - `MOA 0.6938 -> 0.7006`

Bu üçü, değişikliğin “dağınık genişleme” değil, görece kontrollü evrim olduğunu düşündürür.

### Sonuç
Teknik borç için **erken ama zayıf** sinyal vardır:
- coupling artışı,
- anlaşılabilirlik kaybı,
- sınıf/yapı yüzeyindeki büyüme.

Ancak bu sinyallerin şiddeti düşüktür; çünkü aynı anda cohesion ve encapsulation da kötüleşmemiştir. Bu yüzden bu geçişi **“alarm seviyesi yüksek borç birikimi”** olarak değil, **“izlenmesi gereken yavaş yapısal yük artışı”** olarak değerlendirmek daha doğru olur.

---

## 5) Nihai değerlendirme

1.5.2 -> 1.5.3 geçişi **kalite açısından ağırlıklı olarak olumlu**, fakat **iyileşmenin ana kaynağı büyük ölçüde büyüme (`DSC`, `NOH`) ve kapasite artışıdır**.  
Daha temiz, daha az bağlı, daha anlaşılır bir mimariye gidildiğini söylemek için kanıt sınırlıdır; çünkü:
- `DCC` düşmemiş, artmıştır,
- `NOM` artmıştır,
- `Understandability` daha da kötüleşmiştir.

Bu nedenle en dengeli sonuç şudur:

> **Sürüm 1.5.3, 1.5.2'ye göre biraz daha yetenekli ve esnek görünmektedir; ancak bu kazanım bakım/anlaşılabilirlik maliyeti tamamen çözülmeden elde edilmiştir. Teknik borçta sert bir sıçrama yoktur, fakat mimari yük hafifçe artmaktadır.**

---

## Belirsizlik notu

Bu değerlendirme yalnızca verilen **sistem düzeyi ortalama metriklere** dayalıdır.  
Dolayısıyla:
- hangi paketlerin/sınıfların kötüleştiği,
- artışın birkaç hotspot sınıfta mı yoksa tüm sisteme mi yayıldığı,
- coupling artışının mimari katmanlar arasında mı yoksa aynı alt modül içinde mi oluştuğu

bu veriyle görülemez. Bu yüzden teknik borç yorumu **erken sinyal** düzeyindedir; kesin teşhis değildir.