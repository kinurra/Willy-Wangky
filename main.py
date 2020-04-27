import csv

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
    for row in r: # membaca setiap list tipe bentukan (baris di file csv) satu persatu
        array[i] = row
        i += 1
def load ():
    # Prosedur load akan meminta directory file dan mengeset variabel agar
    # menjadi array berisi tipe bentukan sesuai dengan 
    print('$ load')
    f_user = input('Masukkan nama File User : ')
    f_wahana = input('Masukkan nama File Daftar Wahana : ')
    f_pembelian = input('Masukkan nama File Pembelian Tiket : ')
    f_penggunaan = input('Masukkan nama File Penggunaan Tiket : ')
    f_tiket = input('Masukkan nama File Kepemilikan Tiket : ')
    f_refund = input('Masukkan nama File Refund Tiket : ')
    f_kritiksaran = input('Masukkan nama File Kritik dan Saran : ')
    f_kehilangan = input('Masukkan nama File Kehilangan Tiket : ')
    file = [f_user,f_wahana,f_pembelian,f_penggunaan,f_tiket,f_refund,f_kritiksaran,f_kehilangan]
    set_var (file[0],user)
    # unhash password
    i=0
    while user[i]!= ['End']:
        user[i][4]= simpan_password(user[i][4])
        i+=1
    set_var (file[1],wahana)
    set_var (file[2],pembelian)
    set_var (file[3],penggunaan)
    set_var (file[4],tiket)
    set_var (file[5],refund)
    set_var (file[6],kritiksaran)
    set_var (file[7],kehilangan)
    print('File perusahaan Willy Wangky’s Chocolate Factory telah di-load.')
    return file

#F02 - Login User
# Fungsionalitas yang lain dapat digunakan setelah user (admin maupun pemain) melakukan login
def login_user ():
    #Prosedur meminta input berupa username dan password .Apabila username ada dan password benar, 
    #akan ditampilkan pesan selamat datang. Apabila username tidak ada atau password salah akan muncul
    #perintah untuk memasukkan kembali username dan password
    exist = False   
    while(exist == False):
        username = input("Masukkan username: ") 
        password = input("Masukkan password: ")
        indeks = 0
        while (user[indeks] != ['End'] and exist == False):
            if (username == user[indeks][3]) and (password == user[indeks][4]):
                exist = True                
            else:
                indeks+=1            
        if (exist == True):
             print("Selamat bersenang-senang, Willy Wangky!")
        else:
             print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
             print("")
    return username

# F03
def simpan(file,array):
    o = open(file,'w',newline='')
    writer = csv.writer(o,delimiter=',')
    i=0
    while array[i] != ['End']:
        writer.writerow(array[i])
        i+=1
        writer = csv.writer(o,delimiter=',')
    writer.writerow(['End'])
def save_file():
     user_f = input("Masukkan nama File User: ")
     daftar_wahana = input("Masukkan nama File Daftar Wahana: ")
     pembelian_tiket = input("Masukkan nama File Pembelian Tiket: ")
     penggunaan_tiket = input("Masukkan nama File Penggunaan Tiket: ")
     kepemilikan_tiket = input("Masukkan nama File Kepemilikan Tiket: ")
     refund_tiket = input("Masukkan nama File Refund Tiket: ")
     kritik_dan_saran = input("Masukkan nama File Kritik dan Saran: ")
     laporan_kehilangan = input('Masukkan nama File Kehilangan Tiket : ')
     print()
     i=0
     while user[i]!= ['End']:
         user[i][4]= simpan_password(user[i][4])
         i+=1
     simpan(user_f,user)
     simpan(daftar_wahana,wahana)
     simpan(pembelian_tiket,pembelian)
     simpan(penggunaan_tiket,penggunaan)
     simpan(kepemilikan_tiket,tiket)
     simpan(refund_tiket,refund)
     simpan(kritik_dan_saran,kritiksaran)
     simpan(laporan_kehilangan,kehilangan)
     print("Data berhasil disimpan!")
     
     

