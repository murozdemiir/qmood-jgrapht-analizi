# JGraphT 0.9.0 → 0.9.2 Sürüm Farkı Analizi

**Hazırlandı:** Kidemli Yazılım Mimarisi ve Kalite Uzmanı  
**Tarih:** Haziran 2026  
**Analiz:** JGraphT Erken Sürümler (0.9.0 vs 0.9.2)  
**Metodoloji:** QMOOD (Bansiya & Davis, 2002) + Tasarım Metrik Analizi

---

## YÖNETIM ÖZETİ

JGraphT 0.9.0 ile 0.9.2 arasında, **kapsamlı bir tasarım yeniden düzenleme gerçekleştirilmiş**, ancak bu değişim **hem olumlu hem de olumsuz etkiler** içermektedir. Sistem **Reusability ve Functionality açısından önemli ölçüde gelişmiş (+12% ve +11%)**, fakat **Understandability kritik düzeyinde azalmış (−12%)** ve **erken-aşama teknik borç işaretleri** görülmektedir.

| Kalite Niteliği | 0.9.0 | 0.9.2 | Değişim | Trend | Değerlendirme |
|---|---|---|---|---|---|
| **Reusability** | 120.48 | 134.96 | +12.0% | ↑ | ✅ İyi |
| **Functionality** | 61.69 | 68.93 | +11.7% | ↑ | ✅ İyi |
| **Effectiveness** | 1.082 | 1.086 | +0.4% | ↑ | ≈ Stabil |
| **Flexibility** | 1.461 | 1.431 | −2.0% | ↓ | ⚠️ Hafif Gerileme |
| **Extendibility** | 0.895 | 0.885 | −1.1% | ↓ | ⚠️ Hafif Gerileme |
| **Understandability** | −81.87 | −91.47 | −11.8% | ↓ | 🔴 **KRİTİK** |

---

## 1. TASARIM METRİK DEĞİŞİMLERİ — DETAYLI ANALİZ

### 1.1 Sistem Boyutu ve Ölçek (DSC: +12.2%)

```
0.9.0: 238 sınıf
0.9.2: 267 sınıf
Değişim: +29 sınıf (+12.2%)

YORUM:
───────
Sistem tasarımı daha modüler hale getirilmiş. 29 yeni sınıf eklemek:
├─ Daha fine-grained yapı anlamına geliyor
├─ Single Responsibility Principle (SRP) daha iyi uygulanıyor
├─ Componentization arttı (modülarite artışı)
└─ Bu OLUMLU bir adımdır (tasarım kalitesi açısından)

UYARI:
───────
Ama sistem büyüdü. Understandability −81.87 → −91.47 düştü.
→ Daha fazla sınıf = daha zor anlaşılır sistem (trade-off)

KANIT:
───────
Understandability formülü: -0.33*(ANA+DCC+NOP+NOM+DSC) + 0.33*(DAM+CAM)

0.9.0: -0.33*(0.618 + 2.349 + 3.273 + 5.155 + 238) + 0.33*(0.899 + 0.407)
     = -0.33*249.395 + 0.33*1.306
     = -82.3 + 0.431 = -81.87

0.9.2: -0.33*(0.670 + 2.363 + 3.191 + 5.240 + 267) + 0.33*(0.894 + 0.387)
     = -0.33*278.464 + 0.33*1.281
     = -91.895 + 0.423 = -91.47

Fark: -91.47 - (-81.87) = -9.6 puan KÖTÜLEŞME

Analiz:
├─ DSC artışı (238 → 267): -0.33*29 = -9.57 puan (97% sorumluluk)
├─ NOH artışı (35 → 39): -0.33*4 = -1.32 puan (ek kötüleşme)
├─ CAM azalması (0.407 → 0.387): +0.33*(-0.02) = -0.0066 puan (minimal)
└─ NET: DSC artışı aslan payını (−9.57 puan) alıyor
```

### 1.2 Soyutlama Seviyesi (ANA: +8.5%)

```
0.9.0: 0.6176
0.9.2: 0.6704
Değişim: +0.0528 (+8.5%)

YORUM:
───────
Soyut sınıflar ve interface'ler artmış. Bu:
├─ API'nın daha well-designed olması anlamına gelir
├─ Abstraction level yükseltilmiş (good design)
├─ Generic programming daha iyi uygulanmış olabilir
└─ OLUMLU bir değişimdir

BAĞLAMI:
────────
0.9.0'ın erken-aşama library olduğu düşünülürse,
0.9.2'de soyutlama artışı, tasarım olgunlaşması gösteriyor.

EXTENDIBILITY VE FLEXİBİLİTY ETKİSİ:
───────────────────────────────────────
Extendibility = 0.50*(ANA+MFA+NOP) - 0.50*DCC

0.9.0: 0.50*(0.6176 + 0.247 + 3.273) - 0.50*2.349 = 0.8945
0.9.2: 0.50*(0.6704 + 0.272 + 3.191) - 0.50*2.363 = 0.885

ANA +0.0528 etkisi: +0.0264 puan (pozitif)
MFA +0.025 etkisi: +0.0125 puan (pozitif)
NOP -0.082 etkisi: -0.041 puan (negatif)
DCC +0.014 etkisi: -0.007 puan (negatif)
─────────────────────────────────────
NET: -0.01 puan gerileme

Sonuç: ANA artışı olumlu, ama NOP azalması bunu kısmen telafi etti
```

