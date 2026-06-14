# JGraphT (`jgrapht-core`) 1.5.3 — Tek Sürüm QMOOD Derin İncelemesi

**Kapsam:** Tek sürüm anlık görüntü (1.5.3, 618 sınıf). QMOOD + CK metrikleri (ortalama **ve maksimum** değerlerle).
**Model:** QMOOD (Bansiya & Davis, 2002).

---

## ⚠️ Yöntem Notu (önce okunmalı)

Tek sürümlük veride **mutlak QMOOD değerleri tek başına "iyi/kötü" eşiğine oturtulamaz** — QMOOD karşılaştırmalı bir modeldir, referans (baseline) yoktur. Yorumlar iki sağlam dayanağa oturtulmuştur:

1. **Denklem ayrıştırması:** Her niteliğin değerine *hangi metriğin ne kadar katkı verdiği* hesaplandı (her denklem girdilerden birebir yeniden üretildi; ör. Understandability = −0.33·(0.3204+3.0324+3.5453+6.3236+618)+0.33·(0.885+0.366) = **−207,89** ✓; Extendibility = 0.50·(0.3204+0.1512+3.5453)−0.50·3.0324 = **0,4923** ✓).
2. **Ortalama–maksimum dağılımı:** Ortalamalar dengeli görünürken maksimumlar dağılımın kuyruğunu (god-class riskini) açığa çıkarır; asıl kanıt buradadır.

---

## 0. Bağlam: 1.5.x serisi boyunca god sınıf hiç onarılmadı

1.5.3, 1.5.1 ve 1.5.2 ile aynı bakım hattındadır. Kod tabanı ~%3 büyümüştür (600 → 618 sınıf), ancak **baskın aykırı (god) sınıf üç sürüm boyunca birebir aynıdır**:

| Metrik | 1.5.1 | 1.5.2 | 1.5.3 |
|---|---|---|---|
| DSC (sınıf) | 600 | 601 | 618 |
| NOH | 87 | 87 | 91 |
| WMC_max | 381 | 381 | **381** |
| LCOM_max | 4371 | 4371 | **4371** |
| NOM_max | 95 | 95 | **95** |
| CBO_max | 21 | 21 | **21** |
| NOC_max | 28 | 28 | **28** |
| LCOM_mean | 30,21 | 30,22 | **31,24** |
| Understandability | −201,94 | −202,26 | **−207,89** |
| Extendibility | 0,487 | 0,4774 | 0,4923 |

**Okuma:** (1) God sınıf tüm seri boyunca dokunulmamış → birikmiş, çözülmemiş teknik borç. (2) Ortalama LCOM hafif **yükselmiş** (30,21 → 31,24) → eklenen ~18 sınıf kohezyonu biraz daha aşağı çekmiş. (3) Understandability'nin daha negatife (−207,89) kayması **tamamen DSC büyümesinden** kaynaklanır (yapısal bir kötüleşme değil; bkz. Bölüm 2). Değerlendirme özünde 1.5.1/1.5.2 ile aynıdır; abartmamak adına yapay farklılaştırma yapılmamıştır.

---

## 1. Genel Kalite Değerlendirmesi

### 1.1 Asıl bulgu: Ortalamalar ılımlı, maksimumlar felaket (aşırı dağılım)

Ortalama CK metrikleri kabul edilebilir görünür (WMC ~16, CBO ~3, LCOM ~31). Ancak maksimumlar, 618 küçük sınıfın seyrelttiği **en az bir "god class"** olduğunu gösteriyor:

