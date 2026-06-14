# JGraphT 0.9.0 → 0.9.2 – Sürüm Farkı Analizi (QMOOD)

## 1. GENEL DEĞİŞİM ÖZETİ

### Boyut ve Yapısal Büyüme
- **DSC:** 238 → 267 (**+12.2%**)
- **NOH:** 35 → 39 (**+11.4%**)

➡️ Sistem büyümüş ve hiyerarşi genişlemiş.

---

## 2. TASARIM METRİKLERİ YORUMU

### 2.1 Olumlu Değişimler

#### Soyutlama ve Kalıtım
- **ANA:** 0.618 → 0.670 (**+8.5%**)
- **MFA:** 0.247 → 0.272 (**+10.2%**)

➡️ Daha fazla soyutlama ve inheritance kullanımı → **daha iyi yeniden kullanılabilirlik potansiyeli**

#### Kompozisyon
- **MOA:** 0.374 → 0.405 (**+8.2%**)

➡️ Composition artışı → esneklik için olumlu sinyal

---

### 2.2 Olumsuz Değişimler

#### Cohesion
- **CAM:** 0.407 → 0.387 (**-4.8%**)

➡️ Sınıf içi tutarlılık azalmış → cohesion düşmüş

#### Coupling
- **DCC:** 2.349 → 2.363 (**+0.6%**)

➡️ Küçük ama negatif artış → bağımlılıklar artıyor

---

### 2.3 Nötr / Karışık Etkiler

- **DAM:** -0.6% (önemsiz değişim)
- **NOP:** -2.5% → polymorphism biraz azalmış
- **CIS:** -0.2% → stabil
- **NOM:** +1.6% → karmaşıklık hafif artmış

---

## 3. KALİTE ETKİ ANALİZİ

### Pozitif Etkiler:
- ANA ↑ + MFA ↑ → **Extendibility ve Reusability için olumlu**
- MOA ↑ → **Flexibility için olumlu**

### Negatif Etkiler:
- CAM ↓ → cohesion düşüşü → **Understandability ve Maintainability olumsuz**
- DCC ↑ → coupling artışı → **Extendibility ve Maintainability olumsuz**
- NOM ↑ → karmaşıklık artışı → **Understandability olumsuz**

---

## 4. TEKNİK BORÇ ANALİZİ

### Erken Sinyaller:

- **Coupling artıyor (DCC +0.6%)**
- **Cohesion düşüyor (CAM -4.8%)**
- **Karmaşıklık artıyor (NOM +1.6%)**

➡️ Bu üçlü kombinasyon:
- düşük cohesion
- yüksek coupling
- artan complexity

→ **teknik borç birikiminin başlangıç sinyali**

⚠️ Ancak:
- artışlar düşük seviyede → **henüz kritik değil**

---

## 5. GENEL DEĞERLENDİRME

### Olumlu:
- Sistem daha soyut ve genişletilebilir hale geliyor (ANA, MFA, MOA artışı)

### Olumsuz:
- Modüler kalite zayıflıyor (CAM düşüşü, DCC artışı)

### Net Sonuç:
Bu sürüm geçişi:

➡️ **Fonksiyonel ve mimari kapasiteyi artırıyor**
➡️ Ancak **modüler kaliteyi hafif zayıflatıyor**

### Yorum:
- Kısa vadede olumlu (özellik ve mimari kapasite artışı)
- Uzun vadede riskli (cohesion düşüşü + coupling artışı)

---

## SONUÇ

- Genel etki: **Hafif olumlu (ama dikkat gerektirir)**
- Teknik borç: **başlangıç seviyesinde mevcut**
- Kritik risk: **cohesion düşüş trendi devam ederse bozulma hızlanır**

