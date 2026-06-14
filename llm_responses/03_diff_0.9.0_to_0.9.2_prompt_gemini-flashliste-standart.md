# JGraphT Sürüm Karşılaştırmalı Mimari Analiz Raporu (0.9.0 -> 0.9.2)

**Rol:** Yazılım Mimarisi ve Kalite Uzmanı
**Analiz Konusu:** JGraphT 0.9.0 ve 0.9.2 sürümleri arası tasarım metrikleri değişimi.

---

## 1. Tasarım Metriği Değişim Yorumu
JGraphT 0.9.0'dan 0.9.2'ye geçişte belirgin bir "genişleme" evresi gözlemlenmektedir.

* **Büyüme (DSC %12.2):** Sınıf sayısındaki %12.2'lik artış, kütüphaneye yeni özelliklerin eklendiğini gösterir. Ancak bu artış, sistemin karmaşıklığını da beraberinde getirmektedir.
* **Soyutlama (ANA %8.5):** Soyutlama seviyesindeki artış oldukça olumludur. Daha yüksek `ANA` değeri, sistemin genel yapısında arayüz kullanımının veya kalıtım hiyerarşisinin daha bilinçli yönetildiğini (soyut sınıfların artışını) gösterir.
* **Uyum Kaybı (CAM %-4.8):** En dikkat çekici negatif değişimdir. Cohesion (uyum) değerindeki bu düşüş, sınıfların içsel tutarlılığının biraz azaldığına ve metodların tek bir sorumluluğu yerine getirmek yerine dağınıklaştığına işaret eder.



## 2. Kalite Açısından Değerlendirme
Bu değişimleri **karma bir tablo** olarak değerlendiriyorum:

* **Olumlu Gelişmeler:** `ANA` (+%8.5) ve `MFA` (+%10.2) değerlerindeki artış, tasarımın daha "nesne yönelimli" ve genişletilebilir bir hiyerarşiye doğru evrildiğini kanıtlar. Bu, kütüphanenin gelecekteki geliştirmeleri için daha sağlam bir temel atıldığını gösterir.
* **Olumsuz Gelişmeler:** `CAM` değerindeki düşüş (%-4.8), her yeni eklenen sınıfın veya metodun, mevcut sınıfların uyumunu bir miktar zayıflattığını (cohesion erosion) gösterir. Ayrıca `NOP` (polimorfizm) değerindeki %2.5'lik düşüş, tasarımdaki esnekliğin kısıtlı bir şekilde de olsa azaldığına dair sinyal verir.

## 3. Teknik Borç (Technical Debt) Analizi
Bu geçişte acil bir "teknik borç krizi" görünmemekle birlikte, **takip edilmesi gereken bazı riskler** mevcuttur:

1.  **Hafif Sinyaller:** `DCC` (coupling) değerindeki %0.6'lık artış minimaldir, ancak sınıf sayısı (%12.2) artarken bu oranın dengede tutulması, bağımlılıkların kontrollü yönetildiğini gösterir.
2.  **Dikkat Edilmesi Gereken Nokta:** `CAM` (uyum) kaybı, yeni özellikler eklenirken kodun mevcut sınıf sorumluluklarına tam olarak yedirilemediğini (refactoring ihtiyacı) gösterebilir. Eğer bu eğilim sonraki sürümlerde artarak devam ederse, `Understandability` niteliği QMOOD denklemi gereği ciddi zarar görecektir.

---

### Sonuç ve Tavsiye
JGraphT 0.9.2 sürümü, 0.9.0'a kıyasla **mimari açıdan daha soyut (ANA) ve derinlikli (MFA) bir yapıya** evrilmiştir; bu durum olumludur. Ancak, `CAM` metriğindeki düşüş "küçük çaplı bir teknik borç" oluşumuna işaret etmektedir. Bir sonraki sürümlerde sınıf içi uyumun (cohesion) artırılmasına yönelik refactoring çalışmaları önceliklendirilmelidir.