# F04 - Sign Up User
# Fungsi Pendaftaran pemain yang hanya dapat dilakukan oleh admin
# Pendaftar hanya bisa mendaftarkan username yang belum terdaftar
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

#F06 - Pencarian Wahana
# Prosedur ini akan menampilkan wahana-wahana yang sesuai dengan batasan-batasan yang ingin
# diketahui
def cari_wahana():
    print("Jenis batasan umur:")
    print("1. Anak-anak (<17 tahun)")
    print("2. Dewasa (>=17 tahun)")
    print("3. Semua umur")
    print("")
    print("Jenis batasan tinggi badan:")
    print("1. Lebih dari 170 cm")
    print("2. Tanpa batasan")
    print("")
    umur = input("Batasan umur pemain: ")
    while(umur != "1" and umur != "2" and umur != "3"):
        print("Batasan umur tidak valid!")
        umur = input("Batasan umur pemain: ")
    tinggi = input("Batasan tinggi badan: ")
    while(tinggi != "1" and tinggi != "2"):
        print("Batasan tinggi badan tidak valid!")
        tinggi = input("Batasan tinggi badan: ")       
    indeks = 0
    exist = False
    print("Hasil pencarian:")
    while(wahana[indeks] != ['End']):
        if ((wahana[indeks][3] == umur) and (wahana[indeks][4] == tinggi)):
            print(wahana[indeks][0], '|', wahana[indeks][1], '|', wahana[indeks][2])
            exist = True
        indeks = indeks + 1
    if (exist == False):
        print("Tidak ada wahana yang sesuai dengan pencarian kamu.")

# F07 - Pembelian Tiket
# Fungsi untuk pembelian tiket yang hanya bisa dilakukan oleh admin
# Pembelian tiket hanya bisa dilakukan oleh pemain yang telah terdaftar dan melakukan log in
def cari_tinggi_pemain (username):
    # prosedur mencari tinggi pemain
    # mengkategorikan tinggi pemain
    indeks = cari_elemen (user,3,username)
    string = user[indeks][2]
    Tinggi = int(string)
    if(Tinggi >= 170):
        return '1'
    else:
        return '2'
def Syarat_Tinggi (username,ID_Wahana):
    # Prosedur yang mengidentifikasi apakah tinggi pemain sesuai dengan batasan tinggi wahana atau tidak
    # mencari kategori batasan tinggi yang diperbolehkan dalam wahana
    # membandingkan kategori batasan tinggi dalam wahana dengan kategori tinggi pemain
    indeks = cari_elemen(wahana,0,ID_Wahana)
    Kategori_Tinggi = wahana[indeks][4]
    if(cari_tinggi_pemain(username)==Kategori_Tinggi or Kategori_Tinggi == '2'):
        return True
    else:
        return False
def cari_umur_Pemain(username):
    # Prosedur mencari umur pemain
    indeks = cari_elemen(user, 3, username)
    string=user[indeks][1]
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
        return '1'
    elif (umur_pemain>=17):
        return '2'
def Syarat_Umur(username,ID_Wahana):
    # Prosedur yang mengidentifikasi apakah umur pemain sesuai dengan batasan umur wahana atau tidak
    # mencari kategori batasan umur yang diperbolehkan dalam wahana
    # membandingkan kategori batasan umur dalam wahana dengan kategori umur user
    indeks = cari_elemen(wahana, 0, ID_Wahana)
    Kategori_Umur=wahana[indeks][3]
    if(cari_umur_Pemain(username)==Kategori_Umur or Kategori_Umur=='3'):
        return True
    else:
        return False
