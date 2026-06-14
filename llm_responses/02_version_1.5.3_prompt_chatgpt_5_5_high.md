# JGraphT 1.5.3 QMOOD Derin Kalite Değerlendirmesi

## 1. Kapsam ve Veri Seti

Bu rapor, **JGraphT jgrapht-core 1.5.3** sürümüne ait QMOOD tasarım metrikleri, CK metrik ortalamaları ve QMOOD kalite nitelikleri üzerinden hazırlanmıştır. Değerlendirme yalnızca verilen sayısal verilere dayanır; sınıf bazlı kaynak kod analizi yapılmadığı için sınıf/komponent isimleri üzerinde kesin yargı verilmemiştir.

### Kullanılan temel değerler

| Metrik | Değer |
|---|---:|
| DSC / num_classes | 618 |
| NOH | 91 |
| ANA | 0.3204 |
| DAM | 0.8850 |
| DCC / CBO_mean | 3.0324 |
| CAM | 0.3660 |
| MOA / DAC_mean | 0.7006 |
| MFA | 0.1512 |
| NOP | 3.5453 |
| CIS | 4.2249 |
| NOM / NOM_mean | 6.3236 |
| WMC_mean | 15.7848 |
| RFC_mean | 17.2508 |
| LCOM_mean | 31.2379 |
| MPC_mean | 16.8511 |

### Maksimum CK değerleri

| CK maksimum metriği | Değer | Yorum |
|---|---:|---|
| WMC_max | 381 | Bazı sınıflarda çok yüksek metot/karmaşıklık yoğunlaşması var. |
| CBO_max | 21 | Bazı sınıflar geniş bağımlılık ağına sahip. |
| RFC_max | 149 | Bazı sınıfların tepki kümesi çok geniş. |
| LCOM_max | 4371 | Bazı sınıflarda çok güçlü cohesion problemi / God Class riski var. |
| NOM_max | 95 | Bazı sınıflar aşırı büyük arayüz veya sorumluluk taşıyor. |
| MPC_max | 401 | Bazı sınıflarda yoğun mesajlaşma/çağrı bağımlılığı var. |

---

## 2. Genel Kalite Değerlendirmesi

JGraphT 1.5.3 için kalite resmi iki yönlüdür: **işlevsellik ve yeniden kullanılabilirlik sayısal olarak yüksek görünür**, ancak bu yüksekliğin önemli bölümü sistem boyutundan, yani **DSC=618** değerinden gelir. Buna karşılık **Understandability=-207.8903** ve **Extendibility=0.4923** değerleri bakım ve evrim açısından en zayıf sinyallerdir.

| Kalite niteliği | Değer | Kısa değerlendirme |
|---|---:|---|
| Reusability | 310.4459 | Çok yüksek; ancak formülde 0.50\*DSC nedeniyle büyük ölçüde sistem boyutundan besleniyor. |
| Flexibility | 1.5861 | Orta/pozitif; NOP=3.5453 ve MOA=0.7006 destekliyor, DCC=3.0324 düşürüyor. |
| Understandability | -207.8903 | En zayıf nitelik; DSC=618 ve NOM=6.3236 formülde negatif etki yaratıyor. |
| Functionality | 157.7334 | Yüksek; yine DSC=618 ve NOH=91 ana katkı sağlıyor. |
| Extendibility | 0.4923 | Çok düşük; DCC=3.0324 cezası, düşük ANA=0.3204 ve MFA=0.1512 ile birleşiyor. |
| Effectiveness | 1.1205 | Sınırlı pozitif; NOP=3.5453 ana katkı, ANA/MFA düşük kaldığı için güçlü değil. |

**Eleştirel yorum:** Reusability ve Functionality değerleri yüksek olsa da bu doğrudan “mimari kalite çok iyi” anlamına gelmez. Çünkü Reusability’de **DSC katkısı 309.0000**, toplam değer ise **310.4459**’dur. Benzer şekilde Functionality’de **DSC katkısı 135.9600**, NOH katkısı **20.0200**’dir. Bu nedenle bu iki kalite niteliği, tasarımın olgunlaşmasından çok kütüphanenin büyüklüğü ve kapsam genişliği tarafından yukarı taşınmaktadır.

---

## 3. En Zayıf 2 Kalite Niteliği

## 3.1 Understandability — En zayıf kalite niteliği

