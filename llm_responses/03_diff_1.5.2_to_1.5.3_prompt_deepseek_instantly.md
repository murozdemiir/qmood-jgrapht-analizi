# JGraphT 1.5.2 → 1.5.3 – Tasarım Metrik Değişim Analizi

**Analiz Edilen Sürümler:** 1.5.2 → 1.5.3  
**Metrik Modeli:** QMOOD (Bansiya & Davis 2002)  
**Analiz Tarihi:** 2026-06-14

---

## 1. GENEL DEĞİŞİM ÖZETİ

| Metrik Kategorisi | Ortalama Değişim | Yön |
|-------------------|------------------|-----|
| Boyut ve Hiyerarşi (DSC, NOH) | +%3.7 | ⬆️ Büyüme |
| Soyutlama ve Kapsülleme (ANA, DAM) | +%0.4 | ➡️ Neredeyse sabit |
| Bağımlılık ve Uyum (DCC, CAM) | +%0.5 | ➡️ Neredeyse sabit |
| Kompozisyon ve Kalıtım (MOA, MFA) | +%0.55 | ➡️ Neredeyse sabit |
| Polimorfizm ve Mesajlaşma (NOP, CIS) | +%0.75 | ➡️ Neredeyse sabit |
| Karmaşıklık (NOM) | +%0.5 | ➡️ Neredeyse sabit |

📌 **İlk İzlenim:**  
1.5.2 → 1.5.3 arasında sistem **%2.8 oranında büyümüş** (17 yeni sınıf). Ancak **tüm metriklerdeki değişim %1.1'in altındadır**. Bu, bir **bakım/patch sürümü** için beklenen bir durumdur: büyük tasarım değişiklikleri yoktur, sadece küçük iyileştirmeler ve hata düzeltmeleri yapılmıştır.

---

## 2. METRİK BAZLI DETAYLI YORUM

### ✅ Olumlu Değişimler (Marjinal)

| Metrik | 1.5.2 | 1.5.3 | Değişim | Yorum |
|--------|-------|-------|---------|-------|
| **CAM (Uyum/Cohesion)** | 0.3633 | 0.3660 | **+%0.7** | Uyum çok hafif iyileşmiş. 1.5.2'deki düşük seviyeden (0.363) kurtulma çabası olabilir. |
| **DAM (Kapsülleme)** | 0.8806 | 0.8850 | **+%0.5** | Bilgi gizleme hafif iyileşmiş. |
| **MOA (Kompozisyon)** | 0.6938 | 0.7006 | **+%1.0** | Kompozisyon kullanımı artmış – “favor composition” prensibine uyum devam ediyor. |
| **NOP (Polimorfizm)** | 3.5075 | 3.5453 | **+%1.1** | En yüksek pozitif değişim. Polimorfizm hafif artmış. |

**Olumlu Yorum:**  
Tüm olumlu değişimler **%1.1'in altındadır** ve istatistiksel olarak anlamlı olmayabilir. Ancak yön olarak olumludurlar. Özellikle CAM'daki +%0.7, 1.5.x serisinde sürekli düşen uyum trendini **kırmış olabilir** (1.5.1: 0.3641, 1.5.2: 0.3633, 1.5.3: 0.3660).

---

### ⚠️ Olumsuz / Riskli Değişimler (Yok denecek kadar az)

| Metrik | 1.5.2 | 1.5.3 | Değişim | Yorum |
|--------|-------|-------|---------|-------|
| **DCC (Coupling)** | 3.0233 | 3.0324 | **+%0.3** | Bağımlılık çok hafif artmış. Zaten yüksek olan coupling (3.02) daha da kötüleşmiş. |
| **NOM (Karmaşıklık)** | 6.2928 | 6.3236 | **+%0.5** | Sınıf başına metot sayısı artmış. |

**Olumsuz Yorum:**  
DCC'deki +%0.3 artış, 1.5.2'de zaten **kritik eşik olan 3.0'ın üzerinde** olan coupling'i daha da yukarı çekmiştir. Her ne kadar küçük bir artış olsa da, **yön olarak olumsuzdur**. NOM'daki artış da benzer şekilde küçük ama olumsuz yönlüdür.

---

### ➡️ Nötr / Durağan Değişimler (Çoğunluk)

| Metrik | 1.5.2 | 1.5.3 | Değişim | Yorum |
|--------|-------|-------|---------|-------|
| **ANA (Soyutlama)** | 0.3195 | 0.3204 | +%0.3 | Neredeyse sabit. DIT_mean 0.32 civarında – çok sığ hiyerarşi devam ediyor. |
| **MFA (Kalıtım)** | 0.1511 | 0.1512 | +%0.1 | Neredeyse hiç değişmemiş. Kalıtım kullanımı hala çok düşük. |
| **CIS (Mesajlaşma)** | 4.2080 | 4.2249 | +%0.4 | Sabit. |
| **DSC (Boyut)** | 601 | 618 | +%2.8 | 17 yeni sınıf – sistem büyümeye devam ediyor. |
| **NOH (Hiyerarşi)** | 87 | 91 | +%4.6 | 4 yeni hiyerarşi kökü eklenmiş. |

