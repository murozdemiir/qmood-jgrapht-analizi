# JGraphT (`jgrapht-core`) — QMOOD Tasarım Kalitesi Değerlendirmesi

**Kapsam:** 11 sürüm (0.9.0 → 1.5.3). Sistem düzeyi ortalamalar.
**Model:** QMOOD (Bansiya & Davis, 2002) + CK metrikleri.
**Büyüme bağlamı:** Tasarım boyutu (DSC) 238 → 618 (**+159,7%**, ~2,6×); sınıf sayısı 238 → 618. Tüm değerlendirme bu büyüme ışığında okunmalıdır.

---

## ⚠️ Metodolojik Uyarı: Hangi metrikler karşılaştırılabilir?

QMOOD kalite niteliklerinin **yarısı boyuta bağımlıdır (extensive)**, yarısı **boyuttan bağımsızdır (intensive / sınıf başına oran)**. Bu ayrım yapılmadan yapılan yorum yanıltıcı olur:

| Nitelik | Boyut terimi içeriyor mu? | Sürümler arası güvenilir mi? |
|---|---|---|
| Reusability | **Evet** — `0.50·DSC` baskın | Hayır (boyut vekili) |
| Functionality | **Evet** — `0.22·(DSC+NOH)` baskın | Hayır (boyut vekili) |
| Understandability | **Evet** — `-0.33·DSC` baskın | Hayır (boyut vekili) |
| Flexibility | Hayır (yalnızca DAM, DCC, MOA, NOP) | **Evet** |
| Extendibility | Hayır (yalnızca ANA, MFA, NOP, DCC) | **Evet** |
| Effectiveness | Hayır (yalnızca ANA, DAM, MOA, MFA, NOP) | **Evet** |

**Sayısal kanıt:** Reusability(0.9.0) = `−0.25·2.3487 + 0.25·0.4070 + 0.50·3.9202 + 0.50·238 = 120,47`. Bu değerin **119'u (≈%98,8) yalnızca `0.50·DSC`** terimidir. Aynı şekilde Functionality(0.9.0)=61,69'un ≈%97'si `0.22·(DSC+NOH)` terimidir. Dolayısıyla Reusability ve Functionality pratikte **"sistem büyüdü"** ifadesinin yeniden adlandırılmasıdır; gerçek sınıf-içi kalite ölçüsü değildir.

> **Sonuç:** Gerçek kalite eğilimi için (a) boyuttan bağımsız üç QMOOD niteliği (Flexibility, Extendibility, Effectiveness) ve (b) ortalama oldukları için zaten boyuta göre normalize CK metrikleri (WMC, RFC, LCOM, CBO, MPC) kullanılmıştır. Reusability/Functionality "artışı" ve Understandability "çöküşü" büyümeden arındırılmadan kanıt sayılmamıştır.

---

## 1. Genel Kalite Değerlendirmesi

### 1.1 Boyuttan bağımsız (güvenilir) niteliklerin eğilimi

| Nitelik | 0.9.0 | 1.5.3 | Değişim | Yorum |
|---|---|---|---|---|
| **Extendibility** | 0,8944 | 0,4923 | **−45,0%** | Belirgin **kötüleşme** |
| **Flexibility** | 1,4611 | 1,5861 | **+8,6%** | Hafif **iyileşme** |
| **Effectiveness** | 1,0821 | 1,1205 | +3,5% | Pratikte **sabit** |

- **Extendibility −45% (asıl bulgu):** Denklem `0.50·(ANA+MFA+NOP) − 0.50·DCC`. Düşüşün ayrıştırması: ANA 0,6176→0,3204 (−0,30), MFA 0,2469→0,1512 (−0,10), NOP 3,2731→3,5453 (+0,27), DCC 2,3487→3,0324 (**+0,68**). Yani genişletilebilirliği esas olarak **artan coupling (DCC) ve azalan soyutlama/kalıtım-tabanlı yeniden kullanım (ANA, MFA)** aşağı çekmiştir; artan polimorfizm (NOP) bunu yalnızca kısmen telafi etmiştir.
- **Flexibility +8,6%:** Denklem `0.25·DAM − 0.25·DCC + 0.50·MOA + 0.50·NOP`. DAM neredeyse sabit (0,8990→0,8850), DCC ceza yazıyor, ancak **MOA 0,3739→0,7006 (+87,4%)** ve **NOP +8,3%** bu cezayı aşıyor. Bu, **kalıtımdan kompozisyona kayan** bilinçli bir tasarım eğiliminin olumlu yansımasıdır (MFA ve DIT düşerken MOA yükseliyor).
- **Effectiveness ~sabit:** ANA↓ ve MFA↓ ile MOA↑ ve NOP↑ birbirini dengeliyor; tasarım etkinliği korunmuş.

