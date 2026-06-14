# JGraphT (jgrapht-core) 0.9.0 → 0.9.2 — Sürüm Farkı (Diff) Analizi

**Model:** QMOOD (Bansiya & Davis, 2002)
**Yaklaşım:** Eleştirel, kanıt temelli. Her metrik değişimi, etkilediği kalite niteliğine bağlanmıştır.

---

## 0. Özet Hüküm

Bu geçiş, **sağlıklı bir büyüme sürümü** karakteri taşır. Sistem %12 büyürken (DSC 238 → 267) **ortalama coupling neredeyse hiç artmamıştır (DCC +%0.6)** ve soyutlama/kompozisyon/kalıtım göstergeleri iyileşmiştir. Tek belirgin uyarı **kohezyon düşüşüdür (CAM −%4.8)**. Net etki: **hafifçe pozitif-nötr**; yapısal bir teknik borç birikimi paterni **henüz yok**, ancak kohezyon izlenmelidir.

---

## 1. Tasarım Metriği Değişimlerinin Yorumu

| Metrik | 0.9.0 | 0.9.2 | Δ% | Yön | Kalite anlamı |
|---|---|---|---|---|---|
| DSC (boyut) | 238.0 | 267.0 | +12.2% | büyüme | +29 sınıf eklendi (özellik gelişimi) |
| NOH (hiyerarşi) | 35.0 | 39.0 | +11.4% | büyüme | Hiyerarşi sayısı boyutla orantılı arttı |
| **ANA (soyutlama)** | 0.618 | 0.670 | **+8.5%** | 🟢 iyi | Ortalama ata sayısı arttı → daha güçlü soyutlama |
| DAM (kapsülleme) | 0.899 | 0.894 | −0.6% | ~sabit | Kapsülleme yüksek ve durağan |
| **DCC (coupling)** | 2.349 | 2.363 | **+0.6%** | 🟢 iyi | %12 büyümeye rağmen neredeyse sabit |
| **CAM (cohesion)** | 0.407 | 0.387 | **−4.8%** | 🔴 dikkat | Tek belirgin olumsuz sinyal |
| **MOA (kompozisyon)** | 0.374 | 0.405 | **+8.2%** | 🟢 iyi | Kompozisyon kullanımı arttı |
| **MFA (kalıtım)** | 0.247 | 0.272 | **+10.2%** | 🟢 iyi | Kalıtımla işlevsel yeniden kullanım arttı |
| NOP (polimorfizm) | 3.273 | 3.191 | −2.5% | 🟡 hafif | Polimorfik metot oranı biraz düştü |
| CIS (arayüz) | 3.920 | 3.914 | −0.2% | ~sabit | Arayüz boyutu durağan |
| NOM (karmaşıklık) | 5.155 | 5.240 | +1.6% | ~sabit | Sınıf-başına metot çok az arttı |

**En güçlü pozitif kanıt — boyut/coupling ayrışması:** Sistem **%12.2** büyürken DCC yalnızca **%0.6** arttı. DCC burada sınıf-başına ortalama coupling olduğundan, bu **29 yeni sınıfın iyi izole edildiğini** gösterir. Büyüme genelde coupling'i yukarı çeker; burada çekmemesi en olumlu bulgudur.

**İkincil pozitif kanıt — yapısal olgunlaşma:** ANA (+%8.5), MOA (+%8.2) ve MFA (+%10.2) birlikte yükseldi. Yani yeni kod hem daha soyut hem kompozisyon/kalıtımı daha bilinçli kullanır biçimde eklenmiş.

**Tek olumsuz kanıt — kohezyon:** CAM −%4.8 düştü. Sınıflar tek sorumluluk etrafında biraz daha az toplanıyor. Büyüme dönemlerinde sık görülen, ama izlenmesi gereken bir sinyal.

---

## 2. Kalite Niteliklerine Etkisi (Denklem Üzerinden)

Ham nitelik değerleri (referans):

| Nitelik | 0.9.0 | 0.9.2 | Δ | Yorum |
|---|---|---|---|---|
| Reusability | 120.47 | 134.96 | +12.0% | **Boyut kaynaklı** (DSC denklemi eziyor); kalite kanıtı değil |
| Functionality | 61.69 | 68.93 | +11.7% | **Boyut kaynaklı** (DSC+NOH); kalite kanıtı değil |
| Understandability | −81.87 | −91.47 | daha negatif | Çoğunlukla DSC artışı (boyut etkisi) |
| **Flexibility** | 1.4611 | 1.4303 | **−2.1%** | Boyuttan bağımsız — hafif düştü |
| **Extendibility** | 0.8944 | 0.8851 | **−1.0%** | Boyuttan bağımsız — hafif düştü |
| **Effectiveness** | 1.0821 | 1.0863 | **+0.4%** | Boyuttan bağımsız — hafif yükseldi |

