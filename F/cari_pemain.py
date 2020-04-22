# F05-Pencarian Pemain
# Fungsi yang bisa dijalankan admin untuk mencari data diri pemain
def cari_elemen (array, indeks, keyword):
    # Fungsi yang akan mereturn indeks (dalam hal ini baris) suatu array yang sesuai dengan kriteria
    # memiliki isi di indeks (baris dan kolom) tertentu sama dengan keyword yang diberikan
    # dapat digunakan di fungsi lain juga
    i=0
    while array[i] != ['End']:
        if array[i][indeks]==keyword:
            break
        i+=1
    return i
def cari_pemain ():
    # prosedur mencetak data diri pemain dengan username masukan jika ada,
    # jika tidak akan mencetak pesan tidak ada data
    Username = input('Masukkan username : ')
    indeks = cari_elemen (user,3,Username)
    if user[indeks] == ['End'] : # jika mark berarti tidak ditemukan
        print('Data pemain tidak ada')
    else :
        print('Nama Pemain : ', user[indeks][0])
        print('Tinggi Pemain : ', user[indeks][2],'cm')
        print('Tanggal Lahir Pemain : ', user[indeks][1])
