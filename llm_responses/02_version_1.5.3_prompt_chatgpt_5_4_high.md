# JGraphT 1.5.3 - QMOOD Tabanli Derin Kalite Degerlendirmesi

## Kapsam ve yontem
Bu not, **yalnizca verilen 1.5.3 verilerine** dayanir. Yorumlar, QMOOD denklemleri ile CK ortalamalari/maksimumlari birlikte okunarak yapilmistir.

> Onemli sinir: QMOOD kalite niteliklerinin ham degerleri ayni olcekte degildir. Bu nedenle "en zayif" nitelikleri belirlerken yalniz ham skora degil, **formuldeki negatif/pozitif katkilara** ve CK metriklerinin neyi isaret ettigine bakiyorum.

## 1) Kisa kalite ozeti
JGraphT 1.5.3, **islev kapsami genis** ve **yeniden kullanima uygun** bir yapi gosteriyor; ancak **anlasilabilirlik** ve **genisletilebilirlik** tarafinda belirgin baskilar var.

- **Reusability = 310.4459**  
  Bu skorun ana surucusu boyuttur: `0.50*DSC = 309.0000`. Buna ek olarak `0.50*CIS = 2.1125` pozitif katki veriyor. `-0.25*DCC = -0.7581` olumsuz etki yapiyor ama boyut avantaji bunu baskiliyor.
- **Functionality = 157.7334**  
  Bunun da ana surucusu yine boyut ve hiyerarsidir: `0.22*DSC = 135.9600`, `0.22*NOH = 20.0200`. Yani islevsellik yuksek, fakat bu daha cok **sinif ve API kapsam genisligi** ile aciklaniyor.
- **Flexibility = 1.5861** ve **Effectiveness = 1.1205**  
  Her ikisi de pozitif, fakat ozellikle Flexibility, `NOP = 3.5453` ve `MOA = 0.7006` tarafindan tasiniyor; coupling cezasi hala gorunur duzeyde.

Bu nedenle bu surum icin kisa yargi sunudur:

**Guc yan:** kapsamli ve kullanisli bir kutuphane mimarisi.  
**Zayif yan:** buyukluk, coupling ve karmaşıklık arttikca sistemi anlamak ve kontrollu bicimde genisletmek zorlasiyor.

---

## 2) En zayif 2 kalite niteligi ve sorumlu metrikler

## 2.1 Understandability - en zayif nitelik
- **Ham skor:** `-207.8903`

QMOOD formulu:
`Understandability = -0.33*(ANA + DCC + NOP + NOM + DSC) + 0.33*(DAM + CAM)`

### Sayisal katki kirilimi
Negatif terimler:
- `-0.33*DSC = -203.9400`
- `-0.33*NOM = -2.0868`
- `-0.33*NOP = -1.1699`
- `-0.33*DCC = -1.0007`
- `-0.33*ANA = -0.1057`

Pozitif terimler:
- `+0.33*DAM = +0.2921`
- `+0.33*CAM = +0.1208`

Toplam:
- **Negatif blok = -208.3032**
- **Pozitif blok = +0.4128**
- **Net = -207.8903**

### Neden zayif?
1. **Boyut etkisi cok baskin.**  
   `DSC = 618` oldugu icin tek basina `-203.9400` ceza uretmektedir. Bu, Understandability'deki toplam negatif baskinin yaklasik **%97.9**'una karsilik gelir. Yani bu skorun buyuk bolumu, sistemin artik **cok buyuk** hale gelmis olmasindan kaynaklaniyor.

2. **Karmasiklik ve arayuz yuzeyi de cezayi artiriyor.**  
   `NOM = 6.3236` -> `-2.0868`  
   `NOP = 3.5453` -> `-1.1699`  
   `DCC = 3.0324` -> `-1.0007`  
   Bunlar DSC kadar baskin degil, ama "buyuk sistem + daha fazla davranis + daha fazla bagimlilik" kombinasyonunu gosterdigi icin anlasilabilirligi daha da asagi cekiyor.

3. **Pozitif dengeleyiciler zayif kaliyor.**  
   `DAM = 0.8850` yuksek olmasina ragmen katkisi yalniz `+0.2921`;  
   `CAM = 0.3660` ise yalniz `+0.1208` katkı veriyor.  
   Yani kapsulleme iyi olsa da, **cohesion yeterince yuksek degil** ve bu iki metrik, boyut/karmasiklik/coupling baskisini dengeleyemiyor.

