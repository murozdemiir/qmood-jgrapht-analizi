# JGraphT — QMOOD Tabanlı Yazılım Kalite Değerlendirmesi

> **Kapsam:** JGraphT `jgrapht-core` modülü, sürüm 0.9.0 → 1.5.3  
> **Yöntem:** QMOOD (Bansiya & Davis 2002) tasarım metrikleri ve kalite nitelikleri  
> **Uyarı:** Tüm yorumlar doğrudan verilen sayısal verilere dayandırılmıştır; abartı yapılmamıştır.

---

## 1. Genel Kalite Değerlendirmesi

### 1.1 Büyüme Profili

Kütüphane 0.9.0'dan 1.5.3'e kadar sınıf sayısı (DSC) açısından **%160 büyümüştür** (238 → 618 sınıf). Hiyerarşi derinliği (NOH) 35'ten 91'e ulaşmış; bu oran büyüme hızını da aşmaktadır (%160 sınıf artışına karşın %160 NOH artışı — oransal denge korunmuş görünse de mutlak derinlik artışı dikkate değerdir).

### 1.2 Kalite Nitelikleri Özeti

| Nitelik | 0.9.0 | 1.5.3 | Normalize (baseline=1.0) | Yön |
|---|---|---|---|---|
| Reusability | 120.47 | 310.45 | 1.74 | ✅ Belirgin iyileşme |
| Flexibility | 1.461 | 1.586 | 1.40 | ✅ Ilımlı iyileşme |
| Understandability | −81.87 | −207.89 | −1.59 | ❌ Belirgin bozulma |
| Functionality | 61.69 | 157.73 | 1.73 | ✅ Belirgin iyileşme |
| Extendibility | 0.894 | 0.492 | 0.46 | ❌ Ciddi bozulma |
| Effectiveness | 1.082 | 1.121 | 1.01 | ➡️ Neredeyse değişmedi |

**Genel tablo:** Kütüphane işlevsel zenginlik ve yeniden kullanılabilirlik açısından güçlenmiş, ancak anlaşılabilirlik ve genişletilebilirlik açısından ciddi ölçüde kötüleşmiştir.

### 1.3 Öne Çıkan Bozulmalar

**Extendibility** en kritik bozulmayı yaşamıştır: 0.894'ten 0.492'ye düşerek **başlangıç değerinin yalnızca %46'sına** gerilemiştir. Bu, kütüphanenin yeni bileşenler eklenerek genişletilmesinin giderek zorlaştığını göstermektedir.

**Understandability** mutlak değer olarak −81.87'den −207.89'a düşmüştür (normalize: −0.99 → −1.59, **%60 ağırlaşma**). Kütüphane büyüdükçe kodu anlamak orantısız biçimde güçleşmektedir.

---

## 2. Bakım Yapılabilirlik (Maintainability) Analizi

QMOOD modelinde bakım yapılabilirlik doğrudan bir denklem olarak yer almaz; ancak **Understandability**, **Flexibility** ve coupling/cohesion metrikleri birlikte iyi bir vekil ölçüt oluşturur.

### 2.1 Anlaşılabilirlik: Bozulmanın Sürücüleri

Understandability denklemi şöyledir:

```
Understandability = −0.33*(ANA+DCC+NOP+NOM+DSC) + 0.33*(DAM+CAM)
```

Negatif terimler ağır basmaktadır. 1.5.3 için:

- **DCC** (bağlaşım): 2.35 → 3.03 (%29 artış) — her sınıfın ortalama olarak daha fazla başka sınıfa bağlandığını gösterir; anlamak için daha fazla bağlamı zihinde tutmak gerekir.
- **NOM** (karmaşıklık/yöntem sayısı): 5.16 → 6.32 (%22 artış) — sınıf başına metot sayısı arttıkça her sınıfın yüzü genişlemektedir.
- **NOP** (polimorfizm): 3.27 → 3.55 — küçük bir artış; tek başına sorun değil, diğerleriyle birlikte negatif katkı yapar.
- **DAM** (kapsülleme): 0.899 → 0.885 — hafif düşme; olumlu etki azalmaktadır.
- **CAM** (iç uyum): 0.407 → 0.366 (%10 düşme) — pozitif katkı zayıflamaktadır.