**Understandability = -207.8903** değeri, tüm kalite nitelikleri içinde açık ara en problemli değerdir. QMOOD formülünde Understandability şu şekilde hesaplanır:

```text
Understandability = -0.33*(ANA + DCC + NOP + NOM + DSC) + 0.33*(DAM + CAM)
```

1.5.3 değerleri yerine konulduğunda:

```text
Negatif taraf = -0.33*(0.3204 + 3.0324 + 3.5453 + 6.3236 + 618)
              = -208.3032

Pozitif taraf =  0.33*(0.8850 + 0.3660)
              =   0.4128

Sonuç         = -207.8903
```

### Sorumlu metrikler

| Sorumlu metrik | Değer | Understandability etkisi |
|---|---:|---:|
| DSC | 618 | -203.9400 |
| NOM | 6.3236 | -2.0868 |
| NOP | 3.5453 | -1.1699 |
| DCC | 3.0324 | -1.0007 |
| ANA | 0.3204 | -0.1057 |
| DAM | 0.8850 | +0.2921 |
| CAM | 0.3660 | +0.1208 |

**Kanıt temelli yorum:** Understandability’nin bozulmasının ana nedeni açık biçimde **DSC=618** değeridir; tek başına **-203.9400** katkı üretmektedir. Ancak sorun yalnızca sınıf sayısı değildir. **NOM_mean=6.3236**, **DCC=3.0324**, **NOP=3.5453** ve CK tarafında **WMC_mean=15.7848**, **RFC_mean=17.2508**, **LCOM_mean=31.2379** değerleri, sistemin bazı bölgelerinde karmaşıklık ve sorumluluk yoğunlaşması olduğunu destekler. Özellikle **LCOM_max=4371** ve **WMC_max=381**, ortalama değerlerin arkasında çok sorunlu sınıfların bulunabileceğini gösterir.

### Sonuç

Bu sürümde bakım ve anlama maliyeti düşmemiş, aksine yüksek boyut, karmaşıklık ve düşük cohesion riski nedeniyle artmıştır. DAM=0.8850 gibi güçlü kapsülleme değeri olumlu olsa da Understandability formülünde pozitif katkısı yalnızca **+0.2921**’dir; bu katkı DSC kaynaklı **-203.9400** cezayı dengeleyememektedir.

---

## 3.2 Extendibility — İkinci en zayıf kalite niteliği

**Extendibility = 0.4923** değeri pozitif olmakla birlikte oldukça düşüktür. Bu sonuç, sistemin genişletilebilirliğinin coupling ve düşük soyutlama/kalıtım desteği nedeniyle sınırlı olduğunu gösterir.

QMOOD formülü:

```text
Extendibility = 0.50*(ANA + MFA + NOP) - 0.50*DCC
```

1.5.3 değerleriyle:

```text
Pozitif taraf = 0.50*(0.3204 + 0.1512 + 3.5453)
              = 2.0085

Negatif taraf = -0.50*3.0324
              = -1.5162

Sonuç         = 0.4923
```

### Sorumlu metrikler

| Sorumlu metrik | Değer | Extendibility etkisi |
|---|---:|---:|
| NOP | 3.5453 | +1.7727 |
| ANA | 0.3204 | +0.1602 |
| MFA | 0.1512 | +0.0756 |
| DCC | 3.0324 | -1.5162 |

**Kanıt temelli yorum:** Extendibility değerini ayakta tutan ana unsur **NOP=3.5453** değeridir; formüle **+1.7727** katkı yapar. Ancak **DCC=3.0324**, **-1.5162** ceza üretir. Daha kritik olan, soyutlama ve kalıtım katkılarının çok zayıf kalmasıdır: **ANA=0.3204** yalnızca **+0.1602**, **MFA=0.1512** yalnızca **+0.0756** katkı üretmektedir. Bu, genişletilebilirliğin güçlü soyut mimari katmanlardan ziyade polimorfik yapıların sınırlı katkısıyla taşındığını düşündürür.

### CK metrikleriyle destek

