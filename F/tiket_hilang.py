# B04-Laporan Kehilangan Tiket
# Fungsi yang akan mencatat data kehilangan tiket seorang pemain yang dilaporkan (masukan pengguna)
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
def tiket_hilang (file):
    # Fungsi yang akan mereturn array yang telah ditambah data kehilangan masukan pengguna
    # data kehilangan juga akan mengurangi jumlah tiket yang dimiliki pemain
    # asumsi masukan valid
    username = input('Masukkan username : ')
    tanggal = input('Tanggal kehilangan tiket : ')
    ID = input('ID wahana : ')
    jumlah = input('Jumlah tiket yang dihilangkan : ')
    indeks = cari_elemen (tiket,0,username)
    tiket[indeks][2]=str(int(tiket[indeks][2])-int(jumlah))
    array = [[tanggal, ID, username, jumlah]]
    file = tambah_arr (file, array)
    print('Laporan kehilangan tiket Anda telah direkam')
    return file
