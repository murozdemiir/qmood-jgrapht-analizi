# JGraphT (`jgrapht-core`) 1.5.1 — Tek Sürüm QMOOD Derin İncelemesi

**Kapsam:** Tek sürüm anlık görüntü (1.5.1, 600 sınıf). QMOOD + CK metrikleri (ortalama **ve maksimum** değerlerle).
**Model:** QMOOD (Bansiya & Davis, 2002).

---

## ⚠️ Yöntem Notu (önce okunmalı)

Tek sürümlük veride **mutlak QMOOD değerleri tek başına "iyi/kötü" eşiğine oturtulamaz** — QMOOD karşılaştırmalı bir modeldir, referans (baseline) yoktur. Bu nedenle yorumlar iki sağlam dayanağa oturtulmuştur:

1. **Denklem ayrıştırması:** Her niteliğin değerine *hangi metriğin ne kadar katkı verdiği* hesaplanarak (her denklem girdilerden birebir yeniden üretildi).
2. **Ortalama–maksimum dağılımı:** Ortalamalar dengeli görünürken maksimumlar dağılımın kuyruğunu (god-class riskini) açığa çıkardığı için asıl kanıt buradadır.

Tüm QMOOD denklemleri verilen metriklerden **birebir yeniden üretildi** (ör. Understandability = −0.33·(0.3217+3.0183+3.5183+6.32+600)+0.33·(0.8794+0.3641) = −201,94 ✓; Extendibility = 0.50·(0.3217+0.1523+3.5183)−0.50·3.0183 = 0,487 ✓). Sayılar tutarlıdır.

---

## 1. Genel Kalite Değerlendirmesi

### 1.1 Asıl bulgu: Ortalamalar ılımlı, maksimumlar felaket (aşırı dağılım)

Ortalama CK metrikleri kabul edilebilir görünür (WMC ~16, CBO ~3, LCOM ~30). Ancak maksimumlar, 600 küçük sınıfın seyrelttiği **en az bir "god class"** olduğunu gösteriyor:

| CK metrik | Ortalama | **Maksimum** | Maks/Ort | Yorum |
|---|---|---|---|---|
| **LCOM** (kohezyon eksikliği) | 30,21 | **4371** | **~145×** | Tek sınıfta felaket düzeyde kohezyonsuzluk |
| **WMC** (karmaşıklık) | 15,78 | **381** | ~24× | Tek sınıfta aşırı karmaşıklık |
| **MPC** (dışa mesaj geçişi) | 16,77 | **403** | ~24× | Tek sınıfta aşırı dışa bağımlılık |
| **NOM** (metot sayısı) | 6,32 | **95** | ~15× | 95 metotlu dev sınıf |
| **RFC** (yanıt kümesi) | 17,14 | **151** | ~9× | Çok geniş yanıt kümesi → test güçlüğü |
| **NOA** (öznitelik sayısı) | 3,06 | 24 | ~8× | Veri-yoğun sınıf |
| **CBO** (coupling) | 3,02 | 21 | ~7× | Yüksek-coupling aykırı değeri |
| **NOC** (alt sınıf sayısı) | 0,57 | 28 | ~50× | 28 alt sınıflı temel tip (uzantı noktası) |
| **DIT** (kalıtım derinliği) | 0,32 | 3 | — | Sığ hiyerarşi (olumlu) |

**Aykırı değerler büyük olasılıkla aynı sınıfa ait** — kombinatorik kanıt: 95 metotlu bir sınıf için olası en yüksek LCOM = C(95,2) = **4465**; gözlenen LCOM_max = **4371**. Yani 4465 metot çiftinin yalnızca ~47'si ortak alan paylaşıyor (**%98,9'u kohezyonsuz**). Benzer şekilde WMC_max=381 ≈ 95 metot × ~4 karmaşıklık, MPC_max=403 ≈ 95 metot × ~4,2 çağrı. Bu profil tek bir **dev yardımcı/god sınıfa** (muhtemelen statik yardımcı metot yığını) işaret eder. *(Kesin değil; marjinal maksimumlar tek başına aynı sınıfı kanıtlamaz, ancak aritmetik uyum çok güçlü.)*

### 1.2 Genuine güçlü yönler
- **Güçlü kapsülleme:** DAM = 0,8794 → özniteliklerin ~%88'i private/protected. Flexibility ve Effectiveness'e olumlu katkı veren gerçek bir artı.
- **Sığ, sade hiyerarşi:** DIT_max = 3, ortalama 0,32 → anlaşılabilirliği destekler; aşırı kalıtım yok.
- **Kompozisyon ağırlıklı stil:** MOA = 0,6917 yüksek, MFA = 0,1523 düşük → "kalıtım yerine kompozisyon" tercihi. Bu, Flexibility'yi (1,5703) yukarı çeken bilinçli bir tasarım kararıdır.

