# JGraphT (jgrapht-core) Sürüm Bazlı QMOOD Kalite Değerlendirme Raporu

**Hazırlayan:** Kıdemli Yazılım Mimarı / Kalite Uzmanı
**Tarih:** 14 Haziran 2026
**Kapsam:** `jgrapht-core` modülü, v0.9.0 - v1.5.3
**Metodoloji:** QMOOD (Bansiya & Davis 2002) Tasarım Kalite Modeli

---

## 1. Genel Kalite Değerlendirmesi

Projenin `0.9.0` sürümünden `1.5.3` sürümüne kadar olan evrimindeki genel eğilim **fonksiyonel zenginleşme (functionality) ve yeniden kullanılabilirlik (reusability) lehine, ancak anlaşılabilirlik (understandability) ve genişletilebilirlik (extendibility) aleyhine** bir ödünleşme (trade-off) olarak özetlenebilir. Yani kütüphane daha yetenekli ama daha karmaşık hale gelmiştir.

### Sayısal Kanıtlarla Değişimler:

- **Anlaşılabilirlik (Understandability): Sürekli ve En Belirgin Bozulma.**
    - Ham değer `-81.86`'dan `-207.89`'a düşmüştür (yaklaşık %154 bozulma).
    - **Kanıt:** `NOM` (Metot başına satır) `5.15`'ten `6.32`'ye (+%22) ve `DSC` (Sınıf başına satır) `238`'den `618`'e (+%160) yükselmiştir. Formüldeki en büyük negatif etkenler sınıf ve metot boyutlarındaki bu artışlardır.
- **Yeniden Kullanılabilirlik (Reusability): İstikrarlı ve Keskin Artış.**
    - Normalize değer `1.00`'dan `1.73`'e yükselmiştir (+%73).
    - **Kanıt:** Sınıflar arası iletişimi gösteren `CIS` metriği nispeten yüksek seyretmiş (ortalama ~4.2) ve kompozisyonu gösteren `DSC` artmıştır. Bu, sınıfların iyi tanımlanmış arayüzlerle zengin etkileşimler sunduğunu ve yeniden kullanıma uygun olduğunu gösterir.
- **İşlevsellik (Functionality): En Yüksek Pozitif Kazanım.**
    - Normalize değer `1.00`'dan `1.72`'ye yükselmiştir (+%72).
    - **Kanıt:** Artan sınıf sayısı (`num_classes` 238'den 618'e) ve derinlik (`NOH` 35'ten 91'e) ile doğrudan ilişkilidir. Kütüphaneye sürekli yeni yetenekler eklenmiştir.
- **Genişletilebilirlik (Extendibility): Ciddi ve Sürekli Kayıp.**
    - Normalize değer `1.00`'dan `0.46`'ya düşmüştür (-%54).
    - **Kanıt:** Soyutlama (`ANA` `0.6176`'dan `0.3204`'e) ve kalıtımın (`MFA` `0.2469`'dan `0.1512`'ye) belirgin şekilde azalması, sistemin genişletilebilirliğinin temelini oluşturan soyut yapıların ve polimorfizmin (`NOP` artmış olsa da) göreceli olarak zayıfladığını göstermektedir.
- **Esneklik (Flexibility): Ilımlı Artış.**
    - Normalize değer `1.00`'dan `1.40`'a yükselmiştir (+%40). Bu kazanım büyük ölçüde `MOA` (Kompozisyon, `0.3739`'dan `0.7006`'ya) metriğindeki artıştan kaynaklanır. Kalıtım yerine kompozisyonun tercih edilmesi esneklik için olumludur.

---

## 2. Bakım Yapılabilirlik (Maintainability) Analizi

Projenin bakım yapılabilirliği **genel olarak zorlaşmıştır.** Anlaşılabilirlikteki dramatik düşüş, esneklikteki kazanımları ve düşük bağımlılığı gölgelemektedir.