def Syarat_Saldo(username,ID_Wahana):
    # Prosedur yang mengecek apakah saldo user mencukupi untuk melakukan pembelian tiket
    # Mengubah bentuk saldo yang awalnya string menjadi integer
    indeks = cari_elemen (user,3,username)
    string=user[indeks][6]
    saldo=int(string)
    # Mengubah bentuk harga tiket wahana yang awalnya string menjadi integer
    indeks2 = cari_elemen(wahana, 0, ID_Wahana)
    string2 = wahana[indeks2][2]
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
def Kurangi_Saldo(username,ID,jumlah):
    indeks_s = cari_elemen(user,3,username)
    indeks_w = cari_elemen(wahana, 0, ID)
    if(int(user[indeks_s][7])==1): # golden account mendapat diskon setengah harga tiket wahana
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
    if(Syarat_Tinggi(username,ID_Wahana) and Syarat_Umur(username,ID_Wahana)): # Syarat tinggi dan syarat umur terpenuhi
        if(Syarat_Saldo(username,ID_Wahana)): # Syarat saldo
            array = [username,Tanggal_Pembelian,ID_Wahana,  Jumlah_Tiket]
            tambah_arr(pembelian, array)
            array2 = [username,ID_Wahana, Jumlah_Tiket]
            tambah_arr(tiket, array2)
            Kurangi_Saldo(username,ID_Wahana,Jumlah_Tiket)
            Nama = Nama_Wahana(ID_Wahana)
            print("Selamat bersenang-senang di", Nama, ".")
        else: # Syarat Saldo tidak terpenuhi
            print("Saldo Anda tidak cukup")
            print("Silakan mengisi saldo Anda")
    else: # Syarat tinggi dan syarat umur tidak memenuhi
        print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini.")
        print("Silakan menggunakan wahana lain yang tersedia.")

# F08
### Utama
def pakai_tiket(username):
     ID = input("Masukkan ID wahana: ")
     tanggal_penggunaan = input("Masukkan tanggal hari ini: ") # Asumsi input-an valid sesuai format tanggal
     jml_penggunaan_tiket = int(input("Jumlah tiket yang digunakan: "))
     print()
     mark = ["End"]

     # validasi dan akses ID
     exist_ID = False
     indeks = 0 # kolom

     if (pembelian[indeks][2] == ID):
          exist_ID = True

     while (not exist_ID and not pembelian[indeks] == mark):
          if (pembelian[indeks][2] == ID):
               exist_ID = True

          indeks += 1

     if (not exist_ID):
          print("Tiket Anda tidak valid dalam sistem kami")
          print()

     else:     
     # Hitung jumlah tiket 
         baris_jml_tiket = cari_elemen2(tiket, 0, username, 1, ID)  
         if (not tiket[baris_jml_tiket] == mark): #ID_Wahana terhadap username pada kepemilikan tiket, valid
             if(jml_penggunaan_tiket > int(tiket[baris_jml_tiket][2])):
                 print("Tiket Anda tidak valid dalam sistem kami")
                 print()

             else:
                 sisa_tiket = int(tiket[baris_jml_tiket][2]) - jml_penggunaan_tiket
                 tiket[baris_jml_tiket][2] = sisa_tiket
                 print('Terima kasih telah bermain.')
                 tambah_arr(penggunaan,[username,tanggal_penggunaan,ID,jml_penggunaan_tiket])
         else :
             print("Tiket Anda tidak valid dalam sistem kami")
             print()
         
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
    i=0
    while arr_utama[i] != ['End']:
        i+=1
    arr_utama[i] = arr_tambahan
    arr_utama[i+1] = ['End']      
def refund_tiket (username):
    # Prosedur refund mengurangi jumlah tiket dimiliki pemain dan akan menambah saldo
    # (sebesar (harga tiket - 2000)/tiket) jika masukan sesuai dengan data,
    # jika tidak sesuai akan mencetak pesan kesalahan
    ID = input('Masukkan ID wahana : ')
    tanggal = input('Masukkan tanggal refund : ')
    jumlah = input('Jumlah tiket yang di-refund : ')
    indeks = cari_elemen2 (tiket,0,username,1,ID)
    arr = [username, tanggal, ID, jumlah]
    if tiket[indeks] != ['End'] : # Data ditemukan
        if int(tiket[indeks][2])>=int(jumlah) :
            print('Uang refund sudah kami berikan pada akun anda')
            tambah_arr(refund,arr)
            indeks_s = cari_elemen (user,3,username)
            indeks_w = cari_elemen (wahana,0,ID)
            if user[indeks_s][7]==0:
                user[indeks_s][6]=str(int(user[indeks_s][6])+int(jumlah)*(int(wahana[indeks_w][2])-2000))
            else:
                user[indeks_s][6]=str(int(user[indeks_s][6])+int(jumlah)*(int(wahana[indeks_w][2])/2-1000))
            tiket[indeks][2]=str(int(tiket[indeks][2])-int(jumlah))
        else : # Data tidak sesuai
            print('Jumlah tiket yang di-refund melebihi kepunyaan Anda')
    else : # Data tidak ditemukan
        print('Anda tidak memiliki tiket terkait')

