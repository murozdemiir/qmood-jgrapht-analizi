# JGraphT 0.9.0 -> 0.9.2 Sürüm Farkı Analizi

## Kısa Sonuç
0.9.0'dan 0.9.2'ye geçiş **genel olarak sınırlı ölçüde olumlu, ancak net biçimde karma** bir kalite resmi veriyor.  
En güçlü olumlu sinyal, sistemin büyümesine rağmen **işlevsellik ve yeniden kullanılabilirlikte artış** görülmesi. Buna karşılık **cohesion düşüşü (CAM -%4.8)**, **coupling artışı (DCC +%0.6)** ve **karmaşıklık artışı (NOM +%1.6)** bakım açısından hafif bir kötüleşmeye işaret ediyor. Bu nedenle bu geçiş için en doğru yorum: **özellik ve kapsam genişlemiş, fakat iç tasarım kalitesi aynı hızda korunamamış**.

---

## 1) Tasarım metriği değişimlerinin yorumu

### Boyut ve yapı büyümesi
- **DSC 238 -> 267 (+%12.2)**: Sistem anlamlı biçimde büyümüş.
- **NOH 35 -> 39 (+%11.4)**: Hiyerarşi sayısı da artmış; bu, yapısal kapsamın genişlediğini gösteriyor.
- **ANA 0.6176 -> 0.6704 (+%8.5)** ve **MFA 0.2469 -> 0.2721 (+%10.2)**: Soyutlama ve kalıtım kullanımı artmış. Bu, tasarımın daha fazla soyut tip ve kalıtım ilişkisi içerdiğini düşündürür.
- **MOA 0.3739 -> 0.4045 (+%8.2)**: Kompozisyonun artması, modüler tasarım açısından olumlu bir sinyaldir.

### Kapsülleme, bağlaşım ve uyum
- **DAM 0.8990 -> 0.8936 (-%0.6)**: Kapsülleme pratikte sabit kalmış; küçük bir gerileme var ama kuvvetli bir sinyal değil.
- **DCC 2.3487 -> 2.3633 (+%0.6)**: Coupling artmış, ancak artış düşük. Tek başına alarm vermez; yine de büyümeyle birlikte artması izlenmelidir.
- **CAM 0.4070 -> 0.3874 (-%4.8)**: En dikkat çekici olumsuz değişimlerden biri budur. Sınıf içi uyum düşmüş; yani yöntemlerin ortak veri/amaç etrafında toplanma derecesi zayıflamış olabilir.

### Davranışsal genişleme ve karmaşıklık
- **NOP 3.2731 -> 3.1910 (-%2.5)**: Polimorfizm bir miktar azalmış. Bu, genişlemenin daha çok yeni sınıf ekleme şeklinde, daha az davranışsal soyutlama ile yapılmış olabileceğini düşündürür.
- **CIS 3.9202 -> 3.9139 (-%0.2)**: Arayüz/messaging düzeyi neredeyse sabit.
- **NOM 5.1555 -> 5.2397 (+%1.6)**: Metot sayısı/karmaşıklık boyutu hafif artmış. Artış düşük ama CAM düşüşü ile birlikte okunduğunda bakım yükünü artırabilir.

---

## 2) Kalite açısından değişim olumlu mu, olumsuz mu?

### Olumlu taraflar
QMOOD denklemlerine göre bu geçişte iki kalite niteliği belirgin şekilde iyileşiyor:

- **Reusability: 120.4746 -> 134.9630** (**+14.4884**, yaklaşık **+%12.0**)
  - En büyük neden **DSC'nin 238'den 267'ye çıkması**. Reusability denkleminde `0.50*DSC` terimi **119.0 -> 133.5** artarak tek başına **+14.5** katkı yapıyor.
  - Negatif etkiler de var: **DCC artışı** `-0.25*DCC` terimini biraz daha kötüleştiriyor, **CAM düşüşü** ve **CIS'in hafif azalması** da küçük negatif etki yapıyor. Buna rağmen boyut artışı baskın geldiği için toplam sonuç pozitif.

- **Functionality: 61.6914 -> 68.9296** (**+7.2382**, yaklaşık **+%11.7**)
  - Burada ana sürücü yine büyüme: `0.22*(NOP+CIS+DSC+NOH)` bloğu **61.6425 -> 68.8831** yükseliyor.
  - Özellikle **DSC +%12.2** ve **NOH +%11.4** bu kalite niteliğini yukarı çekiyor.
  - **CAM düşüşü** küçük bir eksi yazsa da etkisi sınırlı.

### Olumsuz taraflar
Bazı kalite nitelikleri ise hafif ama net biçimde geriliyor:

