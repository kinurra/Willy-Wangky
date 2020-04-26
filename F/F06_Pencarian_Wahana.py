#F06 - Pencarian Wahana
# Prosedur ini akan menampilkan wahana-wahana yang sesuai dengan batasan-batasan yang ingin
# diketahui
def cari_wahana():
    print("Jenis batasan umur:")
    print("1. Anak-anak (<17 tahun)")
    print("2. Dewasa (>=17 tahun)")
    print("3. Semua umur")
    print("")
    print("Jenis batasan tinggi badan:")
    print("1. Lebih dari 170 cm")
    print("2. Tanpa batasan")
    print("")
    umur = input("Batasan umur pemain: ")
    while(umur != "1" or umur != "2" or umur != "3"):
        print("Batasan umur tidak valid!")
        umur = input("Batasan umur pemain: ")
    tinggi = input("Batasan tinggi badan: ")
    while(tinggi != "1" or tinggi != "2"):
        print("Batasan tinggi badan tidak valid!")
        tinggi = input("Batasan tinggi badan: ")       
    if (umur == '1'):
        if (tinggi == "1"):
            tinggi = '171'
        else:
            tinggi = '-'
        umur = '7'
    elif (umur == '2'):
        if (tinggi == "1"):
            tinggi = '171'
        else:
            tinggi = '-'
        umur = '17'
    else:
        if (tinggi == "1"):
            tinggi = '171'
        else:
            tinggi = '-'
        umur = '-'
    indeks = 0
    exist = False
    print("Hasil pencarian:")
    while(wahana[indeks] = ['End']):
        if (wahana[indeks][4] == umur and wahana[indeks][5] == tinggi):
            print(wahana[indeks][0], '|', wahana[indeks][1], '|', wahana[indeks][2])
            exist = True
        indeks = indeks + 1
    if (exist == False):
        print("Tidak ada wahana yang sesuai dengan pencarian kamu.")
