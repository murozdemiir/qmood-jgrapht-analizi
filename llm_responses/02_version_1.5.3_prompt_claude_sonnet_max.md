# JGraphT 1.5.3 — QMOOD Derin Kalite İncelemesi

> **Kapsam:** `jgrapht-core` modülü, tek sürüm analizi  
> **Yöntem:** QMOOD (Bansiya & Davis 2002) + CK metrikleri  
> **Önemli bağlam:** Tüm QMOOD denklem hesapları bağımsız olarak doğrulanmıştır (maksimum sapma < 0.0001). 1.5.2 → 1.5.3 sürüm geçiş farkları rapor içinde kanıt olarak kullanılmaktadır.

---

## 1. Sürüm Genel Bakış ve 1.5.2 ile Karşılaştırma

| Parametre | 1.5.2 | 1.5.3 | Δ | Yorum |
|---|---|---|---|---|
| Sınıf sayısı (DSC) | 601 | 618 | **+17 (+%2.8)** | Anlamlı ek |
| Hiyerarşi (NOH) | 87 | 91 | **+4 (+%4.6)** | 4 yeni hiyerarşi |
| Ort. bağlaşım (DCC) | 3.0233 | 3.0324 | +0.009 | Sabit sayılabilir |
| Ort. LCOM | 30.22 | **31.24** | **+1.02 (+%3.4)** | Dikkat çekici artış |
| Ort. RFC | 17.13 | 17.25 | +0.12 (+%0.7) | Hafif artış |
| Maks. LCOM | 4371 | **4371** | 0 | Çözülmedi |
| Maks. WMC | 381 | **381** | 0 | Çözülmedi |
| Maks. MPC | 401 | **401** | 0 | Çözülmedi |
| Maks. NOC | 28 | **28** | 0 | Değişmedi |

**1.5.3'ün 1.5.2'den farkı:** Yalnızca yama değil, **17 yeni sınıf ve 4 yeni hiyerarşi** içeren daha kapsamlı bir artımlı sürümdür. Ancak tüm yapısal aşırı değerler (LCOM\_max, WMC\_max, MPC\_max) çözülmemiş olarak taşınmıştır. LCOM ortalamasındaki +%3.4 artış, eklenen sınıfların iç uyum açısından mevcut ortalamayı yukarı çektiğine işaret etmektedir.

---

## 2. Kalite Nitelikleri Değerlendirmesi

### 2.1 Ham Değerler, 1.5.2 Karşılaştırması ve Normalize Tablo

Normalize değerler, 0.9.0 baz alınarak hesaplanmıştır.

| Nitelik | 1.5.3 Ham | 1.5.2 Ham | Δ (ham) | Δ% | Normalize (baz 0.9.0) | Yön |
|---|---|---|---|---|---|---|
| Reusability | 310.45 | 301.94 | +8.51 | +%2.8 | 1.74 | ✅ Güçlü |
| Flexibility | 1.5861 | 1.5650 | +0.021 | +%1.4 | 1.40 | ✅ Orta-İyi |
| Functionality | 157.73 | 153.10 | +4.63 | +%3.0 | 1.73 | ✅ Güçlü |
| Effectiveness | 1.1205 | 1.1105 | +0.010 | +%0.9 | 1.04 | ➡️ Sabit |
| **Understandability** | **−207.89** | −202.26 | −5.63 | **−%2.8** | **−1.59** | **❌ En zayıf** |
| **Extendibility** | **0.4923** | 0.4774 | **+0.015** | **+%3.1** | **0.46** | **❌ En zayıf** |

**Dikkat çekici bulgu:** Extendibility bu sürümde 0.4774'ten 0.4923'e hafifçe **iyileşmiştir** (+%3.1). Bu, 17 yeni sınıfın ANA ve NOP üzerinde küçük de olsa olumlu etki yarattığını göstermektedir. Bununla birlikte normalize değer (0.46) hâlâ baz değerin (0.9.0 = 0.894) yalnızca %52'sindedir; iyileşme mütevazı ve kırılgandır.

> **Belirsizlik notu:** Reusability ve Functionality'nin yüksek görünmesi büyük ölçüde DSC (618 sınıf) ve CIS değerlerinin denklemlerde büyük pozitif ağırlık taşımasından kaynaklanmaktadır. Bu değerleri ölçek etkisinden arındırmadan "iyi tasarım" kanıtı olarak okumak yanıltıcı olur.

