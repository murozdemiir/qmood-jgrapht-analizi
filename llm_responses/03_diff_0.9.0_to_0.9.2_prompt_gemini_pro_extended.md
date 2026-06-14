# JGraphT (v0.9.0 -> v0.9.2) Mimari Sürüm Değişim Analizi

**Rol:** Kıdemli Yazılım Mimarisi ve Yazılım Kalitesi Uzmanı
**İncelenen Sürümler:** JGraphT v0.9.0 ve v0.9.2 (jgrapht-core)

Bu rapor, QMOOD nesne yönelimli tasarım metrikleri temel alınarak, JGraphT kütüphanesinin 0.9.0 sürümünden 0.9.2 sürümüne geçişteki mimari evrimini eleştirel bir yaklaşımla değerlendirmektedir.

---

## 1. GENEL DEĞERLENDİRME: OLUMLU MU, OLUMSUZ MU?

Sayısal verilere dayanarak yapılan analiz sonucunda, bu iki sürüm arasındaki geçişin mimari açıdan **son derece olumlu ve sağlıklı bir büyüme** sergilediği görülmektedir. Sistem hacimsel olarak büyürken, nesne yönelimli tasarımın temel prensiplerinden (soyutlama ve kalıtım) taviz verilmemiş, aksine bu prensipler daha da güçlendirilmiştir. 

Özellikle sistemin boyutunu belirten DSC (Sınıf Sayısı) metriği **%12.2** (238'den 267'ye) artarken, dış sınıflara olan bağımlılığı ölçen DCC (Coupling) metriğinin yalnızca **%0.6** (2.349'dan 2.363'e) artması, yazılım mühendisliği açısından nadir görülen, çok başarılı bir "gevşek bağlı (loosely coupled) büyüme" örneğidir.

---

## 2. METRİK BAZLI KANITLAR VE KALİTE NİTELİKLERİNE ETKİSİ

Verilen değişim yüzdeleri, mimari stratejinin yönü hakkında net kanıtlar sunmaktadır:

### A. Extendibility (Genişletilebilirlik) ve Etkililik Üzerindeki Güçlü Artış
QMOOD formülüne göre Genişletilebilirlik; ANA (Soyutlama) ve MFA (Kalıtım) metrikleriyle doğru, DCC (Bağımlılık) ile ters orantılıdır.
* **Kanıt:** Yeni sürümde ANA metriği **%8.5** (0.618 -> 0.670), MFA metriği ise **%10.2** (0.247 -> 0.272) artmıştır. Hiyerarşi ağacı NOH **%11.4** büyümüştür. 
* **Yorum:** Geliştirici ekip, yeni graf algoritmalarını ve veri yapılarını sisteme eklerken doğrudan somut sınıflar (concrete classes) yazmak yerine, arayüzler (interfaces) ve soyut sınıflar (abstract classes) üzerinden yeni hiyerarşiler inşa etmiştir. DCC'nin neredeyse sabit kalmasıyla birleştiğinde, sistemin yeni özelliklere adaptasyon kapasitesi (Extendibility) ciddi şekilde artmıştır.

### B. Composition (MOA) ve Esneklik
* **Kanıt:** MOA (Kompozisyon) metriği **%8.2** oranında (0.374 -> 0.405) artış göstermiştir.
* **Yorum:** Sınıflar, yeteneklerini artırmak için devasa kalıtım zincirlerine girmek yerine, diğer sınıfları birer özellik (field) olarak içerme (has-a ilişkisi) yoluna gitmiştir. Bu durum QMOOD formülündeki Flexibility (Esneklik) niteliğine doğrudan pozitif katkı sağlamıştır.

### C. Understandability (Anlaşılabilirlik) Paradoksu
* **Kanıt:** QMOOD formülünde DSC (Boyut) ve NOM (Karmaşıklık), Anlaşılabilirlik puanını doğrudan aşağı çeken eksi çarpanlardır. DSC **%12.2**, NOM ise hafifçe **%1.6** artmıştır.
* **Yorum:** Sırf sistem büyüdüğü için QMOOD'un ham Understandability puanı matematiksel olarak bir miktar düşecektir. Ancak, NOP (Polimorfizm) ve CIS (Mesajlaşma) metriklerinin sabit kalması, karmaşıklığın kontrol altında tutulduğunu gösterir. Buradaki düşüş mimari bir çöküş değil, modelin hacme verdiği doğal bir cezadır.

---

## 3. TEKNİK BORÇ (TECHNICAL DEBT) SİNYALLERİ VAR MI?

Büyüme genel olarak çok başarılı olsa da, kod tabanında gelecekte refactoring gerektirebilecek ufak bir teknik borç sinyali belirmektedir:

* **Sinyal: Cohesion (Sınıf İçi Tutarlılık) Düşüşü**
  * **Kanıt:** CAM metriği **%4.8** oranında (0.407 -> 0.387) azalmıştır.
  * **Açıklama:** CAM metriğinin düşmesi, sınıfların içindeki metotların ortak veri tiplerini veya parametreleri eskiye kıyasla daha az paylaştığı anlamına gelir. Eklenen 29 yeni sınıf (DSC artışı) veya mevcut sınıflara eklenen yeni metotlar, Tek Sorumluluk Prensibinden (Single Responsibility Principle) hafifçe sapmaya başlamış olabilir.
  * **Risk Durumu:** Şu an için kritik bir seviyede değildir (belirsizlik yoktur, sadece bir eğilimdir). Ancak sonraki sürümlerde CAM düşmeye, NOM (Metot Sayısı) ve WMC artmaya devam ederse "God Class" (Her Şeyi Yapan Sınıf) anti-örüntüsü ortaya çıkabilir. Geliştirici ekibin modül içi tutarlılığa dikkat etmesi gerekmektedir.