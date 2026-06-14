# JGraphT 1.5.2 — QMOOD Derin Kalite İncelemesi

> **Kapsam:** `jgrapht-core` modülü, tek sürüm analizi  
> **Yöntem:** QMOOD (Bansiya & Davis 2002) + CK metrikleri  
> **Kritik Not:** 1.5.2, önceki sürüm 1.5.1 ile neredeyse identiktir. Tüm metrik farklılıkları %2'nin altındadır ve max değerlerin hiçbiri değişmemiştir. Bu nedenle bu rapor hem 1.5.2'nin bağımsız değerlendirmesini hem de 1.5.1→1.5.2 geçişinin niteliğini kapsamaktadır. Abartma yapmaktan kaçınılmıştır.

---

## 1. Sürüm Genel Bakış

| Parametre | 1.5.1 | 1.5.2 | Δ |
|---|---|---|---|
| Sınıf sayısı (DSC) | 600 | 601 | +1 |
| Hiyerarşi (NOH) | 87 | 87 | 0 |
| Ort. bağlaşım (DCC) | 3.0183 | 3.0233 | +0.0050 |
| Ort. karmaşıklık (WMC) | 15.7767 | 15.7604 | −0.0163 |
| Ort. iç uyumsuzluk (LCOM) | 30.21 | 30.2213 | +0.0113 |
| Maks. LCOM | 4371 | **4371** | 0 |
| Maks. WMC | 381 | **381** | 0 |
| Maks. NOC | 28 | **28** | 0 |
| Maks. MPC | 403 | **401** | −2 |

**Yorum:** 1.5.2, 1.5.1'e yalnızca 1 sınıf eklenmiş bir yama sürümüdür. Hiçbir yapısal sorun çözülmemiş, hiçbir yeni yapısal sorun da eklenmemiştir. Tüm aşırı değerler (LCOM\_max, WMC\_max, NOC\_max) olduğu gibi kalmıştır.

---

## 2. Kalite Nitelikleri Değerlendirmesi

### 2.1 1.5.2 Ham ve Normalize Tablo

Normalize değerler, kütüphanenin ilk ölçülen sürümü olan 0.9.0 baz alınarak verilmektedir (0.9.0 = 1.0).

| Nitelik | 1.5.2 Ham | Normalize | 1.5.1 Ham | Δ (ham) | Yorum |
|---|---|---|---|---|---|
| Reusability | 301.94 | 1.70 | 301.45 | +0.49 | ✅ Güçlü |
| Flexibility | 1.5650 | 1.39 | 1.5703 | −0.005 | ✅ Orta-İyi |
| Functionality | 153.10 | 1.73 | 152.89 | +0.21 | ✅ Güçlü |
| Effectiveness | 1.1105 | 1.01 | 1.1127 | −0.002 | ➡️ Sabit |
| **Understandability** | **−202.26** | **−1.57** | −201.94 | −0.32 | **❌ En zayıf** |
| **Extendibility** | **0.4774** | **0.46** | 0.4870 | −0.010 | **❌ En zayıf** |

> **Belirsizlik notu:** Reusability ve Functionality'nin yüksek görünmesi büyük ölçüde DSC (600+ sınıf) ve CIS değerlerinin bu denklemlerde büyük pozitif ağırlık taşımasından kaynaklanmaktadır. Ölçek etkisi soyutlanmadan bu değerleri "iyi tasarım" kanıtı olarak okumak yanıltıcı olur.

---

## 3. En Zayıf 2 Kalite Niteliği: Derin Analiz

### 3.1 🔴 Understandability — Ham: −202.26

#### Denklem

```
Understandability = −0.33*(ANA + DCC + NOP + NOM + DSC) + 0.33*(DAM + CAM)
```

#### Sayısal Hesap (1.5.2)

```
Negatif terim = −0.33 × (0.3195 + 3.0233 + 3.5075 + 6.2928 + 601.0)
              = −0.33 × 614.143
              = −202.67

Pozitif terim = +0.33 × (0.8806 + 0.3633)
              = +0.33 × 1.2439
              =  +0.41

Toplam ≈ −202.26  ✓
```

#### Sorumlu Metrikler

| Metrik | 1.5.2 Değeri | Negatif Katkı | Toplam İçindeki Pay |
|---|---|---|---|
| **DSC** | 601.0 | −198.33 | **%97.8** |
| NOM | 6.29 | −2.08 | %1.0 |
| NOP | 3.51 | −1.16 | %0.6 |
| DCC | 3.02 | −1.00 | %0.5 |
| ANA | 0.32 | −0.11 | %0.05 |
| DAM + CAM | 1.24 | +0.41 | *(pozitif)* |

#### Yorum

DSC negatif terimde doğrusal katkı sağladığından, **600+ sınıf barındıran herhangi bir sistem** bu denklemde kaçınılmaz olarak büyük negatif Understandability skoru üretir. Bu, kısmen denklemin tasarım özelliğidir. Ancak gerçek bir yapısal sorun da mevcuttur:

