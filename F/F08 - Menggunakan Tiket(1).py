# Username, Tanggal_Penggunaan, ID_Wahana, Jumlah_Tiket
# penggunaan

# Username,ID_Wahana,Jumlah_Tiket
# tiket

# Username, Tanggal_Pembelian, ID_Wahana, Jumlah_Tiket
# pembelian

def isKabisat(tahun):
     if (tahun % 400 == 0 or (not tahun % 400 == 0 and not tahun % 100 == 0 and tahun % 4 == 0)):
          return True
     elif ((not tahun % 400 == 0 and tahun % 100 == 0) or (not tahun % 400 == 0 and not tahun % 100 == 0 and not tahun % 4 == 0)):
          return False 

def isValid_hari(tahun, bulan, hari):
     if (isKabisat(tahun) and (int(bulan) == 2)):
          if (hari == "28"):
               return True
          else:
               return False
     elif (not isKabisat(tahun) and (int(bulan) == 2)):
          if (hari == "29"):
               return True
          else:
               return False
     
     elif (int(bulan) == 1 or int(bulan) == 3 or int(bulan) == 5 or int(bulan) == 7 or int(bulan) == 8 or int(bulan) == 10 or int(bulan) == 12):
          if (hari == "31"):
               return True
          else:
               return False

     elif (int(bulan) == 4 or int(bulan) == 6 or int(bulan) == 9 or int(bulan) == 11):
          if (hari == "30"):
               return True
          else:
               return False

def cari_elemen2 (array, indeks1, keyword1, indeks2, keyword2) :
    #sama dengan fungsi cari_elemen namun dengan dua kriteria
    i=0
    while array[i] != ['End']:
        if array[i][indeks1]==keyword1 and array[i][indeks2]==keyword2:
            break
        i+=1
    return i

### Utama

def pakai_tiket(username):
     ID = input("Masukkan ID wahana: ")
     tanggal_penggunaan = input("Masukkan tanggal hari ini: ") # Asumsi input-an valid sesuai format tanggal
     jml_penggunaan_tiket = int(input("Jumlah tiket yang digunakan: "))
     print()

     mark = ["End"]

     # Validasi tanggal penggunaan tiket terhadap tanggal pembelian (minimal pernah 1 kali membeli)
     baris_tanggal_beli = cari_elemen2(pembelian, 0, username, 2, ID)
     if (pembelian[baris_tanggal_beli] != mark):

          # Ubah hari tanggal pembelian dari str menjadi int 
          digit_hari_beli = 0
          hari_beli_str = ''
          for column in pembelian[baris_tanggal_beli][1]:
               hari_beli_str += column
               digit_hari_beli += 1
               if (digit_hari_beli == 2):
                    break

          hari_beli_int = int(hari_beli_str)

          # Ubah hari tanggal pemakaian dari str menjadi int 
          digit_hari_pakai = 0
          hari_pakai_str = ''
          for column in tanggal_penggunaan:
               hari_pakai_str += column
               digit_hari_pakai += 1
               if (digit_hari_pakai == 2):
                    break

          hari_pakai_int = int(hari_pakai_str)

          ## Ubah bulan tanggal pembelian dari str menjadi int
          i = 0
          digit_bulan_beli = 0
          bulan_beli_str = ''
          for column in pembelian[baris_tanggal_beli][1]: #22/08/2020
               i += 1 
               if (i > 3):
                    bulan_beli_str += column
                    digit_bulan_beli += 1
                    if (digit_bulan_beli == 2):
                         break

          bulan_beli_int = int(bulan_beli_str)

          ## Ubah bulan tanggal pemakaian dari str menjadi int
          i = 0
          digit_bulan_pakai = 0
          bulan_pakai_str = ''
          for column in tanggal_penggunaan:
               i += 1 
               if (i > 3):
                    bulan_pakai_str += column
                    digit_bulan_pakai += 1
                    if (digit_bulan_pakai == 2):
                         break

          bulan_pakai_int = int(bulan_pakai_str)

          ### Ubah tahun tanggal pembelian dari str menjadi int
          i = 0
          digit_tahun_beli = 0
          tahun_beli_str = ''
          for column in pembelian[baris_tanggal_beli][1]:
               i += 1 
               if (i > 6):
                    tahun_beli_str += column
                    digit_tahun_beli += 1
                    if (digit_tahun_beli == 4):
                         break

          tahun_beli_int = int(tahun_beli_str)

          ### Ubah tahun tanggal pemakaian dari str menjadi int
          i = 0
          digit_tahun_pakai = 0
          tahun_pakai_str = ''
          for column in tanggal_penggunaan:
               i += 1 
               if (i > 6):
                    tahun_pakai_str += column
                    digit_tahun_pakai += 1
                    if (digit_tahun_pakai == 4):
                         break

          tahun_pakai_int = int(tahun_pakai_str)

          # Validasi Tanggal, Bulan, dan Tahun Pemakaian berdasarkan kesesuaian input dan kelender Masehi
          tanggal_pakai_Masehi = False #var yg menyatakan apakah tanggal pemakaian (input) valid atau tidak sesuai kalender Masehi
          
          if (not 1 <= bulan_pakai_int <= 12):
               print("Tiket Anda tidak valid dalam sistem kami")
               pakai_tiket(username)

          else: # bulan pemakaian sudah valid sesuai kalender Masehi
               if (not isValid_hari(tahun_pakai_int, bulan_pakai_int, hari_pakai_int)): 
                    print("Tiket Anda tidak valid dalam sistem kami")
                    pakai_tiket(username)

               else:
                    tanggal_pakai_Masehi = True
                    
          # Tanggal pakai valid sesuai kalender Masehi

          # Periksa apakah tanggal pemakaian sesudah tanggal pembelian tiket
          if (tanggal_pakai_Masehi):
               # Validasi hari pemakaian terhadap hari pembelian
               tanggal_pakai = False #var yg menyatakan apakah tanggal pemakaian valid terhadap tanggal pembelian
               
               if (not tahun_beli_int <= tahun_pakai_int or (tahun_beli_int == tahun_pakai_int and not bulan_beli_int <= bulan_pakai_int) or (tahun_beli_int == tahun_pakai_int and bulan_beli_int == bulan_pakai_int and not bulan_beli_int <= bulan_pakai_int)):
                    print("Tiket Anda tidak valid dalam sistem kami")
                    pakai_tiket(username)

               else:
                    tanggal_pakai = True

          else: # Tanggal pakai tidak valid berdasarkan kalender Masehi
               print("Tiket Anda tidak valid dalam sistem kami")
               pakai_tiket(username)  

          # Tanggal pakai sudah valid terhadap tanggal pembelian
          

     else: # Tidak ada kesesuaian antara username dan ID_Wahana pada array kepemilikan tiket
          print("Tiket Anda tidak valid dalam sistem kami")
          pakai_tiket(username)

     # Hitung jumlah tiket 
     if(tanggal_pakai):
          baris_jml_tiket = cari_elemen2(tiket, 0, username, 1, ID)  
          if (not tiket[baris_jml_tiket] == mark): #ID_Wahana terhadap username pada kepemilikan tiket, valid
               if(jml_penggunaan_tiket > int(tiket[baris_jml_tiket][2])):
                    print("Tiket Anda tidak valid dalam sistem kami")
                    pakai_tiket(username)

               else:
                    sisa_tiket = int(tiket[baris_jml_tiket][2]) - jml_penggunaan_tiket
                    tiket[baris_jml_tiket][2] = sisa_tiket
                    
                    
               
             
             
          


          
                         
          
     
     
