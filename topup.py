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
