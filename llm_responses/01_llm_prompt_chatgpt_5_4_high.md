# JGraphT (jgrapht-core) QMOOD Tabanli Kalite Degerlendirmesi

## Kapsam ve okuma notu
Bu degerlendirme yalnizca verilen QMOOD ve CK ortalamalarina dayanir. Dolayisiyla yorumlar **sayisal egilim** uzerinedir; kod/commit baglami gorulmedigi icin nedensellik iddialari sinirli tutulmustur. Ozellikle **Understandability** degerinin formul geregi buyukluk (DSC) arttikca kolayca daha negatif olabilecegi unutulmamalidir; yine de tek basina buyume her seyi aciklamaz, cunku coupling ve cohesion metrikleri de olumsuz yone gitmektedir.

## 1) Genel kalite degerlendirmesi

### Ozet yargi
Surumler boyunca sistem **ciddi bicimde buyumus** ve bununla birlikte **yeniden kullanilabilirlik** ile **islevsellik** belirgin bicimde artmistir; buna karsin **anlasilabilirlik** ve **genisletilebilirlik** bozulmustur. **Esneklik** sinirli bir iyilesme gostermis, **etkinlik** ise buyuk olcude yatay kalmistir.

### Baslangic-son durum
| Nitelik | 0.9.0 | 1.5.3 | Degisim | Yorum |
|---|---:|---:|---:|---|
| Reusability | 120.4746 | 310.4459 | +157.7% | Guclu artis |
| Flexibility | 1.4611 | 1.5861 | +8.6% | Sinirli artis |
| Understandability | -81.8694 | -207.8903 | 126.0 puan daha negatif | Belirgin bozulma |
| Functionality | 61.6914 | 157.7334 | +155.7% | Guclu artis |
| Extendibility | 0.8944 | 0.4923 | -45.0% | Ciddi bozulma |
| Effectiveness | 1.0821 | 1.1205 | +3.5% | Neredeyse yatay |

### Neden?
- **Reusability artisi** buyuk olcude boyut ve arayuz/yetenek artisindan geliyor: **DSC 238 -> 618 (+159.7%)**, **CIS 3.9202 -> 4.2249 (+7.8%)**. Formulde DCC ceza verdigi halde (**DCC 2.3487 -> 3.0324, +29.1%**), DSC ve CIS artisi baskin cikmis.
- **Functionality artisi** da ayni sekilde buyume ve hiyerarsi genislemesiyle uyumlu: **DSC 238 -> 618**, **NOH 35 -> 91 (+160%)**, **NOP 3.2731 -> 3.5453 (+8.3%)**, **CIS 3.9202 -> 4.2249 (+7.8%)**. Bu dort metrigin tamami Functionality formulunde pozitif agirlikla yer aliyor.
- **Understandability bozulmasi** yalnizca buyume ile aciklanamaz. Negatif tarafta yer alan metriklerin cogu artti: **DSC +159.7%**, **DCC +29.1%**, **NOP +8.3%**, **NOM 5.1555 -> 6.3236 (+22.7%)**. Pozitif dengeleyiciler ise zayif: **DAM 0.8990 -> 0.8850 (-1.6%)**, **CAM 0.4070 -> 0.3660 (-10.1%)**.
- **Extendibility dususu** daha yapisaldir: formulde pozitif olan **ANA 0.6176 -> 0.3204 (-48.1%)** ve **MFA 0.2469 -> 0.1512 (-38.8%)** sert sekilde geriliyor; ustune **DCC +29.1%** ceza ekleniyor. Bu yuzden boyume olmasina ragmen genisletilebilirlik iyilesmiyor.
- **Effectiveness** hemen hemen sabit kalmis; cunku pozitif etkiler (**MOA 0.3739 -> 0.7006, +87.4%**, NOP artisi) ile negatif etkiler (ANA ve MFA dususu) birbirini dengelemis.