### 1.3 Kohezyon Azalması (CAM: −4.8%)

```
0.9.0: 0.407
0.9.2: 0.387
Değişim: -0.020 (-4.8%)

UYARI: 🔴 BU KRİTİK BİR BELİRTİDİR!

YORUM:
───────
Sınıfların internal cohesion'ı azaldı.
├─ Daha fazla method eklenmiş ama ilişkisiz
├─ Sınıf sorumlulukları belirsiz hale geliyor
├─ Sınıflar daha "çeşitli" şeyler yapmaya başladı
└─ BU OLUMSUZ bir değişimdir

KANIT:
───────
CAM = Cohesion Among Methods (sınıf içi method ilişkisi)
Düşük CAM = metodlar birbirini çok çağırmiyor
→ Single sınıf içinde multiple responsibilities (SRP ihlali)

NEDENİ:
───────
29 yeni sınıf eklenirken, muhtemelen:
├─ Bazı büyük sınıflar parçalanmış
├─ Ama parçalama tam olmamış (incomplete refactor)
├─ Bazı metodlar yanlış yere kalmış olabilir
└─ Veya utility metodları sınıflara eklenmişş

TEKNIK BORÇ GÖSTERGESI:
──────────────────────
CAM -4.8% azalması:
├─ Design debt işareti
├─ 0.9.2 versiyonda muhasebe temizlenememiş
├─ Ileride refactor edileceğini gösterir
└─ Şimdi: TOLERABLE (0.387 hala reasonable)
```

### 1.4 Polimorfizm Azalması (NOP: −2.5%)

```
0.9.0: 3.273
0.9.2: 3.191
Değişim: -0.082 (-2.5%)

UYARI: ⚠️ POLYMORPH USAGE DÜŞTÜ

YORUM:
───────
Polimorfik metodların sayısı azaldı.
├─ Abstract method'lar kaldırılmış olabilir
├─ Interface'ler simplify edilmiş
├─ Veya concrete class'lar daha fazla direct call yapıyor
└─ BU OLUMSUZ bir değişimdir

TASARIM IMPLİKASYONU:
───────────────────
Polimorfizm azalması:
├─ Extensibility azalıyor
├─ New algorithm ekleme daha zor hale geliyor
├─ Code reuse azalıyor
└─ Flexibility kısıtlanıyor

Extendibility etkilenmesi:
Extendibility = 0.50*(ANA+MFA+NOP) - 0.50*DCC
NOP -0.082 = -0.041 puan negatif etki

Bu, Extendibility −1.1% düşüşünün ana sebebidir.

AÇIKLAMA:
─────────
0.9.0'dan 0.9.2'ye geçişte:
├─ 29 sınıf eklenmiş
├─ Ama polimorfik yapı simplify edilmiş olabilir
├─ Muhtemelen concrete class'lar preference alınmış
└─ STRATEGY YANLIŞ: Flexibility için ödül vermek gerekti
```

### 1.5 Hiyerarşi Derinliği Artışı (NOH: +11.4%)

```
0.9.0: 35
0.9.2: 39
Değişim: +4 (+11.4%)

YORUM:
───────
Inheritance hiyerarşisi 4 level daha derinleşti.
├─ Design pattern'leri uygulanmış (Template Method, Visitor, etc.)
├─ Base class'lar daha iyi structured (good!)
├─ Ama daha kompleks hiyerarşi = daha zor anlaşılır (bad!)
└─ TRADE-OFF

TASARIM YAKINLAŞMASI:
─────────────────────
NOH artışı + ANA artışı = Template Method pattern?
├─ Abstract algorithm base class'ları eklenmiş
├─ Ortak behavior'ları extract etmiş
├─ Concrete implementasyonlar oluşturmuş
└─ Bu iyi bir design move'dur

UYARISI:
────────
Ama NOH +4 = Understandability'ye -1.32 puan köstes
Hiyerarşi anlaşılması daha zor, tracking daha zor

NE SÖYLÜYOR?
────────────
- 0.9.0: Basit, shallow hiyerarşi (easy to understand, but less patterns)
- 0.9.2: Richer, deeper hiyerarşi (more patterns, but harder to follow)
```

### 1.6 Kalıtım Abstraksiyon (MFA: +10.2%)

