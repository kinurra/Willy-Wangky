import csv

# F01-Load file
# Fungsi yang dijalankan pertama kali untuk membuat variabel dari data file csv yang dimasukan
def set_var (file):
    # Fungsi akan mereturn variabel berupa array 2 dimensi dari sebuah directory file csv
    # Fungsi membaca file 2 kali; untuk menentukan banyak data, dan untuk mengassign variabel
    o = open(file, 'r')
    r = csv.reader(o)
    length=0
    for row in r  :
        length+=1
    array = [[''for i in range (length)]for j in range (length)]
    i=0
    o = open(file, 'r')
    r = csv.reader(o)
    for row in r :
        array[i]=row
        i+=1
    return array
def load ():
    # Prosedur load menggunakan global variable yang hasilnya akan serupa menjalankan fungsi
    # yang mereturn tuple variable array yang nantinya diassign di program utama
    global user
    global wahana
    global pembelian
    global tiket
    global refund
    global kritiksaran
    global kehilangan
    user = input('Masukkan nama File User : ')
    wahana = input('Masukkan nama File Daftar Wahana : ')
    pembelian = input('Masukkan nama File Pembelian Tiket : ')
    penggunaan = input('Masukkan nama File Penggunaan Tiket : ')
    tiket = input('Masukkan nama File Kepemilikan Tiket : ')
    refund = input('Masukkan nama File Refund Tiket : ')
    kritiksaran = input('Masukkan nama File Kritik dan Saran : ')
    kehilangan = input('Masukkan nama File Kehilangan Tiket : ')
    user = set_var (user)
    wahana = set_var (wahana)
    pembelian = set_var (pembelian)
    penggunaan = set_var (penggunaan)
    tiket = set_var (tiket)
    refund = set_var (refund)
    kritiksaran = set_var (kritiksaran)
    kehilangan = set_var (kehilangan)
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
        arr_utama[i]=[arr_utama[i]]
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
