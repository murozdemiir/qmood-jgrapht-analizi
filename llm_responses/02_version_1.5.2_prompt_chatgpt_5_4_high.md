# JGraphT 1.5.2 — QMOOD Tabanlı Derin Kalite Değerlendirmesi

## Kapsam ve yorumlama notu
Bu değerlendirme **yalnızca verilen sayısal metriklere** dayanır. Yorumlar, QMOOD denklemlerindeki sürücü metriklere bağlanmıştır.

Önemli bir sınırlama vardır: **QMOOD kalite niteliklerinin ham değerleri aynı ölçekte değildir.** Özellikle **Understandability** denkleminde `DSC` doğrudan yer aldığı için, sistem büyüdükçe bu nitelik çok sert negatifleşir. Bu nedenle aşağıdaki yorumda, kalite niteliğinin kendisi kadar **onu aşağı çeken metrik bileşenleri** de dikkate alınmıştır.

---

## 1) Genel kalite değerlendirmesi
JGraphT 1.5.2, verilen sayılara göre **işlevsel ve yeniden kullanılabilirliği yüksek**, fakat **anlaşılabilirlik ve genişletilebilirlik açısından baskı altında** bir sürümdür.

### Güçlü taraflar
- **Reusability = 301.939**
  - Bu değerin temel sürücüsü **DSC = 601** ve **CIS = 4.208**'dir.
  - Denklem katkıları:
    - `0.50*DSC = 300.50`
    - `0.50*CIS = 2.104`
    - `0.25*CAM = 0.0908`
    - `-0.25*DCC = -0.7558`
  - Yani yeniden kullanılabilirlik skoru büyük ölçüde **sistem boyutu** ve **mesajlaşma/arayüz zenginliği** ile taşınmaktadır.

- **Functionality = 153.101**
  - Bu nitelik de yine büyük ölçüde **DSC = 601** ve **NOH = 87** ile yükselmektedir.
  - Denklem katkıları:
    - `0.22*DSC = 132.22`
    - `0.22*NOH = 19.14`
    - `0.22*NOP = 0.7717`
    - `0.22*CIS = 0.9258`
    - `0.12*CAM = 0.0436`
  - Sonuç: fonksiyonellik yüksek görünmektedir; ancak bu yükseklik esasen **büyüklük ve hiyerarşi genişliği** tarafından desteklenmektedir.

### Zayıf taraflar
- **Understandability = -202.2567**
- **Extendibility = 0.4774**

Bu iki nitelik, bu sürümün en zayıf iki kalite alanıdır.

---

## 2) En zayıf 2 kalite niteliği ve sorumlu metrikler

## 2.1 Understandability — en zayıf nitelik
**Ham skor: -202.2567**

Denklem:

`Understandability = -0.33*(ANA + DCC + NOP + NOM + DSC) + 0.33*(DAM + CAM)`

### Sayısal katkılar
Negatif katkılar:
- `-0.33*DSC = -198.33`
- `-0.33*NOM = -2.0766`
- `-0.33*NOP = -1.1575`
- `-0.33*DCC = -0.9977`
- `-0.33*ANA = -0.1054`

Pozitif katkılar:
- `+0.33*DAM = +0.2906`
- `+0.33*CAM = +0.1199`

Toplam: **-202.2567**

### Neden zayıf?
1. **Boyut çok yüksek:** `DSC = 601`
   - Tek başına **-198.33** etkisi var.
   - Toplam negatif baskının yaklaşık **%97.9**'u DSC'den geliyor.
   - Bu, sürümün anlaşılabilirliğinin ciddi biçimde **ölçek baskısı** altında olduğunu gösterir.

2. **Sınıf/operasyon karmaşıklığı yüksek:** `NOM = 6.2928`, `WMC_mean = 15.7604`, `RFC_mean = 17.1265`
   - NOM doğrudan denklemde cezalandırılıyor: **-2.0766**.
   - CK tarafında da karmaşıklık baskısı görülüyor:
     - `WMC_max = 381`
     - `RFC_max = 149`
     - `NOM_max = 95`
   - Bu uç değerler, bazı sınıfların okunması ve zihinsel izlenmesi zor olduğunu düşündürür.

