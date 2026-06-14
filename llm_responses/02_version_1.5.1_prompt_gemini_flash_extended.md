# JGraphT Sürüm 1.5.1 Mimari ve Kalite Değerlendirme Raporu

Bu teknik rapor, `jgrapht-core` modülünün **1.5.1** sürümünden elde edilen QMOOD ve CK metrik veri kümelerini analiz ederek sistemin mimari durumunu, tasarım kusurlarını ve kritik risk alanlarını kantitatif kanıtlarla ortaya koymaktadır.

---

## 1. Genel Kalite Durum Analizi

JGraphT 1.5.1 sürümü, **600 sınıf** (DSC/num_classes) içeren büyük ölçekli bir kütüphanedir. Sistemin genel tasarım özellikleri incelendiğinde iki temel karakter ön plana çıkmaktadır:

* **Yüksek Enkapsülasyon ve Kompozisyon Eğilimi:** Sistem düzeyinde kapsülleme oldukça başarılıdır (DAM = 0.8794). Sınıflar verilerini büyük oranda gizlemektedir. Benzer şekilde kompozisyon kullanımı da (MOA = 0.6917 / DAC_mean = 0.6917) kütüphanenin kalıtım yerine nesne ilişkilerini tercih ettiğini göstermektedir.
* **Zayıf Soyutlama Mimarisi:** Kararlı tasarımlarda görmeyi beklediğimiz kalıtım derinliği (DIT_mean = 0.3217) ve fonksiyonel kalıtım oranı (MFA = 0.1523) oldukça düşüktür. Bu durum, kütüphanenin geniş tabanlı bir soyutlama hiyerarşisi kurmak yerine somut (concrete) sınıflar üzerinden dikey büyümeyi seçtiğine işaret eder.

---

## 2. En Zayıf 2 Kalite Niteliği ve Sorumlu Metrikler

QMOOD denklemleri ve ham kalite çıktıları analiz edildiğinde, sistemin en zayıf iki yapısal alanı **Understandability (Anlaşılabilirlik)** ve **Extendibility (Genişletilebilirlik)** olarak tespit edilmiştir.

### A. Anlaşılabilirlik (Understandability = -201.9385)
QMOOD modelinde absolute değer olarak en kritik negatif skora sahip niteliktir. Sistemin anlaşılmasının bu denli zor olmasının matematiksel gerekçeleri şunlardır:
* **Yüksek Boyut ve Karmaşıklık Yükü:** Denklemde negatif çarpan ağırlığına sahip olan sınıf sayısı (DSC = 600) ve sınıf başına ortalama metot karmaşıklığı (NOM = 6.32) sistemi basitleştirmekten uzaklaştırmaktadır.
* **Birliktelik (Cohesion) Eksikliği:** Pozitif çarpan olan CAM (Cohesion Among Methods) metriği **0.3641** gibi düşük bir seviyededir. Sınıfların iç odaklanmasının zayıf olması, kodun okunabilirliğini baltalamaktadır.

### B. Genişletilebilirlik (Extendibility = 0.4870)
Esneklik (1.5703) ve Etkinlik (1.1127) değerlerine kıyasla sıfır sınırına en yakın mimari niteliktir. `Extendibility = 0.50*(ANA+MFA+NOP) - 0.50*DCC` formülü üzerinden incelendiğinde zayıflık nedenleri şunlardır:
* **Bağımlılık Baskısı (Coupling):** Sınıflar arası sıkı bağlılık (DCC = 3.0183), formüldeki pozitif soyutlama bloklarının (ANA = 0.3217 + MFA = 0.1523 = 0.4740) toplam etkisini tek başına sıfırlamaktadır. 
* **Polimorfizm Bağımlılığı:** Genişletilebilirlik puanını ayakta tutan yegane unsur polimorfizm (NOP = 3.5183) düzeyidir. Eğer polimorfik yapı zayıflarsa, sistem tamamen kilitlenme (değişikliğe direnç) riski taşımaktadır.

---

