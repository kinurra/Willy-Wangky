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
     print()
     print("$ save")
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
