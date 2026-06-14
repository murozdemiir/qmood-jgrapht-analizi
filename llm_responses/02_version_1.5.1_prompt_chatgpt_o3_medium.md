# JGraphT 1.5.1 — QMOOD Kalite Değerlendirmesi

## En Zayıf Kalite Nitelikleri

| Nitelik | Değer | Neden Zayıf? (formül bileşenleri) |
|---------|-------|-----------------------------------|
| **Understandability** | **-201.94** | Büyük negatif katkılar: yüksek **DSC = 600** (sistem boyutu), yüksek **DCC = 3.02** (coupling), yüksek **NOP = 3.52** (polimorfizm sayısı), yüksek **NOM = 6.32** (metot karmaşıklığı). Pozitif etkili **DAM = 0.88** ve **CAM = 0.36** bu eksiği dengelemeye yetmiyor. |
| **Extendibility** | **0.49** | Formül: *0.5 × (ANA+MFA+NOP) − 0.5 × DCC*. Düşük **ANA = 0.32** (soyutlama) ve **MFA = 0.15** (kalıtım yoğunluğu) artı yüksek **DCC = 3.02** değeri, potansiyel genişletilebilirliği baskılıyor. |

(Referans: QMOOD denklemleri ve 1.5.1 sürüm metrikleri.)

## Sorumlu Tasarım Metrikleri

| Met­rik | Değer | Etkisi |
|---------|-------|--------|
| **DCC** (Coupling) | 3.02 | Yüksek bağlılık, Understandability & Extendibility’yi düşürüyor. |
| **DSC** (Boyut) | 600 | Sistem genişliği arttıkça anlamak zorlaşıyor. |
| **NOP** (Polimorfizm) | 3.52 | Yarar sağlar; fakat diğer olumsuz faktörlerle birlikte Understandability’yi baskılıyor. |
| **NOM** (Karmaşıklık) | 6.32 | Yüksek metod karmaşıklığı, kodu okuma–anlama maliyetini artırıyor. |
| **MFA** (Kalıtım Faktörü) | 0.15 | Düşük kalıtım kullanımı, kodun genişletilebilirliğini sınırlandırıyor. |
| **ANA** (Soyutlama) | 0.32 | Az arayüz/soyut sınıf, yeni özellik eklemeyi zorlaştırıyor. |

> **Özet:** Anlaşılabilirlik, büyük kod tabanı ve yüksek coupling nedeniyle; genişletilebilirlik ise zayıf soyutlama & kalıtım ile sınırlı.

## Refactoring Önerileri

1. ### **God‑Class Ayrıştırması**
   *Kanıt:* `WMC_max = 381`, `LCOM_max = 4371` verileri tek başına devasa ve düşük kohezyonlu sınıflar olduğunu gösteriyor.  
   **Yapılacaklar:**  
   - Sınıfları sorumluluklarına göre *Extract Class* / *Extract Method* ile böl.  
   - Karmaşık metotları sadeleştir; tekrar eden kodu yardımcı sınıflara taşı.  
   **Beklenen Etki:** NOM ve WMC düşer; CAM yükselir → Understandability artar.

2. ### **Coupling’i Azaltmak için Katmanlı Mimari**
   *Kanıt:* `CBO_mean = 3.02`, `CBO_max = 21`. Yüksek bağımlılık, DCC’yi ve bakım maliyetini yükseltiyor.  
   **Yapılacaklar:**  
   - Modüller arası arayüz tanımlayarak bağımlılıkları tersine çevir (Dependency Inversion).  
   - Ortak kodu ayırmak için *Facade* veya *Service* katmanı oluştur.  
   **Beklenen Etki:** DCC ve CBO azalır → Understandability & Extendibility artar.

3. ### **Soyutlama/Kalıtımın Stratejik Artırılması**
   *Kanıt:* `ANA = 0.32` ve `MFA = 0.15` — soyutlama ve kalıtım az kullanılmış.  
   **Yapılacaklar:**  
   - Tekrarlayan davranışları üst sınıfa/arayüze taşı; alt sınıflar gerçeklemeleri sağlar.  
   - Karmaşık koşullu ifadeleri *Polymorphic Dispatch* ile değiştir.  
   **Beklenen Etki:** ANA ve MFA yükselir, DCC bir miktar düşer → Extendibility ve Reusability gelişir.

---
*Hazırlayan:* **Kıdemli Yazılım Mimarisi & Kalite Uzmanı**  
*Kaynak:* QMOOD metrikleri, JGraphT 1.5.1 sürümü (veri 15 Haz 2026).