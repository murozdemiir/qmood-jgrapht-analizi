# JGraphT 1.5.2 — QMOOD Kalite İncelemesi

Bu rapor, **JGraphT 1.5.2** sürümüne ait QMOOD tasarım metrikleri ve türetilen
kalite niteliklerine dayanarak eleştirel ve kanıt temelli bir değerlendirme sunar.

## Özet

| Nitelik | Değer |
|---------|------:|
| Reusability | 301.9390 |
| Flexibility | 1.5650 |
| Understandability | -202.2567 |
| Functionality | 153.1010 |
| Extendibility | 0.4774 |
| Effectiveness | 1.1105 |


En düşük iki kalite niteliği **Understandability** ve **Extendibility**’dir.

---

## 1. Zayıf Kalite Nitelikleri ve Sorumlu Metrikler

| Nitelik | Kritik Metrikler | Gözlenen Değerler | Neden Olumsuz? |
|---------|-----------------|------------------:|----------------|
| Understandability | DSC, DCC, NOM, NOP vs. DAM, CAM | DSC = 601, DCC = 3.02, NOM = 6.29, NOP = 3.51,<br> DAM = 0.88, CAM = 0.36 | DSC’nin 0.9.0’daki 238 → 601’e çıkarak **+153 %** büyümesi ve DCC’nin 2.35 → 3.02’ye yükselmesi, negatif terimleri büyüttü. DAM/CAM artışı yetersiz kaldı. |
| Extendibility | ANA, MFA, NOP, DCC | ANA = 0.32, MFA = 0.15, NOP = 3.51, DCC = 3.02 | Düşük soyutlama (ANA) ve kalıtım kullanımı (MFA) artı yüksek coupling (DCC) 0.48 gibi çok sınırlı bir puanla sonuçlandı. |

---

## 2. Refactoring Önerileri

1. **Soyutlama Katmanları Ekleyin**  
   - **Amaç:** ANA değerini ≥ 0.5’e çıkarmak, Understandability & Extendibility’yi artırmak.  
   - **Yöntem:** Sık kullanılan veri yapıları ve algoritma aileleri için `GraphAlgorithm` gibi arayüzler tanımlayın; somut sınıfları bu arayüzlerden türetin.

2. **Bağımlılıkları Azaltın (Coupling ↓)**  
   - **Amaç:** DCC’yi < 2.5’e çekmek.  
   - **Yöntem:**  
     - Paket sınırları arasında *Dependency Inversion* prensibi uygulayın.  
     - Ortak yardımcı işlevleri `util` paketlerine ayırın, doğrudan sınıf-sınıf bağımlılıklarını azaltın.

3. **Şablon veya Strateji Desenleri ile Kalıtımı Artırın**  
   - **Amaç:** MFA ve NOP’u artırarak genişletilebilirlik için “open for extension, closed for modification” yaklaşımını sağlamak.  
   - **Yöntem:**  
     - Örneğin farklı ağırlıklandırma şemaları için `EdgeWeighter` strateji arayüzü ekleyin.  
     - Var olan büyük `*Utils` sınıflarını soyut sınıflara bölüp alt sınıflarla özelleştirin.

Her öneri yüksek **metrik-etki**–**maliyet** oranı hedefler; önce küçük mimari dokunuşlarla Understandability ve Extendibility’nin iyileştirilmesi beklenir.

---

> Rapor, verilen ham metrikler (DSC = 601, DCC = 3.02, ANA = 0.32, vb.) temel alınarak oluşturulmuştur; tahmine dayalı çıkarımlar yapılmamıştır.