| CK metriği | Değer | Genişletilebilirlik yorumu |
|---|---:|---|
| CBO_mean | 3.0324 | Ortalama bağımlılık seviyesi genişletme maliyetini artırıyor. |
| CBO_max | 21 | Bazı sınıflar çok sayıda dış sınıfa bağlı olabilir. |
| RFC_mean | 17.2508 | Sınıfların tepki kümesi geniş; değişiklik etkisi büyüyebilir. |
| RFC_max | 149 | Bazı sınıflarda değişiklik yayılım riski çok yüksek. |
| MPC_mean | 16.8511 | Ortalama mesajlaşma/çağrı yoğunluğu yüksek. |
| MPC_max | 401 | Belirli sınıflar mimari merkez/bağımlılık düğümü olabilir. |

### Sonuç

Extendibility düşük görünmektedir çünkü sistemde genişletmeyi kolaylaştıracak soyutlama ve kalıtım katkısı sınırlı, buna karşılık coupling cezası yüksektir. Bu nedenle yeni algoritma, graph tipi veya yardımcı bileşen eklemek bazı bölgelerde beklenenden fazla değişiklik gerektirebilir.

---

## 4. Diğer Kalite Nitelikleri Üzerine Kısa Yorum

## 4.1 Reusability

**Reusability=310.4459** yüksek görünmektedir; ancak bu değerin neredeyse tamamı **DSC=618** tarafından üretilir:

| Katkı | Değer |
|---|---:|
| 0.50\*DSC | +309.0000 |
| 0.50\*CIS | +2.1125 |
| 0.25\*CAM | +0.0915 |
| -0.25\*DCC | -0.7581 |
| Toplam | 310.4459 |

Bu nedenle Reusability’nin yüksekliği, “küçük ve temiz bileşenlerin tekrar kullanılabilirliği” şeklinde abartılmamalıdır. Daha doğru yorum: JGraphT 1.5.3 geniş API/kapsam sunduğu için yeniden kullanılabilir yüzey alanı büyüktür; fakat **CAM=0.3660** ve **DCC=3.0324** bu kazanımı kalite açısından sınırlar.

## 4.2 Functionality

**Functionality=157.7334** da yüksek görünür; ancak burada da ana katkı boyut ve hiyerarşiden gelir:

| Katkı | Değer |
|---|---:|
| 0.22\*DSC | +135.9600 |
| 0.22\*NOH | +20.0200 |
| 0.22\*CIS | +0.9295 |
| 0.22\*NOP | +0.7800 |
| 0.12\*CAM | +0.0439 |
| Toplam | 157.7334 |

Bu sürüm işlevsel olarak zengin görünmektedir; fakat Functionality’nin büyük bölümü **618 sınıf** ve **91 hiyerarşi** değerlerinden gelmektedir. Bu, API kapsamının arttığını gösterir; bakım kolaylığını tek başına kanıtlamaz.

## 4.3 Flexibility

**Flexibility=1.5861** pozitif ama sınırlıdır. **NOP=3.5453** ve **MOA=0.7006** olumlu katkı verirken, **DCC=3.0324** değeri **-0.7581** ceza üretmektedir.

| Katkı | Değer |
|---|---:|
| 0.50\*NOP | +1.7727 |
| 0.50\*MOA | +0.3503 |
| 0.25\*DAM | +0.2213 |
| -0.25\*DCC | -0.7581 |
| Toplam | 1.5861 |

---

## 5. Teknik Borç Göstergeleri

1.5.3 sürümünde teknik borç işareti veren metrikler şunlardır:

1. **Yüksek boyut:** DSC=618. Sistem büyük olduğu için Understandability formülünde tek başına **-203.9400** negatif katkı üretmektedir.
2. **Artan/önemli coupling:** DCC/CBO_mean=3.0324. Extendibility’de **-1.5162**, Flexibility’de **-0.7581**, Understandability’de **-1.0007** negatif katkı üretir.
3. **Düşük cohesion:** CAM=0.3660 ve CK tarafında LCOM_mean=31.2379. Ayrıca **LCOM_max=4371**, bazı sınıflarda ciddi cohesion kırılması olabileceğini gösterir.
4. **Sınıf içi karmaşıklık yoğunlaşması:** WMC_mean=15.7848 iken **WMC_max=381**. Ortalama makul görünse bile bazı sınıflar bakım açısından çok riskli olabilir.
5. **Aşırı çağrı/mesajlaşma yoğunluğu:** MPC_mean=16.8511, **MPC_max=401**. Bu değerler değişiklik yayılımı ve test maliyeti açısından teknik borç göstergesidir.
6. **Geniş tepki kümesi:** RFC_mean=17.2508, **RFC_max=149**. Bazı sınıfların davranışsal yüzeyi çok geniştir.