- **WMC\_max = 381:** Ortalama 15.76 iken bir sınıfın ağırlıklı metot karmaşıklığı 381'dir. Bu, dağılımın son derece sağa çarpık olduğunu, yani bir avuç sınıfın tüm karmaşıklığı üstlendiğini göstermektedir.
- **LCOM\_max = 4371:** İç uyumsuzluğu bu denli yüksek bir sınıf, onlarca ilgisiz sorumluluğu tek çatı altında topluyor demektir. Bu sınıfı anlamak ve değiştirmek nesnel olarak güçtür.
- **NOM\_max = 95:** Tek bir sınıfta 95 metot, bireysel geliştiricinin çalışma belleğini (working memory) aşan bir yüktür.

Bu üç aşırı değer, Understandability bozulmasının DSC büyümesinin ötesinde gerçek bir sınıf tasarım sorunundan da beslendiğini kanıtlamaktadır.

---

### 3.2 🔴 Extendibility — Ham: 0.4774 (Baz 0.9.0: 0.894, Bozulma: %47)

#### Denklem

```
Extendibility = 0.50*(ANA + MFA + NOP) − 0.50*DCC
```

#### Sayısal Hesap (1.5.2)

```
Pozitif terim = 0.50 × (0.3195 + 0.1511 + 3.5075)
              = 0.50 × 3.9781
              = 1.989

Negatif terim = 0.50 × 3.0233
              = 1.512

Toplam = 1.989 − 1.512 = 0.477  ✓
```

#### Sorumlu Metrikler — Tarihsel Kıyaslama

| Metrik | 0.9.0 (baz) | 1.5.2 | Δ | Denklemdeki Rol |
|---|---|---|---|---|
| **ANA** | 0.6176 | 0.3195 | **−%48** | Pozitif (+0.50) |
| **MFA** | 0.2469 | 0.1511 | **−%39** | Pozitif (+0.50) |
| **DCC** | 2.3487 | 3.0233 | **+%29** | Negatif (−0.50) |
| NOP | 3.2731 | 3.5075 | +%7 | Pozitif (+0.50) |

#### Yorum

Üç temel metrik birlikte olumsuz yönde hareket etmiştir:

**ANA (Soyutlama) −%48:** 601 sınıfın yalnızca %32'si soyut bir yapı olarak tanımlanmaktadır. 0.9.0'da bu oran %62 idi. Yeni eklenen sınıfların büyük çoğunluğu doğrudan somut sınıf olarak yazılmış; mevcut soyutlamalar genişletilmemiştir.

**MFA (Kalıtım) −%39:** Kalıtımdan türeyen yöntem oranı da gerilemiştir. MOA (kompozisyon) 0.374 → 0.694 artışıyla bunu kısmen telafi etmiştir; ancak MFA kaybı Extendibility denkleminde MOA'nın yer almaması nedeniyle telafi edilemez.

**DCC (Bağlaşım) +%29:** CBO\_max = 21 değeri, bazı sınıfların 21 farklı sınıfa doğrudan bağımlı olduğunu gösterir. Yeni bir sınıf eklerken bu bağımlılık ağını anlamak ve yönetmek gerekmektedir; bu genişletmeyi nesnel olarak güçleştirir.

**Bileşik etki hesabı:**

```
0.9.0: 0.50*(0.6176+0.2469+3.2731) − 0.50*2.3487 = 2.069 − 1.174 = 0.894
1.5.2: 0.50*(0.3195+0.1511+3.5075) − 0.50*3.0233 = 1.989 − 1.512 = 0.477
```

Extendibility, baz değerin %47'sine gerilemiştir. Bu bozulma tek bir nedenle değil, soyutlama erozyonu + kalıtım azalması + bağlaşım artışının **bileşik etkisiyle** gerçekleşmiştir.

---

## 4. Ek Bulgular: Değişmeyen Tehlike Sinyalleri

Aşağıdaki aşırı değerler 1.5.1'den 1.5.2'ye **hiç değişmeden** taşınmıştır. Bu, söz konusu yapısal sorunların aktif olarak ele alınmadığını göstermektedir.

| CK Metrik | Ortalama | Maksimum | Risk Yorumu |
|---|---|---|---|
| LCOM | 30.22 | **4371** | God class adayı; 4371 değeri olağandışı düzeyde |
| WMC | 15.76 | **381** | Ortalama 24× üzerinde karmaşıklık yoğunlaşması |
| NOM | 6.29 | **95** | 95 metotlu sınıf ciddi SRP ihlali |
| MPC | 16.78 | **401** | Koordinatör sınıf; 401 metot çağrısı aşırı |
| RFC | 17.13 | **149** | Yüksek yanıt seti; test kapsamı güçleşiyor |
| NOC | — | **28** | 28 doğrudan alt sınıf; üst sınıf değişime kırılgan |

---

## 5. Refactoring Önerileri

### 5.1 🔴 LCOM\_max = 4371 Sahibi God Class'ı Ayrıştırın

**Kanıt:** LCOM ortalaması 30.22, maksimum 4371. Bu fark (145×) dağılımda son derece aşırı bir değerin varlığını kanıtlar. WMC\_max = 381 ve NOM\_max = 95 muhtemelen aynı sınıfa aittir.