### Kirilma noktalari
- **1.0.1 -> 1.1.0**: ilk sert bozulma. **DCC +0.3066**, **CAM -0.0360**, **NOP +0.3277**, **CIS +0.6470**, **NOM +0.6343**. Sonuc: **Understandability -12.63 puan**, buna karsin **Functionality +9.01**.
- **1.1.0 -> 1.2.0**: soyutlama/kalitim tarafi zayifliyor. **ANA -0.1898**, **MFA -0.0666**. DCC biraz gerilese de (**-0.0884**) genel bakim kalitesi toparlanmiyor.
- **1.3.1 -> 1.5.1**: buyume hizli, kalite dengesi tek tarafli. **DSC +134**, **DCC +0.1084**; **Reusability +66.97**, **Functionality +32.99**, ama **Understandability -44.24** ve **Extendibility -0.1082**.

## 2) Bakim yapilabilirlik (Maintainability) analizi

### Sonuc
Bakim yapilabilirlik genel olarak **kolaylasmamis, zorlasmistir**.

### Gerekce
- **Understandability** surekli kotulesiyor: **-81.8694 -> -207.8903**. Bu, sadece buyume degil; coupling ve komplekslik artisiyla da uyumlu.
- **Flexibility** yalnizca sinirli iyilesiyor: **1.4611 -> 1.5861 (+8.6%)**. Bunun ana nedeni **MOA +87.4%** ve kisitli **NOP** artisidir; fakat **DCC +29.1%** ve **DAM'in yataya yakin kalmasi** bu kazanci sinirliyor.
- **Coupling / cohesion penceresi** bakim acisindan olumsuz:
  - **DCC / CBO_mean: 2.3487 -> 3.0324 (+29.1%)**
  - **CAM: 0.4070 -> 0.3660 (-10.1%)**
  - **LCOM_mean: 13.7563 -> 31.2379 (+127.1%)**
- CK metrikleri bakim maliyetinin arttigini destekliyor:
  - **WMC_mean: 10.3613 -> 15.7848 (+52.3%)**
  - **RFC_mean: 11.2353 -> 17.2508 (+53.5%)**
  - **MPC_mean: 8.6681 -> 16.8511 (+94.4%)**
  - **NOM_mean: 5.1555 -> 6.3236 (+22.7%)**

### Yorumu
Bakim ekibi acisindan resim su: sistem daha fazla kapasite sunuyor, fakat siniflar arasi bagimlilik, mesajlasma ve sinif ici daginiklik arttigi icin **degisikliklerin yan etkisini ongormek** daha zor hale geliyor. Esneklikteki sinirli artis, anlasilabilirlikteki sert dususu telafi etmiyor.

## 3) Teknik borc tahmini

Asagidaki egilimler teknik borc birikimine isaret ediyor:

1. **Artan bagimlilik borcu**
   - **DCC/CBO +29.1%** ve **RFC +53.5%**.
   - Etki: bir sinifta yapilan degisiklik daha fazla sinifi ve daha genis bir cagri yuzeyini etkileyebilir.

2. **Artan davranissal karmasiklik**
   - **WMC +52.3%**, **NOM +22.7%**, **MPC +94.4%**.
   - Etki: test etme, hata ayiklama ve degisiklik etkisi analizi zorlasir.

3. **Cohesion kaybi / sorumluluk daginimi**
   - **CAM -10.1%** ve **LCOM +127.1%**.
   - Etki: siniflarin tek sorumluluga yaklasmak yerine birden fazla ilgisiz davranisi tasiyor olma olasiligi artar.

4. **Soyutlama ve kalitim kapasitesi zayiflamasi**
   - **ANA -48.1%**, **MFA -38.8%**, **Extendibility -45.0%**.
   - Etki: yeni davranis eklemek daha cok mevcut somut kodu degistirmeyi gerektirebilir; bu da teknik borcun tipik belirtisidir.

### En riskli donem
Teknik borcun en belirgin ivmelendigi aralik **1.1.0 - 1.2.0** ve devamidir. Bu bolgede:
- **WMC_mean 11.7724 -> 13.0888 -> 15.4638**
- **LCOM_mean 11.8269 -> 24.6991 -> 30.7989**
- **RFC_mean 12.2500 -> 14.1605 -> 16.0777**
Bu kadar kisa urun araliginda uc metrigin birden bu kadar hizli artmasi, yalnizca "normal buyume" ile aciklanmasi zor bir karmaşıklık birikimine isaret eder.

