# B03
def hitung_kolom_array(pembelian):
     mark = ["End"]
     kolom_total = 0
     while (not pembelian[kolom_total] == mark):
          kolom_total += 1

     return(kolom_total) #kolom_total = 1

def pembanding_minimal(elemen1, elemen2):
     #elemen1 == "YUG123"
     #elemen2 == "ZIY456"
     k = 0
     found = False
     while (k <= 5 and not found):
          if (k <= 2):
               if (int(ord(elemen1[k])) < int(ord(elemen2[k]))):
                    return elemen1
                    found = True
               
               elif (int(ord(elemen1[k])) > int(ord(elemen2[k]))):
                    return elemen2
                    found = True

               else:
                    k += 1
                    
          elif (2 < k <= 5):
               if (int(elemen1[k]) < int(elemen2[k])):
                    return elemen1
                    found = True
                    
               elif (int(elemen1[k]) > int(elemen2[k])):
                    return elemen2
                    found = True
                    
               else:
                    k += 1
          
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
     print()
     batas_kolom = hitung_kolom_array(pembelian)
     
     if (batas_kolom != 0): #baris yang diakses bukan ["End"]
          # Urutkan ID_Wahana
          for i in range (0, (batas_kolom-1)): #benchmark
              kolom_min = i
              for j in range ((i+1), batas_kolom): # Peninjauan terhadap benchmark
                  if (str(pembanding_minimal(pembelian[kolom_min][2], pembelian[j][2])) == str(pembelian[j][2])): 
                      kolom_min = j #didapat kolom pembuat ID_Wahana minimum relatif terhadap kolom i
                      
              #urutkan array utama berdasarkan indeks pembuat ID_Wahana minimum
              Array_Temp = pembelian[i]
              pembelian[i] = pembelian[kolom_min]
              pembelian[kolom_min] = Array_Temp

          # Array sudah terurut berdasarkan ID_Wahana

          # Hitung jumlah tiket total untuk suatu ID_Wahana, nilainya dimasukkan dalam sebuah array.
          # indeks array tersebut menyatakan baris awal tiap ID_Wahana yang memiliki kesamaan ID_Wahana
          total_tiket_ID_Wahana = [0 for i in range (hitung_kolom_array(pembelian))]
        
          mark = ["End"]
          kolom_awal = 0
          i = 0 # akses baris pada kolom ID_Wahana
          sum_tiket = 0
          while ((i <= int(hitung_kolom_array(pembelian)-1)) and kolom_awal <= (hitung_kolom_array(pembelian)-1)):
                    if (pembelian[i][2] == pembelian[kolom_awal][2]):
                        while ((i <= int(hitung_kolom_array(pembelian)-1)) and pembelian[i][2] == pembelian[kolom_awal][2]):
                            sum_tiket += int(pembelian[i][3])
                            i += 1 
                        total_tiket_ID_Wahana[kolom_awal] = sum_tiket
                        sum_tiket = 0

                    else:
                       kolom_awal = i

          # Cari total jumlah tiket urutan pertama dan simpan urutan kolom_awal yang aksesnya terhadap ID_Wahana tertentu 
          max_kolom_pertama = 0
          max_tiket_pertama = total_tiket_ID_Wahana[0]
          for i in range (1, hitung_kolom_array(pembelian)):
              if (max_tiket_pertama < total_tiket_ID_Wahana[i]):
                  max_tiket_pertama = total_tiket_ID_Wahana[i]
                  max_kolom_pertama = i
                    
          total_tiket_ID_Wahana[max_kolom_pertama] = 0

          # Cari total jumlah tiket urutan kedua dan simpan urutan baris yang aksesnya terhadap ID_Wahana tertentu
          max_kolom_kedua = 0
          max_tiket_kedua = total_tiket_ID_Wahana[0]
          for i in range (1, hitung_kolom_array(pembelian)):
              if (max_tiket_kedua < total_tiket_ID_Wahana[i]):
                  max_tiket_kedua = total_tiket_ID_Wahana[i]
                  max_kolom_kedua = i
                    
          total_tiket_ID_Wahana[max_kolom_kedua] = 0

          # Cari total jumlah tiket urutan ketiga dan simpan urutan baris yang aksesnya terhadap ID_Wahana tertentu 
          max_kolom_ketiga = 0
          max_tiket_ketiga = total_tiket_ID_Wahana[0]
          for i in range (1, hitung_kolom_array(pembelian)):
              if (max_tiket_ketiga < total_tiket_ID_Wahana[i]):
                  max_tiket_ketiga = total_tiket_ID_Wahana[i]
                  max_kolom_ketiga = i
                    
          total_tiket_ID_Wahana[max_kolom_ketiga] = 0

               
          if(hitung_kolom_array(pembelian) >= 1): 
              #Cari nama wahana berdasarkan ID_Wahana dengan mengakses array wahana dan memanfaatkan fungsi carielemen2()
              kolom_nama_wahana1 = cari_elemen(wahana, int(0), pembelian[max_kolom_pertama][2])
              nama_wahana1 = wahana[kolom_nama_wahana1][1]
              print("1 | " + str(pembelian[max_kolom_pertama][2]) + " | " + str(nama_wahana1) + " | " + str(max_tiket_pertama))

           
          if(hitung_kolom_array(pembelian) >= 2 and max_tiket_kedua != 0):
              #Cari nama wahana berdasarkan ID_Wahana dengan mengakses array wahana dan memanfaatkan fungsi carielemen2()
              kolom_nama_wahana2 = cari_elemen(wahana, int(0), pembelian[max_kolom_kedua][2])
              nama_wahana2 = wahana[kolom_nama_wahana2][1]
              print("2 | " + str(pembelian[max_kolom_kedua][2]) + " | " + str(nama_wahana2) + " | " + str(max_tiket_kedua))

          if(hitung_kolom_array(pembelian) >= 3 and max_tiket_ketiga != 0):
              #Cari nama wahana berdasarkan ID_Wahana dengan mengakses array wahana dan memanfaatkan fungsi carielemen2()
              kolom_nama_wahana3 = cari_elemen(wahana, int(0), pembelian[max_kolom_ketiga][2])
              nama_wahana3 = wahana[kolom_nama_wahana3][1]
              print("3 | " + str(pembelian[max_kolom_ketiga][2]) + " | " + str(nama_wahana3) + " | " + str(max_tiket_ketiga))
