# B02 - Golden Account
# Prosedur yang mengupgrade akun pemain menjadi golden account
# Golden account hanya bisa diberikan oleh admin
# Golden Account mendapat keuntungan dapat membeli tiket wahana setengah dari harga aslinya
# Pemain harus membayar uang sebasar Rp 150.000
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

def Golden_Account():
    # Prosedur yang mengubah kolom golsen_account pemain menjadi bernilai 1 yang sebelumnya bernilai 0
    # diasumsikan jika admin menjalankan prosedur ini, pemain sudah membayar biaya upgrade sebesar Rp 150.000
    # saat admin memasukkan username pemain maka otomatis account pemain berubah menjadi golden account
    # diasumsikan username yang dimasukkan sudah pasti ada di dalam file user
    # diasumsikan saldo telah mencukupi untuk melakukan upgrade account
    print("$ upgrade_gold")
    username = input("Masukkan username yang ingin di-upgrade: ")
    indeks = cari_elemen(user,3,username)
    user[indeks][7]= str(int(user[indeks][7])+1)
    user[indeks][6]=str(int(user[indeks][6])-150000)