### CK metrikleriyle destek
- `WMC_mean = 15.7848` -> sinif basina davranis yukunun dusuk olmadigini gosteriyor.
- `RFC_mean = 17.2508` -> mesajlasma/cevap yuzeyi genis.
- `LCOM_mean = 31.2379` -> cohesion sorunu sinif icinde hissediliyor.
- `NOM_mean = 6.3236` -> metod sayisi kayda deger.
- Maksimumlar daha da kritik:
  - `WMC_max = 381`
  - `RFC_max = 149`
  - `LCOM_max = 4371`
  - `NOM_max = 95`

Bu maksimumlar, ortalamadan bagimsiz olarak, sistemde **cok problemli hotspot siniflar** bulundugunu gosteriyor. Dolayisiyla anlasilabilirlik yalniz "sistem buyuk" oldugu icin degil, bazi siniflarin **asiri yuklu** olmasi nedeniyle de zayif.

**Sonuc:**  
Understandability'nin en zayif nitelik olmasinin ana nedeni `DSC=618` ile gelen olcek baskisi; ikincil nedenleri ise `NOM`, `DCC`, `RFC`, `WMC` ve ozellikle `LCOM` ile gorulen sinif-ici ve siniflar-arasi karmaşıkliktir.

---

## 2.2 Extendibility - ikinci en zayif nitelik
- **Ham skor:** `0.4923`

QMOOD formulu:
`Extendibility = 0.50*(ANA + MFA + NOP) - 0.50*DCC`

### Sayisal katki kirilimi
Pozitif taraf:
- `+0.50*ANA = +0.1602`
- `+0.50*MFA = +0.0756`
- `+0.50*NOP = +1.7727`

Negatif taraf:
- `-0.50*DCC = -1.5162`

Toplam:
- **Pozitif blok = +2.0085**
- **Negatif blok = -1.5162**
- **Net = +0.4923**

### Neden zayif?
1. **Coupling cezasi cok yuksek.**  
   `DCC = 3.0324`, Extendibility formulu icinde `-1.5162` ceza uretmektedir. Bu, pozitif bloktaki toplam katkının yaklasik **%75.5**'ini geri almaktadir. Baska bir ifadeyle genisletilebilirlik kazanimi var, ama coupling onun buyuk kismini siliyor.

2. **Soyutlama ve kalitim katkisi zayif.**
   - `ANA = 0.3204` -> `+0.1602`
   - `MFA = 0.1512` -> `+0.0756`

   Pozitif tarafta asil agirlik `NOP = 3.5453` ile geliyor (`+1.7727`). Bu da su anlama gelir: sistem polymorphic davranis uretiyor, fakat **bunu tasiyacak abstraction/inheritance omurgasi sinirli**. Dolayisiyla genisletilebilirlik, teorik olarak var ama mimari olarak cok guclu temellenmemis.

3. **CK tarafinda coupling ve yuzey alanı sinyali var.**
   - `CBO_mean = 3.0324`
   - `DAC_mean = 0.7006`
   - `RFC_mean = 17.2508`
   - `CBO_max = 21`

   Ozellikle `CBO_max = 21`, bazi siniflarin cok sayida baska sinifa bagli oldugunu gosterir. Bu tip siniflarda yeni davranis eklemek genelde zincirleme etki yaratir; bu da pratikte extendibility'yi dusurur.

**Sonuc:**  
Extendibility'nin zayif olmasinin temel nedeni **artan coupling**, ikinci nedeni ise **dusuk ANA/MFA ile sinirli soyutlama derinligi**dir. Polimorfizm var, ama onu destekleyen soyut tasarim daha zayif.

---

## 3) Diger kalite nitelikleri icin kisa not
Bu bolum, zayif iki niteligi baglama oturtmak icindir.

### Flexibility = 1.5861
Katkilar:
- `+0.25*DAM = +0.2213`
- `-0.25*DCC = -0.7581`
- `+0.50*MOA = +0.3503`
- `+0.50*NOP = +1.7727`

Burada esneklik **NOP** ve kismen **MOA** ile korunuyor. Ancak `DCC` cezası hala yuksek oldugu icin, daha fazla coupling artisi olursa bu nitelik kolayca bozulabilir.

### Functionality = 157.7334
Katkilar:
- `+0.12*CAM = +0.0439`
- `+0.22*NOP = +0.7800`
- `+0.22*CIS = +0.9295`
- `+0.22*DSC = +135.9600`
- `+0.22*NOH = +20.0200`

Islevsellik guclu; ancak bu skorun buyuk kismi `DSC` ve `NOH` kaynakli. Yani "per-class sadelik" degil, daha cok **kapsam genisligi** bu sonucu uretmektedir.

---

## 4) Uc somut refactoring onerisi

## Oneri 1 - Hotspot siniflari bol: Extract Class / Move Method / Facade ayristirma
**Hedef metrikler:** `WMC`, `RFC`, `NOM`, `LCOM`, dolayli olarak `CAM`

