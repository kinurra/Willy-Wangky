def tambah_arr (arr_utama, arr_tambahan):
    # Fungsi yang akan mereturn gabungan dua array dengan arr_tambahan di akhir arr_utama
    # dapat digunakan di fungsi lain juga, Mark tetap berada di akhir array
    hasil=[]
    i=0
    while arr_utama[i] != ['End']:
        arr_utama[i]=[arr_utama[i]]
        hasil+=arr_utama[i]
        i+=1
    hasil = hasil + arr_tambahan + [['End']]
    return hasil 

def tambah_wahana():
     # Asumsi seluruh input-an valid
     
     print("Masukkan Informasi Wahana yang ditambahkan:")
     ID = input("Masukkan ID Wahana: ")
     nama_wahana = input("Masukkan Nama Wahana: ")
     harga_tiket = input("Masukkan Harga Tiket: ")
     batas_umur = input("Batasan umur: ")
     batas_tinggi = input("Batasan tinggi badan: ")
     print()
     print("Info wahana telah ditambahkan!")

     add_wahana = [[ID, nama_wahana, harga_tiket, batas_umur, batas_tinggi]]
     tambah_arr (wahana, add_wahana)
