# F03 - Sign Up User
# Fungsi Pendaftaran pemain yang hanya dapat dilakukan oleh admin
# Pendaftar hanya bisa mendaftarkan username yang belum terdaftar

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

def tambah_arr (arr_utama, arr_tambahan):
    # Fungsi yang akan mereturn gabungan dua array dengan arr_tambahan di akhir arr_utama
    # dapat digunakan di fungsi lain juga, Mark tetap berada di akhir array
    i=0
    while arr_utama[i] != ['End']:
        i+=1
    arr_utama[i] = arr_tambahan
    arr_utama[i+1] = ['End']

def signUpUser():
    # Prosedur mendaftarkan pemain dengan validasi username agar tidak ada username yang sama
    username = input("Masukkan username: ")
    indeks = cari_elemen(user, 3, username)
    while user[indeks] != ['End']:
        print("username sudah ada. masukkan username berbeda!")
        username = input("Masukkan username: ")
    else: #username valid
        Nama=input("Masukkan nama pemain: ")
        Tanggal_Lahir=input("Masukkan tanggal lahir pemain (DD/MM/YYYY): ")
        Tinggi_Badan=input("Masukkan tinggi badan pemain (cm): ")
        username = input("Masukkan username pemain: ")
        Password=input("Masukkan password pemain: ")
        golden_account = str(0)
        saldo = str(0)
        array =[Nama, Tanggal_Lahir, Tinggi_Badan, username, Password, saldo, golden_account]
        tambah_arr (user, array)
        print("Selamat menjadi pemain, " + Nama + ". Selamat bermain." )



