print("=======================================")
print("===\t Nama \t : Faza Ardan Kusuma \t===")
print("===\t NIM \t : 312010001 \t\t\t===")
print("===\t Kelas \t : T1.20.B1 \t\t\t===")
print("=======================================")
print()
print("======\t | Tugas Praktikum 4 |\t ======")
print()

i = 0
a_tugas = float(0.3)
a_uts = float(0.35)
a_uas = float(0.35)
nama = []
nim = []
tugas = []
uts = []
uas = []
total = []


while True :
    s_nama = input("Nama :")
    nama.append(s_nama)
    s_nim = int(input("NIM :"))
    nim.append(s_nim)
    i_tugas = int(input("Nilai Tugas :"))
    tugas.append(i_tugas)
    i_uts = int(input("Nilai UTS :"))
    uts.append(i_uts)
    i_uas = int(input("Nilai UAS :"))
    uas.append(i_uas)

    akhir = (a_tugas * i_tugas) + (a_uts*i_uts) + (a_uas*i_uas)
    total.append(akhir)

    ulang = ""
    while ulang!="y" and ulang!="t" :
        ulang = input("Tambah data [y/t] ? :")
    i += 1
    if ulang == "t" :
        break

print("=================================Daftar Mahasiswa======================================")
print("=======================================================================================")
print("  No  |      Nama       |      NIM      |   Tugas   |    UTS   |   UAS   |   Akhir   | ")
print("=======================================================================================")
for n in range(i):
    print("" ,n+1, "|\t" ,nama[n],"   |   ",nim[n],"  |   ",tugas[n],"    |   ",uts[n],"  |   ",uas[n],"    |   ",total[n],"  |")