| CK metrik | Ortalama | **Maksimum** | Maks/Ort | Yorum |
|---|---|---|---|---|
| **LCOM** (kohezyon eksikliği) | 31,24 | **4371** | **~140×** | Tek sınıfta felaket düzeyde kohezyonsuzluk |
| **WMC** (karmaşıklık) | 15,78 | **381** | ~24× | Tek sınıfta aşırı karmaşıklık |
| **MPC** (dışa mesaj geçişi) | 16,85 | **401** | ~24× | Tek sınıfta aşırı dışa bağımlılık |
| **NOM** (metot sayısı) | 6,32 | **95** | ~15× | 95 metotlu dev sınıf |
| **RFC** (yanıt kümesi) | 17,25 | **149** | ~9× | Çok geniş yanıt kümesi → test güçlüğü |
| **NOA** (öznitelik sayısı) | 3,02 | 24 | ~8× | Veri-yoğun sınıf |
| **CBO** (coupling) | 3,03 | 21 | ~7× | Yüksek-coupling aykırı değeri |
| **NOC** (alt sınıf sayısı) | 0,57 | 28 | ~49× | 28 alt sınıflı temel tip (uzantı noktası) |
| **DIT** (kalıtım derinliği) | 0,32 | 3 | — | Sığ hiyerarşi (olumlu) |

**Aykırı değerler büyük olasılıkla aynı sınıfa ait** — kombinatorik kanıt: 95 metotlu bir sınıf için olası en yüksek LCOM = C(95,2) = **4465**; gözlenen LCOM_max = **4371**. Yani 4465 metot çiftinin yalnızca ~47'si ortak alan paylaşıyor (**%98,9'u kohezyonsuz**). WMC_max=381 ≈ 95 metot × ~4 karmaşıklık, MPC_max=401 ≈ 95 metot × ~4,2 çağrı ile tutarlı. Bu profil tek bir **dev yardımcı/god sınıfa** (muhtemelen statik yardımcı metot yığını) işaret eder. *(Kesin değil; marjinal maksimumlar tek başına aynı sınıfı kanıtlamaz, ancak aritmetik uyum çok güçlü.)*

### 1.2 Genuine güçlü yönler
- **Güçlü kapsülleme:** DAM = 0,885 (serinin en yükseği) → özniteliklerin ~%88,5'i private/protected. Flexibility ve Effectiveness'e olumlu katkı veren gerçek bir artı.
- **Sığ, sade hiyerarşi:** DIT_max = 3, ortalama 0,32 → anlaşılabilirliği destekler; aşırı kalıtım yok.
- **Kompozisyon ağırlıklı stil:** MOA = 0,7006 (serinin en yükseği), MFA = 0,1512 düşük → "kalıtım yerine kompozisyon" tercihi; Flexibility'yi (1,5861, serinin en yükseği) yukarı çeker.

### 1.3 Genuine zayıf yönler
- **Kronik düşük kohezyon (hafif kötüleşen):** CAM = 0,366 (düşük) + LCOM ortalaması 31,24 (serinin en yükseği) / maks 4371.
- **Soyutlama kıtlığı:** ANA = 0,3204 ve MFA = 0,1512 çok düşük → genişletme iskelesi zayıf.
- **Tek noktada yoğunlaşan coupling:** ortalama CBO ılımlı (3,03) ama MPC_max=401 / CBO_max=21.

> **Not — yüksek Reusability ve Functionality kalite kanıtı DEĞİLDİR.** Reusability=310,45'in ≈%99,5'i tek başına `0.50·DSC` (=309), Functionality=157,73'ün ≈%98,9'u `0.22·(DSC+NOH)` (=155,98) terimidir. Bu iki değer pratikte "sistem 618 sınıf" demektir; sınıf-içi kaliteyi ölçmez. Bu yüzden bu rapor raw değerlerden "en güçlü nitelik" seçmez.

---

## 2. En Zayıf 2 Kalite Niteliği ve Sorumlu Metrikler

**Sıralama yöntemi:** Nitelikler farklı ölçeklerde olduğundan kör büyüklük sıralaması yapılmadı. (a) İşaret olarak **negatif** olan tek nitelik en zayıf kabul edildi; (b) aynı ölçekteki (sınıf-başına, O(1)) üç nitelik — Flexibility 1,5861 · Effectiveness 1,1205 · **Extendibility 0,4923** — adil biçimde karşılaştırıldı; en düşük olan ikinci en zayıf seçildi.

### 🥇 En zayıf #1 — Understandability (= −207,89, tek negatif nitelik)