Sonuç: Negatif metrikler toplu artarken pozitif metrikler hafif gerilemiş; bu kombinasyon **Understandability'yi bileşik biçimde kötüleştirmiştir**.

### 2.2 Esneklik: Ilımlı İyileşme

Flexibility denklemi:

```
Flexibility = 0.25*DAM − 0.25*DCC + 0.50*MOA + 0.50*NOP
```

**MOA** (kompozisyon/agregasyon): 0.374 → 0.701 (%87 artış) — en büyük olumlu etki. Sınıflar kalıtım yerine giderek daha fazla kompozisyon kullanmaktadır; bu nesne yönelimli tasarım açısından olumludur.

**DCC** artışı negatif katkı verse de MOA artışı bunu telafi etmiş ve Flexibility net olarak 1.461'den 1.586'ya yükselmiştir. Ancak bu iyileşme skalar değer olarak mütevazıdır (normalize: 1.0 → 1.40).

### 2.3 Coupling/Cohesion Dengesi

| Metrik | 0.9.0 | 1.5.3 | Yorum |
|---|---|---|---|
| DCC (bağlaşım) | 2.35 | 3.03 | Artış → olumsuz |
| CBO (CK metrik) | 2.35 | 3.03 | DCC ile tutarlı |
| CAM (iç uyum) | 0.407 | 0.366 | Düşüş → olumsuz |
| LCOM (CK metrik) | 13.76 | 31.24 | **%127 artış → ciddi olumsuz** |

LCOM (Lack of Cohesion in Methods) değeri 13.76'dan 31.24'e çıkmıştır. Bu, **sınıfların iç uyumunun neredeyse yarı yarıya azaldığını** göstermekte; sınıfların birden fazla sorumluluğu bünyesinde taşıdığına işaret etmektedir. CBO artışı ile birleşince bakım maliyetinin arttığı söylenebilir.

**Sonuç:** Bakım yapılabilirlik karma bir tablo çizmektedir. Esneklik iyileşmiş, ancak anlaşılabilirlik ve iç uyum bozulması nedeniyle **net bakım yükü artmıştır**.

---

## 3. Teknik Borç Tahmini

Aşağıdaki metrik eğilimleri teknik borç birikiminin sinyallerini taşımaktadır.

### 3.1 Artan Bağlaşım (DCC / CBO)

DCC 2.35'ten 3.03'e, CBO da paralel biçimde artmıştır. Sınıflar arası bağımlılıklar büyüme oranının üzerinde artmaktadır. Bu, değişikliklerin **ripple effect** (dalgalanma etkisi) riski taşıdığını gösterir; bir sınıfta yapılan değişiklik daha fazla başka sınıfı etkileyebilir.

### 3.2 WMC'nin Hızlı Artışı ve Stabilizasyonu

WMC (Weighted Methods per Class) 10.36'dan önce 16.27'ye (1.3.1) tırmanmış, ardından 15.78 (1.5.3) seviyesinde stabilize olmuştur. Bu, 1.3.x döneminde ciddi bir sınıf şişmesi (class bloat) yaşandığını; ancak sonrasında bir ölçüde kontrol altına alındığını gösterir. Stabilizasyon olumlu bir işaret olsa da mevcut ortalama hâlâ yüksektir.

### 3.3 LCOM Patlaması

LCOM'un 13.76'dan 30.22'ye (1.5.x ortalaması) çıkması özellikle dikkat çekicidir. 1.1.0 sürümünde ani bir zıplama (13.56 → 24.70) gözlemlenmektedir. Bu, o sürümde eklenen sınıfların tek sorumluluk ilkesini (SRP) ihlal etme eğiliminde olduğuna işaret eder. **LCOM artışı klasik bir teknik borç göstergesidir**: sınıf ayrıştırılmadan büyütüldüğünde iç uyum düşer.

### 3.4 Düşen ANA ve MFA

- **ANA** (soyutlama): 0.618 → 0.320 (yaklaşık **%48 düşme**)
- **MFA** (kalıtım): 0.247 → 0.151 (**%39 düşme**)