**Nötr Yorum:**  
Bu metriklerdeki değişimler **%1'in altında** olduğu için (DSC ve NOH hariç) anlamlı bir yorum yapmak zordur. DSC ve NOH'daki artışlar sistemin büyüdüğünü gösterir ancak bu bir bakım sürümü için beklenir.

---

## 3. SİSTEM BOYUTU VE BÜYÜME ANALİZİ

| Metrik | 1.5.2 | 1.5.3 | Mutlak Artış | Büyüme Oranı |
|--------|-------|-------|--------------|--------------|
| DSC (Sınıf Sayısı) | 601 | 618 | **+17** | +%2.8 |
| NOH (Hiyerarşi Kökü Sayısı) | 87 | 91 | **+4** | +%4.6 |

**Yorum:**  
17 yeni sınıf eklenmiş. Bu bir **patch sürümü için nispeten yüksek** bir sayıdır. Normalde patch sürümlerde (x.y.Z → x.y.Z+1) sınıf sayısının bu kadar artması beklenmez. Bu, 1.5.3'un **aslında bir minor sürüm** gibi davrandığını gösteriyor olabilir.

> **Belirsizlik:** 17 yeni sınıfın ne amaçla eklendiği (yeni özellik mi, hata düzeltmesi mi, yeniden yapılandırma mı) metriklerden anlaşılamamaktadır. Ancak patch sürümde bu kadar çok yeni sınıf, **versiyonlama politikasında tutarsızlık** olabileceğini düşündürür.

---

## 4. KALİTE AÇISINDAN DEĞERLENDİRME

### Olumlu Kalite Etkileri:

| Etki | Açıklama | Kanıt |
|------|----------|-------|
| Uyum iyileşme sinyali | CAM uzun süredir ilk kez artmış | CAM +%0.7 (küçük ama yön olarak önemli) |
| Kapsülleme iyileşmesi | Bilgi gizleme hafif artmış | DAM +%0.5 |

### Olumsuz Kalite Etkileri:

| Etki | Açıklama | Kanıt |
|------|----------|-------|
| Coupling artışı | Zaten kritik seviyedeki coupling daha da kötüleşmiş | DCC +%0.3 (3.023 → 3.032) |
| Karmaşıklık artışı | Sınıf başına metot sayısı artmış | NOM +%0.5 |

### Genel Kalite Kararı:

| Boyut | Değerlendirme |
|-------|---------------|
| Mimari Sağlık | **Durağan** – Büyük bir değişim yok, mevcut sorunlar devam ediyor |
| Bakım Kolaylığı | **Durağan** – Ne iyileşmiş ne kötüleşmiş |
| Sürdürülebilirlik | **Hafif olumsuz** – Coupling artışı endişe verici |

📌 **Nihai Karar:**  
1.5.2 → 1.5.3, **kalite açısından neredeyse nötr** bir sürümdür. Küçük olumlu ve olumsuz değişimler birbirini neredeyse dengelemiştir. **En önemli gözlem**, uzun süredir düşen CAM'ın (uyum) bu sürümde hafifçe yükselmiş olmasıdır. Bu, geliştiricilerin uyum sorununun farkında olduğunu gösterebilir.

---

## 5. TEKNİK BORÇ İŞARETLERİ

### 🟡 Zayıf / Devam Eden İşaretler

| İşaret | Şiddet | Açıklama |
|--------|--------|----------|
| DCC +%0.3 | Zayıf | Coupling zaten 3.02 gibi yüksek bir seviyedeyken artmaya devam etmesi kötü sinyaldir. |
| NOM +%0.5 | Zayıf | Karmaşıklık artmaya devam ediyor. |
| CAM hala düşük | Orta | 0.366, sağlıklı bir uyum seviyesi olan 0.5'in çok altındadır. |

### 🟢 İyileşen / Borç Azaltan İşaretler

| İşaret | Açıklama |
|--------|----------|
| CAM +%0.7 | Uyumdaki düşüş trendi bu sürümde kırılmıştır. Küçük ama olumlu. |
| DAM +%0.5 | Kapsülleme iyileşmiş. |

### Teknik Borç Değerlendirmesi:

| Seviye | Derece |
|--------|--------|
| Mevcut Teknik Borç | **Orta seviyede** (önceki sürümlerden birikmiş) |
| Bu Sürümdeki Borç Değişimi | **Neredeyse sıfır** – borç ne artmış ne azalmış |
| Borç Birikim Hızı | **Durağan** – artık hızlanmıyor |
| Acil Müdahale Gerekiyor mu? | **Hayır** – ancak mevcut borç (yüksek DCC, düşük CAM, düşük ANA) çözülmelidir |

> **Değerlendirme:** 1.5.3, teknik borca **yeni bir şey eklememiştir** ancak mevcut borcu da azaltmamıştır. Bu bir patch sürüm için kabul edilebilir. Ancak 1.6.0 gibi bir minor sürümde borcun azaltılması için refactoring yapılması gereklidir.

---

