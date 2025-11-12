import os
os.system("cls")

def ambil_soal():
    soal_asli = []
    with open("soal.txt", 'r', encoding='utf-8') as file:
        for line in file:
            soal_asli.append(line.strip())
    return soal_asli

def buat_soal():
    soal_asli = ambil_soal()
    import random
    random.shuffle(soal_asli)

    soal_ujian = []
    for i in range(10):
        soal = soal_asli[i]  # pertanyaan|jawaban1,jawaban2,jawaban3,jawaban4
        data = soal.split("|")  # ["pertanyaan", "jawaban1,jawaban2,jawaban3,jawaban4"]

        pertanyaan = data[0]
        semua_jawaban = data[1]
        jawaban = semua_jawaban.split(",")
        jawaban_benar = jawaban[0]

        random.shuffle(jawaban)

        soal_ujian.append({
            "pertanyaan": pertanyaan,
            "jawaban": jawaban,
            "jawaban_benar": jawaban_benar
        })
    return soal_ujian

def app_ujian():
    soal_ujian = buat_soal()
    for soal in soal_ujian:
        print("Pertanyaan:", soal["pertanyaan"])
        print("Jawaban:")
        for jawaban in soal["jawaban"]:
            print("-", jawaban)

app_ujian()