Bu eğilim, soyut sınıf ve arayüz kullanımının somut sınıf sayısına göre nispi olarak azaldığını gösterir. Extendibility denkleminde ANA ve MFA pozitif katsayıya sahiptir; bu iki metriğin gerilemesi Extendibility bozulmasının baş sebebidir:

```
Extendibility = 0.50*(ANA+MFA+NOP) − 0.50*DCC
0.9.0: 0.50*(0.618+0.247+3.273) − 0.50*2.349 = 2.069 − 1.175 ≈ 0.894
1.5.3: 0.50*(0.320+0.151+3.545) − 0.50*3.032 = 2.008 − 1.516 ≈ 0.492
```

Hesap tutmaktadır: soyutlama azalırken bağlaşım arttığından genişletilebilirlik sıkışmaktadır.

### 3.5 Teknik Borç Özeti

| Gösterge | Eğilim | Borç Riski |
|---|---|---|
| DCC / CBO artışı | 0.9.0→1.5.3: +%29 | Orta-Yüksek |
| LCOM artışı | 0.9.0→1.5.3: +%127 | Yüksek |
| WMC artışı | 0.9.0→1.3.1: +%57, sonra stabil | Orta |
| ANA düşüşü | 0.9.0→1.5.3: −%48 | Yüksek |
| CAM düşüşü | 0.9.0→1.5.3: −%10 | Düşük-Orta |

---

## 4. Refactoring Önerileri

### 4.1 Yüksek LCOM'lu Sınıfları Parçalayın (God Class Ayrıştırması)

**Kanıt:** LCOM ortalaması 13.76'dan 31.24'e çıkmıştır. Ortalamanın bu kadar yükselmesi, dağılımda aşırı değerlerin (god class adayı sınıflar) bulunduğuna işaret eder.

**Öneri:** LCOM > 50 olan sınıfları tespit edip metot gruplarını cohesive sorumluluk kümeleri olarak ayrı sınıflara taşıyın. Hedef: LCOM ortalamasını 20'nin altına indirmek.

### 4.2 Soyutlama Katmanını Güçlendirin (ANA İyileştirmesi)

**Kanıt:** ANA 0.618'den 0.320'ye düşmüştür; somut sınıfların payı artmaktadır.

**Öneri:** Yeni somut sınıf eklenmeden önce ilgili soyut sınıf veya arayüz tanımlanmalıdır. Özellikle algoritma ailelerinde (traversal, shortest path, matching) her ailenin ortak bir soyut üst tipi olması hem ANA'yı hem MFA'yı iyileştirir ve Extendibility denkleminin pozitif terimlerini artırır.

### 4.3 DCC'yi Düşürmek için Bağımlılık Tersine Çevirme (DIP)

**Kanıt:** DCC 2.35'ten 3.03'e artmıştır; CBO da paralel seyretmektedir.

**Öneri:** Somut bağımlılıklar yerine arayüz veya soyut tip üzerinden bağımlılık kurun. Bağımlılık enjeksiyonu (DI) veya fabrika deseni kullanarak sınıflar arası doğrudan referansları azaltın. Hedef: DCC ortalamasının 2.5'in altında tutulması.

### 4.4 RFC ve MPC Artışını Kontrol Altına Alın

**Kanıt:** RFC (Response for a Class) 11.24'ten 17.25'e, MPC (Message Passing Coupling) ise 8.67'den 16.85'e (%94 artış) çıkmıştır.

**Öneri:** Sınıfların dışarıya mesaj gönderme sayısını sınırlandırmak için **Façade** veya **Mediator** deseni değerlendirin. MPC'nin ikiye katlanması, sınıfların giderek daha fazla koordinasyon sorumluluğu üstlendiğini göstermektedir; bu sorumluluk merkezi bir koordinatör sınıfa devredilmelidir.

### 4.5 WMC'yi Kısıtlamak için Metot Düzeyinde SRP Denetimi

**Kanıt:** WMC 10.36'dan 16.27'ye çıkmış, 1.5.x'te 15.78'de stabilize olmuştur. Stabilizasyon olumlu olmakla birlikte mevcut seviye yüksektir.