---

## 3. En Zayıf 2 Kalite Niteliği: Derin Analiz

### 3.1 🔴 Understandability — Ham: −207.89

#### Denklem

```
Understandability = −0.33*(ANA + DCC + NOP + NOM + DSC) + 0.33*(DAM + CAM)
```

#### Sayısal Hesap (1.5.3)

```
Negatif terim = −0.33 × (0.3204 + 3.0324 + 3.5453 + 6.3236 + 618.0)
              = −0.33 × 631.221
              = −208.303

Pozitif terim = +0.33 × (0.8850 + 0.3660)
              = +0.33 × 1.2510
              = +0.413

Toplam = −207.89  ✓
```

#### Negatif Terim Bileşenleri ve Payları

| Metrik | Değer | Negatif Katkı | Toplam İçindeki Pay |
|---|---|---|---|
| **DSC** | 618.0 | −203.94 | **%97.9** |
| NOM | 6.32 | −2.09 | %1.0 |
| NOP | 3.55 | −1.17 | %0.6 |
| DCC | 3.03 | −1.00 | %0.5 |
| ANA | 0.32 | −0.11 | %0.05 |
| DAM + CAM | 1.25 | +0.41 | *(pozitif)* |

#### 1.5.2'ye Göre Bozulmanın Sürücüleri

1.5.2'den 1.5.3'e Understandability −5.63 puan daha kötüleşmiştir. Bu bozulmanın kaynağı:

- **DSC: 601 → 618 (+17):** 17 yeni sınıf, negatif terime 17 × 0.33 = **−5.61 puan** doğrudan katkı sağlamıştır. Bozulmanın neredeyse tamamı DSC artışından gelmektedir.
- **NOM: 6.29 → 6.32 (+0.03):** Yeni eklenen sınıfların metot karmaşıklık ortalaması mevcut ortalamadan hafif yüksektir; katkısı marginaldir.

#### Yapısal Sorun: Denklem Etkisinin Ötesinde Gerçek Problem

DSC'nin %97.9 ağırlık taşıması, denklemin tasarım özelliğidir. Ancak bunun arkasında ölçekten bağımsız gerçek yapısal sorunlar da mevcuttur:

- **LCOM\_mean: 30.22 → 31.24 (+%3.4):** 17 yeni sınıf LCOM ortalamasını yukarı çekmiştir. Bu, eklenen sınıfların iç uyum açısından mevcut ortalamadan daha kötü olduğunu gösterir.
- **LCOM\_max = 4371:** Hiç değişmemiştir. Kütüphanede en az bir sınıf, 3 sürüm boyunca çözülmemiş biçimde aşırı yüksek iç uyumsuzluk taşımaktadır.
- **WMC\_max = 381, NOM\_max = 95:** Bunlar da değişmemiştir. Karmaşıklık yoğunlaşması sistemde sabit bir yük olarak kalmaktadır.

---

### 3.2 🔴 Extendibility — Ham: 0.4923 (Baz 0.9.0: 0.894, Bozulma: %45)

#### Denklem

```
Extendibility = 0.50*(ANA + MFA + NOP) − 0.50*DCC
```

#### Sayısal Hesap — Üç Sürüm Karşılaştırması

```
0.9.0 baz:  pos = 0.50*(0.6176+0.2469+3.2731) = 2.069  neg = 0.50*2.3487 = 1.174  Ex = 0.894
1.5.2:      pos = 0.50*(0.3195+0.1511+3.5075) = 1.989  neg = 0.50*3.0233 = 1.512  Ex = 0.477
1.5.3:      pos = 0.50*(0.3204+0.1512+3.5453) = 2.008  neg = 0.50*3.0324 = 1.516  Ex = 0.492
```

1.5.3'te pozitif terim 1.989'dan 2.008'e yükselmiştir; bu iyileşmenin sürücüsü NOP'un 3.51→3.55 artışıdır. Negatif terim de 1.512'den 1.516'ya hafif artmıştır (DCC: +0.009). Net etki küçük bir iyileşmedir (+0.015).

#### Uzun Vadeli Bozulmanın Kalıcı Sürücüleri