# F10 - Kritik dan Saran
# Prosedur ini akan menyimpan kritik/saran terhadap sebuah wahana dan menyimpan tanggal pelaporan
def kritik_saran():
    ID_wahana = input("Masukkan ID Wahana: ")
    tanggal_pelaporan = input("Masukkan tanggal pelaporan: ")
    kritik_saran = input("Kritik/saran Anda: ")
    print("")
    print("Kritik dan saran Anda kami terima.")
    arr = [username,tanggal_pelaporan,ID_wahana,kritik_saran]
    tambah_arr (kritiksaran, arr)
        
# F11 - Melihat Kritik dan Saran
# Fungsi yang dapat melihat kritik dan saran yang dimasukkan oleh pemain
# Diurutkan bedasarkan ID Wahana secara alfabetis
def lihatKritik():
    a=0
    while kritiksaran[a] != ['End']: # Menghitung total jumlah kolom
        a+=1
    length = a
    for i in range (length):
        maks=i
        for i in range (i+1,length):
            if(kritiksaran[maks][2][0])<(kritiksaran[i][2][0]):
                maks =i
            elif(kritiksaran[maks][2][0])==(kritiksaran[i][2][0]):
                if(kritiksaran[maks][2][1])<(kritiksaran[i][2][1]):
                    maks=i
                else:
                    if(kritiksaran[maks][2][1])<(kritiksaran[i][2][1]):
                        maks=i
        Temp=kritiksaran[maks]
        kritiksaran[maks]=kritiksaran[i]
        kritiksaran[i]=Temp

    indeks=0
    while (kritiksaran[indeks] != ['End']):  # Menghitung total jumlah kolom
        print(kritiksaran[indeks][2], "|" ,kritiksaran[indeks][1], "|" , kritiksaran[indeks][0], "|" , kritiksaran[indeks][3])
        indeks += 1

# F12
def tambah_wahana():
     # Asumsi seluruh input-an valid
     print("Masukkan Informasi Wahana yang ditambahkan:")
     ID = input("Masukkan ID Wahana: ")
     nama_wahana = input("Masukkan Nama Wahana: ")
     harga_tiket = input("Masukkan Harga Tiket: ")
     batas_umur = input("Batasan umur: ")
     batas_tinggi = input("Batasan tinggi badan: ")
     print()
     print("Info wahana telah ditambahkan!")
     add_wahana = [[ID, nama_wahana, harga_tiket, batas_umur, batas_tinggi]]
     tambah_arr (wahana, add_wahana)

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

# F14 - Melihat Riwayat Penggunaan Wahana
# Prosedur ini akan menampilkan riwayan penggunaan wahana. Nilai yang akan ditampilkan adalah
# tanggal bermain, username, dan jumlah tiket
def riwayat_pengguna():
    ID_wahana = input("Masukkan ID Wahana: ")
    print("Riwayat:")
    indeks = 0
    while (penggunaan[indeks] != ['End']):
        if (penggunaan[indeks][2] == ID_wahana):
            print(penggunaan[indeks][1], '|', penggunaan[indeks][0],'|' , penggunaan[indeks][3])
        indeks = indeks + 1

