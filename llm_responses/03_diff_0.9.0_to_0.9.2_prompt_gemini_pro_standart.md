# JGraphT 0.9.0 - 0.9.2 Sürümleri Arası Mimari Değişim ve Kalite Analizi

## 1. Genel Mimari Eğilim: Kontrollü Büyüme
JGraphT 0.9.0'dan 0.9.2'ye geçişte sistem boyutu (`DSC`) %12.2 oranında artarak 238'den 267 sınıfa çıkmıştır. Bu büyüme ile eşzamanlı olarak hiyerarşi derinliği (`NOH`) %11.4 artmıştır (35'ten 39'a). Sürüm geçişindeki en dikkat çekici başarı, yaklaşık %12'lik bu hacimsel büyümenin, sınıflar arası bağımlılıkta (`DCC`: 2.349 -> 2.363, sadece %0.6 artış) bir patlamaya yol açmadan yönetilebilmiş olmasıdır. Bu durum, büyümenin kontrolsüz bir kod yığını şeklinde olmadığını gösterir.

## 2. Olumlu Kalite Değişimleri: Genişletilebilirlik (Extendibility)
Bu sürüm geçişindeki en pozitif tablo, kütüphanenin genişletilebilirlik kapasitesinde görülmektedir.
* **Kanıt:** Sistemin soyutlama oranı (`ANA`) %8.5 (0.618 -> 0.670), kalıtım kullanımı (`MFA`) ise %10.2 (0.247 -> 0.272) oranında artmıştır.
* **Analiz:** Yeni eklenen 29 sınıfın önemli bir kısmının soyut sınıflar (abstract classes) ve arayüzler (interfaces) üzerinden sisteme entegre edildiği, somut (concrete) implementasyonlardan kaçınıldığı görülmektedir. QMOOD Genişletilebilirlik formülüne (`0.50*(ANA+MFA+NOP) - 0.50*DCC`) göre; `ANA` ve `MFA` değerlerindeki bu eşzamanlı sıçrama ve negatif etken olan `DCC`'nin (Bağımlılık) neredeyse sabit kalması, kütüphanenin esnekliğini ciddi şekilde artırmıştır. Yeni özellikler katı bağımlılıklarla değil, polimorfik hiyerarşilerle eklenmiştir.

## 3. Olumsuz Değişimler ve Teknik Borç (Technical Debt) Sinyalleri
Sistem makro mimari ve soyutlama anlamında iyiye gitse de, mikro boyutta (sınıf içi tasarım) belirgin teknik borç sinyalleri üretmekte ve **Understandability (Anlaşılabilirlik)** niteliğine zarar vermektedir.
* **Kanıt 1 (Düşen Uyum):** Sınıf içi metotların ortak veri kullanımını ve odaklılığını ölçen `CAM` (Cohesion) metriği %4.8 düşerek 0.407'den 0.387'ye gerilemiştir.
* **Kanıt 2 (Artan Sınıf Yükü):** Sınıfların başka nesneleri alan (field) olarak barındırma/kompozisyon oranı (`MOA`) %8.2 artarken, ortalama karmaşıklık/metot sayısı (`NOM`) %1.6 artmıştır. 
* **Analiz:** QMOOD Anlaşılabilirlik formülünde pozitif çarpanı olan `CAM` (Uyum) düşerken, negatif etki yaratan `DSC` (Boyut) ve `NOM` (Karmaşıklık) artmıştır. Bu veriler incelendiğinde; sınıfların içine yeni nesne referansları (artan `MOA`) ve yeni metotlar (artan `NOM`) eklendiği, ancak bu yeni eklenen parçaların sınıfın asıl amacıyla veya diğer metotlarla yeterince ilişkili olmadığı (düşen `CAM`) anlaşılmaktadır. Bu durum *Single Responsibility Principle* (Tek Sorumluluk Prensibi) ihlallerinin başladığına ve sınıfların odaklarını kaybederek "şişmeye" (Bloater antipaterni) başladığına dair net bir teknik borç kanıtıdır.

## 4. Sonuç Kararı
**Değerlendirme:** Genel olarak olumlu, ancak iç bakım onarımı gerektiriyor.
1. Kütüphanenin yapısal büyüme stratejisi (yüksek soyutlama, düşük bağımlılık artışı) son derece sağlıklıdır. Kullanıcılar açısından JGraphT 0.9.2, 0.9.0'a göre daha kolay genişletilebilir ve entegre edilebilir bir yapı sunmaktadır.
2. Ancak sistemin *iç geliştiricileri* için tehlike çanları çalmaktadır. Düşen sınıf içi uyum (`CAM`) acil refactoring gerektirir. Büyüyen sınıfların içindeki kopuk metot ve veri kümeleri tespit edilip, yeni alt sınıflara (Extract Class) bölünmezse, artan bilişsel yük ileriki sürümlerde bakım maliyetlerini katlayacaktır.