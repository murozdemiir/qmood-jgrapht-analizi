# LLM Kalite Değerlendirmelerinin Karşılaştırmalı ve Eleştirel Analizi (JGraphT)

> Aynı ana prompt (`prompts/01_full_evolution_prompt.txt`) **15 farklı LLM
> yapılandırmasına** aynı koşulda verilmiştir. Ek olarak `02` (tek sürüm) ve
> `03` (sürüm farkı) promptları da aynı 15 modele verilmiştir (toplam ~90 yanıt,
> `llm_responses/`). Bu belge **01 (tam evrim)** yanıtları üzerinden eleştirel
> karşılaştırmayı içerir.
> Puanlama: `src/llm_quality_scores.py` → `data/llm_qualitative_scores.csv`.
> Yüzeysel ölçüm: `src/compare_llm.py` → `data/llm_comparison.csv`.
> Görseller: `figures/fig_llm_ranking.png`, `fig_llm_qualitative.png`,
> `fig_llm_comparison.png`.

## 1. Test edilen modeller (15 yapılandırma)
| Sağlayıcı | Yapılandırmalar |
|---|---|
| OpenAI ChatGPT | `5_3_instantly`, `5_4_high`, `5_5_high`, `o3_medium` |
| Anthropic Claude | `opus_max`, `sonnet_max`, `haiku_extended` |
| DeepSeek | `expert`, `instantly` |
| Google Gemini | `pro_standart`, `pro_extended`, `flash_standart`, `flash_extended`, `flashlite_extended`, `flashliste-standart` |

## 2. Değerlendirme rubriği (8 kriter, 1–5)
1. **Sayısal Kanıt** — her iddianın metrik + yüzde ile desteklenmesi
2. **Denklem Doğruluğu** — QMOOD denklemlerini ve **metrik tanımlarını** doğru
   yorumlama (DSC = sınıf sayısı, NOM = metot sayısı; "satır" **değil**)
3. **DSC-Artefakt Farkındalığı** — Reusability/Functionality artışının ve
   Understandability çöküşünün **büyük ölçüde boyut (DSC) kaynaklı yapay**
   olduğunu görme *(JGraphT'de DSC 2.6× büyüdüğü için EN kritik kriter)*
4. **Zamansal Granülerlik** — ara sürüm kırılmalarını yakalama (1.1.0 LCOM
   sıçraması, 1.2.0 ANA çöküşü)
5. **Halüsinasyon Direnci** — verilmeyen sınıf adı / uydurma sayı (COCOMO borç,
   saat tahmini) ÜRETMEME
6. **Refactoring Somutluğu** — metrik-hedefli, uygulanabilir öneriler
7. **Sınırlama Farkındalığı** — ortalamaların hotspot gizlemesi, QMOOD'un
   kompozisyonu cezalandırma yanlılığı, normalize tutarsızlığı
8. **Analitik Derinlik** — genel olgunluk

## 3. Sıralama (toplam / 40)
| # | Model | Toplam | Ort. |
|---|---|---|---|
| 1 | **claude_opus_max** | 40 | 5.00 |
| 2 | claude_sonnet_max | 36 | 4.50 |
| 3 | chatgpt_5_5_high | 35 | 4.38 |
| 4 | chatgpt_5_4_high | 34 | 4.25 |
| 5 | gemini_pro_extended | 31 | 3.88 |
| 6 | gemini_pro_standart | 29 | 3.62 |
| 7 | chatgpt_o3_medium | 27 | 3.38 |
| 7 | claude_haiku_extended | 27 | 3.38 |
| 9 | gemini_flash_extended | 26 | 3.25 |
| 9 | gemini_flash_standart | 26 | 3.25 |
| 11 | deepseek_instantly | 25 | 3.12 |
| 11 | deepseek_expert | 25 | 3.12 |
| 13 | chatgpt_5_3_instantly | 24 | 3.00 |
| 14 | gemini_flashlite_extended | 23 | 2.88 |
| 15 | gemini-flashliste-standart | 19 | 2.38 |

## 4. Bulgular (eleştirel)

### 4.1 Niteliksel uzlaşı yüksek, ölçümlerimizle örtüşüyor
15 modelin tamamı çekirdek anlatıda birleşti: **"işlevsellik/yeniden
kullanılabilirlik artarken anlaşılabilirlik ve genişletilebilirlik geriliyor;
coupling (DCC +%29) ve karmaşıklık (WMC +%52, LCOM +%127) artıyor; teknik borç
birikiyor."** Bu, bizim metrik analizimizle birebir uyumludur (Extendibility
−%54, LCOM +%127, ANA −%48). Yani LLM'ler "kaba" sonucu güvenilir biçimde
buluyor.

### 4.2 EN ayırt edici kriter: DSC-artefaktı (extensive vs intensive)
JGraphT'de DSC **238 → 618 (2.6×)** büyüdüğü için, QMOOD denklemlerinde boyut
terimi taşıyan üç nitelik **mekanik olarak** şişer/çöker:
- Reusability "+%157", Functionality "+%156" artışı ve Understandability'nin
  "−126 puan" düşüşünün neredeyse tamamı **DSC terimidir**, gerçek tasarım
  değişimi değil.

