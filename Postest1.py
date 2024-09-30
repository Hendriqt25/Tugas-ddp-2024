while True:
 #username dan password yang digunakan untuk login
 nama_karyawan = "Hendrizaidan"
 nim_karyawan = "013"

 #input nama dan nim
 print("Masukan nama dan nim dengan benar !")
 nama = input("Masukkan nama anda : ")
 nim = input("Masukkan NIM anda : ")

#proses untuk login, apakah nama dan nim benar atau salah
 if nama == nama_karyawan and nim == nim_karyawan:
    print("Login berhasil!")
 else:
    print("Login gagal! Silakan coba lagi.")
    continue
 #saat sudah masuk maka akan ada output seperti ini
 print(f"Halo {nama}, Selamat datang diperusahaan selalu menyala!!")

 print("============================================")
#input jam kerja dan tarif kerja
 jam_kerja = float(input('Masukan jam kerja: '))
 tarif_kerja = float(input('Masukan tarif kerja: Rp. '))
#total gaji
 total_gaji = jam_kerja * tarif_kerja
 print("============================================")

 print("==================================================")
 if jam_kerja > 160:
    bonus = 0.1 * total_gaji
    total_gaji += bonus
    print(f"Bonus tambahan 10 % :{bonus}")
    print(f"Total gaji yang diserahkan: {total_gaji}")

 elif jam_kerja < 160:
    print(f"Total gaji yang di serahkan: Rp.{total_gaji}")
 print("==================================================")
    
 ulang = "ya"

 while(ulang == "ya"):
    ulang = input("Apakah anda menghitung gaji lagi (ya/tidak): ")
    if (ulang == "ya"):
        
        print("============================================")
        #input jam kerja dan tarif kerja
        jam_kerja = float(input("Masukan jam kerja: "))
        tarif_kerja = float(input("Masukan tarif : Rp. "))
        #total gaji
        total_gaji = jam_kerja * tarif_kerja
        print("============================================")

        if jam_kerja > 160:
            bonus = 0.1 * total_gaji
            total_gaji += bonus
            print(f"Bonus tambahan 10 % : {bonus}")
            print(f"Total gaji yang diserahkan: {total_gaji}")
        
        elif jam_kerja < 160:
            print(f"Total gaji yang di serahkan: {total_gaji}")
        print("==================================================")
        
    elif (ulang == "tidak"):
        print("Terima kasih atas kerja sama anda! ")
        break
       




