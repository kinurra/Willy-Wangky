# F01-Load file
# Fungsi yang dijalankan pertama kali untuk membuat variabel dari data file csv yang dimasukan
# inisialisasi variabel
user = [''for i in range (1000)]
wahana = [''for i in range (1000)]
pembelian = [''for i in range (1000)]
penggunaan = [''for i in range (1000)]
tiket = [''for i in range (1000)]
refund = [''for i in range (1000)]
kritiksaran = [''for i in range (1000)]
kehilangan = [''for i in range (1000)]
def set_var (file, array):
    # Prosedur untuk mengassign tiap baris di file csv ke dalam array dengan satu baris
    # merupakan satu tipe bentukan
    o = open(file, 'r')
    r = csv.reader(o)
    i = 0
    for row in r: # membaca setiap list satu persatu
        array[i] = row
        i += 1
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
