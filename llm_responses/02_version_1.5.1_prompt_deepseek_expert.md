# JGraphT v1.5.1 Derinlemesine Kalite Değerlendirme Raporu

**Hazırlayan:** Kıdemli Yazılım Mimarı / Kalite Uzmanı
**Tarih:** 14 Haziran 2026
**Kapsam:** `jgrapht-core` modülü, Sürüm 1.5.1
**Metodoloji:** QMOOD (Bansiya & Davis 2002) Tasarım Kalite Modeli

---

## 1. Sürüm Kalitesi Genel Bakış

v1.5.1, kütüphanenin olgunluk dönemini temsil eden, **fonksiyonel olarak zengin fakat yapısal olarak belirgin bir karmaşıklık ve teknik borç biriktirmiş** bir sürümdür. 600 sınıflık (`num_classes`) büyük bir kod tabanına ulaşan proje, işlevsellik ve yeniden kullanılabilirlikte yüksek puanlar alırken, anlaşılabilirlik ve genişletilebilirlikte ciddi kayıplar yaşamıştır. Bu bir "başarı felci" (success paralysis) görünümüdür: kütüphane çok yeteneklidir, ancak üzerinde değişiklik yapmak veya onu genişletmek giderek zorlaşmaktadır.

### Kalite Nitelikleri Özet Tablosu

| Kalite Niteliği | Ham Değer | Yorum (Ölçek Bağımsız) |
| :--- | :--- | :--- |
| **Functionality** | 152.89 | **Çok Yüksek.** Kütüphane çok sayıda algoritma ve veri yapısı sağlıyor. |
| **Reusability** | 301.45 | **Çok Yüksek.** Sınıflar zengin arayüzlerle yeniden kullanıma uygun tasarlanmış. |
| **Flexibility** | 1.57 | **Düşük-Orta.** Kompozisyon kullanımı iyi, ancak bağımlılık ve düşük soyutlama esnekliği sınırlıyor. |
| **Effectiveness**| 1.11 | **Düşük-Orta.** Soyutlama, kapsülleme ve polimorfizmin düşük olması etkinliği azaltıyor. |
| **Extendibility**| 0.49 | **Çok Düşük (KRİTİK).** Sistem yeni özellik eklemeye elverişli değil. |
| **Understandability**| -201.94 | **Aşırı Düşük (KRİTİK).** Kod tabanını anlamak çok maliyetli ve riskli. |

**Sonuç:** En zayıf iki kalite niteliği, yazılımın yaşam döngüsündeki en büyük maliyet kalemi olan bakımı doğrudan etkileyen **Understandability (Anlaşılabilirlik)** ve **Extendibility (Genişletilebilirlik)**'tir.

---

## 2. En Zayıf 2 Kalite Niteliği ve Sorumlu Metriklerin Analizi

### 2.1. Anlaşılabilirlik (Understandability) - Değer: -201.94 (KRİTİK)

Bu, projenin en acil sorunudur. Negatif ve çok büyük mutlak değer, kod tabanını yeni bir geliştirici için kavramanın aşırı zor olduğunu gösterir.

- **Kök Neden Metrikler (Denklem: -0.33*(ANA + DCC + NOP + NOM + DSC) + 0.33*(DAM + CAM)):**
    - **`DSC` (Sınıf Başına Düşen Satır): 600.0**
        - **Kanıt:** Bu değer, projedeki ortalama bir sınıfın 600 satır uzunluğunda olduğunu gösterir. `DSC_max` değeri verilmediği için, bazı sınıfların çok daha büyük olabileceği ve `WMC_max`'ın 381 olması, bu büyük sınıflarda aşırı karmaşık metotlar olduğu varsayımını güçlendirir. Bir geliştiricinin 600 satırlık bir sınıfı zihninde canlandırması zordur. Bu, denklemdeki en büyük negatif etkendir.
    - **`NOM` (Metot Başına Düşen Satır): 6.32**
        - **Kanıt:** Metotların ortalama 6.32 satır olması normal görünse de, `NOM_max`'ın 95 olması, aykırı (outlier) olarak çok uzun ve karmaşık metotların varlığını kanıtlar. Bu metotlar anlaşılabilirliği baltalayan asıl unsurlardır. `WMC_max`'ın 381 olması da bu karmaşık metotların varlığını doğrular.
    - **`DCC` (Sınıflar Arası Bağımlılık): 3.02**
        - **Kanıt:** Ortalama bir sınıfın yaklaşık 3 diğer sınıfa bağımlı olduğunu gösterir. `CBO_max`'ın 21 olması, bazı sınıfların ("Tanrı Sınıfı" adayları) 21 farklı sınıfa bağımlı olduğunu ortaya koyar. Bu sınıfları anlamak için 21 farklı sınıfın davranışını da bilmek gerekir.

