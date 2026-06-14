# JGraphT Kütüphanesi - QMOOD ve Mimari Kalite Analiz Raporu

**Hazırlayan:** Kıdemli Yazılım Mimarı ve Kalite Uzmanı
**Konu:** JGraphT (0.9.0 - 1.5.3) Sürümleri Arası Nesne Yönelimli Tasarım Metrikleri Analizi

---

## 1. Genel Kalite Değerlendirmesi
JGraphT kütüphanesi, incelenen sürümler boyunca (0.9.0'dan 1.5.3'e) ciddi bir **büyüme (Scale)** yaşamıştır. `DSC` (Design Size in Classes) 238'den 618'e çıkarak 2.6 kat artış göstermiştir.

* **İyileşen Alanlar:** `Functionality` (Fonksiyonellik) 61.69'dan 157.73'e yükselmiştir. Bu, kütüphanenin yeni özellikler, algoritmalar ve yetenekler açısından doygunluğa ulaştığını gösterir. `Reusability` (Yeniden Kullanılabilirlik) skoru 120'den 310'a çıkmıştır; bu büyük oranda `DSC` ve `CIS` (arayüz sayısı) artışıyla tetiklenen aritmetik bir yükseliştir.
* **Bozulan Alanlar:** `Extendibility` (Genişletilebilirlik) çok ciddi bir düşüş yaşamıştır (0.89 -> 0.49). Bunun temel sebebi `ANA` (Abstraction/Soyutlama) metriğinin 0.61'den 0.32'ye düşmesidir. Sistem büyürken soyutlama seviyesi düşmüş, bu da yeni özellik eklemeyi daha maliyetli hale getirmiştir.

---

## 2. Bakım Yapılabilirlik (Maintainability) Analizi
Bakım yapılabilirlik, QMOOD modelinde `Understandability` (Anlaşılabilirlik) metriği ile doğrudan ilişkilidir.

* **Düşüş Trendi:** `Understandability` -81.86'dan -207.89'a gerileyerek kütüphanenin okunabilirliğinin ciddi oranda düştüğünü göstermektedir.
* **Kanıt:** * `DCC` (Coupling/Bağlaşım): 2.34 -> 3.03. Sınıflar arası bağımlılık artmış.
    * `LCOM` (Lack of Cohesion in Methods): 13.7 -> 31.2. Metotlar arası bağdaşıklık (cohesion) kaybı, sınıfların "God Object" veya çok amaçlı, karmaşık yapılara dönüştüğünü gösterir.
* **Sonuç:** Kod tabanı karmaşıklaşmıştır. Yeni bir geliştiricinin sistemi anlaması ve güvenle değişiklik yapması, artan `WMC` (Sınıf başına ağırlıklı metot sayısı: 10.3 -> 15.7) ve `DCC` nedeniyle zorlaşmaktadır.

---

## 3. Teknik Borç (Technical Debt) Tahmini
Metrikler, ciddi bir teknik borç birikimine işaret etmektedir:

| Metrik | Başlangıç (0.9.0) | Son (1.5.3) | Yorum |
| :--- | :--- | :--- | :--- |
| **DCC** | 2.34 | 3.03 | Yüksek bağlaşım; modülerliği tehdit ediyor. |
| **LCOM** | 13.75 | 31.23 | Düşük kohezyon; SRP (Single Responsibility) ihlali. |
| **ANA** | 0.61 | 0.32 | Soyutlama kaybı; "Kod Tekrarı" riskini artırıyor. |
| **WMC** | 10.36 | 15.78 | Karmaşıklık artışı; test yazmayı zorlaştırıyor. |

**Teşhis:** Sistemde "Architectural Erosion" (Mimari erozyon) belirtileri vardır. Artan `LCOM` ve `WMC`, sınıfların artık tek bir sorumluluğa sahip olmadığını, zamanla fonksiyonellik eklenirken sınıfların "şiştiğini" kanıtlamaktadır.

---

## 4. Refactoring Önerileri

Mevcut metrik eğilimlerini tersine çevirmek için aşağıdaki mühendislik adımları atılmalıdır:

1.  **LCOM İyileştirmesi (Interface Segregation):** 31.23'e çıkan LCOM değerini düşürmek için, karmaşık sınıfları (God Objects) parçalara ayırın. `Single Responsibility Principle` (SRP) gereği, bir sınıf içindeki metotları daha anlamlı alt sınıflara (Composition ile) taşıyın.
2.  **DCC'nin (Bağlaşım) Azaltılması:** Sınıflar arası doğrudan bağımlılıklar artmıştır. `Dependency Injection` ve `Event-driven` mimari yaklaşımları kullanarak bileşenler arasındaki sıkı bağımlılığı gevşetin (decoupling).
3.  **Soyutlama (ANA) Restorasyonu:** `ANA` 0.61'den 0.32'ye düşmüştür. Arayüzleri (`Interface`) ve soyut sınıfları (`Abstract Class`) yeniden gözden geçirin. Uygulama kodunu somut sınıflara değil, arayüzlere bağımlı hale getirerek extendibility'i artırın.
4.  **Ölü Kod Temizliği:** `DSC` (618) artarken `MFA` (Method Inheritance) ve `ANA`'nın düşmesi, kütüphanede kalıtsal yapının zayıfladığını gösterir. Artık kullanılmayan veya miras alınmayan "fonsiyonel çöpler" (dead code) temizlenmelidir.

---

## 5. Mimari Kalite Yorumu
JGraphT, olgun bir kütüphane olma yolunda "Boyut" ve "Fonksiyonellik" açısından başarılı olmuştur. Ancak, mimari kalite (genişletilebilirlik ve anlaşılabilirlik) açısından **erozyona uğramıştır.** Sistem, "Big Ball of Mud" (Büyük Çamur Yığını) antipaternine doğru evrilmektedir. Özellikle 1.2.0 sürümünden sonra `LCOM` ve `DCC` değerlerindeki keskin sıçrama, mimari bir dönüm noktasına işaret eder. Bundan sonraki sürümlerde yeni özellik eklemekten ziyade, "Technical Debt" (Teknik Borç) ödemeye odaklanan bir *refactoring sprint* yapılması kütüphanenin sürdürülebilirliği açısından kritiktir.