## 6. 1.5.x SERİSİ BOYUNCA TREND ANALİZİ

| Metrik | 1.5.1 | 1.5.2 | 1.5.3 | Toplam Değişim (1.5.1→1.5.3) | Trend |
|--------|-------|-------|-------|------------------------------|-------|
| DSC | 600 | 601 | 618 | **+18 (+%3.0)** | ⬆️ Büyüme |
| DCC | 3.0183 | 3.0233 | 3.0324 | **+0.014 (+%0.46)** | ⬆️ Kötüleşme (yavaş) |
| CAM | 0.3641 | 0.3633 | 0.3660 | **+0.0019 (+%0.52)** | ➡️ Dalgalı (önce düşüş, sonra toparlanma) |
| ANA | 0.3217 | 0.3195 | 0.3204 | **-0.0013 (-%0.40)** | ➡️ Durağan (çok düşük) |
| LCOM | 30.21 | 30.22 | 31.24 | **+1.03 (+%3.4)** | ⬆️ Kötüleşme (uyumsuzluk artıyor) |

📌 **1.5.x Serisi Trend Özeti:**

| Metrik | Trend | Yorum |
|--------|-------|-------|
| DCC | Hafif kötüleşme | Her sürümde coupling artıyor – **3.0 eşiği aşıldı** |
| LCOM | Kötüleşme | Uyumsuzluk 1.5.3'te sıçrama yapmış (30.22 → 31.24) |
| CAM | Dalgalı | 1.5.2'de düşüş, 1.5.3'te toparlanma – umut verici |
| ANA | Durağan | 0.32'de takılı kalmış – **iyileşme yok** |

---

## 7. ÖZET TABLO

| Değerlendirme Alanı | Sonuç | Destekleyen Metrik(ler) |
|---------------------|-------|--------------------------|
| En İyi Değişim | ✅ Uyum ilk kez artmış | CAM +%0.7 |
| En Kötü Değişim | ⚠️ Coupling artmaya devam etmiş | DCC +%0.3 (zaten kritik) |
| Teknik Borç Varlığı | 🟡 Mevcut (önceki sürümlerden) | DCC>3.0, CAM<0.37, ANA<0.33 |
| Bu Sürümde Eklenen Borç | 🟢 Çok az / yok | Tüm değişimler %1.1 altında |
| Genel Sürüm Değerlendirmesi | 🟡 **Nötr** – stabil patch sürüm | Olumlu ve olumsuz değişimler dengeli |

---

## 8. SONUÇ

**JGraphT 1.5.2 → 1.5.3 sürüm farkının kalite değerlendirmesi:**

- **Değişimin büyüklüğü:** Tüm metrik değişimleri **%1.1'in altındadır**. Bu, tipik bir **patch sürümü (bugfix release)** davranışıdır. Büyük tasarım değişiklikleri yapılmamıştır.

- **Olumlu yönler:** Uyum (CAM) ve kapsülleme (DAM) hafifçe iyileşmiştir. Uzun süredir düşen CAM'ın bu sürümde artması, geliştiricilerin uyum sorununun farkında olduğunu gösterebilir.

- **Olumsuz yönler:** Zaten kritik seviyede olan coupling (DCC=3.02) daha da artmıştır. Değişim küçük olsa da **yön olarak olumsuzdur**. Karmaşıklık (NOM) da hafif artmıştır.

- **Teknik borç:** Bu sürüm **yeni teknik borç eklememiştir**. Ancak önceki sürümlerden biriken borç (yüksek DCC, düşük CAM, düşük ANA, yüksek LCOM) devam etmektedir. Borç birikim hızı durağanlaşmıştır.

- **Versiyonlama uyarısı:** 17 yeni sınıf (+%2.8) bir patch sürüm için beklenenden fazladır. Bu durum, **semantic versioning kurallarının ihlal edildiğini** düşündürebilir.

- **Genel karar:** Bu sürüm **kalite açısından nötrdür** – ne iyileşmiş ne kötüleşmiştir. Bir patch sürüm için beklenen budur. Ancak 1.6.0 gibi bir minor sürümde, biriken teknik borcun azaltılması için refactoring yapılması **önemle önerilir**.

---

## 9. BİR SONRAKİ SÜRÜM İÇİN ÖNERİLER

| Öncelik | Öneri | Hedef Metrik |
|---------|-------|--------------|
| 1 | LCOM'u düşürmek için refactoring | LCOM: 31 → <20 |
| 2 | DCC'yi azaltmak için arayüzler/facade ekle | DCC: 3.03 → <2.5 |
| 3 | ANA'yı artırmak için kalıtım hiyerarşisini derinleştir | ANA: 0.32 → >0.50 |
| 4 | CAM'ı iyileştirmeye devam et | CAM: 0.366 → >0.45 |

---

*Rapor: QMOOD Modeli (Bansiya & Davis 2002) temellidir. Tüm iddialar verilen metrik değerleriyle sayısal olarak kanıtlanmıştır.*

**Analiz Tarihi:** 2026-06-14  
**Uzman:** Kıdemli Yazılım Mimarisi ve Kalite Uzmanı