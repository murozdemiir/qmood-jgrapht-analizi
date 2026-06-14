# JGraphT Sürüm Farkı Kalite Değerlendirme Raporu
**Sürüm Geçişi:** v1.5.2 -> v1.5.3 (jgrapht-core)  
**Analiz Metodolojisi:** QMOOD Model ve Yapısal Metrik Tabanlı Mikro-Değişim Analizi  

---

## 1. Tasarım Metrikleri Değişim Analizi

JGraphT kütüphanesinin v1.5.2 sürümünden v1.5.3 sürümüne geçişi, büyük bir mimari kırılmanın aksine, kod tabanının mevcut yapısal karakteristiğini koruyan mikro ölçekli bir büyüme ve stabilizasyon (maintenance/patch release) evresidir.

### Boyut ve Hiyerarşik Genişleme
* **DSC (Boyut: 601.000 -> 618.000, +%2.8) & NOH (Hiyerarşi: 87.000 -> 91.000, +%4.6):** Kütüphaneye 17 yeni sınıf eklenmiştir. Boyut artışına bağlı olarak kalıtım ağacındaki kök sınıf sayısı da (`NOH`) 4 birim artmıştır. Bu durum, yeni eklenen sınıfların önemli bir kısmının mevcut soyut katmanların altına türetilmek yerine, yeni hiyerarşik kökler veya bağımsız yardımcı yapılar (utility classes) olarak tasarıma dahil edildiğini göstermektedir.

### Nesne Yönelimli Prensipler ve Tasarım Sağlığı
* **ANA (Soyutlama: 0.320 -> 0.320, +%0.3) & MFA (Kalıtım: 0.151 -> 0.151, +%0.1):** Sistemdeki soyutlama seviyesi ve kalıtım yoluyla metot paylaşım oranları neredeyse tamamen sabit kalmıştır. Bu stabilite, yeni eklenen sınıfların kütüphanenin mevcut genel mimari yapısını bozmadığını ancak var olan düşük soyutlama borcunu (sadece %32'lik soyut sınıf/arayüz oranı) iyileştirmek adına bir hamle yapılmadığını da belgeler.
* **DAM (Kapsülleme: 0.881 -> 0.885, +%0.5) & CAM (Uyum: 0.363 -> 0.366, +%0.7):** Kapsülleme ve sınıf içi uyum metriklerinde çok küçük, pozitif yönde salınımlar gözlenmektedir. Büyük bir refactoring olmasa da, yeni eklenen sınıfların veri gizleme kurallarına uyduğu ve kohezyonu baltalamadığı söylenebilir.
* **DCC (Bağlılık: 3.023 -> 3.032, +%0.3) & MOA (Kompozisyon: 0.694 -> 0.701, +%1.0):** Sınıflar arası doğrudan nesne referans bağımlılığı (`DCC`) mikro düzeyde artış göstererek 3.03 seviyesine gelmiştir. Bu hafif artış, nesne kompozisyonundaki (`MOA`) %1.0'lık yükselmeyle paralellik göstermektedir. Geliştiriciler yeni sınıfları entegre ederken kalıtım yerine kompozisyonel bağları tercih etmeye devam etmiştir.

---

## 2. Kalite Niteliği Açısından Değerlendirme

QMOOD denklemleri ve metrik yönelimleri penceresinden bakıldığında, bu sürüm geçişinin kalite üzerindeki etkisi **nötr (stabil)** olarak değerlendirilebilir. 

* **Yüzeysel Değişim Yanılsaması:** Ham QMOOD denklemlerine bakıldığında, boyutun (`DSC`) 601'den 618'e çıkması nedeniyle `Reusability`, `Functionality` ve `Understandability` (negatif yönlü) gibi toplamsal formüllere sahip tüm kalite nitelikleri matematiksel olarak değişecektir. Ancak metriklerin oran tabanlı mikroskobik değişimleri incelendiğinde, yazılım kalitesinde gerçek anlamda radikal bir iyileşme ya da kötüleşme yaşanmamıştır. Tasarım, v1.5.2 sürümündeki yapısal karakteristiğini aynen koruyarak bir sonraki faza aktarmıştır.

---

## 3. Teknik Borç (Technical Debt) Analizi

Bu sürüm geçişinde yeni üretilmiş **akut veya ani bir teknik borç dalgası bulunmamaktadır.** Bağımlılıkların (`DCC` +%0.3) ve iç karmaşıklığın (`NOM` +%0.5) büyüme hızı, boyut büyüme hızının (`DSC` +%2.8) oldukça altında tutulmuştur. Bu durum, bakım aşamasının kontrollü yönetildiğine işaret eder.

Ancak geçmiş sürümlerden devralınan **kronik teknik borçlar** varlığını korumaya devam etmektedir:
1. Sınıflar arası sıkı bağlılık (`DCC: 3.032`) kritik sınır olan 3.0'ın üzerinde kronikleşmiştir.
2. Sınıf içi uyum (`CAM: 0.366`) %50 eşiğinin çok altında kalmaya devam ederek anlaşılabilirliği tehdit etmektedir.
3. Soyutlama oranı (`ANA: 0.320`) sistemin esnek genişlemesini sınırlayan bir bariyer olarak v1.5.3 sürümünde de aynen bırakılmıştır.