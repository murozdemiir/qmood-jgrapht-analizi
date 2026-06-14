# JGraphT 1.5.2 → 1.5.3 — Sürüm Farkı Analizi

> **Kapsam:** jgrapht-core, iki sürüm arası tasarım metriği karşılaştırması  
> **Metodoloji:** QMOOD (Bansiya & Davis, 2002)  
> **Kural:** Her iddia sayısal kanıta dayandırılmıştır.

---

## 1. Metrik Değişimlerinin Özeti

| Metrik | 1.5.2 | 1.5.3 | Değişim % | Yön |
|--------|-------|-------|-----------|-----|
| DSC (boyut) | 601.000 | 618.000 | **+2.8 %** | Büyüme |
| NOH (hiyerarşi) | 87.000 | 91.000 | **+4.6 %** | Büyüme |
| ANA (soyutlama) | 0.3195 | 0.3204 | +0.3 % | ➡ Sabit |
| DAM (kapsülleme) | 0.8806 | 0.8850 | +0.5 % | ➡ Sabit |
| DCC (coupling) | 3.0233 | 3.0324 | +0.3 % | ➡ Sabit |
| CAM (uyum) | 0.3633 | 0.3660 | +0.7 % | ➡ Sabit |
| MOA (kompozisyon) | 0.6938 | 0.7006 | +1.0 % | ➡ Sabit |
| MFA (kalıtım) | 0.1511 | 0.1512 | +0.1 % | ➡ Sabit |
| NOP (polimorfizm) | 3.5075 | 3.5453 | +1.1 % | ➡ Sabit |
| CIS (arayüz) | 4.2080 | 4.2249 | +0.4 % | ➡ Sabit |
| NOM (karmaşıklık) | 6.2928 | 6.3236 | +0.5 % | ➡ Sabit |

**Temel gözlem:** DSC ve NOH dışında hiçbir metrik %1.1'in üzerinde değişmemiştir. Bu geçiş, yoğunluk metriklerini (oransal değerler) neredeyse hiç hareket ettirmeyen, ağırlıklı olarak **sınıf ekleme** odaklı bir yama sürümüdür.

---

## 2. Kalite Nitelikleri — Karşılaştırma

| Nitelik | 1.5.2 | 1.5.3 | Δ (ham) | Δ % | Yön |
|---------|-------|-------|---------|-----|-----|
| Reusability | 301.939 | 310.446 | +8.507 | +2.8 % | ✅ DSC katkısıyla |
| Functionality | 153.101 | 157.733 | +4.632 | +3.0 % | ✅ DSC + NOH katkısıyla |
| Flexibility | 1.5650 | 1.5861 | +0.021 | +1.3 % | ➡ Sabit |
| Effectiveness | 1.1105 | 1.1205 | +0.010 | +0.9 % | ➡ Sabit |
| Extendibility | 0.4774 | 0.4923 | +0.015 | +3.1 % | ➡ Sabit |
| **Understandability** | **−202.257** | **−207.890** | **−5.633** | **−2.8 %** | ❌ Kötüleşme |

> **Ölçek uyarısı:** Reusability ve Functionality'deki artış tamamen DSC = +17 eklenmesinden kaynaklanmaktadır. Bu değerler yapısal bir iyileşme değil, boyut büyümesinin formüle yansımasıdır.

---

## 3. Metrik Değişimlerinin Yorumu

### 3.1 DSC +2.8 %, NOH +4.6 % — Büyüme Dengesi

17 yeni sınıf eklenmiş (601 → 618); buna paralel 4 yeni hiyerarşi oluşmuştur (87 → 91). Bu oran dikkat çekicidir:

- NOH büyüme oranı (+4.6 %) DSC büyüme oranından (+2.8 %) daha yüksektir.
- Bu, yeni sınıfların sıfırdan hiyerarşi oluşturduğuna ya da mevcut hiyerarşilere eklemeler yapıldığına işaret eder.
- ANA sabit kalmıştır (0.3195 → 0.3204, +0.3 %); yani yeni sınıfların soyutluk oranı mevcut sistemin soyutluk oranıyla neredeyse aynıdır. Büyüme mimari profilin dışına çıkmamıştır.

