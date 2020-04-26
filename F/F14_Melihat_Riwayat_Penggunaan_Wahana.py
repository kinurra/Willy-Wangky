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
