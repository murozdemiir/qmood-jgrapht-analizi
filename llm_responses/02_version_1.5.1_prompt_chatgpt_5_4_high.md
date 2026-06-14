# JGraphT 1.5.1 QMOOD Kalite Değerlendirmesi

## 1. Kısa sonuç
JGraphT **1.5.1** sürümü, sayısal olarak **işlevsel kapsamı güçlü** fakat **anlaşılabilirlik ve genişletilebilirlik açısından baskı altında** görünen bir tasarım profili sergiliyor.

- **Güçlü taraflar:** Functionality = **152.8887**, Reusability = **301.4523**, Flexibility = **1.5703**
- **Zayıf taraflar:** Understandability = **-201.9385**, Extendibility = **0.4870**

Önemli metodolojik not: QMOOD kalite niteliklerinin ham değerleri **aynı ölçekte değildir**; bu nedenle nitelikleri yalnızca büyüklüklerine bakarak sıralamak tam olarak doğru değildir. Buna rağmen bu sürümde **Understandability'nin negatif olması** ve **Extendibility'nin sıfıra yakın düşük pozitif kalması**, bu iki niteliği en zayıf sinyaller haline getiriyor.

---

## 2. Genel kalite yorumu
Bu sürümde kütüphane boyutu ve davranışsal kapsam yüksektir:

- **DSC = 600** sınıf
- **NOH = 87**
- **CIS = 4.2317**
- **NOP = 3.5183**

Bu profil, özellikle **Functionality** ve kısmen **Reusability/Flexibility** için olumlu görünür. Nitekim:

- **Functionality = 152.8887**
- **Reusability = 301.4523**
- **Flexibility = 1.5703**

Ancak aynı anda tasarımın okunması ve evrilmesi zorlaşmış görünüyor:

- **Understandability = -201.9385**
- **Extendibility = 0.4870**

CK metrikleri de bu yorumu destekliyor:

- **WMC_mean = 15.7767**, **WMC_max = 381**
- **RFC_mean = 17.1383**, **RFC_max = 151**
- **LCOM_mean = 30.21**, **LCOM_max = 4371**
- **NOM_mean = 6.32**, **NOM_max = 95**
- **CBO_mean = 3.0183**, **CBO_max = 21**

Bu tablo, ortalamada orta-üst karmaşıklık; uç sınıflarda ise ciddi yoğunlaşmış tasarım borcu olduğunu düşündürür.

---

## 3. En zayıf 2 kalite niteliği ve sorumlu metrikler

### 3.1 Understandability — en zayıf sinyal
**Understandability = -201.9385**

Formül:

`Understandability = -0.33*(ANA + DCC + NOP + NOM + DSC) + 0.33*(DAM + CAM)`

Bu sürümde:

- Negatif blok = **ANA + DCC + NOP + NOM + DSC**
  - = 0.3217 + 3.0183 + 3.5183 + 6.32 + 600
  - = **613.1783**
- Pozitif blok = **DAM + CAM**
  - = 0.8794 + 0.3641
  - = **1.2435**

Yani pozitif dengeleme etkisi, negatif bloğun yalnızca yaklaşık **%0.20**'si düzeyindedir. Bu nedenle anlaşılabilirliğin negatif çıkması şaşırtıcı değildir.

#### Başlıca sorumlu metrikler
1. **DSC = 600**  
   Formülde doğrudan negatif tarafta ve açık ara baskın terimdir. Boyut büyüdükçe sistemin zihinsel yükü artar.

2. **NOM = 6.32** ve **WMC_mean = 15.7767**  
   Sınıf başına yöntem ve davranış yoğunluğu yüksektir. Uç değerler daha da kritik:
   - **NOM_max = 95**
   - **WMC_max = 381**

3. **DCC/CBO = 3.0183**  
   Bağlılık düşük değil; genişletilebilirliği de aşağı çekiyor. Uç sınıflarda **CBO_max = 21** olması, bazı sınıfların çok sayıda komşu tipe bağımlı olduğunu gösterir.