**Yorum:** Hiyerarşi büyümesinin DSC büyümesini geçmesi, bu yama sürümünde yeni işlevselliğin kalıtım / soyutlama mimarisine paralel eklendiği anlamına gelir. 0.9.0→0.9.2 geçişindeki sağlıklı büyüme örüntüsüyle tutarlıdır.

---

### 3.2 Yoğunluk Metrikleri — Pratik Değişim Yok

DCC (+0.3 %), CAM (+0.7 %), MOA (+1.0 %), NOP (+1.1 %), NOM (+0.5 %) değerleri istatistiksel gürültü düzeyindedir. Mutlak farklar:

| Metrik | Mutlak Δ | Yorum |
|--------|----------|-------|
| DCC | +0.009 | İhmal edilebilir |
| CAM | +0.003 | İhmal edilebilir |
| MOA | +0.007 | İhmal edilebilir |
| NOP | +0.038 | İhmal edilebilir |
| MFA | +0.001 | Sıfır fark |

17 yeni sınıf eklendiğinde sistem ortalamasının bu kadar küçük değişmesi, yeni sınıfların mevcut tasarım örüntülerini birebir taklit ettiğini gösterir. Bu hem tutarlılık hem de mimari donukluk (ossification) olarak yorumlanabilir — yeni sınıflar sistemi değiştirmiyor, sisteme benzeyerek ekleniyorlar.

---

### 3.3 Understandability: −202.26 → −207.89 (−5.63 puan, −2.8 %)

Bu geçişin tek anlamlı bozulması Understandability'dedir.

**Formül:** `−0.33 × (ANA + DCC + NOP + NOM + DSC) + 0.33 × (DAM + CAM)`

Değişim kaynağı:

| Bileşen | 1.5.2 | 1.5.3 | Δ | Formül katkısı |
|---------|-------|-------|---|----------------|
| DSC | 601.000 | 618.000 | +17.000 | **−5.610** |
| NOM | 6.293 | 6.324 | +0.031 | −0.010 |
| NOP | 3.508 | 3.545 | +0.038 | −0.013 |
| DCC | 3.023 | 3.032 | +0.009 | −0.003 |
| ANA | 0.320 | 0.320 | +0.001 | −0.000 |
| DAM | 0.881 | 0.885 | +0.004 | +0.001 |
| CAM | 0.363 | 0.366 | +0.003 | +0.001 |

**DSC artışının katkısı: −5.610 / toplam −5.633 = %99.6**

Understandability kötüleşmesinin neredeyse tamamı yalnızca DSC = +17'den kaynaklanmaktadır. Diğer tüm metriklerin katkısı toplamda −0.023 puan ile ihmal edilebilir düzeydedir. Bu, QMOOD formülünün DSC'ye aşırı duyarlılığının bir yansımasıdır; ancak büyük sistemlerin gerçekten yönetilmesinin güçleştiğini de doğru biçimde yakalar.

---

## 4. Teknik Borç İşaretleri

### 4.1 Yapısal borç: Mevcut değil (bu geçişte)

Bu yama sürümünde DCC, CAM, LCOM, WMC gibi borç göstergelerinde anlamlı bir hareket yoktur. 3 sürüm boyunca sabit duran WMC_max = 381 ve LCOM_max = 4371 değerleri bu geçişte de değişmemiştir — bu borç birikmeye devam etmektedir ancak bu sürümde yeni borç eklenmemiştir.

### 4.2 Kümülatif borç: Devam ediyor

Mevcut teknik borç göstergeleri 1.5.1'den itibaren taşınmaktadır:

| Gösterge | Değer | Durum |
|----------|-------|-------|
| WMC_max | 381 | 3 sürümdür dokunulmadı |
| LCOM_max | 4371 | 3 sürümdür dokunulmadı |
| ANA | ~0.320 | 3 sürümdür sabit; iyileşme yok |
| DCC_mean | 3.023 → 3.032 | Yavaş artış sürüyor |