3. **Bağlılık ve dağınık davranış sinyali var:** `DCC = 3.0233`, `CBO_mean = 3.0233`, `MPC_mean = 16.782`
   - DCC denklemde **-0.9977** ceza üretir.
   - `CBO_max = 21` ve `MPC_max = 401`, bazı sınıflarda iletişim ağının çok yoğun olduğunu gösterir.

4. **Kohesyon dengelemeye yetmiyor:** `CAM = 0.3633`
   - CAM'in pozitif katkısı yalnızca **+0.1199**.
   - `LCOM_mean = 30.2213`, `LCOM_max = 4371` değerleri de kohesyon probleminin gerçek bir risk olduğunu gösterir.

### Sonuç
Bu sürümün anlaşılabilirliği zayıftır; başlıca neden **çok yüksek boyut (DSC)**, buna eşlik eden **yüksek metod yükü/karmasiklik** ve **sınıflar arası etkileşim yoğunluğu**dur.

---

## 2.2 Extendibility — ikinci en zayıf nitelik
**Ham skor: 0.4774**

Denklem:

`Extendibility = 0.50*(ANA + MFA + NOP) - 0.50*DCC`

### Sayısal katkılar
Pozitif katkılar:
- `0.50*ANA = 0.1598`
- `0.50*MFA = 0.0756`
- `0.50*NOP = 1.7538`

Negatif katkı:
- `-0.50*DCC = -1.5117`

Toplam: **0.4774**

### Neden zayıf?
1. **Coupling yüksek:** `DCC = 3.0233`
   - Tek başına **-1.5117** ceza üretir.
   - Pozitif tarafın toplamı `1.9891`, coupling cezası bunun yaklaşık **%76.0**'ını geri almaktadır.
   - Yani genişletilebilirliğin önündeki ana fren **bağımlılık yoğunluğu**dur.

2. **Soyutlama seviyesi sınırlı:** `ANA = 0.3195`
   - Pozitif katkısı sadece **+0.1598**.
   - CK tarafında `DIT_mean = 0.3195` ve `DIT_max = 3`; bu, derin kalıtım yerine daha sığ bir yapı olduğunu gösterir. Bu tek başına kötü değildir; ancak düşük ANA ile birleşince, genişleme noktalarının sınırlı olabileceğini düşündürür.

3. **Kalıtım katkısı zayıf:** `MFA = 0.1511`
   - Pozitif katkısı yalnızca **+0.0756**.
   - Bu da sistemde genişletme için tekrar kullanılabilecek kalıtımsal çerçevenin sınırlı kaldığını gösterir.

4. **Polimorfizm var ama coupling'i dengelemiyor:** `NOP = 3.5075`
   - Pozitif katkısı **+1.7538** ile en güçlü olumlu etkidir.
   - Ancak bu katkı, yüksek DCC nedeniyle büyük ölçüde eritilmektedir.

### Sonuç
Bu sürüm tamamen “genişletilemez” değildir; ancak **mevcut genişletilebilirlik potansiyeli coupling tarafından bastırılmaktadır**. Sorunun merkezinde DCC vardır; ANA ve MFA da bunu dengeleyecek kadar yüksek değildir.

---

## 3) Kısa teknik yorum
- **Bakım maliyeti muhtemelen yüksektir.** Çünkü `LCOM_mean = 30.2213`, `WMC_mean = 15.7604`, `RFC_mean = 17.1265` ve özellikle `LCOM_max = 4371`, `WMC_max = 381`, `RFC_max = 149` gibi uç değerler bulunmaktadır.
- **Kalite profili dengesizdir.** Reusability ve Functionality yüksek görünürken, bu artışın önemli kısmı **boyut (DSC)** kaynaklıdır. Aynı boyut büyümesi Understandability'yi sert biçimde aşağı çekmektedir.
- **Belirsizlik notu:** En zayıf nitelikler açıkça Understandability ve Extendibility'dir; ancak Understandability'nin çok negatif çıkmasında denklemin DSC'ye yüksek duyarlılığı önemli rol oynar. Bu nedenle yorum “tamamen kötü tasarım” yerine “ölçek ve karmaşıklık baskısı” şeklinde okunmalıdır.

---

## 4) Metrik-temelli 3 somut refactoring önerisi