4. **LCOM_mean = 30.21**, **LCOM_max = 4371**  
   Bu metrik QMOOD Understandability formülünde doğrudan yoktur; ancak düşük kavramsal bütünlüğe işaret ettiği için anlaşılabilirliği pratikte daha da bozar.

#### Yorum
Bu sürümde anlaşılabilirlik problemi sadece “sistem büyük” olduğu için değil, aynı zamanda bazı sınıfların **çok fazla davranış, çok fazla çağrı ilişkisi ve çok düşük birliktelik** taşıması nedeniyle derinleşiyor.

---

### 3.2 Extendibility — ikinci en zayıf nitelik
**Extendibility = 0.4870**

Formül:

`Extendibility = 0.50*(ANA + MFA + NOP) - 0.50*DCC`

Bu sürümde:

- Pozitif blok = **ANA + MFA + NOP**
  - = 0.3217 + 0.1523 + 3.5183
  - = **3.9923**
  - Ağırlıklı katkı = **1.99615**
- Negatif blok = **DCC = 3.0183**
  - Ağırlıklı ceza = **1.50915**

Sonuçta coupling cezası, pozitif yapısal katkının yaklaşık **%75.6**'sını geri alıyor. Bu yüzden net değer yalnızca **0.4870** kalıyor.

#### Başlıca sorumlu metrikler
1. **DCC = 3.0183 / CBO_mean = 3.0183**  
   En baskın negatif etkidir. Uç değer **CBO_max = 21**, bazı sınıfların genişletme sırasında çok sayıda komşu tipe dokunacağını düşündürür.

2. **ANA = 0.3217** düşük  
   Soyutlama katmanı sınırlıdır. DIT_mean ile aynı seviyede olması (**0.3217**), derin soyut hiyerarşilerin baskın olmadığını gösterir.

3. **MFA = 0.1523** düşük  
   Kalıtım-temelli yeniden kullanım ve genişleme kapasitesi sınırlı görünür.

4. **NOP = 3.5183** olumlu ama tek başına yeterli değil  
   Polimorfizm genişletilebilirliğe katkı veriyor; fakat coupling bunu büyük ölçüde nötrlüyor.

#### Yorum
Bu sürüm, yeni davranış eklemeye tamamen kapalı görünmüyor; ancak uzatılabilirlik daha çok mevcut somut tip ağları içinde gerçekleşiyor gibi. Soyutlama ve kalıtım katkısı düşük kaldığı için, değişiklikler muhtemelen daha fazla mevcut tipe temas etmeyi gerektiriyor.

---

## 4. Diğer kalite nitelikleri neden görece güçlü görünüyor?

### Functionality = 152.8887
Bu niteliğin yüksek çıkmasında başlıca sürücüler:
- **DSC = 600**
- **NOH = 87**
- **NOP = 3.5183**
- **CIS = 4.2317**

Yani sistemin sunduğu davranış ve arayüz kapsamı geniştir. Bu, fonksiyonel zenginlik lehine güçlü kanıttır.

### Flexibility = 1.5703
Pozitif sürücüler:
- **DAM = 0.8794**
- **MOA = 0.6917**
- **NOP = 3.5183**

Negatif sürücü:
- **DCC = 3.0183**

Burada kapsülleme ve kompozisyon tasarımı tamamen zayıf değildir; fakat coupling baskısı yüzünden bu nitelik daha da yukarı çıkamamaktadır.

### Reusability = 301.4523
Bu değeri yorumlarken dikkat gerekir. Formülde **DSC** ve **CIS** güçlü pozitif etki yapar. Dolayısıyla yüksek reuse skoru, tek başına “modüler tekrar kullanım çok iyi” anlamına gelmez; burada büyüklük (**DSC = 600**) ve arayüz görünürlüğü (**CIS = 4.2317**) sonucu yukarı taşıyor olabilir.