**Yöntem:**
1. `LCOM > 200` olan sınıfları SonarQube veya PMD ile tespit edin.
2. Her sınıftaki metotları **alan değişkeni kullanım örüntüsüne** göre kümelendirin; paylaşılan alan yoksa metotlar farklı sorumluluk gruplarına aittir.
3. Her kümeyi bağımsız bir sınıfa taşıyın (**Extract Class**).
4. Geriye kalan sınıfı gerekirse bir Façade delegasyonu olarak bırakın; böylece mevcut API bozulmaz.

**Hedef metrikler:** LCOM\_mean < 20, WMC\_max < 100, NOM\_max < 40.

**Beklenen kalite etkisi:** Understandability'nin gerçek bileşenleri (NOM, DCC ortalamaları) iyileşir.

---

### 5.2 🔴 Soyutlama Katmanını Güçlendirin (ANA + MFA Hedefi)

**Kanıt:** ANA 0.6176 → 0.3195 (%48 düşüş), MFA 0.2469 → 0.1511 (%39 düşüş). 601 sınıfın yalnızca %32'si soyut yapı; 0.9.0'da bu %62 idi.

**Yöntem:**
1. Benzer davranışı paylaşan somut sınıf kümelerini belirleyin (özellikle aynı arayüzü doğrudan uygulayan birden fazla somut sınıf).
2. Bu kümeler için **ortak soyut üst sınıf** veya varsayılan davranış sağlayan **arayüz** tanımlayın (*Extract Superclass / Extract Interface*).
3. Algoritma ailelerinde (traversal, shortest-path, matching, coloring, flow) her aile için soyut temel sınıf oluşturun; somut uygulamalar bu temeli genişletsin.
4. Geliştirme kuralı olarak: yeni somut sınıf eklenmeden önce ilgili soyutlamanın var olup olmadığı kod incelemesinde kontrol edilsin.

**Hedef metrikler:** ANA > 0.45, MFA > 0.20.

**Beklenen kalite etkisi:** Extendibility denkleminin pozitif terimi güçlenir; ANA + MFA toplamı artar, bozulmanın büyük bölümü tersine çevrilir.

---

### 5.3 🟡 MPC\_max = 401 Sahibi Koordinatör Sınıfı Parçalayın (Façade / Mediator)

**Kanıt:** MPC ortalaması 16.78 iken bir sınıf 401 metot çağrısı göndermektedir (24× ortalama üzeri). RFC\_max = 149 ve CBO\_max = 21 ile birlikte bu sınıf aşırı koordinasyon sorumluluğu üstlenmiştir.

**Yöntem:**
1. `MPC > 80` olan sınıfları tespit edin.
2. Bu sınıfların koordine ettiği sorumluluk alanlarını ayırt edin (örn. grafik oluşturma, algoritma yürütme, sonuç biçimlendirme, serileştirme).
3. Her sorumluluk alanı için ayrı bir **Façade** sınıfı oluşturun; istemciler alt sistemle doğrudan değil Façade üzerinden konuşsun.
4. Alt sistem bileşenleri arasındaki koordinasyonu, tek bir büyük sınıf yerine daha küçük ve odaklı bir **Mediator** üstlensin.

**Hedef metrikler:** MPC\_max < 150, DCC\_mean < 2.5.

**Beklenen kalite etkisi:** DCC ve MPC ortalamaları düşer → Extendibility denkleminin negatif terimi zayıflar, Flexibility ve Understandability iyileşir.

---

## 6. Özet

### 6.1 1.5.1 → 1.5.2: Anlamlı Değişim Yok

| Boyut | Durum |
|---|---|
| Kalite niteliklerinde değişim | Tümü <%2, istatistiksel olarak ihmal edilebilir |
| Yapısal sorunlar (god class, aşırı bağlaşım) | Çözülmemiş, aynen taşınmış |
| Yeni sorun eklenmesi | Yok |

Bu sürüm geçişi bir **yama (patch) yayınıdır**; yeni işlevsellik eklenmiş, yapısal iyileştirme yapılmamıştır.

### 6.2 Öncelik Matrisi

| Öncelik | Refactoring | Hedef Metrik | Etkilenen Nitelik |
|---|---|---|---|
| 🔴 1 | God class ayrıştırması (LCOM\_max=4371) | LCOM, NOM, WMC | Understandability |
| 🔴 2 | Soyutlama katmanı yeniden inşası | ANA, MFA | Extendibility |
| 🟡 3 | Koordinatör sınıf parçalama (MPC\_max=401) | DCC, MPC, RFC | Extendibility, Flexibility |

Bu üç adım, en kritik iki nitelik olan **Understandability** ve **Extendibility**'deki bozulmanın kök nedenlerini doğrudan hedeflemektedir.

---

*Rapor, sağlanan QMOOD ve CK metrik verileri temelinde hazırlanmıştır. Sınıf düzeyinde dağılım bilgisi olmadan hangi sınıfların aşırı değerlere yol açtığı kesin olarak belirlenemez; SonarQube veya PMD ile statik analiz yapılarak doğrulama önerilir.*