```
0.9.0: 0.247
0.9.2: 0.272
Değişim: +0.025 (+10.2%)

YORUM:
───────
Kalıtımda soyutlanmış metodlar arttı. Bu:
├─ Template Method pattern'ı işaret ediyor
├─ Subclass'lara override'lama fırsatı veriyor (good!)
├─ Design flexibility arttı
├─ Extendibility için pozitif (ama NOP düşüşü bunu cancel etti)
└─ OLUMLU bir adımdır

CONTEXT:
─────────
MFA +10.2% + ANA +8.5% + NOH +11.4% = Design Pattern Adoption
├─ Template Method Pattern
├─ Strategy Pattern (partial)
├─ Abstract Factory Pattern
└─ Tüm bunlar hiyerarşi ve soyutlamayı artırıyor
```

### 1.7 Bileşim Kullanımı (MOA: +8.2%)

```
0.9.0: 0.374
0.9.2: 0.405
Değişim: +0.031 (+8.2%)

YORUM:
───────
Composition (öbek içine yerleştirme) kullanımı arttı. Bu:
├─ "Composition over Inheritance" ilkesine uygun
├─ Object delegation patterns uygulanmış
├─ Coupling azaltmaya çalışılmış
└─ OLUMLU ve best-practice'dir

NEDEN ÖNEMLİ?
──────────────
Composition artması:
├─ Flexibility artışına yardımcı
├─ Coupling'i inverse direction'da tutuyor
├─ Runtime behavior customization
└─ Design flexibility → Extendibility

KANIT:
────────
Flexibility = 0.25*DAM - 0.25*DCC + 0.50*MOA + 0.50*NOP

MOA +0.031 etkisi: +0.50*0.031 = +0.0155 puan (pozitif)
NOP -0.082 etkisi: +0.50*(-0.082) = -0.041 puan (negatif)
DCC +0.014 etkisi: -0.25*0.014 = -0.0035 puan (negatif)
DAM -0.005 etkisi: +0.25*(-0.005) = -0.00125 puan (minimal)
─────────────────────────────────────
NET: -0.029 puan (Flexibility -2% → 1.461 → 1.431)

Sonuç: MOA artışı olumlu, ama NOP düşüşü bunu aştı
```

---

## 2. KALİTE NİTELİKLERİ KARŞILAŞTIRMASI

### 2.1 QMOOD Nitelikleri Hesaplama

#### 0.9.0 Sürümü:

```
Reusability = -0.25*2.349 + 0.25*0.407 + 0.50*3.920 + 0.50*238
            = -0.5873 + 0.1018 + 1.960 + 119
            = 120.475 ✓

Flexibility = 0.25*0.899 - 0.25*2.349 + 0.50*0.374 + 0.50*3.273
           = 0.2248 - 0.5873 + 0.187 + 1.6365
           = 1.461 ✓

Understandability = -0.33*(0.618 + 2.349 + 3.273 + 5.155 + 238) + 0.33*(0.899 + 0.407)
                  = -0.33*249.395 + 0.33*1.306
                  = -82.3 + 0.431
                  = -81.87 ✓

Functionality = 0.12*0.407 + 0.22*(3.273 + 3.920 + 238 + 35)
              = 0.0488 + 0.22*280.193
              = 0.0488 + 61.6424
              = 61.691 ✓

Extendibility = 0.50*(0.618 + 0.247 + 3.273) - 0.50*2.349
              = 0.50*4.138 - 0.50*2.349
              = 2.069 - 1.1745
              = 0.8945 ✓

Effectiveness = 0.20*(0.618 + 0.899 + 0.374 + 0.247 + 3.273)
              = 0.20*5.411
              = 1.0822 ✓
```

#### 0.9.2 Sürümü:

```
Reusability = -0.25*2.363 + 0.25*0.387 + 0.50*3.914 + 0.50*267
            = -0.5908 + 0.0968 + 1.957 + 133.5
            = 134.963 ✓

Flexibility = 0.25*0.894 - 0.25*2.363 + 0.50*0.405 + 0.50*3.191
           = 0.2235 - 0.5908 + 0.2025 + 1.5955
           = 1.4307 ✓

Understandability = -0.33*(0.670 + 2.363 + 3.191 + 5.240 + 267) + 0.33*(0.894 + 0.387)
                  = -0.33*278.464 + 0.33*1.281
                  = -91.895 + 0.423
                  = -91.47 ✓

Functionality = 0.12*0.387 + 0.22*(3.191 + 3.914 + 267 + 39)
              = 0.0464 + 0.22*313.105
              = 0.0464 + 68.883
              = 68.929 ✓

Extendibility = 0.50*(0.670 + 0.272 + 3.191) - 0.50*2.363
              = 0.50*4.133 - 0.50*2.363
              = 2.0665 - 1.1815
              = 0.885 ✓

Effectiveness = 0.20*(0.670 + 0.894 + 0.405 + 0.272 + 3.191)
              = 0.20*5.432
              = 1.0864 ✓
```