| Metrik | 0.9.0 (baz) | 1.5.3 | Değişim | Denklemdeki Rol |
|---|---|---|---|---|
| **ANA** | 0.6176 | 0.3204 | **−%48** | Pozitif (+0.50) — hâlâ kritik açık |
| **MFA** | 0.2469 | 0.1512 | **−%39** | Pozitif (+0.50) — hâlâ kritik açık |
| **DCC** | 2.3487 | 3.0324 | **+%29** | Negatif (−0.50) — hâlâ baskı uygular |
| NOP | 3.2731 | 3.5453 | +%8 | Pozitif; kısmen telafi |

1.5.3'teki hafif Extendibility iyileşmesi gerçektir ancak yapısal kökenli değildir: ANA, MFA ve DCC kaynaklı bozulma **devam etmektedir**. Mevcut iyileşme yalnızca NOP'un hafif artışından kaynaklanmaktadır ve kırılgandır.

---

## 4. Ek Bulgular: CK Metrik Tehlike Sinyalleri

### 4.1 LCOM Ortalaması Artmaya Devam Ediyor

| Sürüm | LCOM\_mean | LCOM\_max |
|---|---|---|
| 1.5.1 | 30.21 | 4371 |
| 1.5.2 | 30.22 | 4371 |
| **1.5.3** | **31.24 (+%3.4)** | **4371** |

1.5.2 → 1.5.3 arasında LCOM ortalaması anlamlı biçimde artmıştır (+1.02). Bu, eklenen 17 sınıfın iç uyum kalitesinin mevcut ortalamadan daha düşük olduğunu göstermektedir. God class (LCOM\_max = 4371) ise üç sürüm boyunca çözülmemiştir.

### 4.2 Değişmeyen Kritik Aşırı Değerler

| CK Metrik | 1.5.1 | 1.5.2 | 1.5.3 | Risk |
|---|---|---|---|---|
| LCOM\_max | 4371 | 4371 | **4371** | God class — 3 sürümdür çözülmemiş |
| WMC\_max | 381 | 381 | **381** | Karmaşıklık yoğunlaşması |
| NOM\_max | 95 | 95 | **95** | 95 metotlu sınıf — SRP ihlali |
| MPC\_max | 401 | 401 | **401** | Aşırı koordinasyon yükü |
| CBO\_max | 21 | 21 | **21** | Maksimum bağımlılık yoğunluğu |
| NOC\_max | 28 | 28 | **28** | Üst sınıf kırılganlığı |

Bu tablonun önemi şuradan gelir: **3 art arda sürümde hiçbir aşırı değer düzeltilmemiştir.** Bu, refactoring gündeminin aktif olmadığını sayısal olarak kanıtlamaktadır.

---

## 5. Refactoring Önerileri

### 5.1 🔴 LCOM\_max = 4371 Sahibi God Class'ı Ayrıştırın

**Kanıt:** LCOM\_max = 4371 ve LCOM\_mean = 31.24 arasındaki 140× fark, dağılımda son derece uç bir değer varlığını kanıtlar. Bu değer 3 sürümdür değişmemiştir; aktif bir çözüm girişimi olmadığı anlaşılmaktadır. WMC\_max = 381 ve NOM\_max = 95 büyük ihtimalle aynı sınıfa aittir.

**Yöntem:**
1. SonarQube, PMD veya SpotBugs ile `LCOM > 200` olan sınıfları raporlayın.
2. Her aday sınıfta metotların hangi alan değişkenlerini kullandığını matris olarak çıkarın; paylaşımsız metot kümeleri ayrı sorumlulukları işaret eder.
3. Her kümeyi bağımsız, odaklı bir sınıfa taşıyın (**Extract Class**).
4. Orijinal sınıfı API uyumluluğunu korumak için Façade delegatörü olarak bırakın; kademeli geçişe olanak tanır.

**Hedef metrikler:** LCOM\_mean < 20, WMC\_max < 100, NOM\_max < 40.

**Beklenen kalite etkisi:** NOM ve DCC ortalamaları düşer → Understandability'nin kontrol edilebilir bileşenleri iyileşir.

---

### 5.2 🔴 Soyutlama Katmanını Güçlendirin (ANA + MFA)

**Kanıt:** ANA baz değerden %48 düşmüştür (0.6176 → 0.3204); 618 sınıfın yalnızca %32'si soyut yapıdır. MFA %39 gerilemiştir (0.2469 → 0.1512). LCOM ortalamasındaki son artış (+%3.4), yeni eklenen 17 sınıfın da somut ve iç uyumsuz biçimde geldiğine işaret etmektedir.

