# JGraphT 0.9.0 -> 0.9.2 Sürüm Farkı Analiz Raporu

**Hazırlayan:** Kıdemli Yazılım Mimarı ve Kalite Uzmanı
**Konu:** JGraphT Sürüm Geçişi (0.9.0 -> 0.9.2) Metrik Tabanlı Kalite Değerlendirmesi
**Tarih:** 14 Haziran 2026

---

## 1. Genel Durum Özeti
JGraphT'nin 0.9.0 sürümünden 0.9.2 sürümüne geçişi, kütüphanenin büyüme (Scale) aşamasında olduğunu göstermektedir (`DSC` +%12.2). Mimari açıdan bakıldığında, sistemin daha soyut (abstract) bir yapıya kavuştuğu gözlemlense de, sınıfların içsel bağdaşıklığı (cohesion) konusunda hafif bir erozyon başlamıştır.



## 2. Temel Metrik Analizi ve Yorumlar

| Metrik | Değişim | Mimari Yorum |
| :--- | :--- | :--- |
| **DSC (Boyut)** | +12.2% | Kütüphane yeni sınıflar ve özellikler ile genişlemiştir. Normal bir büyüme. |
| **ANA (Soyutlama)** | +8.5% | **Çok Olumlu.** Tasarımın somut sınıflardan ziyade arayüzlere/soyut sınıflara doğru evrildiğini gösterir. |
| **CAM (Cohesion)** | -4.8% | **Dikkat Gerektirir.** Sınıflar arası işlevsel bağdaşıklık azalıyor. Sınıflar daha geniş/karmaşık hale geliyor olabilir. |
| **DCC (Coupling)** | +0.6% | **Stabil.** Büyümeye rağmen sınıflar arası bağımlılık (coupling) neredeyse hiç artmamış. Bu, modülerliğin korunduğunu kanıtlar. |
| **MFA (Kalıtım)** | +10.2% | Yeniden kullanılabilirlik (reusability) için kalıtımın daha etkin kullanıldığını gösterir. |

---

## 3. Kalite Açısından Değerlendirme

### Olumlu Gelişmeler
* **Soyutlama (ANA):** 0.618'den 0.670'e çıkan ANA değeri, kütüphanenin genişletilebilirliğini (extendibility) artırmıştır. Geliştiriciler artık uygulamalarında somut sınıflara (concrete classes) değil, arayüzlere daha fazla odaklanabilmektedir.
* **Bağlılık Kontrolü (DCC):** Boyut %12 artmasına rağmen DCC'nin sadece %0.6 artması, mimari tasarımın "tight coupling" (sıkı bağlılık) tuzağına düşmeden genişlediğini gösterir. Bu, başarılı bir mimari disipline işarettir.

### Olumsuz/Riskli Gelişmeler
* **Bağdaşıklık Kaybı (CAM):** CAM değerinin 0.407'den 0.387'ye düşmesi, sınıfların odak noktalarının (responsibility) bir miktar dağıldığını gösterir. QMOOD denklemine göre bu, hem *Reusability* hem de *Understandability* (Anlaşılabilirlik) üzerinde doğrudan negatif bir etkiye sahiptir.

---

## 4. Teknik Borç (Technical Debt) İşareti

Verilerde **"erken aşama teknik borç"** işareti bulunmaktadır.

* **Neden:** `DSC` (Boyut) artarken `CAM` (Cohesion) değerinin düşmesi, yeni özelliklerin mevcut sınıflara "yama" şeklinde eklendiğini veya "God Object" (her işi yapan sınıf) antipaternine doğru küçük bir kayma olduğunu düşündürmektedir.
* **Kanıt:** `Understandability` denklemi `CAM` değerini pozitif yönde etkiler (denklemdeki `+0.33 * CAM`). Cohesion'un düşmesi, kodun okunabilirliğini doğrudan zayıflatır.

---

## 5. Mimari Öneriler

1. **CAM (Cohesion) İzleme:** Bir sonraki sürümde `CAM` değerinin düşüşü devam ederse, yüksek metot sayısına sahip sınıflarda "Extract Class" (Sınıf Çıkarma) refactoring yöntemi uygulanmalıdır.
2. **Soyutlamayı Koruyun:** `ANA` değerindeki artış çok başarılı bir trenddir; bu disiplin (arayüz odaklı programlama) korunmalıdır.
3. **Refactoring Önceliği:** Kod tabanı büyümeye devam edeceği için, CAM'i düşüren sınıfların "Single Responsibility Principle" (Tek Sorumluluk Prensibi) kapsamında gözden geçirilmesi, uzun vadeli bakım maliyetini (maintainability) düşürecektir.

**Sonuç:** Bu sürüm geçişi, kütüphanenin büyüme hızı ve mimari disiplini açısından **olumlu ve sürdürülebilir** olarak değerlendirilmiştir. `CAM` üzerindeki küçük düşüş, henüz bir "borç" değil, izlenmesi gereken bir "risk" olarak tanımlanmalıdır.