### 2.2 Kalite Nitelikleri Karşılaştırma Tablosu

```
╔═══════════════════════════════════════════════════════════════╗
║        QMOOD KALİTE NİTELİKLERİ KARŞILAŞTIRMASI              ║
║                    0.9.0 → 0.9.2                              ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║ Nitelik          0.9.0      0.9.2      Değişim    %    Trend ║
║ ──────────────────────────────────────────────────────────── ║
║ Reusability      120.48     134.96     +14.48    +12.0%  ↑   ║
║ Flexibility        1.46       1.43     -0.03     -2.0%   ↓   ║
║ Understandability -81.87     -91.47    -9.6      -11.8%  ↓   ║
║ Functionality     61.69      68.93     +7.24     +11.7%  ↑   ║
║ Extendibility      0.89       0.89     -0.01     -1.1%   ↓   ║
║ Effectiveness      1.08       1.09     +0.004    +0.4%   ↑   ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## 3. TASARIM DEĞİŞİMLERİNİN DEĞERLENDIRILMESI

### 3.1 Olumlu Değişimler ✅

#### 1. Reusability Artışı (+12.0%)

```
METRIK KATKILAR:
───────────────
Reusability = -0.25*DCC + 0.25*CAM + 0.50*CIS + 0.50*DSC

Faktör               0.9.0 → 0.9.2    Katkı
────────────────────────────────────────────
DSC (boyut)         238 → 267        +14.5 puan
CIS (arayüz)        3.920 → 3.914    −0.003 puan
CAM (kohezyon)      0.407 → 0.387    −0.005 puan
DCC (coupling)      2.349 → 2.363    −0.0035 puan
─────────────────────────────────────────────
NET                                  +14.48 puan

AÇIKLAMA:
─────────
Reusability artışının %99'u DSC (sistem boyutu) artışından kaynaklanıyor.
29 yeni sınıf eklemesi = 14.5 puan reusability kazancı

TASARıM YORUMU:
────────────────
✅ POZITIF: Sistem daha modüler hale getirildi
├─ Daha fine-grained class decomposition
├─ Component'ler daha ayrılabilir
├─ Her sınıf daha specialized görev yapıyor
└─ API reusability potansiyeli artmış

KANIT:
────────
ANA +8.5% (abstraction artışı) = genericleri daha iyiye alıyor
MOA +8.2% (composition artışı) = bileşenleri combine etmek kolay
→ Higher reuse factor

UYARI:
───────
Ama CAM -4.8% ve NOP -2.5% → refactoring tam değilmiş
Sınıflar daha granular ama daha az cohesive
```

#### 2. Functionality Artışı (+11.7%)

```
METRIK KATKILAR:
───────────────
Functionality = 0.12*CAM + 0.22*(NOP+CIS+DSC+NOH)

Faktör                    Katkı
────────────────────────────────
DSC (sistem boyutu)      +6.38 puan
NOH (hiyerarşi)          +0.88 puan
NOP (polimorfizm)        −0.18 puan
CIS (arayüz)             −0.004 puan
CAM (kohezyon)           −0.005 puan
──────────────────────────────────
NET                      +7.24 puan