- **Understandability: -81.8694 -> -91.4705** (**-9.6012 puan**, daha kötü)
  - Bu kötüleşmenin ana nedeni **DSC artışı**. Understandability denklemindeki negatif blok `-(ANA+DCC+NOP+NOM+DSC)` olduğu için, sistem büyüdükçe skor daha da negatife gidiyor.
  - Negatif bloğun katkısı **-82.3003 -> -91.8933** olmuş; bu tek başına yaklaşık **-9.59** puanlık kötüleşme yaratıyor.
  - Ayrıca **CAM düşüşü** ve **DAM'deki küçük gerileme** pozitif dengeleyici tarafı da biraz zayıflatıyor.

- **Flexibility: 1.4611 -> 1.4303** (**-0.0308**, yaklaşık **-%2.1**)
  - **MOA artışı** olumlu katkı yapıyor (`0.5*MOA`: **0.18695 -> 0.20225**).
  - Ancak **NOP düşüşü** daha büyük negatif etki yaratıyor (`0.5*NOP`: **1.63655 -> 1.59550**).
  - Üstüne **DCC artışı** ve **DAM düşüşü** de eklenince toplam etki hafif negatif oluyor.

- **Extendibility: 0.8944 -> 0.8851** (**-0.00935**, yaklaşık **-%1.0**)
  - Bu kalite niteliğinde pozitif blok `0.5*(ANA+MFA+NOP)` neredeyse sabit kalıyor: **2.0688 -> 2.0668**.
  - **ANA** ve **MFA** artmasına rağmen **NOP düşüşü** bu kazancı büyük ölçüde siliyor.
  - **DCC artışı** da `-0.5*DCC` terimini biraz daha kötüleştiriyor.

- **Effectiveness: 1.0821 -> 1.0863** (**+0.0042**, yaklaşık **+%0.4**)
  - Bu nitelik pratikte **yatay** sayılabilir; belirgin iyileşme yok.

### Net kalite yorumu
Bu nedenle kalite açısından değişim:
- **Dışa dönük kapasite / kapsam / işlevsellik açısından olumlu**,
- **iç anlaşılırlık ve esneklik açısından hafif olumsuz**.

Yani bu sürüm geçişi, **özellik kazanımı lehine, iç tasarım saflığı aleyhine küçük bir ödünleşim** içeriyor.

---

## 3) Teknik borç işareti var mı?

**Evet, ama güçlü değil; daha çok erken ve düşük şiddette teknik borç sinyali var.**

### Teknik borç lehine kanıtlar
- **CAM -%4.8**: Cohesion düşüşü, sınıfların tek sorumluluk etrafında daha zayıf toplanmaya başladığını gösterebilir.
- **DCC +%0.6**: Coupling küçük de olsa artıyor; sistem büyürken bağımlılıkların da arttığını gösterir.
- **NOM +%1.6**: Metot yükü artıyor; CAM düşüşü ile birlikte okunduğunda sınıf içi dağınıklık riski yükselir.
- **Flexibility ve Extendibility geriliyor**: Bu da büyümenin tamamen "temiz" olmadığını düşündürür.
- **Understandability belirgin kötüleşiyor**: Bunun önemli kısmı ölçek etkisinden geliyor, ancak yine de bakım maliyetinin artacağını ima eder.

### Teknik borç aleyhine kanıtlar
- **MOA +%8.2**, **ANA +%8.5**, **MFA +%10.2**: Tasarım tamamen düzensiz büyümüyor; kompozisyon, soyutlama ve kalıtım tarafında da mimari yatırım var.
- **DCC artışı çok sınırlı**: +%0.6 tek başına agresif bir bağımlılık patlaması göstermiyor.
- **DAM neredeyse sabit**: Kapsülleme korunmuş.

### Sonuç
Bu geçişte **"teknik borç patlaması" yok**, fakat **erken tasarım aşınması sinyali** var. Özellikle **cohesion düşüşü + coupling artışı + karmaşıklık artışı** kombinasyonu, sonraki sürümlerde kontrol edilmezse daha belirgin bakım sorunlarına dönüşebilir.

---

## 4) Son değerlendirme
0.9.0 -> 0.9.2 geçişi:
- **olumlu**, çünkü sistem daha büyük, daha işlevsel ve yeniden kullanılabilir hale gelmiş,
- fakat **tam anlamıyla sağlıklı değil**, çünkü bu büyüme sırasında cohesion düşmüş, coupling az da olsa artmış ve understandability gerilemiş.

En dengeli sonuç şudur:

> Bu sürüm geçişi kalite açısından **ılımlı derecede olumlu fakat mimari açıdan kusursuz değil**. Kapsam artışı başarılıdır; ancak bakım kolaylığı ve tasarım berraklığı küçük ölçüde zayıflamıştır. Bu yüzden teknik borç şu aşamada **hafif ve yönetilebilir**, ama göz ardı edilirse ileriki sürümlerde birikme potansiyeli taşır.