## 3. CK Maksimum Değerlerinin (Outlier) Kritik Analizi

Sistem ortalamaları (mean) kabul edilebilir sınırlar içinde görünse de, maksimum (`_max`) CK değerleri sistemde çok ciddi mimari sapmalar (anomali) olduğunu kanıtlamaktadır:

* **LCOM_max = 4371:** Sistemin ortalama LCOM değeri 30.21 iken, bir veya birkaç sınıfın 4371 gibi aşırı yüksek bir LCOM değerine sahip olması, bu sınıfların **"Cohesion" (Eşbirliktelik) ilkesini tamamen ihlal ettiğini** gösterir. Bu sınıflar muhtemelen birbiriyle tamamen alakasız yüzlerce işi bir arada yapan devasa "Utility" veya "God Class" yapılarıdır.
* **WMC_max = 381:** Sınıf içi ağırlıklı karmaşıklığın 381 olması, tek bir sınıfın içinde yüzlerce kontrol ifadesi (if-else, switch, loop) barındığını gösterir. Bu sınıfın bakımını yapmak, hata ayıklamak ve birim testini yazmak neredeyse imkansızdır.
* **MPC_max = 403 ve RFC_max = 151:** Bir sınıfın dışarıya 403 farklı mesaj göndermesi (MPC) ve yanıt kümesinde 151 metoda erişebilmesi (RFC), sistemin merkezinde **aşırı merkeziyetçi (Hub Class)** bir yapının kurulduğunu, bu yapının çökmesi durumunda tüm kütüphanenin etkileneceğini gösterir.

---

## 4. Somut Refactoring (Yeniden Yapılandırma) Önerileri

Mevcut metrik anomalilerini temizlemek ve sistemin hayati değerlerini iyileştirmek için şu 3 somut yeniden yapılandırma adımı uygulanmalıdır:

### Öneri 1: Tanrı Sınıfların Parçalanması (Extract Class / Extract Subclass)
* **Hedef Metrikler:** LCOM_max (4371) değerini düşürmek, CAM (0.3641) değerini yükseltmek.
* **Uygulama:** LCOM değeri binlerin üzerinde olan uç sınıflar tespit edilmeli, içerdikleri metotlar ve örnek değişkenler (instance variables) mantıksal sorumluluklarına göre gruplanmalıdır. Bu gruplar bağımsız, tek sorumluluğa sahip (SRP) yeni alt sınıflara bölünmelidir. Bu sayede Understandability doğrudan iyileşecektir.

### Öneri 2: Koşullu Mantığın Polimorfizme Dönüştürülmesi (Replace Conditional with Polymorphism)
* **Hedef Metrikler:** WMC_max (381) ve WMC_mean (15.77) değerlerini düşürmek, ANA (0.3217) değerini yükseltmek.
* **Uygulama:** Graf veri yapılarının veya algoritmalarının varyasyonlarını (örn. farklı yönlü/yönsüz graf tipleri için işletilen özel mantıklar) tek bir sınıfın içinde `if-else` veya `switch-case` bloklarıyla yönetmek yerine, üst bir arayüz (Interface) tanımlanmalı ve her varyasyon polimorfik bir alt sınıfa devredilmelidir. Bu, dikey karmaşıklığı azaltıp soyutlamayı artıracaktır.

### Öneri 3: Mesaj Trafiğinin Sınırlandırılması ve Arayüz İzolasyonu (Extract Interface / Facade Pattern)
* **Hedef Metrikler:** MPC_max (403), CBO_max (21) ve DCC (3.0183) değerlerini azaltmak.
* **Uygulama:** Diğer sınıflarla aşırı yüksek etkileşim içinde olan merkezi düğüm sınıflarının önüne birer soyutlama katmanı veya Facade (Görünüş) arayüzü eklenmelidir. Sınıfların birbirine doğrudan somut referanslar üzerinden bağlanması engellenerek, bağımlılık çağrı trafiği arayüzler üzerinden dağıtılmalıdır. Bu müdahale, sistemin Extendibility puanını doğrudan yükseltecektir.