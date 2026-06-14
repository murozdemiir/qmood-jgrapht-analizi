# JGraphT 1.5.1 — QMOOD Derin Kalite İncelemesi

> **Kapsam:** `jgrapht-core` modülü, tek sürüm analizi  
> **Yöntem:** QMOOD (Bansiya & Davis 2002) + CK metrikleri  
> **Uyarı:** Tüm yorumlar doğrudan verilen sayısal verilere dayandırılmıştır. Sınıf düzeyinde dağılım verisi olmadığından ortalama tabanlı yorumlar olasılıksal niteliktedir.

---

## 1. Sürüm Genel Bakış

| Parametre | Değer |
|---|---|
| Sınıf sayısı (DSC) | 600 |
| Hiyerarşi derinliği (NOH) | 87 |
| Ortalama bağlaşım (DCC/CBO) | 3.02 |
| Ortalama yöntem sayısı (WMC) | 15.78 |
| Ortalama iç uyumsuzluk (LCOM) | 30.21 |
| Maks. LCOM | **4371** |
| Maks. WMC | **381** |
| Maks. NOC | **28** |

600 sınıf ve 87 kalıtım hiyerarşisi ile JGraphT 1.5.1, olgun ve kapsamlı bir kütüphane ölçeğindedir. Ancak bazı aşırı değerler (LCOM\_max = 4371, WMC\_max = 381) sistemde ciddi yoğunlaşma noktaları bulunduğuna işaret etmektedir.

---

## 2. Kalite Nitelikleri Değerlendirmesi

### 2.1 Ham ve Normalize Tablo

Normalize değerler, kütüphanenin ilk ölçülen sürümü olan 0.9.0 baz alınarak hesaplanmıştır (0.9.0 değerleri = 1.0 referans noktası).

| Nitelik | Ham Değer | Normalize (0.9.0 = 1.0) | Yorum |
|---|---|---|---|
| Reusability | 301.45 | 1.70 | ✅ Güçlü |
| Flexibility | 1.5703 | 1.39 | ✅ Orta-İyi |
| Functionality | 152.89 | 1.68 | ✅ Güçlü |
| Effectiveness | 1.1127 | 1.01 | ➡️ Neredeyse değişmedi |
| **Understandability** | **−201.94** | **−1.57** | **❌ En zayıf** |
| **Extendibility** | **0.487** | **0.46** | **❌ En zayıf** |

En güçlü nitelikler ölçek büyümesinden doğrudan yararlanan Reusability ve Functionality'dir (DSC ve CIS büyük pozitif katkı sağlar). En zayıf iki nitelik ise aşağıda ayrıntılı incelenmektedir.

---

## 3. En Zayıf 2 Kalite Niteliği: Derin Analiz

### 3.1 🔴 Understandability — Ham: −201.94 (Baz: −81.87, Bozulma: %147)

#### Denklem

```
Understandability = −0.33*(ANA + DCC + NOP + NOM + DSC) + 0.33*(DAM + CAM)
```

#### Sayısal Hesap (1.5.1)

```
Negatif terim = −0.33 * (0.3217 + 3.0183 + 3.5183 + 6.32 + 600.0)
              = −0.33 * 613.176
              = −202.35

Pozitif terim = +0.33 * (0.8794 + 0.3641)
              = +0.33 * 1.2435
              =  +0.41

Toplam ≈ −201.94  ✓ (veriyle tutarlı)
```

#### Sorumlu Metrikler

| Metrik | Değer | Negatif Katkı | Açıklama |
|---|---|---|---|
| **DSC** | 600.0 | −198.0 | Toplam negatif katkının **%97.9'u** tek başına DSC'den geliyor |
| NOM | 6.32 | −2.09 | Sınıf başına ortalama 6.32 metot; yüksek |
| NOP | 3.52 | −1.16 | Orta düzey polimorfizm; tek başına sorun değil |
| DCC | 3.02 | −1.00 | Bağlaşım katkısı; orta ama MOA ile birleşince anlamlı |
| DAM+CAM | 1.24 | +0.41 | Pozitif katkı çok zayıf kalıyor |

#### Yorum

Understandability denkleminin yapısal bir sorunu vardır: DSC (toplam sınıf sayısı) negatif terimde doğrusal katkı sağlar. Bu nedenle **600 sınıflık herhangi bir sistem** bu denklemde çok düşük Understandability skoru üretecektir. Bu, kısmen denklemin tasarım kararından kaynaklanmaktadır.

