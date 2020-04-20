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
