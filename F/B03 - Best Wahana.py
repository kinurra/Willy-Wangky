# Username, Tanggal_Pembelian, ID_Wahana, Jumlah_Tiket
# pembelian

# [kinura, 22/08/2020, FHG908, 20]
# [kinura, 23/08/2020, FHG908, 9]
# [HUYA, 24/08/2020, HIU122, 12]
# [End]

# Misal masih teracak

# Skenario 1
# Fungsi
# loop
     # Cari baris ke berapa aja untuk suatu ID_Wahana
     # Jumlahkan semua kolom 3 untuk baris-baris tersebut
# Hilangkan baris yang sudah dicari
# Baris habis = False then
     # Fungsi
# Baris habis = True then
     # Hitung yang terbesar

# Skenario 2
# Urutkan berdasarkan ID_Wahana (ascending)
     # Tentukan indeks pembuat ID_Wahana minimum
# Hitung jumlah tiket ID_Wahana yang paling banyak


def hitung_baris_array(pembelian):
     mark = ["End"]
     baris_total = 0
     while (not pembelian[baris_total] == mark):
          baris_total += 1

     return(baris_total)

def pembanding_minimal(elemen1, elemen2):
     #elemen1 == "YUG123"
     #elemen2 == "ZIY456"
     i = 0
     found = False
     while (i <= 5 and not found):
          if (i <= 2):
               if (int(ord(elemen1[i])) < int(ord(elemen2[i]))):
                    return elemen1
                    found = True
               
               elif (int(ord(elemen1[i])) > int(ord(elemen2[i]))):
                    return elemen2
                    found = True

               else:
                    i += 1
                    
          elif (2 < i <= 5):
               if (int(elemen1[i]) < int(elemen2[i])):
                    return elemen1
                    found = True
                    
               elif (int(elemen1[i]) > int(elemen2[i])):
                    return elemen2
                    found = True
                    
               else:
                    i += 1
          
     if (not found):
          return elemen1

def cari_elemen (array, indeks, keyword):
    # Fungsi yang akan mereturn indeks (dalam hal ini baris) suatu array yang sesuai dengan kriteria
    # memilik isi di indeks (baris dan kolom) tertentu sama dengan keyword yang diberikan
    # dapat digunakan di fungsi lain juga
    i=0
    while array[i] != ['End']:
        if array[i][indeks]==keyword:
            break
        i+=1
    return i
     
def best_wahana():
     batas_baris = hitung_baris_array(pembelian)
     
     if (batas_baris != 0): #baris yang diakses bukan ["End"]
          # Urutkan ID_Wahana
          for i in range (0, (batas_baris - 1)): #benchmark              
               for j in range ((i+1), batas_baris): #yg mau ngadu
                    if (pembanding_minimal(pembelian[i][2], pembelian[j][2]) == pembelian[j][2]):  #YUG123 < ZIY456
                         baris_min = j
                         
                    ID_temp = pembelian[i][2]
                    pembelian[i][2] = pembelian[baris_min][2]
                    pembelian[baris_min][2] = ID_temp

                    jlm_tiket_temp = pembelian[i][3]
                    pembelian[i][3] = pembelian[baris_min][3]
                    pembelian[baris_min][3] = jml_tiket_temp

                    username_temp = pembelian[i][0]
                    pembelian[i][0] = pembelian[baris_min][0]
                    pembelian[baris_min][0] = username_temp

                    tanggal_beli_temp = pembelian[i][1]
                    pembelian[i][1] = pembelian[baris_min][1]
                    pembelian[baris_min][1] = tanggal_beli_temp

          # ID_Wahana dan jumlah tiket sudah terurut

          # Hitung jumlah tiket total untuk suatu ID_Wahana, nilainya dimasukkan dalam sebuah array.
          # indeks array tersebut menyatakan baris awal tiap ID_Wahana yang memiliki kesamaan ID_Wahana
          total_tiket_ID_Wahana = [0 for i in range (hitung_baris_array(pembelian))]
          
          baris_awal = 0
          i = 0 # akses baris pada kolom ID_Wahana
          initial = pembelian[baris_awal][2]
          sum_tiket = 0
          while (baris_awal <= hitung_baris_array(pembelian)):
               while (pembelian[i][2] == initial):
                    sum_tiket += int(pembelian[i][3])
                    i += 1
               total_tiket_ID_Wahana[baris_awal] = sum_tiket 
               baris_awal = i

         
          # Cari total jumlah tiket urutan pertama dan simpan urutan baris_awal yang aksesnya terhadap ID_Wahana tertentu      
          max_baris_pertama = 0
          max_tiket_pertama = total_tiket_ID_Wahana[0]
          for i in range (1, hitung_baris_array(pembelian)):
               if (max_tiket_pertama < total_tiket_ID_Wahana[i]):
                    max_tiket_pertama = total_tiket_ID_Wahana[i]
                    max_baris_pertama = i
                    
          total_tiket_ID_Wahana[max_baris_pertama] = 0

          # Cari total jumlah tiket urutan kedua dan simpan urutan baris yang aksesnya terhadap ID_Wahana tertentu 
          max_baris_kedua = 0
          max_tiket_kedua = total_tiket_ID_Wahana[0]
          for i in range (1, hitung_baris_array(pembelian)):
               if (max_tiket_kedua < total_tiket_ID_Wahana[i]):
                    max_tiket_kedua = total_tiket_ID_Wahana[i]
                    max_baris_kedua = i
                    
          total_tiket_ID_Wahana[max_baris_kedua] = 0

          # Cari total jumlah tiket urutan ketiga dan simpan urutan baris yang aksesnya terhadap ID_Wahana tertentu 
          max_baris_ketiga = 0
          max_tiket_ketiga = total_tiket_ID_Wahana[0]
          for i in range (1, hitung_baris_array(pembelian)):
               if (max_tiket_ketiga < total_tiket_ID_Wahana[i]):
                    max_tiket_ketiga = total_tiket_ID_Wahana[i]
                    max_baris_ketiga = i
                    
          total_tiket_ID_Wahana[max_baris_ketiga] = 0

          #Cari nama wahana berdasarkan ID_Wahana dengan mengakses array wahana dan memanfaatkan fungsi carielemen2()

          # Tinjau rank 1
          baris_nama_wahana1 = cari_elemen(wahana, int(0), pembelian[max_baris_pertama][2])
          nama_wahana1 = wahana[baris_nama_wahana1][1]
          print("1 | " + str(pembelian[max_baris_pertama][2]) + " | " + str(nama_wahana1) + " | " + str(max_tiket_pertama))

          # Tinjau rank 2
          baris_nama_wahana2 = cari_elemen(wahana, int(0), pembelian[max_baris_kedua][2])
          nama_wahana2 = wahana[baris_nama_wahana2][1]
          print("2 | " + str(pembelian[max_baris_kedua][2]) + " | " + str(nama_wahana2) + " | " + str(max_tiket_kedua))

          # Tinjau rank 3
          baris_nama_wahana3 = cari_elemen(wahana, int(0), pembelian[max_baris_ketiga][2])
          nama_wahana3 = wahana[baris_nama_wahana3][1]
          print("3 | " + str(pembelian[max_baris_ketiga][2]) + " | " + str(nama_wahana3) + " | " + str(max_tiket_ketiga))
          
                    
          
               

               


               
               
               
                    
                    
               
     
          
     
               

          
         
