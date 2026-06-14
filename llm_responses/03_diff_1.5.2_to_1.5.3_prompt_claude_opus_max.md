# JGraphT (jgrapht-core) 1.5.2 → 1.5.3 — Sürüm Farkı (Diff) Analizi

**Model:** QMOOD (Bansiya & Davis, 2002)
**Yaklaşım:** Eleştirel, kanıt temelli. Her metrik değişimi, etkilediği kalite niteliğine bağlanmıştır.

---

## 0. Özet Hüküm

Bu geçiş **küçük bir bakım sürümüdür** (DSC +%2.8). Önceki diff'lerden farklı olarak, bu kez **tüm metrik hareketleri ya sabit ya hafif olumlu** yöndedir; hiçbir metrik gerilemedi. Boyuttan bağımsız üç nitelik (Flexibility, Extendibility, Effectiveness) **hafifçe iyileşti**. Ancak değişimlerin büyüklüğü **gürültü/marjinal** bandda olduğundan bu, gerçek bir kalite sıçraması değil, **olumlu yönde küçük bir kayma**dır. Kritik nokta: 1.5.1/1.5.2'den beri süregelen **yapısal sorunlar (yüksek DCC, düşük ANA/MFA) bu sürümde de giderilmemiştir** — borç ödenmedi, sadece artmadı.

---

## 1. Tasarım Metriği Değişimlerinin Yorumu

