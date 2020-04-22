# B04-Laporan Kehilangan Tiket
# Fungsi yang akan mencatat data kehilangan tiket seorang pemain yang dilaporkan (masukan pengguna)
def tiket_hilang ():
    # Fungsi yang akan mereturn array yang telah ditambah data kehilangan masukan pengguna
    # data kehilangan juga akan mengurangi jumlah tiket yang dimiliki pemain
    # asumsi masukan valid
    username = input('Masukkan username : ')
    tanggal = input('Tanggal kehilangan tiket : ')
    ID = input('ID wahana : ')
    jumlah = input('Jumlah tiket yang dihilangkan : ')
    indeks = cari_elemen (tiket,0,username)
    tiket[indeks][2]=str(int(tiket[indeks][2])-int(jumlah))
    array = [tanggal, ID, username, jumlah]
    tambah_arr (kehilangan, array)
    print('Laporan kehilangan tiket Anda telah direkam')