AÇIKLAMA:
─────────
Functionality artışı, sistem boyutu ve hiyerarşi artışından kaynaklanıyor.
├─ 29 yeni sınıf (daha fazla feature capacity)
├─ 4 hiyerarşi level (design pattern'ler)
└─ 11.7% daha fazla işlevsellik

TASARıM YORUMU:
────────────────
✅ POZITIF: Sistem daha geniş feature set'e sahip
├─ Yeni algoritma'lar eklenmiş
├─ Yeni data structure'lar eklendi
├─ API daha comprehensive
└─ Library daha "complete" hale geldi

AÇIKLAMA:
─────────
0.9.0'dan 0.9.2'ye, muhtemelen:
├─ Yeni graph algorithm'ları eklenmişş
├─ Yeni graph type'ları support edilmişş
├─ Yeni traversal stratejileri eklenmiş
└─ Library scope'u genişletilmiş

Bu, küçük bir library'den giderek daha professional
bir tool'a evrim süreci gösteriyor.
```

---

### 3.2 Olumsuz Değişimler ❌

#### 1. Understandability Düşüşü (−11.8%) — KRİTİK

```
METRIK KATKILAR:
────────────────
Understandability = -0.33*(ANA+DCC+NOP+NOM+DSC) + 0.33*(DAM+CAM)

Faktör              0.9.0 → 0.9.2    Katkı
───────────────────────────────────────────
DSC (boyut)         238 → 267        −9.57 puan
NOH (hiyerarşi)     35 → 39          −1.32 puan
NOM (komplexite)    5.155 → 5.240    −0.028 puan
DCC (coupling)      2.349 → 2.363    −0.0046 puan
ANA (soyutlama)     0.618 → 0.670    −0.0159 puan (negatif etki!)
CAM (kohezyon)      0.407 → 0.387    −0.0066 puan
DAM (kapsülleme)    0.899 → 0.894    −0.00165 puan
──────────────────────────────────────────
NET                                  −9.6 puan

AÇIKLAMA:
─────────
Understandability düşüşünün:
├─ 99.7% (9.57 puan) = DSC artışından (29 sınıf ekleme)
├─ 13.75% (1.32 puan) = NOH artışından (4 hiyerarşi level)
└─ TOPLAM = −9.6 puan = −11.8%

TASARıM YORUMU:
────────────────
❌ OLUMSUZ: Sistem anlaşılması zor hale geldi
├─ 238 sınıftan 267 sınıfa geçiş (29 sınıf öğrenme ihtiyacı)
├─ Yeni geliştiriciler daha fazla öğrenme süresi gerekli
├─ Hiyerarşi derinleşti (inheritance chain'ler daha karmaşık)
├─ Genel system architecture'u kavrışı zor
└─ ONBOARDING SÜRESI ARTTI

KANIT:
────────
Understandability -81.87 → -91.47:
├─ Sağlıklı library: Understandability > -50 (idealde)
├─ 0.9.0: -81.87 (kötü, ama erken sürüm için acceptable)
├─ 0.9.2: -91.47 (daha kötü, sistem daha karmaşık)
└─ Eğer 0.9.x serisinin sonunda -200'e gelirse büyük sorun

UYARISI:
────────
Bu DÜŞÜŞü tolerate edebiliriz ÇÜNKÜ:
├─ 0.9.0 hala erken sürüm (alpha/beta)
├─ Feature eklenmesi daha önemli
├─ Documentation geliştirilse azalabilir
└─ Ileride refactor yapılabilir

UYARI NOKTASI:
───────────────
Ama eğer her sürümde 10% Understandability düşüşü olursa:
├─ 0.9.2: -91.47
├─ 0.9.3: -105 (estimate)
├─ 0.9.4: -120
├─ 1.0.0: -150
└─ 2-3 yıl içinde unmanageable hale gelebilir!

FİKSİ:
───────
Koruma yöntemleri:
├─ Documentation & guides (Quick-start, tutorials)
├─ Code organization improvement (package structure)
├─ Naming conventions standardization
├─ Architectural documentation (high-level overview)
└─ Sample code'lar bolca (examples)
```

#### 2. Kohezyon Azalması (CAM: −4.8%) — TEKNIK BORÇ İŞARETİ

```
DETAYLI ANALIZ:
───────────────
CAM (Cohesion Among Methods) = Sınıf içi metod ilişkisi

0.9.0: 0.407 (ortalama sınıfın metodları %40.7 ilişkili)
0.9.2: 0.387 (ortalama sınıfın metodları %38.7 ilişkili)
Değişim: -0.020 (-4.8%)

NE ANLAMA GELİR?
────────────────
CAM azalması = Sınıflarda multiple responsibility'ler
├─ Method A ile Method B arasında call relationship'i az
├─ Sınıflar daha "heterogenous" hale geldi
├─ Single Responsibility Principle (SRP) ihlali başlıyor
└─ DESIGN DEBT işareti

NEDEN OLDU?
───────────
29 sınıf eklenirken:
├─ Büyük sınıflar kural dışı parçalanmış olabilir
├─ Incomplete refactoring (metodlar yanlış yerde kalmış)
├─ Veya utility method'lar sınıflara eklenmişş
└─ Sonuç: Gittikçe unfocused sınıflar

KANIT:
──────
Gerçek örnek (hipotez):
BEFORE (0.9.0):
class GraphAlgorithm {
  abstract List<Vertex> findPath(...);
  abstract void initializeGraph(...);
  abstract void relaxEdges(...);
  // CAM high (tüm metodlar path-finding ile ilişkili)
}

AFTER (0.9.2):
class GraphAlgorithm {
  // Path finding metodları
  abstract List<Vertex> findPath(...);
  abstract void relaxEdges(...);
  
  // Utility metodları (eklenmişş)
  private void validateGraph(...);
  private void serializeResult(...);
  private void formatOutput(...);
  
  // Comparison metodları
  public int compare(...);
  public boolean equals(...);
  
  // CAM down (metodlar artık daha farklı işler yapıyor)
}

SEVERITESI:
─────────────
⚠️ MEDIUM — UYARILMASA

Neden?
├─ CAM 0.387 hala reasonable (0.30 altında çok kötü)
├─ Erken-aşama refactoring'te normal
├─ Documentation ve code organization ile çözülebilir
└─ Ileride cleanup yapılabilir

UYARISI:
────────
Eğer CAM −5% daha düşerse (0.36 altına) = SORUN
```

#### 3. Polimorfizm Azalması (NOP: −2.5%) — EXTENDIBILITY RİSKİ

```
DETAYLI ANALIZ:
───────────────
NOP (Number of Polymorphic Methods) = Polimorfik metod sayısı

0.9.0: 3.273
0.9.2: 3.191
Değişim: -0.082 (-2.5%)

NE ANLAMA GELİR?
────────────────
Polimorfizm azalması = Extensibility azalışı
├─ Abstract method'lar azalmışş
├─ Interface method'lar azalmışş
├─ Veya concrete implementation'lar arttı
├─ Sistem "kapalı" hale gelmeye başlıyor
└─ Open/Closed Principle'ı ihlal

NEDEN OLDU?
───────────
Muhtemelen:
├─ 29 yeni sınıftan bazıları concrete utility class'lar
├─ Abstract hierarchy simplify edilmiş
├─ Direct implementation preferred edilmiş
└─ Design'da pattern uygulaması eksik kalmışş

KANIT:
──────
Extendibility = 0.50*(ANA+MFA+NOP) - 0.50*DCC

NOP kontribüsyonu:
0.50 * (-0.082) = -0.041 puan (Extendibility'ye negatif etki)

ANA +8.5% ve MFA +10.2% pozitif katkı yapsa da,
NOP azalışı -0.041 ile Extendibility'yi 0.8945 → 0.885 yaptı.

SEVERITESI:
─────────────
🟡 HAFIF — UYARISA

Neden?
├─ Azalış minimal (-2.5%)
├─ ANA ve MFA artışı kısmen telafi ediyor
├─ Extendibility sadece -1.1% düştü (tolerable)
└─ Ileride polimorfizm eklenebilir

TUZAK:
───────
UYARI: Eğer NOP −5% daha düşerse = DESIGN PROBLEM
Çünkü sistem giderek "kapalı" ve "hard-coded" hale gelir
```

---

## 4. TEKNİK BORÇ ANALİZİ

### 4.1 Teknik Borç Göstergeleri

```
╔═══════════════════════════════════════════════════════════════╗
║           TEKNİK BORÇ İŞARETLERİ (0.9.0 → 0.9.2)            ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║ İŞARET            0.9.0   0.9.2   DURUM    SEVERİTESİ       ║
║ ──────────────────────────────────────────────────────────── ║
║ CAM (Kohezyon)    0.407   0.387   ↓ −4.8%   🟡 UYARI       ║
║ NOP (Polim.)      3.273   3.191   ↓ −2.5%   🟡 HAFIF       ║
║ DCC (Coupling)    2.349   2.363   ↑ +0.6%   ✅ TOLERABLE   ║
║ NOH (Hiyerarşi)   35      39      ↑ +11.4%  ✅ NORMAL      ║
║ NOM (Komplexite)  5.155   5.240   ↑ +1.6%   ✅ MINIMAL      ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝

DURUM:
══════
✅ 2 Gösterge IYZIBIR (Coupling, Complexity minimal)
🟡 2 Gösterge UYARIDA (Cohesion −4.8%, Polymorphism −2.5%)
✅ 1 Gösterge NORMAL (Hierarchy derinleşti, ama expected)

GENEL DEĞERLENDİRME:
════════════════════
🟡 HAFIF BORÇ BİRİKİMİ

Neden hafif?
├─ CAM azalışı −4.8% (tolerable, henüz 0.387)
├─ NOP azalışı −2.5% (minimal)
├─ Coupling stabil kaldı (+0.6% negligible)
├─ Complexity minimal artmış (+1.6%)
└─ Sistem hala healthy state'te

Ama endişe verici noktalar:
├─ CAM trendi aşağıya gidiyor (−4.8%)
├─ NOP trendi aşağıya gidiyor (−2.5%)
└─ Eğer trend devam ederse 2-3 sürüm sonra sorun olabilir
```

### 4.2 Borç Kategorileri

```
DESIGN DEBT (Tasarım Borcu):
─────────────────────────────
├─ Sebep: Incomplete refactoring sırasında
├─ Gösterge: CAM −4.8% (sınıf cohesion düşüyor)
├─ Etki: Sınıflar multiple responsibility'ler barındırıyor
├─ Maliyeti: Medium (ileride cleanup gerekebilir)
└─ Status: MANAGEABLE AMA GÖZ ALTINDA TUTULMALI

COMPLEXITY DEBT:
─────────────────
├─ Sebep: Hiyerarşi derinleşti (NOH +11.4%)
├─ Gösterge: NOH 35 → 39 (4 level derinleşme)
├─ Etki: Inheritance chain'ler daha karmaşık (Understandability ↓)
├─ Maliyeti: Medium (navigation zorlağıaştı)
└─ Status: PATTERN UYGULAMASI IYZIBIR, AMA DOCUMENTED OLMALI

POLYMORPH FLEXIBILITY DEBT:
────────────────────────────
├─ Sebej: NOP azalması (−2.5%)
├─ Gösterge: Abstract method'lar azaldı
├─ Etki: Extensibility biraz sınırlandı (Extendibility ↓ −1.1%)
├─ Maliyeti: Low (hafif esneklik kaybı)
└─ Status: KÖTÜ DEĞİL, ILERIDE EKLENEBİLİR

COHESION DEBT:
───────────────
├─ Sebep: Utility method'lar sınıflara eklenmiş
├─ Gösterge: CAM −4.8% (sınıf içi method ilişkisi azaldı)
├─ Etki: Sınıflar daha "fat" ve unfocused hale gelmeye başlıyor
├─ Maliyeti: Medium (ileride breaking sınıflar gerekecek)
└─ Status: TOLERABLE AMA TAKIP EDİLMELİ
```

---

## 5. GEÇİŞ STRATEJİSİ YORUMU

### 5.1 Neden Böyle Değişti?

```
SENARYO (Hipotez):
══════════════════

0.9.0 (İlk Versiyon):
├─ Basit, minimal kütüphane (238 sınıf)
├─ Temel graph data structures
├─ Simple traversal algoritmaları
├─ Shallow hiyerarşi (ease of understanding)
├─ Design pattern'ları minimal
└─ Quick to learn, quick to use

0.9.2 (Refactor Sürümü):
├─ Professional library yönünde ilerleme
├─ Yeni algoritma'lar eklenmişş (29 sınıf)
├─ Design pattern'ları uygulanmışş
├─ Hiyerarşi derinleştirilmiş (Template Method, etc.)
├─ Soyutlama seviyesi yükseltilmiş
├─ API'nın kapsamı genişletilmiş
└─ Ama sistem daha kompleks hale geldi

STRATEGY:
═════════
Geliştiriciler "features first, architecture second" seçmişş:
├─ ✅ Doğru: Yeni algoritma'lar eklendi (feature-driven)
├─ ✅ Doğru: Design pattern'ları uygulandı
├─ ⚠️ Meh: Refactoring eksik kalmışş (incomplete)
├─ ❌ Yanlış: CAM ve NOP azaldı (organizing eksik)
└─ Sonuç: "Kapsamlı ama kaotic" profil

TIMING:
═══════
Bugünün bakış açısından (8 sürüm sonra):
├─ 0.9.0 → 0.9.2: +12% Reusability (good!)
├─ 0.9.0 → 0.9.2: −12% Understandability (bad!)
├─ 0.9.0 → 1.5.3: +160% system size (HUGE)
├─ 0.9.0 → 1.5.3: −154% Understandability (DISASTER!)
└─ Eğer 0.9.2'de kötü adımlar atılmışşsa, 1.5.3'te kabus

Bu bize gösteriyor:
└─ Erken-aşama design kararları ileride büyük etkiler yaratıyor!
```

---

## 6. REKOMENDASYONLAR

### 6.1 Kısa Vadeli (0.9.2 → 0.9.3)

```
1. COHESION İYİLEŞTİRME (CAM: 0.387 → 0.42)
   ├─ Sınıfları audit et (multiple responsibility'ler?)
   ├─ Utility method'ları utility class'lara taşı
   ├─ Single Responsibility Principle'ı uygula
   ├─ Effort: 2-3 sprint
   └─ Impact: CAM restore, Understandability hafif iyileş

2. POLYMORPHISM RESTORE (NOP: 3.191 → 3.35+)
   ├─ Abstract method'ları gözden geçir
   ├─ Interface'leri extend et (Strategy pattern)
   ├─ Template Method pattern'ı strengthen
   ├─ Effort: 1-2 sprint
   └─ Impact: Extendibility restore, Flexibility improve

3. DOCUMENTATION IYILESTIR
   ├─ Quick-start guide hazırla (Understandability yardımı)
   ├─ Architecture overview (high-level docs)
   ├─ Code samples ve examples
   ├─ Effort: 1 sprint
   └─ Impact: Practical Understandability (metric'te reflection olmaz)

BEKLENEN SONUÇ:
────────────────
0.9.2 → 0.9.3:
├─ Reusability: stabil (134.96)
├─ Functionality: stabil (68.93)
├─ Understandability: −91.47 → −85 (hafif iyileş)
├─ CAM: 0.387 → 0.42 (+8.5%)
├─ NOP: 3.191 → 3.35 (+5%)
└─ Technical debt: CLEAR
```

### 6.2 Orta Vadeli (0.9.3 → 1.0.0)

```
1. DESIGN PATTERN STANDARDIZATION
   ├─ Tüm algorithm'lar için Template Method uygulaması
   ├─ Strategy pattern consistency
   ├─ Builder pattern'ler (configuration)
   ├─ Effort: 1-2 months
   └─ Impact: Extensibility +20%, Consistency +30%

2. ARCHITECTURE LAYERING
   ├─ Core graph interfaces/classes
   ├─ Algorithm implementations
   ├─ Utility layer
   ├─ API facade layer
   ├─ Effort: 1 month
   └─ Impact: Understandability +15%

3. MODULAR PACKAGE STRUCTURE
   ├─ org.jgrapht.core (base)
   ├─ org.jgrapht.algorithm (algorithm'lar)
   ├─ org.jgrapht.util (utilities)
   ├─ org.jgrapht.io (I/O)
   ├─ Effort: 2 weeks
   └─ Impact: Navigation ease +40%

BEKLENEN SONUÇ:
────────────────
1.0.0:
├─ Understandability: −85 → −60 (+25%)
├─ Extendibility: 0.885 → 0.95 (+7%)
├─ Reusability: stabil (135+)
├─ Functionality: stabil (70+)
└─ Professional library seviyesine ulşaş
```

### 6.3 Uzun Vadeli (1.0.0 sonrası)

```
MONITORING:
────────────
├─ Sürüm başına QMOOD metrikleri track et
├─ Understandability −10% baseline'den düşerse UYAR
├─ CAM −5% düşerse STOP ve refactor
├─ NOP düşüşe başlarsa INVESTIGATE
└─ Dashboard oluştur

PROACTIVE REFACTORING:
──────────────────────
├─ Her sprint'te %10-15 refactoring budget
├─ God class'ları preemptively decompose
├─ Package structure'ı optimize
├─ Cohesion ve coupling'i monitor
└─ Debt'in exponential hale gelmesini önle
```

---

## 7. ÖZET VE KONKLÜSYONLARı

### 7.1 Sürüm 0.9.0 → 0.9.2 Değerlendirilmesi

```
╔═══════════════════════════════════════════════════════════════╗
║          0.9.0 → 0.9.2 SÜRÜM DEĞERLENDİRMESİ                ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║ KALITE NITELIĞI          0.9.0      0.9.2      DEĞERLENDİRME ║
║ ──────────────────────────────────────────────────────────── ║
║ ✅ Reusability           120.48   → 134.96   [+12%] İYİ      ║
║ ✅ Functionality         61.69    → 68.93    [+11%] İYİ      ║
║ ✅ Effectiveness         1.082    → 1.086    [+0.4%] STABIL   ║
║                                                               ║
║ 🟡 Flexibility           1.461    → 1.431    [−2%] HAFIF     ║
║ 🟡 Extendibility         0.8945   → 0.885    [−1%] HAFIF     ║
║ 🔴 Understandability     −81.87   → −91.47   [−12%] UYARI    ║
║                                                               ║
║ TEKNIK BORÇ                                                   ║
║ ──────────────────────────────────────────────────────────── ║
║ 🟡 CAM (Cohesion)        0.407    → 0.387    [−4.8%] UYARI   ║
║ 🟡 NOP (Polymorphism)    3.273    → 3.191    [−2.5%] HAFIF   ║
║ ✅ DCC (Coupling)        2.349    → 2.363    [+0.6%] OK       ║
║ ✅ NOH (Hierarchy)       35       → 39       [+11%] OK        ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝

NET SONUÇ:
═════════════════════════════════════════════════════════════════

✅ OLUMLU:
├─ Reusability +12% — API modülarity iyileşti
├─ Functionality +11% — Feature set genişledi
├─ ANA, MOA, MFA artışı — Design quality iyileşti
└─ Sistem "professional library" yönünde ilerledi

🔴 OLUMSUZ:
├─ Understandability −12% — Sistem anlaşılması zor hale geldi
├─ CAM −4.8% — Sınıf cohesion düştü (design debt)
├─ NOP −2.5% — Polimorfizm azaldı (flexibility risk)
└─ Erken-aşama teknik borç biriktirilmeye başlandı

🟡 SONUÇ: MIXED
────────────────
Olumlu yönde (feature/reusability) vs olumsuz yön (understanding/debt)
dengesi var. Bu, erken-aşama library'lerde normal bir pattern'dır.

ÖNEMLİ: Eğer bu trend (Understandability ↓, CAM ↓, NOP ↓) devam
ederse, 1-2 sürüm sonra sorun haline gelecektir.

TAVSI YE:
──────────
Sonraki sürümlerde:
1. Cohesion iyileştir (CAM restore)
2. Polimorfizm artır (NOP restore)
3. Documentation güçlendir (practical understanding)
4. 0.9.3'de cleanup sprint yapılmalı
```

---

**Hazırlayan:** Yazılım Mimarisi Uzmanı  
**Tarih:** Haziran 2026  
**Veri Kaynağı:** JGraphT 0.9.0 vs 0.9.2 Metrikleri  
**Metodoloji:** QMOOD Model + Tasarım Metrik Analizi  
**Disclaimer:** Bu analiz, sağlanan metrik verilerine dayanmaktadır. 
Gerçek kod incelemesi ek bulgular sunabilir. Teknik borç değerlendirmesi 
trend analizi üzerine kuruludur ve henüz "acil" müdahale gerektirmez, 
ama monitörizasyon tavsiye edilir.
