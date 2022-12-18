# Contoh program yang dibuat raffi


while (True) :
    angka = int(input("Masukan Angka : "))
# Menggunakan except untuk membuat pemberitahuan program eror   
    try :
        hasil = 10/angka
        print(f"Hasil = {hasil}")
        is_done = input("lanjutkan program (y/n) ? ")
        if is_done == "n":
            break
# Jika memasukan angka 0, program tidak bisa membaca sehingga pemberitahuan dibawah akan muncul
    except:
        print("Pembagi nol, silakan masukan input lagi")
print("Akhiri dari program")