Modeller bu konuda keskin ayrıştı:
- **`claude_opus_max`** bunu **sayısal kanıtladı:** Reusability(0.9.0)=120.47'nin
  **119'u (≈%98.8) yalnızca `0.50·DSC`** terimi; Understandability düşüşünün
  ≈%99'u `−0.33·ΔDSC`. Bu yüzden gerçek kaliteyi yalnızca **boyuttan bağımsız**
  nitelikler (Flexibility, Extendibility, Effectiveness) + CK ortalamaları
  üzerinden okudu. **En yüksek analitik derinlik.**
- `chatgpt_5_5_high`, `claude_sonnet_max`, `gemini_pro_extended` bunu niteliksel
  olarak doğru biçimde "yanıltıcı/boyut artefaktı" diye işaretledi.
- Zayıf modeller (`chatgpt_5_3_instantly`, `gemini-flashliste-standart`)
  "Reusability +%157 iyileşme" sonucunu **olduğu gibi** olumlu rapor etti —
  yanıltıcı.

### 4.3 Halüsinasyon: uzunluk ≠ rigor
- **`claude_haiku_extended` (619 satır, en uzun yanıt)** çarpıcı biçimde
  **uydurma sayılar** üretti: COCOMO temelli "13.600 problem puanı", "1.500–2.000
  saat refactoring", gerçekte var olmayan eşik değerleri ve örnek kodlarda hayalî
  sınıf adları (`GraphProcessor`, `WeightedEdgeManager`…). Bunlar **verilen toplu
  veriden türetilemez.** Gösterişli ama düşük rigor → halüsinasyon puanı düşük.
- `deepseek_instantly` refactoring hedefi olarak gerçek-gibi sınıf/paket adları
  (`GraphTests`, `GraphMetrics`, `org.jgrapht.alg`) uydurdu.

### 4.4 Metrik tanımı / kavram hataları
- **`deepseek_expert`** DSC'yi *"sınıf başına satır"*, NOM'u *"metot başına
  satır"* sandı — **yanlış tanım** (ikisi de sayımdır). Sonuçları kısmen
  geçersiz kılar.
- Birden çok Gemini (`flash_extended`, `flashlite_extended`) **ANA ile
  DIT_mean'i aynı metrik** gibi yazdı (bu veri setinde değerleri yakın olsa da
  kavramsal olarak farklıdırlar).
- `gemini_flash_standart`'ta bir kodlama bozulması (yabancı alfabe karakteri)
  görüldü.

### 4.5 Veri kalitemizi yakalayan model
`chatgpt_5_5_high`, VERİ 3'teki normalize tutarsızlığını tespit etti: ham
Reusability oranı ≈2.58× iken normalize tablo 1.74 gösteriyor. Bu, LLM'in
**verinin kendisini** eleştirebildiğinin kanıtıdır (raporda §6.4'e işlenebilir).

### 4.6 En sofistike içgörü: kompozisyon yanlılığı
En güçlü modeller (`opus_max`, `sonnet_max`, `gemini_pro_extended`), MOA +%87 /
MFA −%39 / DIT düşüşünü **bilinçli "kalıtım→kompozisyon" kayması** olarak okudu
ve QMOOD'un kalıtımı ödüllendirdiği için Extendibility/Effectiveness'i
**haksızca** cezalandırdığını belirtti. Bu nüans, ölçüsüz "mimari çöküş"
yorumundan ayrışan üst düzey bir okumadır.

### 4.7 Kademe/mod etkisi
- **Üst düzey reasoning modları** (Claude `opus/sonnet max`, ChatGPT `*_high`)
  açık ara önde; DSC-artefaktını ayrıştırma, kırılma noktası tespiti ve
  halüsinasyondan kaçınmada üstün.
- **Gemini Pro** sürümleri **Flash** sürümlerinden belirgin biçimde iyi;
  `flashliste-standart` (36 satır) en zayıf yanıt.
- İlginç anomali: **Claude Haiku** (hızlı/küçük kademe) "extended" modda çok uzun
  yazdı ama rigor düşük kaldı — **uzunluk derinlik garantisi değil.**

## 5. Genel sonuç
LLM'lerin niteliksel uzlaşısı yüksek ve bizim ölçümlerimizle örtüşüyor; asıl
ayrışma **derinlikte**. JGraphT gibi **hızlı büyüyen** (2.6×) bir sistemde QMOOD
metrikleri ağır biçimde boyut-karışımlıdır (size-confounded); yalnızca üst düzey
reasoning modelleri (özellikle `claude_opus_max`) boyut artefaktını gerçek
tasarım değişiminden ayırarak **doğru** kalite hikâyesini kurdu: *Extendibility
gerçekten geriledi (ANA/MFA çöküşü + DCC artışı), Flexibility hafif arttı
(kompozisyon), sınıf-içi sağlık (LCOM/WMC/MPC) belirgin bozuldu.* Pratik çıkarım:
**boyut-karışımlı metrik yorumunda LLM kullanılacaksa üst düzey reasoning modu
şarttır ve çıktı sınıf-düzeyi veriyle çapraz doğrulanmalıdır** — aksi halde
zayıf modeller "+%157 iyileşme" gibi yanıltıcı sonuçları olduğu gibi aktarıyor.
