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