Bununla birlikte gerçek bir sorun da mevcuttur: NOM ortalaması 6.32 (maks. 95) ve WMC ortalaması 15.78 (maks. 381) değerleri, bazı sınıfların çok yüksek sayıda metot barındırdığını göstermektedir. WMC\_max = 381, dağılımın son derece sağa çarpık olduğuna, yani küçük sayıda sınıfın tüm karmaşıklığı üstlendiğine işaret eder. Bu sınıflar kodu gerçekten anlaşılması güç hâle getirmektedir.

---

### 3.2 🔴 Extendibility — Ham: 0.487 (Baz: 0.894, Bozulma: %45)

#### Denklem

```
Extendibility = 0.50*(ANA + MFA + NOP) − 0.50*DCC
```

#### Sayısal Hesap (1.5.1)

```
Pozitif terim = 0.50 * (0.3217 + 0.1523 + 3.5183)
              = 0.50 * 3.9923
              =  1.996

Negatif terim = 0.50 * 3.0183
              =  1.509

Toplam = 1.996 − 1.509 = 0.487  ✓ (veriyle tutarlı)
```

#### Sorumlu Metrikler

| Metrik | Değer | Referans (0.9.0) | Değişim | Etki |
|---|---|---|---|---|
| **ANA** | 0.3217 | 0.6176 | **−%48** | Pozitif katkı yarı yarıya azalmış |
| **MFA** | 0.1523 | 0.2469 | **−%38** | Pozitif katkı önemli ölçüde azalmış |
| DCC | 3.0183 | 2.3487 | **+%29** | Negatif katkı artmış |
| NOP | 3.5183 | 3.2731 | +%7 | Pozitif katkı hafif artmış; diğerlerini telafi edemiyor |

#### Yorum

Üç metrik aynı anda ters yönde hareket etmiştir:

- **ANA düşmüş:** 600 sınıfın yalnızca %32'si soyut bir yapı (arayüz veya soyut sınıf) olarak tanımlanmaktadır. Bu oran 0.9.0'da %62 idi. Somut sınıf birikimi, yeni işlevsellik eklemek için mevcut soyutlamaların genişletilmesi yerine doğrudan somut sınıf yazılmasının tercih edildiğine işaret etmektedir.

- **MFA düşmüş:** Kalıtımdan türeyen yöntem oranı azalmaktadır. Bu, eklenen somut sınıfların hiyerarşiden bağımsız biçimde büyüdüğünü göstermektedir. MOA'nın artmasıyla (0.374 → 0.692) bir kısmı kompozisyona dönmüş olsa da MFA kaybı telafi edilememiştir.

- **DCC artmış:** Sınıf başına ortalama 3.02 bağımlılık, maks. 21'e kadar çıkmaktadır. Yeni sınıf eklemek için önce mevcut bağımlılık ağını anlamak gerekmektedir; bu da genişletmeyi zorlaştırır.

**Sonuç:** Extendibility bozulması tek bir metrikten değil, soyutlama erozyonu + kalıtım azalması + bağlaşım artışının **bileşik etkisinden** kaynaklanmaktadır.

---

## 4. Ek Bulgular: CK Metriklerinden Tehlike Sinyalleri

### 4.1 LCOM: Ortalama 30.21, Maksimum 4371

LCOM (Lack of Cohesion in Methods) ortalaması 30.21 ve maks. 4371 değeri son derece çarpıcıdır. LCOM = 4371, ilgili sınıftaki metot çiftlerinin büyük çoğunluğunun ortak alan değişkeni paylaşmadığı anlamına gelir. Bu, **tek sorumluluk ilkesini (SRP) ağır biçimde ihlal eden bir god class'ın** varlığına güçlü şekilde işaret etmektedir.

### 4.2 WMC: Ortalama 15.78, Maksimum 381

WMC\_max = 381, standart bir sınıf karmaşıklığının onlarca katıdır. Bu sınıf muhtemelen onlarca metot barındırmakta ve büyük ihtimalle LCOM\_max = 4371 ile örtüşmektedir. Tek sınıfın tüm karmaşıklık yükünü taşıması hem test edilebilirliği hem de değiştirilme maliyetini artırır.

### 4.3 NOC\_max = 28 ve DIT\_max = 3

DIT maksimumu yalnızca 3 olmasına karşın bir sınıfın 28 doğrudan alt sınıfı bulunmaktadır (NOC\_max = 28). Bu durum, bir üst sınıfta yapılacak değişikliğin 28 alt sınıfı etkileyebileceğini göstermektedir. Söz konusu üst sınıf değişime karşı özellikle kırılgandır.

### 4.4 MPC\_max = 403

Bir sınıfın başka sınıflara 403 mesaj (metot çağrısı) göndermesi aşırı bir koordinasyon yüküdür. Bu sınıf büyük ihtimalle bir **koordinatör/orkestrasyoncu** rolü üstlenmiş; Mediator veya Façade gibi bir desenle parçalanması gerekmektedir.

