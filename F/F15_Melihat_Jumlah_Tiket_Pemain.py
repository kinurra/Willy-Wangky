# F15 - Melihat Jumlah Tiket Pemain
# Fungsi untuk melihat jumlah tiket yang dimiliki pemain
# Jumlah tiket pemain hanya dapat dilihat oleh admin
def Nama_Wahana(ID_Wahana):
    # Prosedur Nama_Wahana digunakan untuk mencari nama wahana berdasarkan ID wahana
    indeks=0
    while (wahana[indeks][0]!=ID_Wahana):
        indeks += 1
    print(wahana[indeks][1])
def jumlahTiket():
    Username=input("Masukkan username: ")
    print("Riwayat")
    indeks=0
    while(tiket[indeks] != ['End']):
        if(tiket[indeks][0]==Username):
            print(tiket[indeks][2]], "|" ,Nama_Wahana, "|" ,tiket[indeks][3])
        indeks +=1