### Gerekce
- `WMC_mean = 15.7848`, `WMC_max = 381`
- `RFC_mean = 17.2508`, `RFC_max = 149`
- `NOM_mean = 6.3236`, `NOM_max = 95`
- `LCOM_mean = 31.2379`, `LCOM_max = 4371`

Bu sayilar, bazi siniflarin asiri fazla sorumluluk topladigini gosteriyor. Tek sinifta cok fazla metod, yuksek response seti ve cok yuksek LCOM genelde **God Class / Blob** belirtisidir.

### Somut uygulama
- Algoritma ailelerini (ornegin traversal, shortest path, matching, flow vb.) daha dar amacli yardimci tiplere ayirmak
- Durum yonetimi, validasyon, donusum ve algoritmik cekirdegi ayni sinifta topluyorsa bunlari ayri siniflara tasimak
- Genis yuzeyli yardimci siniflar uzerine Facade koyup, ic detaylari ic modullere itmek

### Beklenen etki
- `NOM`, `WMC`, `RFC` ve `LCOM` duser
- `CAM` artar
- **Understandability** dogrudan iyilesir

---

## Oneri 2 - Yuksek bagimlilikli siniflarda Interface Segregation + Dependency Inversion uygula
**Hedef metrikler:** `DCC/CBO`, `RFC`, kismen `CIS`

### Gerekce
- `DCC = 3.0324`
- `CBO_mean = 3.0324`, `CBO_max = 21`
- `RFC_mean = 17.2508`

Genisletilebilirlikteki en buyuk ceza dogrudan `DCC`'den geliyor (`-1.5162`). Bu nedenle refactoring'in en yuksek getirili alani coupling'i dusurmektir.

### Somut uygulama
- Somut tiplere bagli kullanimlari dar arabirimlere cekmek
- Bir sinif birden fazla "rol" oynuyorsa arabirimleri bolmek
- Iki yonlu bagimliliklari event/callback veya adapter ile tek yone dusurmek
- Ozellikle cok sayida graph varyantina dogrudan bagli siniflarda "capability interface" yapisi kullanmak

### Beklenen etki
- `DCC/CBO` azalir
- `RFC` duser
- **Extendibility** ve **Flexibility** iyilesir
- Degisikliklerin zincirleme yan etkisi azalir

---

## Oneri 3 - Ortak davranislar icin hedefli soyutlama: Template Method / Strategy / abstract helper katmani
**Hedef metrikler:** `ANA`, `MFA`, kismen `CAM`

### Gerekce
- `ANA = 0.3204` dusuk
- `MFA = 0.1512` dusuk
- `DIT_mean = 0.3204`, `NOC_mean = 0.568`

Bu tablo, sistemin polimorfik davranis urettigini (`NOP = 3.5453`) ama bunu tasiyan soyut tasarimin daha sinirli oldugunu gosteriyor. Yani varyasyonlar var; fakat bu varyasyonlar her yerde yeterince ortak soyutlama altina alinmamis olabilir.

### Somut uygulama
- Benzer algoritma adimlari icin Template Method kullanmak
- Heuristik/agirliklandirma/edge policy gibi degisen kurallari Strategy nesnelerine cikarmak
- Benzer yardimci akislari abstract base veya protected helper katmaninda toplamak
- Ancak bunu yaparken gereksiz derin kalitim zinciri kurmamak; amac `ANA` ve `MFA`'yi **hedefli** bicimde artirmaktir

### Beklenen etki
- `ANA` ve `MFA` artar
- Kopya davranis azalir
- Yeni varyant ekleme maliyeti duser
- **Extendibility** daha dengeli hale gelir

---

## 5) Sonuc
JGraphT 1.5.3, **buyuk ve islevsel** bir kutuphane gorunumu veriyor; ancak kalite profilinde iki belirgin zayiflik var:

1. **Understandability (-207.8903)**  
   En baskin neden `DSC = 618` ile gelen olcek etkisi; bunu `NOM`, `DCC`, `RFC`, `WMC` ve ozellikle `LCOM` destekli hotspot karmaşıkligi izliyor.

2. **Extendibility (0.4923)**  
   En baskin neden `DCC = 3.0324` ile gelen coupling cezasi; dusuk `ANA` ve `MFA` bu cezayi yeterince dengeleyemiyor.

Kisa yargi:
- **Kapsam ve kullanislik guclu**
- **Bakim ve kontrollu genisleme maliyeti yukselme egiliminde**
- En yuksek geri donus, **hotspot sinif bolme**, **coupling azaltma** ve **hedefli soyutlama** refactoring'lerinden gelecektir.