# F15 - Melihat Jumlah Tiket Pemain
# Fungsi untuk melihat jumlah tiket yang dimiliki pemain
# Jumlah tiket pemain hanya dapat dilihat oleh admin
def jumlahTiket():
    Username=input("Masukkan username: ")
    print("Riwayat")
    indeks=0
    while(tiket[indeks] != ['End']):
        if(tiket[indeks][0]==Username):
            indeks_w = cari_elemen(wahana,0,tiket[indeks][1])
            print(tiket[indeks][1], "|" ,wahana[indeks_w][1], "|" ,tiket[indeks][2])
        indeks +=1

# F16
def exit():
     close = input("Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ? ")

     while (not close == 'Y' and not close == 'N'):
          close = input("Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ? ")

     if (close == "Y"):
        print('$ save')
        save_file()
     return False

# B01 - Penyimpanan Password
# Fungsi membalikkan masing-masing character sesuai prosedur di bawah
# Fungsi akan mengubah nilai password menjadi password enkripsi.
def simpan_password (password):
    i = 0
    for char in password:   #mencari panjang password
        i = i + 1
    a = ['0' for indeks in range(i)]    #array password enkripsi
    i = 0
    for char in password:
        if (char == 'a'):
            a[i] = 'b'
        elif (char == 'b'):
            a[i] = 'a'
        elif (char == 'c'):
            a[i] = 'd'
        elif (char == 'd'):
            a[i] = 'c'
        elif (char == 'e'):
            a[i] = 'f'
        elif (char == 'f'):
            a[i] = 'e'
        elif (char == 'g'):
            a[i] = 'h'
        elif (char == 'h'):
            a[i] = 'g'
        elif (char == 'i'):
            a[i] = 'j'
        elif (char == 'j'):
            a[i] = 'i'
        elif (char == 'k'):
            a[i] = 'l'
        elif (char == 'l'):
            a[i] = 'k'
        elif (char == 'm'):
            a[i] = 'n'
        elif (char == 'n'):
            a[i] = 'm'
        elif (char == 'o'):
            a[i] = 'p'
        elif (char == 'p'):
           a[i] = 'o'
        elif (char == 'q'):
            a[i] = 'r'
        elif (char == 'r'):
            a[i] = 'q'
        elif (char == 's'):
            a[i] = 't'
        elif (char == 't'):
            a[i] = 's'
        elif (char == 'u'):
            a[i] = 'v'
        elif (char == 'v'):
            a[i] = 'u'
        elif (char == 'w'):
            a[i] = 'x'
        elif (char == 'x'):
            a[i] = 'w'
        elif (char == 'y'):
            a[i] = 'z'
        elif (char == 'z'):
            a[i] = 'y'
        elif (char == 'A'):
            a[i] = 'B'
        elif (char == 'B'):
            a[i] = 'A'
        elif (char == 'C'):
            a[i] = 'D'
        elif (char == 'D'):
            a[i] = 'C'
        elif (char == 'E'):
            a[i] = 'F'
        elif (char == 'F'):
            a[i] = 'E'
        elif (char == 'G'):
            a[i] = 'H'
        elif (char == 'H'):
            a[i] = 'G'
        elif (char == 'I'):
            a[i] = 'J'
        elif (char == 'J'):
            a[i] = 'I'
        elif (char == 'K'):
            a[i] = 'L'
        elif (char == 'L'):
            a[i] = 'K'
        elif (char == 'M'):
            a[i] = 'N'
        elif (char == 'N'):
            a[i] = 'M'
        elif (char == 'O'):
            a[i] = 'P'
        elif (char == 'P'):
            a[i] = 'O'
        elif (char == 'Q'):
            a[i] = 'R'
        elif (char == 'R'):
            a[i] = 'Q'
        elif (char == 'S'):
            a[i] = 'T'
        elif (char == 'T'):
            a[i] = 'S'
        elif (char == 'U'):
            a[i] = 'V'
        elif (char == 'V'):
            a[i] = 'U'
        elif (char == 'W'):
            a[i]= 'X'
        elif (char == 'X'):
            a[i] = 'W'
        elif (char == 'Y'):
            a[i] = 'Z'
        elif (char == 'Z'):
            a[i] = 'Y'
        elif (char == '1'):
            a[i] = '2'
        elif (char == '2'):
            a[i] = '1'
        elif (char == '3'):
            a[i] = '4'
        elif (char == '4'):
            a[i] = '3'
        elif (char == '5'):
            a[i] = '6'
        elif (char == '6'):
            a[i] = '5'
        elif (char == '7'):
            a[i] = '8'
        elif (char == '8'):
            a[i] = '7'
        elif (char == '9'):
            a[i] = '0'
        elif (char == '0'):
            a[i] = '9'
        else:
            a[i] = char
        i = i +1
    # Mengubah a(list) menjadi string
    password_enkripsi = a[0]
    for i in range(1,i):
        password_enkripsi = password_enkripsi + a[i]
    #Mengembalikan password enkripsi
    return password_enkripsi

