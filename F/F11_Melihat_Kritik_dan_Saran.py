# F11 - Melihat Kritik dan Saran
# Fungsi yang dapat melihat kritik dan saran yang dimasukkan oleh pemain
# Diurutkan bedasarkan ID Wahana secara alfabetis
def lihatKritik():
    a=0
    while array[i] != ['End']: # Menghitung total jumlah kolom
        a+=1
    a=length
    for i in range (length):
        maks=i
        for i in range (i+1,length):
            if(kritiksaran[maks][2][0])<(kritiksaran[i][2][0]):
                maks =i
            elif(kritiksaran[maks][2][0])==(kritiksaran[i][2][0]):
                if(kritiksaran[maks][2][1])<(kritiksaran[i][2][1]):
                    maks=i
                else:
                    if(kritiksaran[maks][2][1])<(kritiksaran[i][2][1]):
                        maks=i
        Temp=kritiksaran[maks]
        kritiksaran[maks]=kritiksaran[i]
        kritiksaran[i]=Temp

    indeks=0
    while array[i] != ['End']:  # Menghitung total jumlah kolom
        indeks += 1
        print(kritiksaran[indeks][2], "|" ,kritiksaran[indeks][1], "|" , kritiksaran[indeks][0], "|" , kritiksaran[indeks][3])
