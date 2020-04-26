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
            if (username == user[indeks][3]) and (password == user[indeks][4]:
                exist = True                
            else:
                indeks+=1            
         if (exist == True):
            print("Selamat bersenang-senang, Willy Wangky!")
         else:
             print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
             print("")