---

## 6. Somut Refactoring Önerileri

## Öneri 1 — God Class / Large Class ayrıştırması

**Hedef metrikler:** WMC_max=381, NOM_max=95, LCOM_max=4371, RFC_max=149

Bazı sınıflarda aşırı metot, karmaşıklık ve cohesion problemi birikmiş görünmektedir. Bu sınıflar için:

- `Extract Class`
- `Extract Method`
- `Move Method`
- `Introduce Facade` veya `Service Split`

uygulanmalıdır.

**Beklenen metrik etkisi:** WMC_max, NOM_max, LCOM_max ve RFC_max düşer. Bu da Understandability üzerinde doğrudan olmasa da CK tabanlı bakım riskini azaltır; ayrıca QMOOD tarafında NOM ve dolaylı olarak CAM/DCC üzerinde iyileşme sağlayabilir.

---

## Öneri 2 — Coupling azaltma ve bağımlılık yönünü kontrol etme

**Hedef metrikler:** DCC=3.0324, CBO_max=21, MPC_mean=16.8511, MPC_max=401

DCC, Extendibility üzerinde **-1.5162** ceza üretmektedir. Bu nedenle yoğun bağımlı sınıflarda:

- `Dependency Inversion`
- `Interface Segregation`
- `Adapter` veya `Strategy` ile değişen algoritmaları soyutlama
- Utility/helper sınıflarına aşırı merkezi bağımlılık varsa sorumlulukları modüllere dağıtma

uygulanmalıdır.

**Beklenen metrik etkisi:** DCC/CBO ve MPC düşer. Extendibility ve Flexibility doğrudan iyileşir; çünkü her iki formülde de DCC negatif katsayıyla yer almaktadır.

---

## Öneri 3 — Cohesion artırma ve API yüzeyini sadeleştirme

**Hedef metrikler:** CAM=0.3660, LCOM_mean=31.2379, NOM_mean=6.3236, NOM_max=95

CAM düşük, LCOM yüksek olduğu için bazı sınıfların birden fazla sorumluluğu aynı anda taşıdığı düşünülmelidir. Bu sınıflarda:

- aynı veri kümesiyle çalışan metotları bir arada tutma,
- ilgisiz metot gruplarını ayrı sınıflara taşıma,
- geniş public API’leri daha küçük, amaca yönelik arayüzlere bölme,
- algoritma seçeneklerini `Strategy` veya küçük kompozisyon nesneleriyle ayırma

önerilir.

**Beklenen metrik etkisi:** CAM artar, LCOM ve NOM düşer. Understandability’de pozitif CAM katkısı artar; ayrıca NOM azalırsa Understandability üzerindeki negatif yük hafifler.

---

## 7. Sonuç

JGraphT 1.5.3 işlevsel kapsam bakımından güçlüdür: **DSC=618**, **NOH=91**, **Functionality=157.7334** ve **Reusability=310.4459** bunu göstermektedir. Ancak bu değerler önemli ölçüde sistem büyüklüğünden kaynaklandığı için mimari kaliteyi tek başına kanıtlamaz.

En zayıf iki kalite niteliği:

1. **Understandability = -207.8903**  
   Ana nedenler: **DSC=618**, **NOM=6.3236**, **DCC=3.0324**, **LCOM_mean=31.2379**, **WMC_max=381**, **LCOM_max=4371**.

2. **Extendibility = 0.4923**  
   Ana nedenler: **DCC=3.0324** kaynaklı **-1.5162** ceza, düşük **ANA=0.3204** ve düşük **MFA=0.1512** katkısı.

Genel değerlendirme: JGraphT 1.5.3 geniş kapsamlı ve fonksiyonel olarak zengin bir sürümdür; ancak bakım ve genişletilebilirlik açısından teknik borç riski taşır. Özellikle yüksek maksimum CK değerleri, problemin sistem geneline eşit dağılmadığını; belirli büyük, yoğun bağımlı ve düşük cohesion’lı sınıflarda biriktiğini göstermektedir. Bu nedenle refactoring önceliği tüm sistemi küçültmek değil, **WMC_max, LCOM_max, RFC_max, MPC_max ve CBO_max değerlerini üreten odak sınıfları** hedeflemek olmalıdır.