### 1.2 Boyuta bağımlı niteliklerin "ham" eğilimi (dikkatle okunmalı)

| Nitelik | 0.9.0 | 1.5.3 | Ham değişim | Gerçek anlam |
|---|---|---|---|---|
| Reusability | 120,47 | 310,45 | +157,7% | ≈ DSC büyümesi (+159,7%) — **boyut artefaktı** |
| Functionality | 61,69 | 157,73 | +155,7% | ≈ DSC+NOH büyümesi — **boyut artefaktı** |
| Understandability | −81,87 | −207,89 | −126 (daha negatif) | ≈ `−0.33·ΔDSC` — **boyut artefaktı** |

**Understandability'nin kanıtı:** Ham düşüşün −125,4'ü tek başına `−0.33·(618−238)` DSC teriminden gelir; toplam değişim −126'dır. Yani çöküşün ≈%99'u "kod tabanı büyüdü" demektir, sınıf-başı anlaşılabilirlik kaybı değil. **Gerçek anlaşılabilirlik sinyali için sınıf-içi CK metriklerine bakılmalıdır** (bkz. Bölüm 2).

**Bölüm özeti:** Büyümeden arındırıldığında tablo şudur — *genişletilebilirlik gerilemiş, esneklik hafif artmış, etkinlik korunmuş*; buna karşın sınıf-içi sağlık (kohezyon, karmaşıklık, coupling) gözle görülür biçimde bozulmuştur.

---

## 2. Bakım Yapılabilirlik (Maintainability) Analizi

Ham Understandability boyut güdümlü olduğundan, bakım kolaylığı **sınıf-başına ortalama CK metrikleriyle** değerlendirilmiştir (bunlar ortalama oldukları için boyuta karşı dengelidir):

| Metrik (sınıf başına ort.) | 0.9.0 | 1.5.3 | Değişim | Etki |
|---|---|---|---|---|
| **LCOM** (kohezyon eksikliği) | 13,76 | 31,24 | **+127,0%** | ↑ kötü |
| **RFC** (yanıt kümesi) | 11,24 | 17,25 | **+53,5%** | ↑ kötü |
| **WMC** (karmaşıklık) | 10,36 | 15,78 | **+52,3%** | ↑ kötü |
| **MPC** (mesaj geçişi) | 8,67 | 16,85 | **+94,4%** | ↑ kötü |
| **CBO/DCC** (coupling) | 2,35 | 3,03 | **+29,1%** | ↑ kötü |
| **NOM** (metot sayısı) | 5,16 | 6,32 | +22,7% | ↑ kötü |
| **CAM** (metot kohezyonu) | 0,4070 | 0,3660 | −10,1% | ↓ kötü |

**Değerlendirme — bakım belirgin biçimde zorlaşmıştır:**
- **Kohezyon erozyonu en güçlü sinyaldir:** LCOM iki kattan fazla arttı (+127%). Bir sınıfın metotları giderek ortak alanları paylaşmıyor; bu, sorumlulukların dağılması ("god class" eğilimi) ve değişiklik maliyetinin yükselmesi demektir. CAM'in −%10'luk düşüşü aynı yönü bağımsız olarak doğrular.
- **Karmaşıklık birikimi:** WMC +52% ve RFC +53% birlikte, sınıf başına test edilmesi/anlaşılması gereken yüzeyin yarıdan fazla genişlediğini gösterir.
- **Etkileşim coupling'i:** MPC'nin ~iki katına çıkması (+94%) ve CBO'nun +%29 artması, "konuşkan" (chatty) nesne etkileşimlerine ve dalgalanma (ripple) riskinin artmasına işaret eder.

> Özetle: ham QMOOD Understandability büyüme nedeniyle "çöküyor" görünse de, **bağımsız ve büyümeye dirençli CK metriklerinin tamamı aynı yönde bozulduğu için** bakım zorluğundaki artış sağlam bir bulgudur.