### 1.3 Genuine zayıf yönler
- **Kronik düşük kohezyon:** CAM = 0,3641 (düşük) + LCOM ortalaması 30 / maks 4371.
- **Soyutlama kıtlığı:** ANA = 0,3217 ve MFA = 0,1523 çok düşük → genişletme iskelesi zayıf.
- **Tek noktada yoğunlaşan coupling:** ortalama CBO ılımlı (3,02) ama MPC_max=403 / CBO_max=21.

> **Not — yüksek Reusability ve Functionality kalite kanıtı DEĞİLDİR.** Reusability=301,45'in ≈%99,5'i tek başına `0.50·DSC` (=300), Functionality=152,89'un ≈%98,9'u `0.22·(DSC+NOH)` (=151,14) terimidir. Bu iki değer pratikte "sistem 600 sınıf" demektir; sınıf-içi kaliteyi ölçmez. Bu yüzden bu rapor raw değerlerden "en güçlü nitelik" seçmez.

---

## 2. En Zayıf 2 Kalite Niteliği ve Sorumlu Metrikler

**Sıralama yöntemi:** Nitelikler farklı ölçeklerde olduğundan kör büyüklük sıralaması yapılmadı. (a) İşaret olarak **negatif** olan tek nitelik en zayıf kabul edildi; (b) aynı ölçekteki (sınıf-başına, O(1)) üç nitelik — Flexibility 1,5703 · Effectiveness 1,1127 · **Extendibility 0,487** — adil biçimde karşılaştırıldı; en düşük olan ikinci en zayıf seçildi.

### 🥇 En zayıf #1 — Understandability (= −201,94, tek negatif nitelik)

| Terim | Değer | Katkı |
|---|---|---|
| −0.33·**DSC** | 600 | **−198,00** |
| −0.33·NOM | 6,32 | −2,09 |
| −0.33·NOP | 3,52 | −1,16 |
| −0.33·DCC | 3,02 | −1,00 |
| −0.33·ANA | 0,32 | −0,11 |
| +0.33·DAM | 0,88 | +0,29 |
| +0.33·CAM | 0,36 | +0,12 |
| **Toplam** | | **−201,94** |

**Sorumlu metrikler:** Ezici biçimde **DSC=600** (toplam etkinin **%98'i**). Bu büyük ölçüde bir **boyut artefaktıdır** — denklem boyuta göre normalize değil. Eyleme dönük gerçek sınıf-içi katkılar küçüktür: **NOM (−2,09)** ve **DCC (−1,00)**; ayrıca **CAM düşük olduğundan** (+0,12) pozitif tampon neredeyse yok. *Abartmamak adına:* ham Understandability'nin çöküşü esasen "kod büyük" demektir; gerçek anlaşılabilirlik sorunu üniform değil, **Bölüm 1.1'deki god-class'ta yoğunlaşmıştır** (WMC_max=381, LCOM_max=4371, RFC_max=151).

### 🥈 En zayıf #2 — Extendibility (= 0,487; aynı ölçekteki en düşük nitelik)

| Terim | Değer | Katkı |
|---|---|---|
| +0.50·**NOP** | 3,5183 | +1,759 |
| +0.50·ANA | 0,3217 | +0,161 |
| +0.50·MFA | 0,1523 | +0,076 |
| −0.50·**DCC** | 3,0183 | **−1,509** |
| **Toplam** | | **0,487** |

**Sorumlu metrikler:** İki yönlü zayıflık — (1) **DCC=3,0183 yüksek**, pozitif bütçenin (1,996) ~%75'ini (−1,509) yiyor; (2) **ANA=0,3217 ve MFA=0,1523 çok düşük**, ikisi birlikte yalnızca +0,237 katkı veriyor. Yani tasarım yalnızca **polimorfizm (NOP, +1,759)** sayesinde genişletilebiliyor; **soyutlama ve kalıtım-tabanlı yeniden kullanım iskelesi neredeyse yok** ve **coupling** kalanı tüketiyor.

### Ortak suçlu: DCC (coupling)
**DCC, iki en zayıf niteliğin İKİSİNİ birden** aşağı çekiyor (Understandability'de negatif kovada, Extendibility'de doğrudan −0,50 katsayıyla). Bu nedenle coupling düşürmek tek hamlede iki niteliği iyileştirir → aşağıdaki #2 önerisinin gerekçesi.

---

## 3. Üç Somut Refactoring Önerisi (metrik-hedefli)

**1) Dev sınıfı (god class) ayrıştır — `NOM_max=95, WMC_max=381, LCOM_max=4371, MPC_max=403, RFC_max=151`.**
Bu tek sınıf, beş metriğin felaket kuyruğundan aynı anda sorumlu. LCOM'u olası maksimuma çok yakın (≈%99 kohezyonsuz) olduğundan, *Extract Class* ile sorumluluk bazında bölün; statik yardımcı yığınıysa konu başlıklarına göre ayrı yardımcı sınıflara dağıtın.
→ *Beklenen etki:* LCOM_max, WMC_max, MPC_max, RFC_max büyük ölçüde düşer; **aykırı değer ortalamaları da şişirdiği için** LCOM_mean (30,21) ve WMC_mean (15,78) birlikte iyileşir; Understandability'nin gerçek sınıf-içi bileşeni rahatlar.

