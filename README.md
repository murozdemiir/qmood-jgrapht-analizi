# QMOOD Tabanlı Yazılım Kalitesi Analizi ve LLM Destekli Değerlendirme

**Ders:** Yazılım Mimarileri ve Tasarım Yöntemleri — Dönem Projesi
**Analiz edilen sistem:** [JGraphT](https://github.com/jgrapht/jgrapht) — `jgrapht-core` modülü (açık kaynak Java graf teorisi kütüphanesi)
**İncelenen sürüm sayısı:** 11 (JGraphT 0.9.0 → 1.5.3)

## Amaç
Nesne yönelimli bir yazılım sisteminin **11 farklı sürümünü** QMOOD (Quality Model
for Object-Oriented Design) modeline göre analiz ederek yazılımın zaman içindeki
kalite değişimini ölçmek; ardından aynı metrik verilerini farklı **Büyük Dil
Modellerine (LLM)** vererek kalite değerlendirme yeteneklerini karşılaştırmak.

> Hiçbir hazır metrik aracı kullanılmamıştır. Tüm metrikler `javalang` ile
> kaynak koddan **kendi yazdığımız çözümleyici** ile çıkarılmıştır
> (yönerge: "hazır analiz sonuçlarının doğrudan kullanılması yasaktır").

**Neden JGraphT?** Tek ve sürekli git geçmişine, zengin nesne yönelimli tasarıma
(graf tipi hiyerarşisi: `Graph` → `AbstractGraph` → `SimpleGraph`/
`DirectedPseudograph`…, ve geniş algoritma sınıfı ailesi — güçlü kalıtım ve
polimorfizm) ve **belirgin bir evrime** sahiptir: 0.9.0 → 1.0.0 büyük yeniden
yazımı dahil, `jgrapht-core` modülü **182 → 464 Java dosyasına** (≈2.5×) büyür.
Bu büyüme, QMOOD'un soyutlama/kalıtım/polimorfizm metriklerini ve "yazılım
büyüdükçe kalite değişimi" analizini anlamlı kılar.

## Klasör yapısı
```
proje-jgrapht/
├── src/
│   ├── fetch_versions.py   # JGraphT sürümlerini indirir (git archive)
│   ├── metrics.py          # Java kaynaktan sınıf düzeyi OO metrik çıkarımı
│   ├── qmood.py            # QMOOD tasarım metrikleri + kalite nitelikleri
│   ├── analyze.py          # tüm sürümleri işler, CSV üretir
│   ├── visualize.py        # grafikler (figures/)
│   └── run_all.py          # QMOOD analiz pipeline'ı
├── data/                   # CSV çıktıları + indirilen kaynak sürümler
└── figures/                # PNG grafikler
```
> `prompts/`, `llm_responses/` ve `report/` klasörleri sonraki adımlarda
> (prompt hazırlığı → LLM yanıtları → karşılaştırma → rapor) eklenecektir.

## Çalıştırma
```bash
pip install -r requirements.txt
# Windows'ta Türkçe yol için UTF-8:
#   PowerShell:  $env:PYTHONUTF8=1
python src/run_all.py            # fetch + analyze + visualize
```

## Hesaplanan metrikler
**CK takımı (sınıf düzeyi):** DIT, NOC, WMC, CBO, RFC, LCOM, NOM, NOA, MPC, DAC
**QMOOD tasarım metrikleri (sistem düzeyi):** DSC, NOH, ANA, DAM, DCC, CAM, MOA,
MFA, NOP, CIS, NOM
**QMOOD kalite nitelikleri:** Reusability, Flexibility, Understandability,
Functionality, Extendibility, Effectiveness

## Referanslar
- J. Bansiya, C. G. Davis, "A Hierarchical Model for Object-Oriented Design
  Quality Assessment," *IEEE TSE*, 2002.
- S. R. Chidamber, C. F. Kemerer, "A Metrics Suite for Object Oriented Design,"
  *IEEE TSE*, 1994.
- JGraphT — https://github.com/jgrapht/jgrapht
