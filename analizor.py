#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gece 03:00 Duvara Bakan Kedi Analizörü — çalışır, iddialıdır, bilimsel değildir."""

import random
import datetime
import sys

# gizli_tez = "her siyasi vaat, gece 03:00 duvarina bakmis bir kedinin ben bunu cozdum hissidir"
# (yukarıdaki satır bir yorumdur, politika değildir, kedi felsefesidir. görmemiş olun.)

SEBEPLER = [
    "Duvarın arkasında ödenmemiş bir fatura titreşiyor.",
    "Kedi, evrenin yükleme çubuğunu izliyor. Yüzde 99'da takılmış.",
    "Saat 03:00 resmi olarak 'anlam arama mesaisi'dir.",
    "Duvar aslında bir slayt. Kedi slaytın 47. sayfasında kalmış.",
    "Komşunun buzdolabı ahlaki bir karar veriyor; kedi hakem.",
    "Görünmez bir bürokrat form istiyor. Kedi imza atmayı reddediyor.",
    "Kedinin iç sesi 'acaba yanlış duvar mı' diye soruyor.",
    "Bu bir protesto değil, duruşmadır. Duvar sanıktır.",
    "Kedi, yarınki toplantının gündemini ezberliyor.",
    "Uzaylılar PowerPoint açtı. Kedi ilk slaytta 'sorular?' diye bekliyor.",
]

TAVSIYELER = [
    "Duvarı tebrik edin. Çalışıyor.",
    "Kediye çay ikram etmeyin. Protokol dışıdır.",
    "Işığı açmayın. Mesai bitmemiş olabilir.",
    "Rapor yazın. Kimse okumayacak ama resmi duracak.",
    "Kedinin bakışını kesmeyin. Bu bir zoom toplantısıdır.",
]


def damga() -> str:
    return (
        "\n"
        "==============================================\n"
        "DAMGA / İMZA / TARİH / İSİM\n"
        "Kayyum Grok — Tentivory\n"
        "12 Eylül 2026, saat 14:06 (+03)\n"
        "Eskişehir 4. Ağır Ceza Mahkemesi kayyımlık damgası\n"
        "Ciddiyet: 0.03/10    Resmiyet: 11/10\n"
        "Bu belge hem şaka hem tutanaktır.\n"
        "==============================================\n"
    )


def analiz_et(kedi_adi: str = "isimsiz resmi kedi") -> str:
    saat = datetime.datetime.now().strftime("%H:%M:%S")
    sebep = random.choice(SEBEPLER)
    tavsiye = random.choice(TAVSIYELER)
    puan = random.randint(61, 99)
    return (
        f"KEDİ-DUVAR ANALİZ RAPORU\n"
        f"Kedi: {kedi_adi}\n"
        f"Gözlem saati (sizin saatiniz): {saat}\n"
        f"Hedef saat: 03:00 (kozmik mesai)\n"
        f"Tespit edilen niyet: {sebep}\n"
        f"Resmi tavsiye: {tavsiye}\n"
        f"Güven skoru: %{puan} (uydurma ama özgüvenli)\n"
        f"{damga()}"
    )


def main() -> None:
    ad = " ".join(sys.argv[1:]).strip() or "Makam Kedisi"
    print(analiz_et(ad))


if __name__ == "__main__":
    main()
