# JGraphT (Sürüm 0.9.0 -> 0.9.2) Yapısal Değişim ve Mimari Kalite Analiz Raporu

Bu rapor, `jgrapht-core` modülünün **0.9.0** sürümünden **0.9.2** sürümüne geçiş sürecindeki mimari evrimini, sağlanan kantitatif tasarım metrikleri ve QMOOD (Quality Model for Object-Oriented Design) kalite modeli ilkeleri doğrultusunda eleştirel bir yaklaşımla analiz etmektedir.

---

## 1. Tasarım Metriklerinin Boyutsal ve Yapısal Değerlendirmesi

Kütüphanenin iki sürümü arasındaki metrik değişimleri incelendiğinde, projenin kontrollü ancak bazı alanlarda tasarım kalitesinden ödün veren bir büyüme evresinde olduğu görülmektedir:

### A. Sistemsel Hacim ve Hiyerarşik Genişleme (DSC, NOH, NOM)
* **DSC (Boyut):** Sınıf sayısı %12.2 oranında artarak **238'den 267'ye** yükselmiştir. Bu 29 yeni sınıf, kütüphaneye net bir fonksiyonel genişleme (yeni graf algoritmaları veya veri yapıları) eklendiğini doğrulamaktadır.
* **NOH (Hiyerarşi):** Sınıf hiyerarşi sayısı %11.4 artışla **35'ten 39'a** çıkmıştır. Hiyerarşideki artışın boyut büyümesiyle paralel olması (%12.2 vs %11.4), yeni eklenen modüllerin sisteme rastgele saçılmak yerine yeni kalıtım ağaçları kurularak organize edildiğini gösterir.
* **NOM (Metot Karmaşıklığı):** Sınıf başına ortalama metot sayısı %1.6 gibi oldukça sınırlı bir artışla **5.155'ten 5.240'a** çıkmıştır. Bu durum, sınıfların içsel metot şişmesine uğramadığını, büyümenin yatayda (yeni sınıflar eklenerek) yönetildiğini kanıtlar.

### B. Soyutlama ve Kalıtım Stratejisi (ANA, MFA, NOP)
* **ANA (Soyutlama) & MFA (Kalıtım):** Ortalama soyutlama seviyesi %8.5 artarak **0.618'den 0.670'e**, kalıtım yoluyla metotların yeniden kullanılma oranı ise %10.2 artışla **0.247'den 0.272'ye** yükselmiştir. Bu iki metrik mimari açıdan **oldukça olumludur**. Geliştiricilerin yeni sınıfları tasarlarken üst sınıflardan (Abstract Class / Interface) türetme yoluna gittiklerini ve kalıtım mekanizmasını daha etkin işlettiklerini gösterir.
* **NOP (Polimorfizm):** Sınıf başına polimorfik metot sayısı %2.5 oranında azalarak **3.273'ten 3.191'e** düşmüştür. Soyutlama ve kalıtım artarken polimorfizmin düşmesi, yeni kurulan hiyerarşilerin esnek (overriding içeren) yapılardan ziyade, doğrudan kod paylaşımı (code reuse) odaklı dikey yapılar olduğunu gösterir.

### C. Bağımlılık ve Eşbirliktelik Dengesi (DCC, CAM)
* **DCC (Bağımlılık/Coupling):** Sınıflar arası doğrudan sıkı bağlılık oranı yalnızca %0.6 artarak **2.349'dan 2.363'e** çıkmıştır. Sistemin boyutu %12.2 büyürken bağımlılık katsayısının neredeyse sabit kalması **büyük bir mimari başarıdır**. Yeni eklenen sınıfların mevcut sınıflara spagetti bağımlılıklarla bağlanmadığını, modüler yapının korunduğunu gösterir.
* **CAM (Eşbirliktelik/Cohesion):** Sınıf içi metotların odaklanmışlığını ölçen CAM metriği %4.8 oranında azalarak **0.407'den 0.387'ye** gerilemiştir. Bu düşüş, **tasarım kalitesi açısından olumsuzdur**. Sınıfların tek bir sorumluluğa odaklanma (Single Responsibility Principle) gücünün zayıfladığını, metotların parametre ve işlev varyasyonlarının heterojenleşmeye başladığını gösterir.

---

## 2. QMOOD Kalite Nitelikleri Açısından Değerlendirme

Tasarım metriklerindeki bu değişimlerin QMOOD kalite denklemlerine yansıması formüller üzerinden analitik olarak aşağıda türetilmiştir:

### A. Reusability (Yeniden Kullanılabilirlik) — Olumlu
* **Denklem:** $-0.25 \cdot DCC + 0.25 \cdot CAM + 0.50 \cdot CIS + 0.50 \cdot DSC$
* **Analiz:** CAM metrisindeki düşüş (-%4.8) ve DCC'deki hafif artış (+%0.6) negatif etki yaratsa da, formülde $0.50$ gibi çok yüksek bir çarpan ağırlığına sahip olan DSC (Boyut) metriğinin %12.2 artması, net Reusability skorunu matematiksel olarak yukarı taşımıştır. Kütüphane daha fazla yeniden kullanılabilir bileşene (sınıfa) sahip olmuştur.