## 4) Metrik temelli refactoring onerileri

### 1. Yuksek coupling odakli bagimlilik azaltma
- Hedef metrikler: **DCC/CBO, RFC, MPC**
- Neden: DCC/CBO **+29.1%**, RFC **+53.5%**
- Oneri: paket/sinif sinirlarinda **Dependency Inversion**, **Facade**, **Interface Segregation** kullan; ozellikle cok sayida sinifi cagiran servisleri daha dar arayuzlere bol.

### 2. Dusuk cohesion siniflarini bol
- Hedef metrikler: **CAM, LCOM, WMC**
- Neden: CAM **-10.1%**, LCOM **+127.1%**
- Oneri: **Extract Class** ve **SRP** odakli bolme yap; ayni sinifta gevsek iliskili algoritma + veri yapisi + yardimci davranislar bir aradaysa ayir.

### 3. Buyuk/mesaj-yogun siniflarda davranissal sadeleştirme
- Hedef metrikler: **WMC, RFC, CIS, NOM**
- Neden: WMC **+52.3%**, RFC **+53.5%**, NOM **+22.7%**
- Oneri: **Extract Method**, **Move Method**, gereksiz public metodlari daraltma; genis API yuzeyi olan siniflarda sorumluluklari modullere dagit.

### 4. Soyutlama noktalarini geri kazan
- Hedef metrikler: **ANA, MFA, Extendibility**
- Neden: ANA **-48.1%**, MFA **-38.8%**, Extendibility **-45.0%**
- Oneri: degisken algoritmalar icin **Strategy**, olusum mantigi icin **Factory**, varyasyon noktalarinda arayuz tabanli tasarim. Ama amac sadece kalitim eklemek degil; **degisken davranisi somut siniflardan ayirmak** olmali.

### 5. Mimari bagimlilik yonunu gorunur hale getir
- Hedef metrikler: **DCC, CBO, DAC, MOA**
- Neden: **DAC/MOA +87.4%** yararli olabilir, fakat coupling ile birlikte artmasi kontrolsuz nesne agina da isaret edebilir.
- Oneri: veri yapilari, algoritmalar ve yardimci katmanlar arasinda **tek yonlu bagimlilik** kuralini netlestir; paket-ici/packets-arasi bagimlilik denetimi ekle.

## 5) Mimari kalite yorumu: architectural erosion var mi?

### Kisa cevap
**Evet, kismi ama belirgin bir architectural erosion belirtisi var.**

### Sayisal dayanak
- Sistem buyuyor: **DSC 238 -> 618 (+159.7%)**
- Fakat buyume ile birlikte:
  - **DCC/CBO +29.1%**
  - **CAM -10.1%**
  - **LCOM +127.1%**
  - **WMC +52.3%**
  - **RFC +53.5%**
  - **ANA -48.1%**
  - **MFA -38.8%**
  - **Extendibility -45.0%**
- Yani mimari sadece "buyumuyor"; ayni anda **daha bagimli, daha daginik ve daha az soyut** hale geliyor.

### Dengeleyici nokta
Tam bir cokus resmi de yok:
- **Functionality +155.7%**
- **Reusability +157.7%**
- **Effectiveness** yaklasik sabit
Bu, ekibin kapasite ve ozellik kazanimi urettigini; ancak bunu uzun vadede daha pahali bir mimari zeminde yaptigini dusundurur.

## Sonuc
JGraphT `jgrapht-core` surumlerinde genel egilim su sekilde ozetlenebilir:

- **Urun kapasitesi artmis**: Functionality ve Reusability cok guclu artiyor.
- **Bakim maliyeti artmis**: Understandability sert bicimde kotulesiyor; coupling, complexity ve cohesion kaybi bunu destekliyor.
- **Gelecekte degisiklik yapma maliyeti yukselmis**: Extendibility dususu ve ANA/MFA gerilemesi bunun en guclu isareti.
- Bu nedenle kalite hikayesi **"daha yetenekli ama daha zor evrilen sistem"** olarak okunmalidir.