**2) Coupling'i düşür — `DCC=3,0183` (iki zayıf niteliğin ortak suçlusu); `MPC_max=403, CBO_max=21`.**
Yüksek-MPC sınıfı ile işbirlikçileri arasına **arayüz / Facade / Mediator** koyun; "feature envy" çağrı zincirlerini sadeleştirin. Hedef: aykırı sınıfın CBO'sunu 21'den ortalamaya (≈3) çekmek ve sistem DCC'sini azaltmak.
→ *Beklenen etki:* DCC düşünce **hem Extendibility yükselir** (−0.50·DCC terimi küçülür) **hem de Understandability'nin per-class kısmı iyileşir**.

**3) Hedefli soyutlama ekle — `ANA=0,3217`, `MFA=0,1523` (ikisi de çok düşük).**
Extendibility soyutlamadan aç. Kompozisyon-ağırlıklı tasarımın tekrar eden/sabit-kodlanmış davranış bıraktığı yerlerde, **derin kalıtım dayatmadan** paylaşılan arayüz/abstract tipleri kilit uzantı noktalarında çıkarın. Kod tabanı bunu zaten yapabiliyor (NOC_max=28'lik bir temel tip mevcut uzantı noktası); bu deseni seçici biçimde çoğaltın.
→ *Beklenen etki:* ANA ve MFA yükselir → Extendibility (ve Effectiveness) artar; DIT sığ kaldığından (maks 3) anlaşılabilirlik bozulmaz.

> Üç önerinin tamamı doğrudan iki en zayıf niteliği hedefler: #1 ve #2 Understandability'nin gerçek (per-class) sorununu ve coupling'i, #2 ve #3 ise Extendibility'yi onarır.

---

## Belirsizlikler ve Sınırlamalar
- **Tek anlık görüntü, referans yok.** Mutlak QMOOD değerleri eşiklenemez; yorumlar denklem ayrıştırması ve ortalama–maksimum dağılımına dayandırıldı.
- **Marjinal maksimumlar aynı sınıfı kesin kanıtlamaz.** "Tek god class" çıkarımı güçlü aritmetik uyuma dayanır (LCOM_max ≈ C(NOM_max,2)), ancak kesinlik için sınıf düzeyinde liste gerekir.
- **Boyut iç içeliği (confound):** Reusability/Functionality/Understandability ham değerleri DSC ile iç içedir; "iyi/kötü" kanıtı olarak okunmamalıdır.
- **Ortalamalar dağılımı gizler;** öneriler kasıtlı olarak ortalamayı değil **kuyruğu (aykırı sınıfı)** hedefler.
- LCOM tanımı uygulamaya göre değişebilir; burada klasik CK-LCOM (kohezyonsuz metot çiftleri) varsayıldı — kombinatorik üst sınır bu varsayıma dayanır.

---

### Tek Cümlelik Özet
1.5.1, **iyi kapsüllenmiş (DAM 0,88), sığ ve kompozisyon-ağırlıklı** büyük bir tasarımdır; ortalama metrikleri kabul edilebilir olsa da **en az bir god class** (NOM 95 / WMC 381 / LCOM 4371 / MPC 403 / RFC 151) baskın kalite ve bakım yüküdür — QMOOD'da en zayıf iki nitelik **Understandability** (≈%98 DSC-boyut güdümlü; gerçek sorun god-class'ta yoğun) ve **Extendibility** (0,487; yüksek **DCC** + çok düşük **ANA/MFA**) olup, çözüm dağınık değil **yoğunlaşmıştır**: aykırı sınıfı bölmek + coupling'i düşürmek + hedefli soyutlama eklemek birden çok metriği aynı anda iyileştirir.
