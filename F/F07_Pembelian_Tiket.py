# F07 - Pembelian Tiket
# Fungsi untuk pembelian tiket yang hanya bisa dilakukan oleh admin
# Pembelian tiket hanya bisa dilakukan oleh pemain yang telah terdaftar dan melakukan log in

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

def cari_tinggi_pemain (username):
    # prosedur mencari tinggi pemain
    # mengkategorikan tinggi pemain
    indeks = cari_elemen (user,3,username)
    string = user[indeks][2]
    Tinggi = int(string)
    if(Tinggi >= 170):
        return 1
    else:
        return 2

def Syarat_Tinggi (username,ID_Wahana):
    # Prosedur yang mengidentifikasi apakah tinggi pemain sesuai dengan batasan tinggi wahana atau tidak
    # mencari kategori batasan tinggi yang diperbolehkan dalam wahana
    # membandingkan kategori batasan tinggi dalam wahana dengan kategori tinggi pemain
    indeks = cari_elemen(wahana,0,ID_Wahana)
    Kategori_Tinggi = wahana[indeks][4]
    if(cari_tinggi_pemain(username)==Kategori_Tinggi):
        return True
    else:
        return False



def cari_umur_Pemain(username):
    # Prosedur mencari umur pemain
    indeks = cari_elemen(user, 3, username)
    string=user[indeks][2]
    # Memecah string menjadi bentuk integer tahun, bulan, dan hari lahir user
    tahun = int(string[6:10])
    bulan = int(string[3:5])
    hari = int(string[:2])
    # Memecah string menjadi bentuk integer tahun, bulan, dan hari saat user membeli tiket
    indeks2=cari_elemen(pembelian, 0, username)
    string2=pembelian[indeks2][1]
    tahun2 = int(string2[6:10])
    bulan2 = int(string2[3:5])
    hari2 = int(string2[:2])
    # Menghitung umur pemain
    umur=tahun2-tahun-1
    if(bulan2>bulan):
        umur+=1
    elif(bulan2==bulan):
        if(hari2>=hari):
            umur+=1
    umur_pemain=umur
    if(umur_pemain<17):
        return 1
    elif (umur_pemain>=17):
        return 2

def Syarat_Umur(username,ID_Wahana):
    # Prosedur yang mengidentifikasi apakah umur pemain sesuai dengan batasan umur wahana atau tidak
    # mencari kategori batasan umur yang diperbolehkan dalam wahana
    # membandingkan kategori batasan umur dalam wahana dengan kategori umur user
    indeks = cari_elemen(wahana, 0, ID_Wahana)
    Kategori_Umur=wahana[indeks][3]
    if(cari_umur_Pemain(username)==Kategori_Umur or Kategori_Umur==3):
        return True
    else:
        return False

def tambah_arr (arr_utama, arr_tambahan):
    # Fungsi yang akan mereturn gabungan dua array dengan arr_tambahan di akhir arr_utama
    # dapat digunakan di fungsi lain juga, Mark tetap berada di akhir array
    i=0
    while arr_utama[i] != ['End']:
        i+=1
    arr_utama[i] = arr_tambahan
    arr_utama[i+1] = ['End']

def Syarat_Saldo(username,ID_Wahana):
    # Prosedur yang mengecek apakah saldo user mencukupi untuk melakukan pembelian tiket
    # Mengubah bentuk saldo yang awalnya string menjadi integer
    indeks = cari_elemen (user,3,username)
    string=user[indeks][6]
    saldo=int(string)
    # Mengubah bentuk harga tiket wahana yang awalnya string menjadi integer
    indeks2 = cari_elemen(wahana, 0, ID_Wahana)
    string2 = wahana[indeks][2]
    integer= int(string2) # harga tiket yang dengan bentuk integer
    # Mengecek apakah pemain memiliki account golden account atau tidak
    if(user[indeks][7]==1): # golden account
        Harga_Tiket= integer/2
    else: #bukan golden account
        Harga_Tiket=integer
    # Mengecek apakah saldo cukup atau tidak untuk membeli tiket wahana
    if(saldo>=Harga_Tiket):
        return True
    else:
        return False

def Kurangi_Saldo(username,ID):
    indeks_s = cari_elemen(user,3,username)
    indeks_w = cari_elemen(wahana, 0, ID)
    if(int(user[indeks][7])==1): # golden account mendapat diskon setengah harga tiket wahana
        user[indeks_s][6] = str(int(user[indeks_s][6]) - int(jumlah) * (int(wahana[indeks_w][2]))/2)
    else:  # tidak golden account
        user[indeks_s][6]=str(int(user[indeks_s][6])-int(jumlah)*(int(wahana[indeks_w][2])))

def Nama_Wahana(ID_Wahana):
    # Prodesur mencari Nama wahana berdasarkan ID wahana
    Nama=cari_elemen(wahana, 0, ID_Wahana)
    Nama = wahana[Nama][1]
    return Nama

def pembelianTiket(username):
    # Prosedur pembelian tiket
    ID_Wahana=input("Masukkan ID wahana: ")
    Tanggal_Pembelian=input("Masukkan tanggal hari ini: ")
    Jumlah_Tiket=input("Jumlah tiket yang dibeli: ")
    if(Syarat_Tinggi(username,ID_Wahana)): # Syarat tinggi dan syarat umur terpenuhi
        if(Syarat_Saldo(username,ID_Wahana)): # Syarat saldo
            array = [ID_Wahana, Tanggal_Pembelian, Jumlah_Tiket]
            tambah_arr(tiket, array)
            Kurangi_Saldo(username,ID_Wahana)
            Nama = Nama_Wahana(ID_Wahana)
            print("Selamat bersenang-senang di", Nama, ".")
        else: # Syarat Saldo tidak terpenuhi
            print("Saldo Anda tidak cukup")
            print("Silakan mengisi saldo Anda")
    else: # Syarat tinggi dan syarat umur tidak memenuhi
        print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini.")
        print("Silakan menggunakan wahana lain yang tersedia.")