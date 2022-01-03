print("-------UTS SOAL NO. 2 DDP SITI NUR KAFFAH TI03-------")
print("------------------Seven Electronic-------------------")
print("--------RUKO TOL BOULEVARD JL.PELAYANGAN NO.18-------")
print("---------------TANGERANG SELATAN, BANTEN-------------")
print("-----------------------15310-------------------------")
print("============================================================")
Nama_Pelanggan = str(input("Masukkan Nama Pelanggan\t: "))
Produk_Pilihan = input("Produk Pilihan\t\t: ")

if (Produk_Pilihan == "Kipas Angin"):
    harga = 1000000
    print("Harga Produk\t\t: %i" % (harga))

elif (Produk_Pilihan == "TV"):
    harga = 2000000
    print("Harga Produk\t\t: %i" % (harga))

elif (Produk_Pilihan == "Mesin Cuci"):
    harga = 3000000
    print("Harga Produk\t\t: %i" % (harga))

elif (Produk_Pilihan == "AC"):
    harga = 4000000
    print("Harga Produk\t\t: %i" % (harga))

else:
    (Produk_Pilihan == "Kulkas")
    harga = 5000000
    print("Harga Produk\t\t: %i" % (harga))

Jumlah_Beli = int(input("Jumlah Beli\t\t: "))

print("-----------------------------------------------------")

Harga_Kotor = harga * Jumlah_Beli
print("Harga Kotor\t\t: %i" % (Harga_Kotor))

if (Produk_Pilihan == "Kulkas" and Jumlah_Beli >= 5):
    Diskon = 0.20 * Harga_Kotor
elif (Produk_Pilihan == "AC" and Jumlah_Beli >= 3):
    Diskon = 0.10 * Harga_Kotor
else:
    Diskon = 0.05 * Harga_Kotor
print("Diskon\t\t\t: %i" % (Diskon))   

PPN = ((Harga_Kotor - Diskon) * 0.10)
print("PPN\t\t\t: %i" % (PPN))

Harga_Bersih = ((Harga_Kotor - Diskon) + PPN)
print("Harga Bersih\t\t: %i" % (Harga_Bersih))

print("============================================================")
print("--------------TERIMA KASIH TELAH BERBELANJA----------")
print("-----------------SILAHKAN DATANG KEMBALI-------------")