## Öneri 1 — Yüksek WMC/RFC/LCOM'lu sınıfları parçala
**Hedef metrikler:** `WMC_mean`, `RFC_mean`, `LCOM_mean`, `NOM_mean`

### Gerekçe
- `WMC_mean = 15.7604`, `WMC_max = 381`
- `RFC_mean = 17.1265`, `RFC_max = 149`
- `LCOM_mean = 30.2213`, `LCOM_max = 4371`
- `NOM_max = 95`

Bu değerler, bazı sınıflarda çok fazla sorumluluk ve zayıf iç tutarlılık olduğunu gösteriyor.

### Refactoring
- **Extract Class**
- **Extract Method**
- **Move Method**
- Geniş API veren sınıflarda **Facade + iç servis ayrıştırması**

### Beklenen etki
- `NOM`, `WMC`, `RFC`, `LCOM` düşer.
- `CAM` artabilir.
- Dolaylı olarak **Understandability** iyileşir.

---

## Öneri 2 — Coupling'i düşürmek için bağımlılık sınırlarını netleştir
**Hedef metrikler:** `DCC`, `CBO_mean`, `MPC_mean`

### Gerekçe
- `DCC = 3.0233`
- `CBO_mean = 3.0233`, `CBO_max = 21`
- `MPC_mean = 16.782`, `MPC_max = 401`

Bu tablo, bazı sınıfların çok sayıda başka sınıfla konuştuğunu gösteriyor. Bu durum genişletilebilirliği doğrudan bastırıyor.

### Refactoring
- **Dependency Inversion** uygula.
- Somut sınıflara doğrudan bağımlılık yerine **arayüz/taban sözleşme** kullan.
- Paketler arasında **Adapter / Facade** ile geçiş katmanı oluştur.
- Sık kullanılan çapraz bağımlılıkları tek yerde toplayıp **orchestration/service layer** üzerinden yönlendir.

### Beklenen etki
- `DCC`, `CBO`, `MPC` düşer.
- **Extendibility** ve kısmen **Flexibility** iyileşir.

---

## Öneri 3 — Değişken algoritma davranışlarını soyut stratejilere taşı
**Hedef metrikler:** `ANA`, `NOP`, `CAM`, kısmen `MFA`

### Gerekçe
- `ANA = 0.3195` düşük-orta seviyede.
- `MFA = 0.1511` düşük.
- `NOP = 3.5075` iyi bir temel sunuyor ama coupling bunu bastırıyor.

Bu, sistemde polimorfik davranış olduğunu; fakat bunun yeterince sistematik soyutlama/uzatma noktasına dönüştürülmediğini düşündürür.

### Refactoring
- Algoritma varyasyonlarını **Strategy** ile ayır.
- Şablon akışları için **Template Method** veya uygun yerlerde **Policy Object** kullan.
- Veri yapısı seçimi ile algoritma davranışını aynı sınıfta tutmak yerine uzatma noktalarını açık soyut tiplerde topla.

### Beklenen etki
- `ANA` artabilir.
- `NOP` daha kontrollü ve faydalı kullanılır.
- Sınıf içi rol netleşirse `CAM` artabilir.
- **Extendibility** iyileşir; yeni davranış ekleme maliyeti düşer.

---

## 5) Sonuç
JGraphT 1.5.2'nin bu metrik setine göre **en zayıf iki kalite niteliği**:
1. **Understandability (-202.2567)**
2. **Extendibility (0.4774)**

### Ana nedenler
- **Understandability** için başlıca nedenler: `DSC = 601`, `NOM = 6.2928`, `DCC = 3.0233`, düşük etkili `CAM = 0.3633`, ayrıca yüksek `WMC/LCOM/RFC` uç değerleri.
- **Extendibility** için başlıca nedenler: `DCC = 3.0233`'ün yüksek cezası, `ANA = 0.3195` ve `MFA = 0.1511`'in sınırlı kalması.

### Kısa hüküm
Bu sürüm **özellik ve kapsama açısından güçlü**, fakat **büyüklük, bağlılık ve sınıf içi dağınıklık** nedeniyle bakım ve genişleme açısından baskı altında görünmektedir. En rasyonel iyileştirme sırası:
1. hotspot sınıfları parçalamak,
2. coupling'i düşürmek,
3. genişleme noktalarını daha sistematik soyutlamalarla netleştirmek.