### B. Flexibility (Esneklik) — Kararsız / Hafif Olumsuz
* **Denklem:** $0.25 \cdot DAM - 0.25 \cdot DCC + 0.50 \cdot MOA + 0.50 \cdot NOP$
* **Analiz:** Kompozisyonun (MOA) %8.2 artması esnekliği beslerken; enkapsülasyonun (DAM) %0.6 azalması, bağımlılığın (DCC) %0.6 artması ve en önemlisi esnekliğin ana motoru olan polimorfizmin (NOP) %2.5 azalması sistemi daha statik bir yapıya çekmiştir. Esneklik kazanımı sınırlı kalmış veya hafif bir erozyona uğramıştır.

### C. Understandability (Anlaşılabilirlik) — Olumsuz
* **Denklem:** $-0.33 \cdot (ANA+DCC+NOP+NOM+DSC) + 0.33 \cdot (DAM+CAM)$
* **Analiz:** Sistemin anlaşılabilirliği bu sürüm geçişinde **net bir şekilde gerilemiştir**. Formülün pozitif tarafında yer alan CAM %4.8, DAM %0.6 azalmıştır. Negatif tarafta ise projenin hacmi (DSC = +%12.2) ve karmaşıklığı (NOM = +%1.6) büyümüştür. Proje büyüdükçe ve sınıfların iç bütünlüğü (cohesion) düştükçe, yeni bir geliştiricinin sistemi anlaması zorlaşmıştır.

### D. Extendibility (Genişletilebilirlik) — Olumlu
* **Denklem:** $0.50 \cdot (ANA+MFA+NOP) - 0.50 \cdot DCC$
* **Analiz:** Polimorfizmdeki (NOP) %2.5'lik düşüş olumsuz bir girdi olsa da; soyutlamanın (ANA = +%8.5) ve fonksiyonel kalıtımın (MFA = +%10.2) güçlü yükselişi, DCC'deki minimal artışı bastırmıştır. Sistem, yeni soyut katmanlar kazandığı için gelecekteki geliştirmelere daha açık hale gelmiştir.

---

## 3. Teknik Borç (Technical Debt) Analizi ve İşaretleri

Sürüm 0.9.0'dan 0.9.2'ye geçişte projenin bir **Teknik Borç** biriktirdiğine dair iki belirgin erken uyarı sinyali (Architectural Smell) bulunmaktadır:

1.  **"Cohesion Drop" (Birliktelik Aşınması):** CAM metriğinin %4.8 oranında düşmesi (0.407 -> 0.387), sisteme yeni işlevler eklenirken mevcut sınıfların içine ya da yeni açılan sınıfların gövdesine tam olarak o sınıfa ait olmayan metotların eklendiğini gösterir. Bu durum, uzun vadede sınıfların "Tanrı Sınıf" (God Class) formuna evrilmesine zemin hazırlayan ilk borçlanma adımıdır.
2.  **"Code Reuse Over Polymorphism" (Tasarım Yerine Kolay Kalıtım):** Kalıtım (MFA = +%10.2) ve soyutlama (ANA = +%8.5) artarken polimorfizmin (NOP = -%2.5) düşmesi, kalıtım mekanizmasının nesne yönelimli tasarım esnekliği yaratmak için değil, sadece üst sınıftaki hazır kodları alt sınıflara kopyalamadan taşımak (yani kolay yoldan kod kurtarma) amacıyla kullanıldığını gösterir. Bu, kırılgan hiyerarşiler (Fragile Base Class) yaratma riski taşıyan bir tasarım borcudur.

---

## 4. Sonuç ve Mimari Öneriler

JGraphT'nin 0.9.0 -> 0.9.2 evrimi genel hatlarıyla **kontrollü ve başarılı bir büyümedir**. Bağımlılıkların (DCC) büyüme esnasında dizginlenmesi mimari ekibin başarısıdır. Ancak fonksiyonel genişleme sağlanırken **Understandability** ve **CAM (Cohesion)** kalitesinden ödün verilmiştir.

### Teknik Borcu Kapatmak İçin Somut Refactoring Önerileri:
1.  **Extract Class / Method:** CAM değerini tekrar 0.40 seviyesinin üzerine çekmek için, uyuşmazlığı yüksek sınıflar tespit edilmeli ve ortak parametre/durum paylaşmayan metotlar yeni küçük yardımcı sınıflara bölünmelidir.
2.  **Push Down Method / Refactor Hierarchy:** Kalıtım hiyerarşilerinde (MFA) yukarı taşınan ancak alt sınıfların tamamında polimorfik olarak özelleştirilmeyen metotlar incelenmeli, üst sınıfların sadece ortak soyut sözleşmeleri (interface sorumluluklarını) dikte etmesi sağlanarak NOP puanı optimize edilmelidir.