#DENDI MAHAWARMAN (JCDSVL-005-014)

menu = ['1. Menampilkan Data Kontak Telepon',
        '2. Menambahkan Data Kontak Telepon',
        '3. Mengubah Data Kontak Telepon',
        '4. Menghapus Data Kontak Telepon',
        '5. Exit']

menu_show = ['1. Menampilkan Seluruh Data',
            '2. Menampilkan Data Tertentu',
            '3. Kembali Ke Menu Utama',]

menu_tambah = ['1. Menambahkan Data Kontak Telepon',
            '2. Kembali Ke Menu Utama',]

menu_update = ['1. Mengubah Data Kontak Telepon',
            '2. Kembali Ke Menu Utama',]

menu_hapus = ['1. Menghapus Data Kontak Telepon',
            '2. Kembali Ke Menu Utama',]

kontakTelepon = [{'Initial' : 'DEN', 'Kode_Wilayah' : '021', 'Nama' : 'Dendi Mahawarman', 'Kota' : 'Jakarta', 'Nomor_Telepon' : '205993'},
                {'Initial' : 'NUR', 'Kode_Wilayah' : '022', 'Nama' : 'Nur Annisa', 'Kota' : 'Bandung', 'Nomor_Telepon' : '203445'},
                {'Initial' : 'RAF', 'Kode_Wilayah' : '021', 'Nama' : 'Rafardhan', 'Kota' : 'Jakarta', 'Nomor_Telepon' : '202887'},
                {'Initial' : 'AKS', 'Kode_Wilayah' : '022', 'Nama' : 'Aksara', 'Kota' : 'Bandung', 'Nomor_Telepon' : '201335'}]

def menu_1 ():
    while(1):
        print("\n===== Menampilkan Data Kontak Telepon =====\n")
        for i in menu_show:
            print(i)
        pilihanSubMenu = input("\nSilahkan Pilih Sub Menu [1-3] : ")
        if(pilihanSubMenu == '1'):
            if(len(kontakTelepon) == 0):
                print("--- Tidak ada data kontak telepon ---")
            else:
                print("\nDaftar Kontak Telepon : ")
                for key in range(len(kontakTelepon)):
                    print("{}. Initial : {}, Kode Wilayah : {}, Nama : {}, Kota : {}, Nomor Telepon : {}".format(key+1, kontakTelepon[key]['Initial'], kontakTelepon[key]['Kode_Wilayah'], kontakTelepon[key]['Nama'], kontakTelepon[key]['Kota'], kontakTelepon[key]['Nomor_Telepon']))
        elif(pilihanSubMenu == '2'):
            a = 0
            uniqueKode1 = input("\nMasukkan Initial Nama : ")
            uniqueKode2 = input("Masukkan Kode Wilayah : ")
            print("Data Kontak Telepon dengan Initial Nama : {} dan Kode Wilayah : {}".format(uniqueKode1, uniqueKode2))
            for j in range(len(kontakTelepon)):
                if(kontakTelepon[j]['Initial'] == uniqueKode1 and kontakTelepon[j]['Kode_Wilayah'] == uniqueKode2):
                    print("1. Initial : {}, Kode Wilayah : {}, Nama : {}, Kota : {}, Nomor Telepon : {}".format(kontakTelepon[j]['Initial'], kontakTelepon[j]['Kode_Wilayah'], kontakTelepon[j]['Nama'], kontakTelepon[j]['Kota'], kontakTelepon[j]['Nomor_Telepon']))
                    a = 1
            if(a==0):
                print("--- Tidak ada data kontak telepon ---")
        elif(pilihanSubMenu == '3'):
            break
        else:
            print("\n--- Pilihan yang anda masukkan salah ---")
            
def menu_2 ():
    while(1):
        print("\n===== Menambahkan Data Kontak Telepon =====\n")
        for i in menu_tambah:
            print(i)
        pilihanSubMenu = input("\nSilahkan Pilih Sub Menu [1-2] : ")
        if(pilihanSubMenu == '1'):
            a = 0
            uniqueKode1 = input("\nMasukkan Initial Nama : ")
            uniqueKode2 = input("Masukkan Kode Wilayah : ")
            for j in range(len(kontakTelepon)):
                if(kontakTelepon[j]['Initial'] == uniqueKode1 and kontakTelepon[j]['Kode_Wilayah'] == uniqueKode2):
                    print("\n--- Data Sudah Ada ---")
                    a = 1
            if(a == 0):
                dataNama = input("Masukkan Nama : ")
                dataKota = input("Masukkan Kota : ")
                dataNomor = input("Masukkan Nomor Telepon : ")
                while(1):
                    simpanData = input("Apakah Data Akan Disimpan ? (Y/N) : ")

                    if(simpanData == 'Y' or simpanData == 'N'):
                        break
                if(simpanData == 'Y'):
                    kontakTelepon.append({'Initial' : uniqueKode1, 'Kode_Wilayah' : uniqueKode2, 'Nama' : dataNama, 'Kota' : dataKota, 'Nomor_Telepon' : dataNomor})
                    print("\n--- Data Tersimpan ---")
        elif(pilihanSubMenu == '2'):
            break
        else:
            print("\n--- Pilihan yang anda masukkan salah ---")
        
