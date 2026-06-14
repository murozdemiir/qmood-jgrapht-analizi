# JGraphT 1.5.3 Sürümü Teknik Kalite ve Mimari Değerlendirme Raporu

**Rol:** Yazılım Mimarisi ve Kalite Uzmanı
**Analiz Konusu:** JGraphT 1.5.3 (QMOOD ve CK Metrikleri)

---

## 1. Genel Kalite Değerlendirmesi
JGraphT 1.5.3, kütüphanenin büyümesini (DSC: 618) sürdürdüğünü ve fonksiyonel derinliğinin (Functionality: 157.73) arttığını göstermektedir. Ancak, tasarım metrikleri sistemin karmaşıklığının yönetilebilirliğinin ötesine geçtiğine dair güçlü işaretler vermektedir. Özellikle `Understandability` skorundaki erozyon, sistemin teknik borcunun mimariyi baskıladığını kanıtlamaktadır.

## 2. En Zayıf 2 Kalite Niteliği ve Sorumlu Metrikler

Analiz edilen veriler ışığında, sistemin kalitesini en çok kısıtlayan iki nitelik şunlardır:

### A. Understandability (Anlaşılabilirlik) | Skoru: -207.89
Bu niteliğin negatifliği, sistemin artık "bilişsel olarak karmaşık" bir yapıya dönüştüğünü gösterir.
* **Sorumlu Metrikler:**
    * **DSC (618.0):** QMOOD denkleminde `DSC` (sınıf sayısı) negatif katsayı ile çarpıldığı için, sistem büyüdükçe bu nitelik kaçınılmaz olarak düşmektedir.
    * **LCOM_max (4371) ve LCOM_mean (31.24):** `LCOM` (Lack of Cohesion in Methods) değerlerinin yüksekliği, sınıfların içindeki metodların birbirinden bağımsız ve kopuk olduğunu gösterir. Bu durum, sınıfların anlaşılmasını zorlaştıran temel etkendir.

### B. Extendibility (Genişletilebilirlik) | Skoru: 0.492
Sistemin değişime karşı gösterdiği direnç artmaktadır. 
* **Sorumlu Metrikler:**
    * **ANA (0.3204):** Soyutlama seviyesi kritik düzeyde düşüktür. Soyut sınıfların ve arayüzlerin eksikliği, sistemin esnek genişlemesini kısıtlamaktadır.
    * **DCC (3.0324):** Sınıflar arası yüksek bağımlılık (coupling), yeni bir özellik eklerken diğer modüllerde kırılmalara yol açma riskini artırmaktadır.



---

## 3. Somut Refactoring Önerileri

Mevcut CK ve QMOOD metrikleri doğrultusunda, mimariyi rahatlatmak için aşağıdaki 3 refactoring adımı önerilmektedir:

1.  **Sorumluluk Ayrıştırma (Decomposition of God Classes):** `WMC_max (381)` ve `LCOM_max (4371)` değerleri, bazı sınıfların çok fazla işlev yüklendiğini göstermektedir. Bu "God Class" yapıları, *Extract Class* yöntemi ile küçük, yüksek uyumlu (high cohesion) ve yönetilebilir sınıflara bölünmelidir.
2.  **Soyutlama Katmanlarını Genişletme:** `ANA (0.3204)` değerini yükseltmek amacıyla, doğrudan somut sınıf bağımlılıkları yerine arayüz (Interface) tabanlı programlama prensibi benimsenmelidir. Bu, sistemin modülerliğini ve genişletilebilirliğini artıracaktır.
3.  **Bağımlılıkları Düşürme (Reduce Coupling):** `RFC_max (149)` değeri, sınıfların çok sayıda farklı metodla etkileşime girdiğini göstermektedir. Bu etkileşimi azaltmak için *Dependency Injection* deseninin uygulanması ve sınıflar arası "message-passing" (CIS) yükünün minimize edilmesi hedeflenmelidir.

---
*Not: Bu analiz, Bansiya & Davis (2002) QMOOD modeli ve CK metrikleri referans alınarak, JGraphT 1.5.3 verileri üzerinden gerçekleştirilmiştir.*