---

## 5. Somut refactoring önerileri

### Öneri 1 — Hotspot sınıfları böl: Extract Class + Move Method + Facade inceltme
**Gerekçe:**
- **WMC_max = 381**
- **NOM_max = 95**
- **RFC_max = 151**
- **LCOM_max = 4371**

Bu uç değerler, birkaç sınıfın aşırı sorumluluk topladığını gösteriyor. Bu tür sınıflar bölünmedikçe anlaşılabilirlik ve bakım maliyeti yüksek kalır.

**Hedeflenen metrik etkisi:**
- **WMC düşer**
- **NOM düşer**
- **RFC düşer**
- **LCOM düşer**, **CAM artar**
- Dolaylı olarak **Understandability** iyileşir

**Pratik uygulama:**
- Büyük yardımcı/facade/manager sınıflarını davranış kümelerine ayır
- Veri erişimi, algoritma seçimi, validasyon ve orchestration sorumluluklarını ayrı sınıflara taşı

---

### Öneri 2 — Coupling azalt: Dependency Inversion + interface tabanlı sınırlar
**Gerekçe:**
- **DCC/CBO_mean = 3.0183**
- **CBO_max = 21**
- **Extendibility = 0.4870**

Genişletilebilirlikteki temel sorun, coupling cezasının pozitif yapısal katkının büyük kısmını silmesi.

**Hedeflenen metrik etkisi:**
- **DCC/CBO düşer**
- **ANA artar**
- **Extendibility** yükselir
- **Flexibility** de iyileşir

**Pratik uygulama:**
- Somut sınıf bağımlılıklarını arayüzlere taşı
- Strateji, adapter veya provider desenleriyle değişken davranış noktalarını soyutla
- Sınıfların doğrudan birbirini tanıdığı yerlerde aracı abstraction katmanı ekle

---

### Öneri 3 — Cohesion artır: Feature envy ve dağınık veri erişimini toparla
**Gerekçe:**
- **CAM = 0.3641** yalnızca orta seviyede
- **LCOM_mean = 30.21**, **LCOM_max = 4371** çok yüksek
- **NOA_mean = 3.06** ve **DAC_mean = 0.6917** veri/ilişki alanı da büyümüş durumda

Bu tablo, bazı sınıflarda yöntemlerin aynı veri çekirdeği etrafında toplanmadığını düşündürür.

**Hedeflenen metrik etkisi:**
- **CAM artar**
- **LCOM düşer**
- **WMC/RFC** ikincil olarak düşebilir
- **Understandability** ve bakım yapılabilirlik iyileşir

**Pratik uygulama:**
- Aynı alanları kullanan metodları birlikte tut, ilgisiz metodları ayır
- Veri yapısı yönetimi ile algoritmik işlemleri aynı sınıfta tutmaktan kaçın
- İç durumun farklı bölümlerine dokunan metod gruplarını ayrı bileşenlere çıkar

---

## 6. Son hüküm
JGraphT **1.5.1**, metriklere göre **özellikçe zengin ve fonksiyonel olarak güçlü**, fakat **okunması ve güvenle evrilmesi daha zor** bir sürümdür.

Bu yargının ana kanıtları:
- **Understandability = -201.9385**
- **Extendibility = 0.4870**
- **DCC/CBO_mean = 3.0183**
- **WMC_mean = 15.7767**, **WMC_max = 381**
- **RFC_mean = 17.1383**, **RFC_max = 151**
- **LCOM_mean = 30.21**, **LCOM_max = 4371**

En kritik risk, ortalamanın ötesinde **az sayıda ama çok problemli hotspot sınıfların** bulunmasıdır. Bu nedenle refactoring önceliği tüm sisteme yaygın değil, önce **yüksek WMC/RFC/LCOM/CBO** taşıyan sınıflara odaklı olmalıdır.