- **Anlaşılabilirlik (Understandability) – Çok Zorlaştı:**
    - Daha önce belirtildiği gibi, `NOM` ve `DSC` metriklerindeki artışlar sınıf ve metot başına düşen sorumluluğun ve karmaşıklığın arttığını kanıtlar. Örneğin, bir sınıfın boyutu (`DSC`) `v1.3.0`'da `433` satıra, `v1.5.3`'te ise `618` satıra çıkmıştır. Geliştiriciler bu kodu okumakta ve anlamakta giderek daha fazla zorlanacaktır. `WMC_mean` değerinin `10.36`'dan `15.78`'e yükselmesi de sınıf başına düşen metot karmaşıklığının arttığının bir diğer göstergesidir.

- **Esneklik (Flexibility) vs. Bağımlılık – Karışık Sinyaller:**
    - **Olumlu:** Esneklikteki artış (+%40) ve `MOA`'daki (Kompozisyon) yükseliş, modüllerin gevşek bağlı olduğuna işaret eder. Bu bakımı kolaylaştıran bir faktördür.
    - **Olumsuz:** `DCC` (Sınıflar arası bağımlılık) metriği `2.34`'ten `3.03`'e yükselmiştir (+%29). Bu, sınıfların giderek daha fazla sayıda başka sınıfa bağımlı hale geldiğini gösterir. Bir değişikliğin beklenmedik dalgalanma etkilerine yol açma riski artmıştır. `CBO_mean` metriğindeki benzer artış (`2.34`'ten `3.03`'e) bu bulguyu desteklemektedir.

---

## 3. Teknik Borç (Technical Debt) Tahmini

Aşağıdaki metrik eğilimleri, projede **biriken bir teknik borca** işaret etmektedir. Bu eğilimler, kodun zaman içinde "temiz" kalma prensibinden uzaklaştığını, kısa vadeli işlevsellik kazanımları için uzun vadeli yapısal bütünlüğün feda edildiğini gösterir.

1.  **Azalan Uyum (CAM - Cohesion):** Bir sınıfın metotlarının ortak veri üzerinde çalışma derecesi `0.4070`'den `0.3660`'a düşmüştür. Bu, sınıfların giderek "daha az ilgili" işleri yapmaya başladığının (Tanrı Nesnesi eğilimi) ve Tek Sorumluluk Prensibi'nin ihlal edildiğinin bir göstergesidir.
2.  **Zayıflayan Kapsülleme (DAM - Encapsulation):** `0.8990`'dan `0.8850`'ye hafif bir düşüş olsa da, `v1.5.x` serisinde bu düşüşün devam etmesi, artan oranda sınıf içsel detayının dışarıya açılmaya başlamış olabileceğini düşündürmektedir.
3.  **Patlayan Karmaşıklık (WMC & LCOM):**
    - `WMC_mean` (Ağırlıklı Metot Karmaşıklığı) `10.36`'dan `15.78`'e (+%52) fırlamıştır. Test edilmesi ve anlaşılması zor sınıfların sayısı artmıştır.
    - `LCOM_mean` (Metot Uyum Eksikliği) `13.75`'ten `31.23`'e (%127 artış) yükselmiştir. Bu, teknik borcun en çarpıcı kanıtıdır. Sınıfların, ortak hiçbir veri alanı kullanmayan ve ayrı sınıflara bölünmesi gereken metot kümeleri barındırdığını neredeyse kesin olarak kanıtlar.
4.  **Artan Bağımlılık (CBO & DCC):** Daha önce belirtildiği gibi, artan `CBO_mean` ve `DCC` değerleri, değişiklik maliyetini katlayan bir mimari bağımlılık ağı oluşturur.

---

## 4. Refactoring Önerileri

Aşağıdaki 3 öneri, metriklerle tespit edilen en kritik sorunları hedef alır.

