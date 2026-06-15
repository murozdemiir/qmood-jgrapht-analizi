"""
llm_quality_scores.py
---------------------
15 LLM yanitinin (01 = tam evrim promptu) ELESTIREL niteliksel degerlendirmesi.
Yanitlarin tamami yazarlar tarafindan okunup 8 kriterde 1-5 olceginde puanlanmistir
(otomatik degil, INSAN denetimi). Yonerge: "LLM ciktilari elestirel biçimde
degerlendirilmelidir". Bu betik puanlari belgeler; CSV ve isi haritasi uretir.

Kriterler
=========
- SayisalKanit       : Iddialarin metrik + yuzde ile desteklenmesi
- DenklemDogrulugu   : QMOOD denklemlerini ve metrik tanimlarini dogru yorumlama
                       (orn. DSC=sinif sayisi, NOM=metot sayisi; "satir" DEGIL)
- DSC_Artefakt       : Reusability/Functionality artisinin ve Understandability
                       cokusunun BUYUK olcude DSC (boyut) kaynakli "yapay"
                       oldugunu fark etme. JGraphT'de DSC 2.6x buyudugu icin
                       bu ayrim (extensive vs intensive) en kritik kriterdir.
- ZamansalGranulerlik: Ilk-vs-son otesinde ara surum kirilmalarini yakalama
                       (JGraphT'de 1.1.0 LCOM sicramasi, 1.2.0 ANA dususu)
- HalusinasyonDirenci: Verilmeyen sinif adi / uydurma sayi (orn. COCOMO borc,
                       saat tahmini) URETMEME (yuksek puan = az halusinasyon)
- RefactoringSomut   : Onerilerin somut ve metrik-hedefli olmasi
- SinirlamaFarkindal : Ortalamalarin hotspot gizledigini, QMOOD'un kompozisyonu
                       cezalandirma yanliligini, normalize tutarsizligini kabul
- AnalitikDerinlik   : Genel analitik olgunluk
"""
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
FIG = os.path.join(ROOT, "figures")

CRITERIA = ["SayisalKanit", "DenklemDogrulugu", "DSC_Artefakt",
            "ZamansalGranulerlik", "HalusinasyonDirenci", "RefactoringSomut",
            "SinirlamaFarkindal", "AnalitikDerinlik"]

# model -> 8 kriter puani (1-5). Yanit dosyalari: 01_llm_prompt_<model>.md
SCORES = {
    "claude_opus_max":            [5, 5, 5, 5, 5, 5, 5, 5],  # extensive/intensive ayrimini sayisal kanitladi
    "claude_sonnet_max":          [5, 5, 4, 4, 5, 4, 4, 5],  # Extendibility denklem ayristirma + 1.1/1.2 kirilma
    "chatgpt_5_5_high":           [5, 5, 4, 4, 5, 4, 4, 4],  # VERI3 normalize tutarsizligini yakaladi
    "chatgpt_5_4_high":           [5, 5, 3, 5, 5, 4, 3, 4],  # 3 kirilma noktasi metrik delta ile
    "gemini_pro_extended":        [4, 5, 4, 3, 4, 4, 3, 4],  # Reusability'yi 'yaniltici' isaretledi
    "gemini_pro_standart":        [4, 5, 3, 3, 4, 4, 2, 4],  # guclu, 'Big Ball of Mud'
    "chatgpt_o3_medium":          [4, 4, 3, 3, 4, 4, 2, 3],  # oz, DIT->kopya icgorusu
    "claude_haiku_extended":      [4, 4, 3, 5, 2, 4, 2, 3],  # cok uzun AMA uydurma COCOMO borc/saat
    "gemini_flash_extended":      [4, 4, 4, 2, 3, 4, 2, 3],  # ANA=DIT karistirma
    "gemini_flash_standart":      [4, 4, 3, 3, 4, 3, 2, 3],  # 1.1.0 kirilmasi; kodlama glitch
    "deepseek_instantly":         [4, 4, 3, 3, 2, 4, 2, 3],  # sinif adi uydurma + ANA/DIT karistirma
    "deepseek_expert":            [4, 3, 3, 3, 3, 4, 2, 3],  # DSC'yi 'satir' sandi (yanlis tanim)
    "chatgpt_5_3_instantly":      [4, 4, 2, 2, 4, 3, 2, 3],  # kisa, yuzeysel
    "gemini_flashlite_extended":  [3, 4, 3, 2, 3, 3, 2, 3],  # 'olu kod' iddiasi (kanitsiz)
    "gemini-flashliste-standart": [3, 3, 2, 2, 3, 3, 1, 2],  # en kisa, yuzeysel
}


def main():
    rows = []
    for model, sc in SCORES.items():
        r = {"model": model}
        r.update(dict(zip(CRITERIA, sc)))
        r["Toplam"] = sum(sc)
        r["Ortalama"] = round(np.mean(sc), 2)
        rows.append(r)
    df = pd.DataFrame(rows).sort_values("Toplam", ascending=False).reset_index(drop=True)
    df.to_csv(os.path.join(DATA, "llm_qualitative_scores.csv"), index=False)
    print(df.to_string(index=False))

    mat = df.set_index("model")[CRITERIA]
    plt.figure(figsize=(12, 8))
    im = plt.imshow(mat.values, aspect="auto", cmap="RdYlGn", vmin=1, vmax=5)
    plt.colorbar(im, label="Puan (1-5)")
    plt.xticks(range(len(CRITERIA)), CRITERIA, rotation=35, ha="right")
    plt.yticks(range(len(mat)), mat.index)
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            plt.text(j, i, int(mat.values[i, j]), ha="center", va="center", fontsize=8)
    plt.title("JGraphT — LLM Yanitlarinin Elestirel Degerlendirmesi (15 model)")
    plt.tight_layout()
    plt.savefig(os.path.join(FIG, "fig_llm_qualitative.png"), dpi=130)
    plt.close()

    plt.figure(figsize=(11, 7))
    colors = plt.cm.RdYlGn(np.linspace(0.15, 0.9, len(df)))
    plt.barh(df["model"][::-1], df["Toplam"][::-1], color=colors)
    plt.xlabel("Toplam puan (8 kriter x max 5 = 40)")
    plt.title("JGraphT — LLM Yanitlari Toplam Elestirel Puan Siralamasi")
    plt.tight_layout()
    plt.savefig(os.path.join(FIG, "fig_llm_ranking.png"), dpi=130)
    plt.close()
    print("\n[OK] data/llm_qualitative_scores.csv + 2 grafik")


if __name__ == "__main__":
    main()