# B02 - Golden Account
# Prosedur yang mengupgrade akun pemain menjadi golden account
# Golden account hanya bisa diberikan oleh admin
# Golden Account mendapat keuntungan dapat membeli tiket wahana setengah dari harga aslinya
# Pemain harus membayar uang sebasar Rp 150.000
def Golden_Account():
    # Prosedur yang mengubah kolom golsen_account pemain menjadi bernilai 1 yang sebelumnya bernilai 0
    # diasumsikan jika admin menjalankan prosedur ini, pemain sudah membayar biaya upgrade sebesar Rp 150.000
    # saat admin memasukkan username pemain maka otomatis account pemain berubah menjadi golden account
    # diasumsikan username yang dimasukkan sudah pasti ada di dalam file user
    # diasumsikan saldo telah mencukupi untuk melakukan upgrade account
    username = input("Masukkan username yang ingin di-upgrade: ")
    indeks = cari_elemen(user,3,username)
    user[indeks][7]= str(int(user[indeks][7])+1)
    user[indeks][6]=str(int(user[indeks][6])-150000)
    print('Akun anda telah diupgrade.')

# B03
def hitung_kolom_array(pembelian):
     mark = ["End"]
     kolom_total = 0
     while (not pembelian[kolom_total] == mark):
          kolom_total += 1

     return(kolom_total) #kolom_total = 1

def pembanding_minimal(elemen1, elemen2):
     #elemen1 == "YUG123"
     #elemen2 == "ZIY456"
     k = 0
     found = False
     while (k <= 5 and not found):
          if (k <= 2):
               if (int(ord(elemen1[k])) < int(ord(elemen2[k]))):
                    return elemen1
                    found = True
               
               elif (int(ord(elemen1[k])) > int(ord(elemen2[k]))):
                    return elemen2
                    found = True

               else:
                    k += 1
                    
          elif (2 < k <= 5):
               if (int(elemen1[k]) < int(elemen2[k])):
                    return elemen1
                    found = True
                    
               elif (int(elemen1[k]) > int(elemen2[k])):
                    return elemen2
                    found = True
                    
               else:
                    k += 1
          
     if (not found):
          return elemen1
  