**1. Düşük Uyum (Low Cohesion) Odaklı "Sınıf Ayırma" Operasyonu:**
- **Metrik Kanıt:** `CAM` puanı `0.3660`'a düşmüş ve `LCOM_mean` `31.23`'e fırlamıştır.
- **Eylem:** En yüksek `LCOM` değerine sahip sınıfları hedef alın. Bu sınıflar içindeki, farklı veri alanları üzerinde çalışan metot gruplarını (doğal kümeleri) tespit edip ayrıştırarak yeni, daha odaklı (cohesive) sınıflar oluşturun. Bu, `CAM`'i doğrudan artıracak ve `LCOM`'u düşürecektir.

**2. Yüksek Karmaşıklık ve Bağımlılık için "Metot Çıkarma ve Bağımlılık Enjeksiyonu":**
- **Metrik Kanıt:** `WMC_mean` `15.78` ve `CBO_mean` `3.03` seviyesindedir.
- **Eylem:** Karmaşık metotları (`WMC`'ye katkısı yüksek olanlar) daha küçük, tek sorumluluklu metotlara bölün (`NOM`'u geçici olarak artıracak ama `WMC`'yi azaltacaktır). Yüksek `CBO`'lu sınıflarda, doğrudan bağımlılığı kırmak için Arayüz Ayırma Prensibi'ni (ISP) uygulayarak ve bağımlılıkları constructor/setter üzerinden enjekte ederek gevşek bağlılığı (loose coupling) artırın.

**3. Azalan Soyutlama için "Strateji veya Şablon Metot Deseni Uygulama":**
- **Metrik Kanıt:** `ANA` (Soyutlama) metriği `0.3204`'e gerilemiş ve `MFA` (Kalıtım) `0.1512` ile düşük seyretmektedir.
- **Eylem:** `switch-case` veya uzun `if-else` bloklarıyla dolu, farklı algoritma varyasyonlarını içeren sınıfları tespit edin. Bu davranışları Strategy deseni ile soyutlayın. Bu, somut `DSC` ve `NOM`'u azaltırken, soyut sınıf/arayüz (`ANA` ve `MFA`) oranını doğrudan yükseltecektir.

---

## 5. Mimari Kalite Yorumu: Mimari Bozulma (Architectural Erosion)

**Evet, yazılım büyüdükçe (`DSC` 238'den 618'e, sınıf sayısı iki katından fazla) net mimari bozulma belirtileri gözlemlenmektedir.**

- **Bozulmanın Temel Kanıtı:** `Understandability` ve `Extendibility`'deki sürekli düşüştür. Başlangıçta esnek ve anlaşılır bir yapı, artan fonksiyonaliteyi yönetmekte zorlanmıştır.
- **Sebeplerin Analizi:**
    1.  **Somut Sınıf Patlaması (`ANA` ve `MFA` düşüşü):** Yeni özelliklerin, soyut katmanlar (arayüzler, soyut sınıflar) üzerine inşa edilmek yerine, doğrudan somut sınıflar eklenerek gerçekleştirildiğini gösteriyor. Bu, `Extendibility`'deki %54'lük kaybın başlıca nedenidir. Sistem genişlemeye değil, şişmeye başlamıştır.
    2.  **Tanrı Nesnesi Oluşumu (`LCOM` ve `CAM`):** Sınıfların boyutu (`DSC`/`num_classes` oranı) büyüdükçe, sorumlulukların yanlış bir şekilde mevcut büyük sınıflara yığıldığını görüyoruz. `LCOM`'daki patlama bunun en net ispatıdır. Bu, Bakım Yapılabilirlik için en büyük tehdittir.

Bu bulgular, `v1.3.0` sonrası artan teknik borcun, önerilen refactoring'lerle hedeflenmiş bir şekilde azaltılması gerektiğine işaret etmektedir. Aksi takdirde, bakım maliyeti üstel olarak artmaya devam edecektir.