| Terim | Değer | Katkı |
|---|---|---|
| −0.33·**DSC** | 618 | **−203,94** |
| −0.33·NOM | 6,3236 | −2,09 |
| −0.33·NOP | 3,5453 | −1,17 |
| −0.33·DCC | 3,0324 | −1,00 |
| −0.33·ANA | 0,3204 | −0,11 |
| +0.33·DAM | 0,885 | +0,29 |
| +0.33·CAM | 0,366 | +0,12 |
| **Toplam** | | **−207,89** |

**Sorumlu metrikler:** Ezici biçimde **DSC=618** (toplam etkinin **%98'i**). Bu büyük ölçüde bir **boyut artefaktıdır** — denklem boyuta göre normalize değil; nitekim 1.5.2→1.5.3 düşüşünün (−202,26→−207,89) tamamı +17 sınıfın `−0.33·ΔDSC` katkısıdır. Eyleme dönük gerçek sınıf-içi katkılar küçüktür: **NOM (−2,09)** ve **DCC (−1,00)**; ayrıca **CAM düşük olduğundan** (+0,12) pozitif tampon neredeyse yok. *Abartmamak adına:* ham Understandability "çöküşü" esasen "kod büyük" demektir; gerçek anlaşılabilirlik sorunu üniform değil, **Bölüm 1.1'deki god-class'ta yoğunlaşmıştır** (WMC_max=381, LCOM_max=4371, RFC_max=149).

### 🥈 En zayıf #2 — Extendibility (= 0,4923; aynı ölçekteki en düşük nitelik)

| Terim | Değer | Katkı |
|---|---|---|
| +0.50·**NOP** | 3,5453 | +1,773 |
| +0.50·ANA | 0,3204 | +0,160 |
| +0.50·MFA | 0,1512 | +0,076 |
| −0.50·**DCC** | 3,0324 | **−1,516** |
| **Toplam** | | **0,4923** |

**Sorumlu metrikler:** İki yönlü zayıflık — (1) **DCC=3,0324 yüksek**, pozitif bütçenin (2,008) ~%75'ini (−1,516) yiyor; (2) **ANA=0,3204 ve MFA=0,1512 çok düşük**, ikisi birlikte yalnızca +0,236 katkı veriyor. Yani tasarım yalnızca **polimorfizm (NOP, +1,773)** sayesinde genişletilebiliyor; **soyutlama ve kalıtım-tabanlı yeniden kullanım iskelesi neredeyse yok** ve **coupling** kalanı tüketiyor. *(Not: Extendibility 1.5.2'ye göre 0,4774→0,4923 hafif yükseldi; nedeni NOP'un 3,5075→3,5453 artması, DCC'nin ise sabit kalmasıdır — yapısal bir iyileşme değil, küçük bir dalgalanma.)*

### Ortak suçlu: DCC (coupling)
**DCC, iki en zayıf niteliğin İKİSİNİ birden** aşağı çekiyor (Understandability'de negatif kovada, Extendibility'de doğrudan −0,50 katsayıyla). Coupling düşürmek tek hamlede iki niteliği iyileştirir → aşağıdaki #2 önerisinin gerekçesi.

---

## 3. Üç Somut Refactoring Önerisi (metrik-hedefli)

**1) Dev sınıfı (god class) ayrıştır — `NOM_max=95, WMC_max=381, LCOM_max=4371, MPC_max=401, RFC_max=149`.**
Bu tek sınıf, beş metriğin felaket kuyruğundan aynı anda sorumlu ve **tüm 1.5.x serisi boyunca (1.5.1→1.5.2→1.5.3) hiç onarılmamış** (bkz. Bölüm 0) — serinin standing en yüksek öncelikli borcudur. LCOM'u olası maksimuma çok yakın (≈%99 kohezyonsuz) olduğundan, *Extract Class* ile sorumluluk bazında bölün; statik yardımcı yığınıysa konu başlıklarına göre ayrı yardımcı sınıflara dağıtın.
→ *Beklenen etki:* LCOM_max, WMC_max, MPC_max, RFC_max büyük ölçüde düşer; **aykırı değer ortalamaları da şişirdiği için** LCOM_mean (31,24) ve WMC_mean (15,78) birlikte iyileşir; Understandability'nin gerçek sınıf-içi bileşeni rahatlar.