def best_wahana():
     print()
     batas_kolom = hitung_kolom_array(pembelian)
     
     if (batas_kolom != 0): #baris yang diakses bukan ["End"]
          # Urutkan ID_Wahana
          for i in range (0, (batas_kolom-1)): #benchmark
              kolom_min = i
              for j in range ((i+1), batas_kolom): # Peninjauan terhadap benchmark
                  if (str(pembanding_minimal(pembelian[kolom_min][2], pembelian[j][2])) == str(pembelian[j][2])): 
                      kolom_min = j #didapat kolom pembuat ID_Wahana minimum relatif terhadap kolom i
                      
              #urutkan array utama berdasarkan indeks pembuat ID_Wahana minimum
              Array_Temp = pembelian[i]
              pembelian[i] = pembelian[kolom_min]
              pembelian[kolom_min] = Array_Temp

          # Array sudah terurut berdasarkan ID_Wahana

          # Hitung jumlah tiket total untuk suatu ID_Wahana, nilainya dimasukkan dalam sebuah array.
          # indeks array tersebut menyatakan baris awal tiap ID_Wahana yang memiliki kesamaan ID_Wahana
          total_tiket_ID_Wahana = [0 for i in range (hitung_kolom_array(pembelian))]
        
          mark = ["End"]
          kolom_awal = 0
          i = 0 # akses baris pada kolom ID_Wahana
          sum_tiket = 0
          while ((i <= int(hitung_kolom_array(pembelian)-1)) and kolom_awal <= (hitung_kolom_array(pembelian)-1)):
                    if (pembelian[i][2] == pembelian[kolom_awal][2]):
                        while ((i <= int(hitung_kolom_array(pembelian)-1)) and pembelian[i][2] == pembelian[kolom_awal][2]):
                            sum_tiket += int(pembelian[i][3])
                            i += 1 
                        total_tiket_ID_Wahana[kolom_awal] = sum_tiket
                        sum_tiket = 0

                    else:
                       kolom_awal = i

          # Cari total jumlah tiket urutan pertama dan simpan urutan kolom_awal yang aksesnya terhadap ID_Wahana tertentu 
          max_kolom_pertama = 0
          max_tiket_pertama = total_tiket_ID_Wahana[0]
          for i in range (1, hitung_kolom_array(pembelian)):
              if (max_tiket_pertama < total_tiket_ID_Wahana[i]):
                  max_tiket_pertama = total_tiket_ID_Wahana[i]
                  max_kolom_pertama = i
                    
          total_tiket_ID_Wahana[max_kolom_pertama] = 0

          # Cari total jumlah tiket urutan kedua dan simpan urutan baris yang aksesnya terhadap ID_Wahana tertentu
          max_kolom_kedua = 0
          max_tiket_kedua = total_tiket_ID_Wahana[0]
          for i in range (1, hitung_kolom_array(pembelian)):
              if (max_tiket_kedua < total_tiket_ID_Wahana[i]):
                  max_tiket_kedua = total_tiket_ID_Wahana[i]
                  max_kolom_kedua = i
                    
          total_tiket_ID_Wahana[max_kolom_kedua] = 0

          # Cari total jumlah tiket urutan ketiga dan simpan urutan baris yang aksesnya terhadap ID_Wahana tertentu 
          max_kolom_ketiga = 0
          max_tiket_ketiga = total_tiket_ID_Wahana[0]
          for i in range (1, hitung_kolom_array(pembelian)):
              if (max_tiket_ketiga < total_tiket_ID_Wahana[i]):
                  max_tiket_ketiga = total_tiket_ID_Wahana[i]
                  max_kolom_ketiga = i
                    
          total_tiket_ID_Wahana[max_kolom_ketiga] = 0

               
          if(hitung_kolom_array(pembelian) >= 1): 
              #Cari nama wahana berdasarkan ID_Wahana dengan mengakses array wahana dan memanfaatkan fungsi carielemen2()
              kolom_nama_wahana1 = cari_elemen(wahana, int(0), pembelian[max_kolom_pertama][2])
              nama_wahana1 = wahana[kolom_nama_wahana1][1]
              print("1 | " + str(pembelian[max_kolom_pertama][2]) + " | " + str(nama_wahana1) + " | " + str(max_tiket_pertama))

           
          if(hitung_kolom_array(pembelian) >= 2 and max_tiket_kedua != 0):
              #Cari nama wahana berdasarkan ID_Wahana dengan mengakses array wahana dan memanfaatkan fungsi carielemen2()
              kolom_nama_wahana2 = cari_elemen(wahana, int(0), pembelian[max_kolom_kedua][2])
              nama_wahana2 = wahana[kolom_nama_wahana2][1]
              print("2 | " + str(pembelian[max_kolom_kedua][2]) + " | " + str(nama_wahana2) + " | " + str(max_tiket_kedua))

          if(hitung_kolom_array(pembelian) >= 3 and max_tiket_ketiga != 0):
              #Cari nama wahana berdasarkan ID_Wahana dengan mengakses array wahana dan memanfaatkan fungsi carielemen2()
              kolom_nama_wahana3 = cari_elemen(wahana, int(0), pembelian[max_kolom_ketiga][2])
              nama_wahana3 = wahana[kolom_nama_wahana3][1]
              print("3 | " + str(pembelian[max_kolom_ketiga][2]) + " | " + str(nama_wahana3) + " | " + str(max_tiket_ketiga))