| Metrik | 1.5.2 | 1.5.3 | Δ% | Yön | Kalite anlamı |
|---|---|---|---|---|---|
| DSC (boyut) | 601.0 | 618.0 | +2.8% | büyüme | +17 sınıf eklendi (küçük gelişim) |
| NOH (hiyerarşi) | 87.0 | 91.0 | +4.6% | büyüme | Boyutla orantılı |
| ANA (soyutlama) | 0.320 | 0.320 | +0.3% | ~sabit | Soyutlama düzeyi değişmedi |
| DAM (kapsülleme) | 0.881 | 0.885 | +0.5% | 🟢 hafif | Kapsülleme yüksek, çok az arttı |
| DCC (coupling) | 3.023 | 3.032 | +0.3% | ~sabit | Coupling neredeyse sabit (ama hâlâ yüksek) |
| CAM (cohesion) | 0.363 | 0.366 | +0.7% | 🟢 hafif | Kohezyon az da olsa **arttı** (önceki diff'in tersine) |
| MOA (kompozisyon) | 0.694 | 0.701 | +1.0% | 🟢 hafif | Kompozisyon az arttı |
| MFA (kalıtım) | 0.151 | 0.151 | +0.1% | ~sabit | Değişmedi (düşük seviyede sabit) |
| NOP (polimorfizm) | 3.507 | 3.545 | +1.1% | 🟢 hafif | Polimorfizm az arttı |
| CIS (arayüz) | 4.208 | 4.225 | +0.4% | ~sabit | Durağan |
| NOM (karmaşıklık) | 6.293 | 6.324 | +0.5% | ~sabit | Sınıf-başına metot çok az arttı |

**Ana gözlem — hareketlerin hizalanması:** Önceki sürümlerde (örn. 0.9.0→0.9.2'de CAM ve NOP düşmüştü) karışık sinyaller vardı. Burada **hiçbir metrik gerilemedi**; küçük de olsa CAM (+%0.7), NOP (+%1.1), MOA (+%1.0), DAM (+%0.5) hepsi yukarı, DCC neredeyse sabit. Bu, **temiz/düzenli bir küçük sürüm** profilidir.

**Ancak büyüklük uyarısı:** Metriklerin **9'u %1.1 veya altında** değişti. Bunlar tek tek anlamlı tasarım iyileşmeleri olarak değil, **gürültü mertebesinde küçük dalgalanmalar** olarak okunmalıdır. Yalnızca DSC (+%2.8) ve NOH (+%4.6) gerçek (boyut kaynaklı) hareketlerdir.

---

## 2. Kalite Niteliklerine Etkisi (Denklem Üzerinden)

Ham nitelik değerleri (referans):

| Nitelik | 1.5.2 | 1.5.3 | Δ% | Yorum |
|---|---|---|---|---|
| Reusability | 301.94 | 310.45 | +2.8% | **Boyut kaynaklı** (DSC); kalite kanıtı değil |
| Functionality | 153.10 | 157.73 | +3.0% | **Boyut kaynaklı** (DSC+NOH); kalite kanıtı değil |
| Understandability | −202.26 | −207.89 | daha negatif | Çoğunlukla DSC artışı (boyut etkisi) |
| **Flexibility** | 1.5650 | 1.5861 | **+1.3%** | Boyuttan bağımsız — hafif iyileşti |
| **Extendibility** | 0.4774 | 0.4923 | **+3.1%** | Boyuttan bağımsız — iyileşti (ama hâlâ düşük) |
| **Effectiveness** | 1.1105 | 1.1205 | **+0.9%** | Boyuttan bağımsız — hafif iyileşti |

> Not: Reusability/Functionality artışları **DSC ile şişer**; "kalite arttı" diye okunmamalı. Understandability'nin daha negatif olması da boyut etkisidir. Dürüst sinyal boyuttan bağımsız üç nitelikte ve bu kez **üçü de pozitif**.

**Neden Extendibility iyileşti (+%3.1)?**
`Extendibility = 0.50·(ANA+MFA+NOP) − 0.50·DCC`
ANA ve MFA neredeyse sabit; iyileşmenin **tamamına yakını NOP artışından** geliyor (+0.038 → katkı +0.019). DCC artışı (+0.009 → ceza +0.0046) bunu kısmen törpülüyor. Sorumlu metrik: **NOP**.
**Önemli uyarı:** %3.1 artışa rağmen Extendibility hâlâ **0.4923 ile en zayıf nitelik**. DCC=3.032 cezası pozitif potansiyelin **~%75'ini** silmeye devam ediyor. Yani yön olumlu, ama **seviye hâlâ kötü**.

**Neden Flexibility iyileşti (+%1.3)?**
`Flexibility = 0.25·DAM − 0.25·DCC + 0.50·MOA + 0.50·NOP`
NOP (+0.038) ve MOA (+0.0068) kazanımları, DCC artışının (+0.009) küçük cezasını aştı. Sorumlu metrikler: **NOP, MOA**.

**Neden Effectiveness iyileşti (+%0.9)?**
`Effectiveness = 0.20·(ANA+DAM+MOA+MFA+NOP)`
NOP, MOA, DAM'deki küçük artışların toplamı. Negatif terim olmadığı için tüm küçük kazanımlar birikti.

---

## 3. Olumlu mu, Olumsuz mu?

**Yön olumlu, ama büyüklük marjinal.** Gerekçe:
- ✅ Boyuttan bağımsız üç niteliğin **üçü de** yükseldi (Flexibility +%1.3, Extendibility +%3.1, Effectiveness +%0.9).
- ✅ Hiçbir tasarım metriği gerilemedi; CAM bile (önceki diff'in tersine) hafif arttı.
- ✅ %2.8 büyümeye rağmen coupling sabit kaldı (DCC +%0.3).
- 🟡 Ancak değişimler gürültü bandında; **gerçek bir kalite sıçraması değil**.
- 🔴 Yapısal zayıflıklar **dokunulmadan duruyor**: DCC hâlâ 3.03 (yüksek), ANA 0.32 / MFA 0.15 (çok düşük), Extendibility 0.49 (kötü).

**Net:** Kalite açısından **hafif pozitif, temiz bir küçük sürüm** — ama köklü iyileşme yok. "İyi yönde, küçük adım" demek doğru olur; abartılmamalı.

---

## 4. Teknik Borç İşareti Var mı?

**Yeni borç işareti yok; mevcut borç ödenmedi, dondurulmuş durumda.**

- ❌ **Yeni borç yok:** DCC (+%0.3), NOM (+%0.5), CAM (+%0.7 — iyileşme yönünde). Hiçbir metrik borç biriktiren yönde hareket etmedi.
- 🔴 **Mevcut borç sabit:** ANA (0.32) ve MFA (0.15) **değişmedi** (+%0.3 / +%0.1). Yüksek coupling (DCC≈3.03) korunuyor. Yani önceki sürümlerden devralınan **yapısal borç bu sürümde de adreslenmemiş** — sadece büyümedi.

> Belirsizlik notu: Bu prompttaki veride CK **maksimum** değerleri (LCOM_max, WMC_max, MPC_max) yer almıyor. Önceki sürümlerde tespit edilen **god class** sorununun (1.5.2'de LCOM_max=4371, WMC_max=381) bu sürümde giderilip giderilmediği **bu veriden doğrulanamaz**. Ortalama metriklerdeki durağanlık (LCOM/WMC değişmedi) gidersilmediğine işaret eder ama kesin değildir.

---

## Özet Tablo

| Soru | Yanıt |
|---|---|
| Değişimin karakteri | Küçük, **temiz bakım** sürümü (DSC +%2.8) |
| Metrik hareketleri | Tümü sabit veya hafif olumlu; gerileyen yok |
| Kalite açısından net | **Hafif pozitif** (Flexibility +%1.3, Extendibility +%3.1, Effectiveness +%0.9) — ama gürültü bandında |
| Asıl iyileşme sürücüsü | **NOP** (polimorfizm) artışı + MOA |
| Kalıcı sorun | DCC hâlâ yüksek (3.03), ANA/MFA çok düşük, Extendibility hâlâ kötü (0.49) |
| Teknik borç | Yeni işaret **yok**; mevcut yapısal borç **ödenmedi** (dondurulmuş) |

*Belirsizlik notu: <%1.1'lik metrik değişimleri gürültü mertebesindedir; tek tek büyütülmemiştir. Reusability/Functionality artışları DSC ile şiştiğinden kalite kanıtı sayılmamıştır. CK max verisi olmadığından god class durumu doğrulanamamıştır. Yorumlar yalnızca verilen sayılara dayanır.*
