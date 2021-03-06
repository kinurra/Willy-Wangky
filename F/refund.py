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
        if int(tiket[indeks][2])>int(jumlah) :
            print('Uang refund sudah kami berikan pada akun anda')
            tambah_arr(refund,arr)
            indeks_s = cari_elemen (user,3,username)
            indeks_w = cari_elemen (wahana,0,ID)
            user[indeks_s][6]=str(int(user[indeks_s][6])+int(jumlah)*(int(wahana[indeks_w][2])-2000))
            tiket[indeks][2]=str(int(tiket[indeks][2])-int(jumlah))
        else : # Data tidak sesuai
            print('Jumlah tiket yang di-refund melebihi kepunyaan Anda')
    else : # Data tidak ditemukan
        print('Anda tidak memiliki tiket terkait')
