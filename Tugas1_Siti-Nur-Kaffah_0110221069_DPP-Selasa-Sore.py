print("-------------UTS SOAL NO. 1 DDP SITI NUR KAFFAH TI03-------------")
pegawai = [
#[Nama, Agama , Gaji pokok, Jumlah Anak]    
['Ahmad', 'Islam', 4000000, 2],
['ALex', 'Kristen Protestan', 6000000, 5],
]

for i in pegawai:
    nama = i[0]
    agama = i[1]
    gaji_pokok = i[2]
    jumlah_anak = i[3]
    tunjangan_jabatan = gaji_pokok * (20/100)
    tunjangan_keluarga = None
    if jumlah_anak > 0 and jumlah_anak <= 2:
        tunjangan_keluarga = gaji_pokok * (10/100)
    elif jumlah_anak > 2:
        tunjangan_keluarga = gaji_pokok * (20/100)
    else:
        tunjangan_keluarga = 0
    gaji_kotor = gaji_pokok + tunjangan_jabatan + tunjangan_keluarga
#tuple&list
    zakat_profesi = (0, 0.025)[agama == 'Islam' and gaji_kotor >= 6000000] * gaji_kotor
    gaji_bersih = gaji_kotor - zakat_profesi
    print("SLIP GAJI PT. XYZ")
    print("------------------")
    print("Nama Pegawai \t \t :", nama)
    print("Agama \t \t \t :", agama)
    print("Jumlah Anak \t \t :", jumlah_anak)
    print("Gaji Pokok \t \t : Rp.", gaji_pokok)
    print("Tunjangan Jabatan \t : Rp.", tunjangan_jabatan)
    print("Tunjangan Keluarga \t : Rp.", tunjangan_keluarga)
    print("Gaji Kotor \t \t : Rp.", gaji_kotor)
    print("Zakat Profesi \t \t : Rp.", zakat_profesi)
    print("Take Home Pay \t \t : Rp.", gaji_bersih)