**Risk:** God class adayları (WMC = 381, LCOM = 4371) her yeni sürümde dokunulmadan bırakıldıkça borcun "faizi" artmaktadır. Yeni sınıflar bu sınıflara bağımlılık ekledikçe refactoring maliyeti yükselir.

### 4.3 Büyüme örüntüsü: Düşük borç riski

17 yeni sınıfın yoğunluk metriklerini neredeyse hareket ettirmemesi iki şekilde okunabilir:

- **Olumlu:** Yeni sınıflar sistemi daha karmaşık hale getirmedi; DCC ve NOM sabit kaldı.
- **Nötr/Dikkat:** Yeni sınıflar sistemi iyileştirmedi de; ANA, CAM ve MFA'da anlamlı artış yok. Fırsat kaçırılmış olabilir.

---

## 5. 1.5.1 → 1.5.2 → 1.5.3 Bağlam Karşılaştırması

| Metrik | 1.5.1 | 1.5.2 | 1.5.3 | Toplam Δ |
|--------|-------|-------|-------|----------|
| DSC | 600 | 601 | 618 | +18 |
| DCC | 3.018 | 3.023 | 3.032 | +0.014 |
| ANA | 0.322 | 0.320 | 0.320 | −0.002 |
| CAM | 0.364 | 0.363 | 0.366 | +0.002 |
| Understandability | −201.94 | −202.26 | −207.89 | −5.95 |
| Extendibility | 0.487 | 0.477 | 0.492 | +0.005 |

1.5.1 → 1.5.2 geçişi neredeyse sıfır değişim içerirken (**+1 sınıf**), 1.5.2 → 1.5.3 geçişi **+17 sınıf** ile bu serinin tek anlamlı büyümesini barındırmaktadır. Buna rağmen yoğunluk metrikleri sabit kalmıştır; Understandability bozulmasının tamamı bu boyut büyümesinden gelmektedir.

---

## 6. Genel Değerlendirme

| Boyut | Yargı | Gerekçe |
|-------|-------|---------|
| Büyüme kalitesi | ✅ Kontrollü | NOH büyümesi DSC'yi geçiyor; hiyerarşiler kullanılıyor |
| Soyutlama | ➡ Sabit | ANA +0.3 %; ne iyileşme ne kötüleşme |
| Coupling | ➡ Sabit | DCC +0.3 %; ihmal edilebilir |
| Cohesion | ➡ Sabit | CAM +0.7 %; ihmal edilebilir |
| Anlaşılırlık | ❌ DSC etkisiyle kötüleşiyor | −5.63 puan; tamamı boyut büyümesinden |
| Teknik borç (yeni) | ✅ Eklenmedi | Bu geçişte yeni borç sinyali yok |
| Teknik borç (kümülatif) | ⚠️ Devam ediyor | WMC_max = 381, LCOM_max = 4371 dokunulmadı |

> **Özet:** 1.5.2 → 1.5.3 geçişi, yoğunluk metriklerini hareket ettirmeyen sade bir **yama büyümesidir.** Olumlu tarafta: DCC kontrollü, yeni sınıflar mevcut mimari profiline uygun eklenmiş, yeni teknik borç oluşturulmamıştır. Olumsuz tarafta: DSC = +17 Understandability'yi 5.63 puan daha bozmuş; ANA ve cohesion'da iyileştirme fırsatı değerlendirilmemiştir. Kümülatif borç (WMC_max = 381, LCOM_max = 4371) bu sürümde de adreslenmedan geçilmiştir.

---

## 7. Belirsizlikler

- **Yoğunluk sabitliğinin kaynağı:** 17 yeni sınıfın tüm metrikleri bu denli sabit tutması dikkat çekicidir. Sınıfların mevcut kodun kopyası mı yoksa gerçekten bağımsız küçük yardımcı sınıflar mı olduğu sınıf düzeyi veri olmadan belirlenemez.
- **NOH artışının kalitesi:** 4 yeni hiyerarşinin hangi alana ait olduğu ve mevcut soyutlamalarla ilişkisi commit geçmişi incelenmeden netleştirilemeaz.

---

*Rapor QMOOD (Bansiya & Davis, 2002) temel alınarak hazırlanmıştır.*