**Öneri:** Yeni geliştirme kuralı olarak sınıf başına maksimum WMC eşiği (örn. 20) belirleyin ve CI sürecine statik analiz entegre edin. Eşiği aşan sınıflar için extract method / extract class refactoring uygulanmasını zorunlu tutun.

---

## 5. Mimari Kalite Yorumu: Mimari Erozyon Var mı?

### 5.1 Büyüme ile Gelen Bozulmalar

DSC 238'den 618'e (%160) artarken:

- ANA: 0.618 → 0.320 (−%48) — soyutlama oranı düşmüş
- CAM: 0.407 → 0.366 (−%10) — iç uyum zayıflamış
- Extendibility: 0.894 → 0.492 (−%45) — genişletilebilirlik ciddi ölçüde kötüleşmiş
- LCOM: 13.76 → 31.24 (+%127) — iç uyumsuzluk artmış

Bu eğilimler birlikte değerlendirildiğinde, kütüphanenin büyüdükçe **mimarisinin özgün soyutlama yapısını kaybettiğine** işaret eden anlamlı sinyaller mevcuttur. Yeni sınıflar çoğunlukla somut ve yüksek bağlaşımlı eklenmiş; soyut katman bunlara yetişememiştir.

### 5.2 Kritik Geçiş Noktası: 1.1.0 ve 1.2.0

0.9.0–1.0.1 arasında büyüme düzenli ve görece az bozulumlu ilerlemektedir. Ancak **1.1.0 ile birlikte** LCOM 24.70'e (önceki 11.83'ten) sıçramış, DCC 2.87'ye yükselmiş ve Extendibility 0.69'a gerilemiştir. **1.2.0'da** ANA 0.386'ya düşmüştür (bir önceki sürümde 0.576). Bu iki sürüm, mimari yönde bir köşe dönümünü simgelemektedir.

### 5.3 Dengeleyici Faktörler

Tam anlamıyla bir mimari çöküş (architectural collapse) yaşandığı söylenemez; zira:

- **DAM (kapsülleme)** neredeyse yüksek kalmaktadır (0.899 → 0.885); alanlar hâlâ büyük ölçüde gizlenmektedir.
- **Effectiveness** neredeyse sabit seyretmiştir (1.082 → 1.121, normalize: +%1.4); temel polimorfizm, soyutlama ve kapsüllemenin birleşik etkisi korunmuştur.
- **MOA (kompozisyon)** 0.374'ten 0.701'e yükselmiştir; kalıtım yerine kompozisyon yönelimi artmıştır, bu iyi bir tasarım kararıdır.

### 5.4 Genel Mimari Yargı

Veriler, **kısmi mimari erozyon** tanısını desteklemektedir. Kütüphane işlevsel ve yeniden kullanılabilir olmaya devam etmektedir; ancak soyutlama katmanının nispi küçülmesi, LCOM artışı ve bağlaşım yoğunlaşması, büyüme stratejisinin uzun vadede tasarım kısıtlarına yol açabileceğine işaret etmektedir. Yapılacak refactoring çalışmaları öncelikli olarak 4.1 ve 4.2 numaralı önerilere (LCOM ayrıştırması ve soyutlama güçlendirme) yoğunlaşmalıdır.

---

## Ek: Temel Metrik Zaman Serileri (Özet)

| Sürüm | DCC | LCOM | ANA | MOA | Extendibility |
|---|---|---|---|---|---|
| 0.9.0 | 2.35 | 13.76 | 0.618 | 0.374 | 0.894 |
| 1.0.0 | 2.47 | 12.82 | 0.640 | 0.453 | 0.774 |
| 1.1.0 | 2.87 | 24.70 | 0.576 | 0.461 | 0.697 |
| 1.2.0 | 2.79 | 30.80 | 0.386 | 0.542 | 0.740 |
| 1.3.1 | 2.91 | 27.77 | 0.352 | 0.652 | 0.595 |
| 1.5.3 | 3.03 | 31.24 | 0.320 | 0.701 | 0.492 |

---

*Rapor, QMOOD çerçevesine ve sağlanan ham verilere dayanılarak hazırlanmıştır. Yorumlar olasılıksal niteliktedir; sınıf düzeyinde detay analizi yapılmadan kesin tanı konulamaz.*