# B04-Laporan Kehilangan Tiket
# Fungsi yang akan mencatat data kehilangan tiket seorang pemain yang dilaporkan (masukan pengguna)
def tiket_hilang ():
    # Prosedur yang akan mengubah array kehilangan yang telah ditambah data kehilangan masukan pengguna
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

def lihat_perintah(username):
    indeks = cari_elemen(user,3,username)
    print()
    print('Perintah yang tersedia')
    if user[indeks][5]=='admin':
        print('Sign Up User : signup \nPencarian Pemain : cari_pemain \nPencarian Wahana : cari')
        print('Melihat Kritik dan Saran : lihat_laporan \nMenambahkan Wahana Baru : tambah_wahana \nTop Up Saldo : topup')
        print('Melihat Riwayat Penggunaan Wahana : riwayat_wahana \nMelihat Jumlah Tiket Pemain : tiket_pemain')
        print('Upgrade Akun : upgrade_gold \nBest Wahana : best_wahana \nLihat Perintah : lihat_perintah \nSave : save \nKeluar : exit')
    else :
        print('Pencarian Pemain : cari_pemain \nPencarian Wahana : cari \nPembelian Tiket : beli_tiket')
        print('Menggunakan Tiket : main \nPengembalian Tiket : refund \nKritik dan Saran : kritik_saran')
        print('Laporan Kehilangan Tiket : tiket_hilang \nBest Wahana : best_wahana \nLihat Perintah : lihat_perintah \nSave : save \nKeluar : exit')
    print()

login = False
print(55*'-')
print('     Selamat Datang di Taman Bermain Willy Wangky!     ')
print(55*'-','\n')
while True:
    print('Silakan load file data dan lakukan Login!\n')
    load()
    print('\n$ login')
    username = login_user()
    login = True
    lihat_perintah(username)
    while login:
        perintah = input('$ ')
        indeks = cari_elemen(user,3,username)
        if user[indeks][5]=='admin':
            if perintah == 'signup':
                signUpUser()
            elif perintah == 'cari_pemain':
                cari_pemain()
            elif perintah == 'cari':
                cari_wahana()
            elif perintah == 'lihat_laporan':
                lihatKritik()
            elif perintah == 'tambah_wahana':
                tambah_wahana()
            elif perintah == 'topup':
                topup()
            elif perintah == 'riwayat_wahana':
                riwayat_pengguna()
            elif perintah == 'tiket_pemain':
                jumlahTiket()
            elif perintah == 'upgrade_gold':
                Golden_Account()
            elif perintah == 'best_wahana':
                best_wahana()
            elif perintah == 'lihat_perintah':
                lihat_perintah(username)
            elif perintah == 'exit':
                login = exit()
            elif perintah == 'save':
                save_file()
            else:
                print('Peritah masukan salah! Sila tulis kembali')
        else:
            if perintah == 'cari_pemain':
                cari_pemain()
            elif perintah == 'cari':
                cari_wahana()
            elif perintah == 'beli_tiket':
                pembelianTiket(username)
            elif perintah == 'main':
                pakai_tiket(username)
            elif perintah == 'refund':
                refund_tiket(username)
            elif perintah == 'kritik_saran':
                kritik_saran()
            elif perintah == 'tiket_hilang':
                tiket_hilang()
            elif perintah == 'best_wahana':
                best_wahana()
            elif perintah == 'save':
                save_file()
            elif perintah == 'lihat_perintah':
                lihat_perintah(username)
            elif perintah == 'exit':
                login = exit()
            else:
                print('Peritah masukan salah! Sila tulis kembali')
        print()