---

## 5. Refactoring Önerileri

### 5.1 LCOM\_max Sahibi God Class'ı Ayrıştırın

**Kanıt:** LCOM\_max = 4371, LCOM\_mean = 30.21. Ortalama bu denli yüksekse dağılımın kuyruğunda çok daha yüksek değerler vardır; maks. değer bunu doğrulamaktadır.

**Yöntem:**
1. LCOM > 200 olan sınıfları statik analiz aracıyla (PMD, SonarQube) tespit edin.
2. Her sınıftaki metot gruplarını alan değişkeni kullanım örüntüsüne göre kümelendirin.
3. Her kümeyi bağımsız, odaklı bir sınıfa taşıyın (**Extract Class** refactoring).
4. Orijinal sınıfı gerekirse bir Façade veya delegasyon katmanı olarak bırakın.

**Beklenen etki:** LCOM\_mean düşer, NOM ortalaması dengelenir, Understandability'nin gerçek bileşenleri (NOM, DCC) iyileşir.

---

### 5.2 Soyutlama Katmanını Yeniden İnşa Edin (ANA + MFA)

**Kanıt:** ANA = 0.32 (0.9.0'da 0.62 idi), MFA = 0.15 (0.9.0'da 0.25 idi). Somut sınıfların payı giderek artmaktadır.

**Yöntem:**
1. Benzer davranışı paylaşan somut sınıf kümelerini belirleyin (örn. aynı arayüzü doğrudan uygulayan birden fazla somut sınıf).
2. Bu kümeler için ortak soyut üst sınıf veya varsayılan davranıç sağlayan arayüz tanımlayın (**Extract Superclass / Extract Interface**).
3. Özellikle algoritma ailelerinde (traversal, shortest-path, matching, coloring) her algoritma türü için soyut temel sınıf oluşturun; somut uygulamalar bu temeli genişletsin.
4. Yeni geliştirme kuralı: her yeni somut sınıf eklendiğinde, ilgili soyutlamanın var olup olmadığı gözden geçirilsin.

**Beklenen etki:** ANA artar → Extendibility'nin pozitif terimi güçlenir. MFA artar → kalıtımdan gelen yöntemler arttıkça bireysel sınıfların yük paylaşımı iyileşir.

---

### 5.3 MPC\_max Sahibi Koordinatör Sınıfı Parçalayın (Mediator / Façade)

**Kanıt:** MPC\_max = 403 (ortalama 16.77 iken bir sınıf 403 metot çağrısı göndermektedir), CBO\_max = 21, RFC\_max = 151. Bu üç metrik aynı sınıfı veya sınıf grubunu işaret ediyor olabilir.

**Yöntem:**
1. MPC > 100 olan sınıfları belirleyin.
2. Bu sınıfların koordine ettiği sorumluluk alanlarını ayırt edin (örn. grafik okuma, algoritma çalıştırma, sonuç biçimlendirme).
3. Her sorumluluk alanı için ayrı bir **Façade** sınıfı oluşturun; istemciler doğrudan alt sistemle değil Façade ile konuşsun.
4. Gerekirse bir **Mediator** deseni ile alt sistem bileşenleri arasındaki iletişimi merkezi ama daha küçük bir koordinatör üzerinden yönetin.

**Beklenen etki:** DCC ve MPC ortalamaları düşer → Extendibility'nin negatif terimi zayıflar, Flexibility artar. Maks. değerlerin normalleşmesiyle bakım maliyeti azalır.

---

## 6. Özet ve Öncelik Matrisi

| Öncelik | Refactoring | Hedef Metrik | Etkilenen Nitelik |
|---|---|---|---|
| 🔴 1 | God class ayrıştırması (LCOM\_max=4371) | LCOM, NOM, WMC | Understandability |
| 🔴 2 | Soyutlama katmanı yeniden inşası | ANA, MFA | Extendibility |
| 🟡 3 | Koordinatör sınıf parçalama (MPC\_max=403) | DCC, MPC, CBO | Extendibility, Flexibility |

Bu üç adım, en kritik iki nitelik olan Understandability ve Extendibility'deki bozulmanın kök nedenlerini doğrudan hedeflemektedir.

---

*Rapor, sağlanan QMOOD ve CK metrik verileri temelinde hazırlanmıştır. Sınıf düzeyinde dağılım bilgisi olmadan hangi sınıfların söz konusu aşırı değerlere yol açtığı kesin olarak belirlenemez; statik analiz araçlarıyla doğrulama önerilir.*