**2) Coupling'i düşür — `DCC=3,0324` (iki zayıf niteliğin ortak suçlusu); `MPC_max=401, CBO_max=21`.**
Yüksek-MPC sınıfı ile işbirlikçileri arasına **arayüz / Facade / Mediator** koyun; "feature envy" çağrı zincirlerini sadeleştirin. Hedef: aykırı sınıfın CBO'sunu 21'den ortalamaya (≈3) çekmek ve sistem DCC'sini azaltmak.
→ *Beklenen etki:* DCC düşünce **hem Extendibility yükselir** (−0.50·DCC terimi küçülür) **hem de Understandability'nin per-class kısmı iyileşir**.

**3) Hedefli soyutlama ekle — `ANA=0,3204`, `MFA=0,1512` (ikisi de çok düşük).**
Extendibility soyutlamadan aç. Kompozisyon-ağırlıklı tasarımın tekrar eden/sabit-kodlanmış davranış bıraktığı yerlerde, **derin kalıtım dayatmadan** paylaşılan arayüz/abstract tipleri kilit uzantı noktalarında çıkarın. Kod tabanı bunu zaten yapabiliyor (NOC_max=28'lik bir temel tip mevcut uzantı noktası); bu deseni seçici biçimde çoğaltın.
→ *Beklenen etki:* ANA ve MFA yükselir → Extendibility (ve Effectiveness) artar; DIT sığ kaldığından (maks 3) anlaşılabilirlik bozulmaz.

> Üç önerinin tamamı doğrudan iki en zayıf niteliği hedefler: #1 ve #2 Understandability'nin gerçek (per-class) sorununu ve coupling'i, #2 ve #3 ise Extendibility'yi onarır.

---

## Belirsizlikler ve Sınırlamalar
- **Tek anlık görüntü, referans yok.** Mutlak QMOOD değerleri eşiklenemez; yorumlar denklem ayrıştırması ve ortalama–maksimum dağılımına dayandırıldı.
- **1.5.3, 1.5.x bakım hattının devamıdır.** Bu sürüme özgü tek gerçek değişiklik ~%3 büyüme (600→618 sınıf) ve ortalama LCOM'un hafif artışıdır (30,21→31,24); god sınıf değişmemiştir. Değerlendirme bilinçli olarak 1.5.1/1.5.2 ile paraleldir (yapay farklılaştırma yapılmadı).
- **Marjinal maksimumlar aynı sınıfı kesin kanıtlamaz.** "Tek god class" çıkarımı güçlü aritmetik uyuma dayanır (LCOM_max ≈ C(NOM_max,2)), ancak kesinlik için sınıf düzeyinde liste gerekir.
- **Boyut iç içeliği (confound):** Reusability/Functionality/Understandability ham değerleri DSC ile iç içedir; "iyi/kötü" kanıtı olarak okunmamalıdır.
- **Ortalamalar dağılımı gizler;** öneriler kasıtlı olarak ortalamayı değil **kuyruğu (aykırı sınıfı)** hedefler.
- LCOM tanımı uygulamaya göre değişebilir; burada klasik CK-LCOM (kohezyonsuz metot çiftleri) varsayıldı — kombinatorik üst sınır bu varsayıma dayanır.

---

### Tek Cümlelik Özet
1.5.3, **1.5.x bakım hattının son halkasıdır**; ~%3 büyümüş (618 sınıf) ve ortalama kohezyonu hafif kötüleşmiş (LCOM 30,21→31,24) olsa da baskın god sınıf **üç sürüm boyunca birebir aynı kalmıştır** (NOM 95 / WMC 381 / LCOM 4371 / MPC 401 / RFC 149) — iyi kapsüllenmiş (DAM 0,885), sığ ve kompozisyon-ağırlıklı bu tasarımda en zayıf iki nitelik **Understandability** (≈%98 DSC-boyut güdümlü; gerçek sorun god-class'ta yoğun) ve **Extendibility** (0,4923; yüksek **DCC** + çok düşük **ANA/MFA**) olup, çözüm dağınık değil **yoğunlaşmıştır**: serinin standing borcu olan aykırı sınıfı bölmek + coupling'i düşürmek + hedefli soyutlama eklemek birden çok metriği aynı anda iyileştirir.