---

## 3. Teknik Borç (Technical Debt) Tahmini

Aşağıdaki eş-yönlü ve birbirini doğrulayan eğilimler teknik borç birikimine işaret eder:

| Borç sinyali | Metrik kanıtı | Yorum |
|---|---|---|
| **Kohezyon borcu** | LCOM +127%, CAM −10% | En kritik kalem; refactoring olmadan birikmeye devam eder |
| **Karmaşıklık borcu** | WMC +52%, RFC +53%, NOM +23% | Sınıflar şişiyor |
| **Coupling borcu** | CBO/DCC +29%, MPC +94%, DAC/MOA +87% | Bağımlılık ağı yoğunlaşıyor |
| **Soyutlama kaybı** | ANA −48%, MFA −39%, DIT 0,62→0,32 | Hiyerarşi düzleşti; somut sınıflar soyutlamaları geride bıraktı |

### Kritik kırılma noktaları (sürüm bazında)
Borç tek tip birikmemiş; iki sürüm sıçrama yaratmıştır:

- **1.1.0 — Kohezyon sıçraması:** LCOM yerel minimumdan (1.0.1'de 11,83) **24,70'e fırladı (~2×)** ve bir daha toparlanmadı. Aynı sürümde WMC 11,77→13,09, CBO 2,57→2,87. Bu sürümde eklenen kodun odaklı gözden geçirilmesi önerilir.
- **1.2.0 — Soyutlama düzleşmesi:** ANA 0,5759→**0,3861**, MFA 0,2384→**0,1718** keskin biçimde düştü; buna karşılık MOA 0,4613→0,5416 yükseldi. Bu, kalıtım→kompozisyon yeniden yapılandırmasının gerçekleştiği sürümdür.

> Not: 1.3.x sonrası metrikler **yatay seyrediyor** (örn. LCOM ~28–31, WMC ~15,8, DCC ~3,0). Yani borç esas olarak 1.1.0–1.2.0 aralığında oluşmuş, sonrasında **stabilize** olmuştur — kontrolsüz hızlanan bir bozulmadan çok, telafi edilmemiş tek seferlik bir sıçrama profili.

---

## 4. Refactoring Önerileri (somut, metrik-temelli)

1. **LCOM hedefli sınıf ayrıştırması (öncelik #1).** LCOM +127% ve sıçramanın 1.1.0'da olması nedeniyle, yüksek-LCOM sınıflarını *Extract Class* ile tek-sorumluluğa bölün. Hedef: sürüm başına ortalama LCOM'u 1.0.x seviyesine (~12–14) yaklaştırmak. İlk taranacak aday kümesi: 1.1.0 ve 1.2.0'da eklenen/değişen sınıflar.
2. **WMC/RFC düşürme (*Extract Method* + sorumluluk taşıma).** WMC 15,8 ve RFC 17,3 seviyesindeki en karmaşık sınıflarda metot sayısını (NOM) ve metot karmaşıklığını azaltın. Hedef: WMC ortalamasını ≤13'e çekmek (1.0.x bandı).
3. **Coupling/MPC azaltma (arayüz ve cephe).** MPC +94% ve CBO +29% göz önünde, doğrudan sınıf-sınıf çağrılarını arayüzler / *Facade* / *Mediator* ardına alın; "feature envy" çağrı zincirlerini sadeleştirin. Hedef: ortalama CBO'yu ~2,6 (1.0.1) bandına indirmek.
4. **Soyutlama kaybını seçici telafi (Extendibility için).** ANA −48% ve MFA −39%, Extendibility'yi −45% düşüren ana etkenlerdendir. Kompozisyona geçiş bilinçli olabilir; bu nedenle **derin kalıtım dayatmadan**, tekrar eden davranışı paylaşılan **arayüz/abstract tipler** ile toparlayın. Böylece DCC artmadan Extendibility kısmen geri kazanılır.
5. **CAM kohezyonunu yükseltme.** CAM 0,407→0,366 düşüşüne karşı, parametre-tip imzaları heterojen olan sınıfları imza türüne göre gruplayarak bölün. Hedef: CAM'i ≥0,40 bandına döndürmek.

> Sıralama gerekçesi: 1 ve 2 doğrudan bakım maliyetini (LCOM/WMC) düşürür; 3 dalgalanma riskini azaltır; 4 ve 5 QMOOD'un boyuttan bağımsız niteliklerinden Extendibility/Effectiveness'i hedefler.

---

## 5. Mimari Kalite Yorumu (Architectural Erosion)

**Soru:** Yazılım büyüdükçe (DSC 238→618) mimari bozulma belirtisi var mı?
**Yanıt: Karışık — net erozyon sinyalleri var, ancak bir kısmı bilinçli/sağlıklı evrim.**

**Erozyon yönünde kanıtlar:**
- Coupling büyümeyle birlikte artıyor: CBO/DCC +29%, MPC +94% (boyutla orantısız büyük). Sağlıklı bir mimaride büyüme coupling'i bu denli artırmamalıydı.
- Kohezyon büyümeyle birlikte düşüyor: LCOM +127%, CAM −10%. Modülerlik, boyut arttıkça zayıflamış.
- Soyutlama somut sınıfların gerisinde kalmış: ANA −48%. Yeni somut sınıflar, soyutlama katmanından daha hızlı eklenmiş.

**Sağlıklı/bilinçli evrim yönünde kanıtlar:**
- Kompozisyona geçiş: MOA/DAC +87%, MFA −39%, DIT 0,62→0,32. "Kalıtım yerine kompozisyon" modern tasarım ilkesiyle tutarlıdır ve Flexibility'yi (+8,6%) yükseltmiştir.
- Polimorfizm artışı: NOP +8,3% — genişletme noktalarının sayısı artmış.
- Bozulma 1.3.x sonrası **stabilize** olmuş (metrikler yataylaşmış); kontrolsüz hızlanan bir erozyon profili gözlenmiyor.

> **Mimari kanaat:** Klasik anlamda "kontrolden çıkmış erozyon" değil, **kohezyon ve coupling ekseninde telafi edilmemiş bir kalite düşüşü** söz konusudur. Tasarım stili kasıtlı olarak kompozisyona kaymış (bu QMOOD'un kalıtım-odaklı ödüllendirmesi nedeniyle Extendibility/Effectiveness'i kısmen "haksızca" cezalandırır), ancak LCOM ve MPC'deki büyük artışlar **gerçek ve stil-bağımsız** mimari risklerdir. Öncelik, kompozisyon kararını geri almak değil; o kararın yanında **kohezyonu ve coupling'i toparlayacak** hedefli refactoring yapmaktır.

---

## Belirsizlikler ve Sınırlamalar

- **Yalnızca sistem düzeyi ortalamalar verildi; dağılım/varyans yok.** Birkaç aşırı uçtaki "god class", LCOM/WMC ortalamasını tek başına yukarı çekiyor olabilir. Bu nedenle öneriler "şu spesifik sınıf" düzeyinde değil, "şu metrik profilindeki sınıflar" düzeyinde verilmiştir.
- **QMOOD, kalıtım-tabanlı yeniden kullanımı (MFA, ANA) ödüllendirir.** Kompozisyona geçiş bu modelde kısmen olumsuz görünür; Extendibility/Effectiveness düşüşünün bir bölümü mutlak kalite kaybından çok **model yanlılığıdır**.
- **Reusability/Functionality ham değerleri boyutla iç içedir (confounded);** "iyileşme" olarak okunmamalıdır.
- **Ham Understandability boyutla iç içedir;** bakım yorumu bu nedenle CK metriklerine dayandırılmıştır.
- Tüm yüzde değişimleri ilk (0.9.0) ve son (1.5.3) sürüm arasındadır; ara sürümlerdeki yerel hareketler (örn. 1.1.0, 1.2.0 kırılmaları) metinde ayrıca belirtilmiştir.

---

### Tek Cümlelik Özet
Kod tabanı ~2,6× büyürken **boyut güdümlü nitelikler (Reusability/Functionality) mekanik olarak şişti ve ham Understandability mekanik olarak çöktü**; büyümeden arındırılmış gerçek tabloda ise **Extendibility −45% geriledi, Flexibility +8,6% arttı, Effectiveness sabit kaldı**, buna karşılık sınıf-içi sağlık (**LCOM +127%, MPC +94%, RFC +53%, WMC +52%, CBO +29%**) belirgin biçimde bozularak bakım maliyetini ve teknik borcu yükseltti.