**Yöntem:**
1. Ortak davranış paylaşan somut sınıf kümelerini belirleyin: aynı arayüzü doğrudan uygulayan birden fazla somut sınıf bu kümelerin adayıdır.
2. Her küme için **ortak soyut üst sınıf** veya şablon metot sağlayan temel sınıf tanımlayın (**Extract Superclass**).
3. Algoritma ailelerinde (shortest-path, spanning-tree, matching, coloring, flow, traversal) her aile için soyut temel sınıf oluşturun; somut uygulamalar bu temeli genişletsin.
4. Geliştirme sürecine kural ekleyin: yeni somut sınıf PR'ı açılırken ilgili soyutlamanın var olup olmadığı kod incelemesinde kontrol edilsin. Yoksa soyutlama önce eklensin.

**Hedef metrikler:** ANA > 0.45, MFA > 0.20.

**Beklenen kalite etkisi:** Extendibility denkleminin pozitif terimi güçlenir. 0.9.0 → 1.5.3 bozulmasının ana sürücüsünü tersine çevirir.

---

### 5.3 🟡 MPC\_max = 401 Sahibi Koordinatör Sınıfı Parçalayın (Façade / Mediator)

**Kanıt:** MPC ortalaması 16.85 iken bir sınıf 401 metot çağrısı göndermektedir (24× ortalama üzeri). CBO\_max = 21 ve RFC\_max = 149 ile birlikte bu sınıf aşırı koordinasyon sorumluluğu üstlenmiştir. Bu değer de 3 sürümdür sabit kalmıştır.

**Yöntem:**
1. `MPC > 80` olan sınıfları tespit edin.
2. Koordine edilen sorumluluk alanlarını ayırt edin (grafik oluşturma, algoritma yürütme, serileştirme, sonuç biçimlendirme gibi).
3. Her sorumluluk alanı için ayrı bir **Façade** sınıfı oluşturun; istemciler doğrudan alt sistemle değil Façade üzerinden etkileşsin.
4. Alt sistem bileşenleri arasındaki koordinasyonu daha küçük ve odaklı bir **Mediator** sınıfına devredin.

**Hedef metrikler:** MPC\_max < 150, DCC\_mean < 2.7.

**Beklenen kalite etkisi:** DCC ortalaması düşer → Extendibility ve Flexibility denklemlerinin negatif terimi zayıflar.

---

## 6. Özet

### 6.1 1.5.3'ün Özgün Konumu

1.5.3, 1.5.1 ve 1.5.2'den farklı olarak gerçek anlamda yeni içerik ekleyen (17 sınıf, 4 hiyerarşi) bir sürümdür. Bu ekleme, Extendibility'de küçük bir iyileşme (+%3.1) ve Reusability/Functionality'de ölçekle orantılı artış üretmiştir. Ancak LCOM ortalamasının +%3.4 artması ve tüm yapısal aşırı değerlerin çözülmeden kalması, yeni içeriğin mevcut mimari sorunların çözümüyle eş zamanlı geliştirilmediğini göstermektedir.

### 6.2 Öncelik Matrisi

| Öncelik | Refactoring | Hedef Metrik | Etkilenen Nitelik |
|---|---|---|---|
| 🔴 1 | God class ayrıştırması (LCOM\_max=4371, 3 sürümdür çözülmemiş) | LCOM, NOM, WMC | Understandability |
| 🔴 2 | Soyutlama katmanı güçlendirme (ANA −%48, MFA −%39) | ANA, MFA | Extendibility |
| 🟡 3 | Koordinatör sınıf parçalama (MPC\_max=401, 3 sürümdür çözülmemiş) | DCC, MPC, RFC | Extendibility, Flexibility |

Bu üç öneri 1.5.x serisinin tamamı için geçerlidir: sorunlar sürümler arasında aktarılmaya devam etmektedir.

---

*Tüm QMOOD denklem hesapları bağımsız olarak doğrulanmıştır. Sınıf düzeyinde dağılım verisi olmadan hangi sınıfların aşırı değerlere yol açtığı kesin olarak belirlenemez; SonarQube veya PMD ile sınıf düzeyinde analiz yapılarak doğrulama önerilir.*
