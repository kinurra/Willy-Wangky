# F08
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
          pakai_tiket(username)

     else:     
     # Hitung jumlah tiket 
         baris_jml_tiket = cari_elemen2(tiket, 0, username, 1, ID)  
         if (not tiket[baris_jml_tiket] == mark): #ID_Wahana terhadap username pada kepemilikan tiket, valid
             if(jml_penggunaan_tiket > int(tiket[baris_jml_tiket][2])):
                 print("Tiket Anda tidak valid dalam sistem kami")
                 print()
                 pakai_tiket(username)

             else:
                 sisa_tiket = int(tiket[baris_jml_tiket][2]) - jml_penggunaan_tiket
                 tiket[baris_jml_tiket][2] = sisa_tiket
                 print('Terima kasih telah bermain.')
                 tambah_arr(penggunaan,[username,tanggal_penggunaan,ID,jml_penggunaan_tiket])
         else :
             print("Tiket Anda tidak valid dalam sistem kami")
             print()
             pakai_tiket(username)
