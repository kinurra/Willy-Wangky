import csv

#F02 - Login User
# Fungsionalitas yang lain dapat digunakan setelah user (admin maupun pemain) melakukan login
def login_user (username):
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
    while(umur != "1" or umur != "2" or umur != "3"):
        print("Batasan umur tidak valid!")
        umur = input("Batasan umur pemain: ")
    tinggi = input("Batasan tinggi badan: ")
    while(tinggi != "1" or tinggi != "2"):
        print("Batasan tinggi badan tidak valid!")
        tinggi = input("Batasan tinggi badan: ")       
    if (umur == '1'):
        if (tinggi == "1"):
            tinggi = '171'
        else:
            tinggi = '-'
        umur = '7'
    elif (umur == '2'):
        if (tinggi == "1"):
            tinggi = '171'
        else:
            tinggi = '-'
        umur = '17'
    else:
        if (tinggi == "1"):
            tinggi = '171'
        else:
            tinggi = '-'
        umur = '-'
    indeks = 0
    exist = False
    print("Hasil pencarian:")
    while(wahana[indeks] == ['End']):
        if (wahana[indeks][4] == umur and wahana[indeks][5] == tinggi):
            print(wahana[indeks][0], '|', wahana[indeks][1], '|', wahana[indeks][2])
            exist = True
        indeks = indeks + 1
    if (exist == False):
        print("Tidak ada wahana yang sesuai dengan pencarian kamu.")

# F10 - Kritik dan Saran
# Prosedur ini akan menyimpan kritik/saran terhadap sebuah wahana dan menyimpan tanggal pelaporan
def kritik_saran():
    ID_wahana = input("Masukkan ID Wahana: ")
    tanggal_pelaporan = input("Masukkan tanggal pelaporan: ")
    kritik_saran = input("Kritik/saran Anda: ")
    print("")
    print("Kritik dan saran Anda kami terima.")

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






            



            

           