### 2.2. Genişletilebilirlik (Extendibility) - Değer: 0.49 (ÇOK DÜŞÜK)

Bu değer, kütüphaneye yeni bir algoritma veya grafik türü eklemenin kalıtım ve soyutlama mekanizmaları üzerinden kolayca yapılamadığını gösterir.

- **Kök Neden Metrikler (Denklem: 0.50*(ANA + MFA + NOP) - 0.50*DCC):**
    - **`ANA` (Soyutlama): 0.3217**
        - **Kanıt:** Sınıfların yalnızca %32'si soyut sınıf veya arayüzdür. Bu, projenin somut sınıflar üzerine kurulu olduğunu gösterir. Yeni bir davranış eklemek için mevcut bir soyut yapıyı (arayüzü) genişletmek yerine, genellikle somut bir sınıfı değiştirmek veya yeni bir somut sınıf ekleyip onu birçok yere bağlamak gerekir. Bu, genişletilebilirliğin önündeki en büyük engeldir.
    - **`MFA` (Kalıtım): 0.1523**
        - **Kanıt:** Metotların yalnızca %15'i kalıtım yoluyla gelir. Bu çok düşük bir orandır ve `DIT_mean`'in 0.32 olmasıyla (çoğu sınıfın `Object`'ten türediği) uyumludur. Polimorfizmden yararlanmak için temel mekanizma olan kalıtım neredeyse hiç kullanılmamıştır.
    - **`DCC` (Bağımlılık): 3.02**
        - **Kanıt:** Yüksek bağımlılık, genişletmeyi zorlaştıran ikincil ama güçlü bir faktördür. Bir sınıfı genişletmek, onun bağımlı olduğu 3 (veya aşırı durumda 21) sınıfı da anlamayı ve yönetmeyi gerektirir, bu da genişletme maliyetini katlar.

---

## 3. Somut Refactoring Önerileri

Aşağıdaki 3 öneri, en zayıf kalite niteliklerini iyileştirmek için belirli metrikleri hedef alır.

**1. "Tanrı Sınıfı" Operasyonu: Yüksek CBO ve WMC'li Sınıfları Parçala**
- **Hedef Metrikler:** `CBO_max` (21), `WMC_max` (381), `LCOM_max` (4371).
- **Eylem:** `CBO` değeri 21 ve `WMC` değeri 381 olan sınıfı (`CBO_max` ve `WMC_max` sahibi) tespit edin. Bu sınıf, `LCOM` değerinin de 4371 gibi aşırı bir seviyede olmasıyla neredeyse kesin olarak bir "Tanrı Sınıfı"dır. Bu sınıfı, anlamlı ve uyumlu (`CAM`'i yüksek) parçalara bölerek, her yeni sınıfın en fazla 1-2 sorumluluğu olmasını sağlayın. Bu, `DCC` ve `WMC`'yi düşürecek, `CAM`'i yükseltecek ve doğrudan **Understandability**'yi artıracaktır.

**2. "Soyutlama Enjeksiyonu" Operasyonu: Strateji/Şablon Metot Desenlerini Uygula**
- **Hedef Metrikler:** `ANA` (0.3217), `MFA` (0.1523).
- **Eylem:** `DIT_mean` (0.32) değerinin düşük olması, fırsat kaçırıldığını gösterir. Örneğin, farklı grafik gezinme algoritmalarını (BFS, DFS, Topolojik Sıralama vb.) içeren kodları tarayın. Eğer bu algoritmalar `switch-case` veya `if-else` bloklarıyla seçiliyorsa, her bir algoritmayı ortak bir `GraphIterator` arayüzünden (`ANA`'yı artırır) türeyen somut bir Strateji sınıfına taşıyın. Bu, `NOM`'u ve `DSC`'yi azaltıp `MFA` ve `NOP`'u artırarak **Extendibility**'yi doğrudan güçlendirecektir.

**3. "Metot Düzleştirme" Operasyonu: Aykırı Uzun Metotları (NOM_max=95) Hedef Al**
- **Hedef Metrikler:** `NOM_max` (95), `WMC_max` (381).
- **Eylem:** Uzunluğu 95 satır olan metodu (`NOM_max`) bulun. Bu metot, yüksek ihtimalle birden fazla işi bir arada yapıyordur. Metodu, her biri tek ve iyi tanımlanmış bir alt görevi yerine getiren daha küçük özel metotlara (`private` yardımcı metotlara) bölün. Bu işlem `NOM` ortalamasını çok az etkileyecek ancak aykırı karmaşıklığı (`WMC_max`) ve anlaşılma zorluğunu dramatik şekilde azaltarak **Understandability**'yi iyileştirecektir. `LCOM` üzerinde de olumlu bir etkisi olması muhtemeldir.