def update_data (b, kolomUpdate, dataKolom):
    while(1):
        updateData2 = input("Apakah data akan diupdate (Y/N) : ")
        if(updateData2 == 'Y' or updateData2 == 'N'):
            break

    if(updateData2 == 'Y'):
        kontakTelepon[b][kolomUpdate] = dataKolom
        print("\n--- Data Updated ---")
    elif(updateData2 == 'N'):
        print("\n--- Data Tidak Terupdate ---")

def menu_3 ():
    while(1):
        print("\n===== Mengubah Data Kontak Telepon =====\n")
        for i in menu_update:
            print(i)
        pilihanSubMenu = input("\nSilahkan Pilih Sub Menu [1-2] : ")
        if(pilihanSubMenu == '1'):
            a = 0
            b = 0
            uniqueKode1 = input("\nMasukkan Initial Nama : ")
            uniqueKode2 = input("Masukkan Kode Wilayah : ")
            for j in range(len(kontakTelepon)):
                if(kontakTelepon[j]['Initial'] == uniqueKode1 and kontakTelepon[j]['Kode_Wilayah'] == uniqueKode2):
                    a = 1
                    b = j
            if(a == 0):
                print("\n--- Data Tidak Ada ---")
            elif(a == 1):
                print("\n1. Initial : {}, Kode Wilayah : {}, Nama : {}, Kota : {}, Nomor Telepon : {}".format(kontakTelepon[b]['Initial'], kontakTelepon[b]['Kode_Wilayah'], kontakTelepon[b]['Nama'], kontakTelepon[b]['Kota'], kontakTelepon[b]['Nomor_Telepon']))
                while(1):
                    updateData = input("\nTekan Y jika ingin lanjut update data atau N jika ingin cancel update (Y/N) : ")
                    if(updateData == 'Y' or updateData == 'N'):
                        break
                if(updateData == 'Y'):
                    kolomUpdate = input("\nMasukkan kolom/keterangan yang ingin di edit : ")
                    if(kolomUpdate == 'Initial'):
                        dataInitial = input("Masukkan Initial Baru : ")
                        update_data(b, kolomUpdate, dataInitial)
                    elif(kolomUpdate == 'Kode_Wilayah'):
                        dataKode = input("Masukkan Kode Wilayah Baru : ")
                        update_data(b, kolomUpdate, dataKode)
                    elif(kolomUpdate == 'Nama'):
                        dataNama = input("Masukkan Nama Baru : ")
                        update_data(b, kolomUpdate, dataNama)
                    elif(kolomUpdate == 'Kota'):
                        dataKota = input("Masukkan Kota Baru : ")
                        update_data(b, kolomUpdate, dataKota)
                    elif(kolomUpdate == 'Nomor_Telepon'):
                        dataNomor = input("Masukkan Nomor Telepon Baru : ")                     
                        update_data(b, kolomUpdate, dataNomor)
                    else:
                        print("\n--- Kolom Tidak Ada ---")
                elif(updateData == 'N'):
                    print("\n--- Data Tidak Terupdate ---")
        elif(pilihanSubMenu == '2'):
            break
        else:
            print("\n--- Pilihan yang anda masukkan salah ---")

def menu_4 ():
    while(1):
        print("\n===== Menghapus Data Kontak Telepon =====\n")
        for i in menu_hapus:
            print(i)
        pilihanSubMenu = input("\nSilahkan Pilih Sub Menu [1-2] : ")
        if(pilihanSubMenu == '1'):
            a = 0
            b = 0
            uniqueKode1 = input("\nMasukkan Initial Nama : ")
            uniqueKode2 = input("Masukkan Kode Wilayah : ")
            for j in range(len(kontakTelepon)):
                if(kontakTelepon[j]['Initial'] == uniqueKode1 and kontakTelepon[j]['Kode_Wilayah'] == uniqueKode2):
                    a = 1
                    b = j
            if(a == 0):
                print("\n--- Data Tidak Ada ---")
            elif(a == 1):
                while(1):
                    updateData = input("Apakah data akan dihapus (Y/N) : ")
                    if(updateData == 'Y' or updateData == 'N'):
                        break
                if(updateData == 'Y'):
                    del kontakTelepon[b]
                    print("Data Deleted")
                elif(updateData == 'N'):
                    print("Data Tidak Terhapus")
        elif(pilihanSubMenu == '2'):
            break
        else:
            print("\n--- Pilihan yang anda masukkan salah ---")

while(1):
    print("\n##### Yellow Pages - Data Kontak Telepon #####\n")
    for i in menu:
        print(i)
    pilihanMenu = input("\nSilahkan Pilih Menu [1-5] : ")

    if(pilihanMenu == '1'):
        menu_1()
    elif(pilihanMenu == '2'):
        menu_2()
    elif(pilihanMenu == '3'):
        menu_3()
    elif(pilihanMenu == '4'):
        menu_4()
    elif(pilihanMenu == '5'):
        break
    else:
        print("\n----- Pilihan yang anda masukkan salah -----")

print("\nTerima Kasih :) \n")