> Not: Reusability/Functionality artışları **DSC ile şişer**; bu nedenle bunları "kalite arttı" diye okumak yanıltıcıdır. Dürüst sinyal boyuttan bağımsız üç nitelikte (Flexibility, Extendibility, Effectiveness).

**Neden Flexibility düştü (−%2.1)?**
`Flexibility = 0.25·DAM − 0.25·DCC + 0.50·MOA + 0.50·NOP`
MOA kazanımı (+0.031 → katkı +0.0155) olumlu olsa da, **NOP düşüşü** (−0.082 → katkı −0.041) bunu bastırıyor. Sorumlu metrik: **NOP**.

**Neden Extendibility düştü (−%1.0)?**
`Extendibility = 0.50·(ANA+MFA+NOP) − 0.50·DCC`
ANA (+0.052) ve MFA (+0.025) yükseldi; ancak **NOP düşüşü** (−0.082) ve hafif **DCC artışı** (+0.014) net etkiyi negatife çevirdi. Sorumlu metrikler: **NOP + DCC**.

**Neden Effectiveness yükseldi (+%0.4)?**
`Effectiveness = 0.20·(ANA+DAM+MOA+MFA+NOP)`
ANA/MOA/MFA kazanımları (+0.052+0.031+0.025 = +0.108), DAM/NOP kayıplarını (−0.087) aştı. Sorumlu metrikler: **ANA, MOA, MFA**.

---

## 3. Olumlu mu, Olumsuz mu?

**Karışık ama net biçimde pozitife yakın.** Gerekçe:
- ✅ Coupling disiplini korundu (DSC +%12.2'ye karşı DCC +%0.6).
- ✅ Soyutlama, kompozisyon, kalıtım birlikte iyileşti (ANA/MOA/MFA).
- ✅ Kapsülleme yüksek ve durağan (DAM ≈ 0.90).
- 🔴 Kohezyon geriledi (CAM −%4.8) → tek belirgin zayıflık.
- 🟡 Polimorfizm düşüşü (NOP −%2.5), Flexibility ve Extendibility'yi hafifçe aşağı çekti.

Boyuttan bağımsız üç nitelikteki değişim ±%2 bandında ve karışık olduğundan, kalite açısından bu sürüm **küçük net etkili, eğilimi pozitif** bir büyüme adımıdır. Abartılmamalı: dramatik bir iyileşme de, bozulma da değil.

---

## 4. Teknik Borç İşareti Var mı?

**Belirgin/yapısal bir borç birikimi sinyali yok; yalnızca tek bir erken uyarı var.**

- ❌ **Coupling borcu yok:** DCC +%0.6 — büyümeye rağmen coupling birikmedi. (Borç paterni tam tersi olurdu.)
- ❌ **Karmaşıklık borcu yok:** NOM +%1.6 — ihmal edilebilir.
- 🟡 **Tek erken sinyal — kohezyon:** CAM −%4.8. Tek başına alarm değil, ama ileride DCC artışıyla birleşirse borç çekirdeği olabilir. **İzlenmeli.**

> Belirsizlik notu: Bu yalnızca iki sürüm arası tek bir adımdır; CAM düşüşünün kalıcı bir eğilim mi yoksa tek seferlik dalgalanma mı olduğu bu veriden anlaşılamaz. Birkaç sürümlük seri gerekir.

---

## Özet Tablo

| Soru | Yanıt |
|---|---|
| Değişimin karakteri | Sağlıklı **büyüme** sürümü (DSC +%12.2) |
| En güçlü pozitif | Coupling sabit kaldı (DCC +%0.6) + ANA/MOA/MFA arttı |
| Tek olumsuz | Kohezyon düştü (CAM −%4.8) |
| Kalite açısından net | Hafif pozitife yakın; boyuttan bağımsız nitelikler ±%2 bandında karışık |
| Teknik borç | Yapısal işaret **yok**; CAM düşüşü tek **erken uyarı** |

*Belirsizlik notu: Reusability/Functionality artışları DSC ile şiştiğinden kalite kanıtı sayılmamıştır. Yorumlar yalnızca verilen sayılara dayanır; tek adımlık diff, uzun vadeli eğilim için yeterli değildir.*
