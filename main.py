import csv

# F01-Load file
# Fungsi yang dijalankan pertama kali untuk membuat variabel dari data file csv yang dimasukan
# inisialisasi variabel
user = []
wahana = []
pembelian = []
penggunaan = []
tiket = []
refund = []
kritiksaran = []
kehilangan = []
def set_var (file, array):
    # Prosedur untuk menambahkan tiap baris di file csv ke dalam array dengan satu baris
    # merupakan satu tipe bentukan
    o = open(file, 'r')
    r = csv.reader(o)
    for row in r  :
        array += [row]
def load ():
    # Prosedur load meminta masukan directory file kemudian akan mengeset variabel agar
    # menjadi array berisi tipe bentukan sesuai dengan file
    f_user = input('Masukkan nama File User : ')
    f_wahana = input('Masukkan nama File Daftar Wahana : ')
    f_pembelian = input('Masukkan nama File Pembelian Tiket : ')
    f_penggunaan = input('Masukkan nama File Penggunaan Tiket : ')
    f_tiket = input('Masukkan nama File Kepemilikan Tiket : ')
    f_refund = input('Masukkan nama File Refund Tiket : ')
    f_kritiksaran = input('Masukkan nama File Kritik dan Saran : ')
    f_kehilangan = input('Masukkan nama File Kehilangan Tiket : ')
    set_var (f_user,user)
    set_var (f_wahana,wahana)
    set_var (f_pembelian,pembelian)
    set_var (f_penggunaan,penggunaan)
    set_var (f_tiket,tiket)
    set_var (f_refund,refund)
    set_var (f_kritiksaran,kritiksaran)
    set_var (f_kehilangan,kehilangan)
    print('File perusahaan Willy Wangky’s Chocolate Factory telah di-load.')
    
# F05-Pencarian Pemain
# Fungsi yang bisa dijalankan admin untuk mencari data diri pemain
def cari_elemen (array, indeks, keyword):
    # Fungsi yang akan mereturn indeks (dalam hal ini baris) suatu array yang sesuai dengan kriteria
    # memilik isi di indeks (baris dan kolom) tertentu sama dengan keyword yang diberikan
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
    if user[indeks] == ['End'] :
        print('Data pemain tidak ada')
    else :
        print('Nama Pemain : ', user[indeks][0])
        print('Tinggi Pemain : ', user[indeks][3])
        print('Tanggal Lahir Pemain : ', user[indeks][1])

# F09-Refund
# Fungsi untuk melakukan refund yang jika sesuai akan menambah saldo pemain dan
# mengurangi jumlah tiket yang dimiliki pemain
def cari_elemen2 (array, indeks1, keyword1, indeks2, keyword2) :
    #sama dengan fungsi cari_elemen namun dengan dua kriteria
    i=0
    while array[i] != ['End']:
        if array[i][indeks1]==keyword1 and array[i][indeks2]==keyword2:
            break
        i+=1
    return i
def tambah_arr (arr_utama, arr_tambahan):
    # Fungsi yang akan mereturn gabungan dua array dengan arr_tambahan di akhir arr_utama
    # dapat digunakan di fungsi lain juga, Mark tetap berada di akhir array
    hasil=[]
    i=0
    while arr_utama[i] != ['End']:
        hasil+=arr_utama[i]
        i+=1
    hasil = hasil + arr_tambahan + [['End']]
    return hasil        
def refund_tiket (username, file):
    # Prosedur refund mengurangi jumlah tiket dimiliki pemain dan akan menambah saldo
    # (sebesar (harga tiket - 2000)/tiket) jika masukan sesuai dengan data,
    # jika tidak sesuai akan mencetak pesan kesalahan
    ID = input('Masukkan ID wahana : ')
    tanggal = input('Masukkan tanggal refund : ')
    jumlah = input('Jumlah tiket yang di-refund : ')
    indeks = cari_elemen2 (tiket,0,username,1,ID)
    arr = [[username, tanggal, ID, jumlah]]
    if tiket[indeks] != ['End'] :
        if int(tiket[indeks][2])>int(jumlah) :
            print('Uang refund sudah kami berikan pada akun anda')
            file = tambah_arr (file, arr)
            indeks_s = cari_elemen (user,3,username)
            indeks_w = cari_elemen (wahana,0,ID)
            user[indeks_s][6]=str(int(user[indeks_s][6])+int(jumlah)*(int(wahana[indeks_w][2])-2000))
            tiket[indeks][2]=str(int(tiket[indeks][2])-int(jumlah))
        else :
            print('Jumlah tiket yang di-refund melebihi kepunyaan Anda')
    else :
        print('Anda tidak memiliki tiket terkait')
    return file
        
# F13-Top UP Saldo
# Fungsi yang dapat dijalankan admin untuk menambah saldo pemain
def topup() :
    # Prosedur topup menambah jumlah saldo pemain sebesar saldo yang dimasukkan
    # asumsi masukan valid
    username=input('Masukkan username : ')
    saldo=input('Masukkan saldo yang di-top up : ')
    indeks = cari_elemen (user,3,username)
    user[indeks][6]=str(int(user[indeks][6])+int(saldo))
    print('Top up berhasil. Saldo',user[indeks][0], 'bertambah menjadi', user[indeks][6])

# B04-Laporan Kehilangan Tiket
# Fungsi yang akan mencatat data kehilangan tiket seorang pemain yang dilaporkan (masukan pengguna)
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

load()
