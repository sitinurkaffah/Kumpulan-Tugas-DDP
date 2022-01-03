from Lingkaran import *
from PersegiPanjang import *
from SegitigaSiku2 import *

print("============= Siti Nur Kaffah =============")
print("=============== 0110221069 ================")
print("================== TI03 ===================")
print("============= Lingkaran 1 =============")

ling = Lingkaran(21)
keliling_ling = ling.keliling()
luas_ling = ling.luas()
jari_lingkaran = 21
print('Jari-Jari\t = ',jari_lingkaran)
print ('Keliling\t = ',int(keliling_ling))
print('Luas\t\t = ',int(luas_ling))

print("============= Lingkaran 2 =============")

ling2 = Lingkaran(14)
keliling_ling2 = ling2.keliling()
luas_ling2 = ling2.luas()
jari_lingkaran2 = 14
print('Jari-Jari\t = ',jari_lingkaran2)
print ('Keliling\t = ',int(keliling_ling2))
print('Luas\t\t = ',int(luas_ling2))

print("============= Persegi Panjang 1 =============")

pp = PersegiPanjang(3,4)
keliling_pp = pp.keliling()
luas_pp = pp.luas()
panjang_pp = 3
lebar_pp = 4
print('Panjang\t\t = ', panjang_pp)
print('Lebar\t\t = ', lebar_pp)
print ('Keliling\t = ',keliling_pp)
print('Luas\t\t = ',luas_pp)

print("============= Persegi Panjang 2 =============")

pp2 = PersegiPanjang(8,5)
keliling_pp2 = pp2.keliling()
luas_pp2 = pp2.luas()
panjang_pp2 = 8
lebar_pp2 = 5
print('Panjang\t\t = ', panjang_pp2)
print('Lebar\t\t = ', lebar_pp2)
print ('Keliling\t = ',keliling_pp2)
print('Luas\t\t = ',luas_pp2)

print("============= Segitiga Siku-Siku 1 =============")

sss = SegitigaSikuSiku(5,12,13)
keliling_sss = sss.keliling()
luas_sss = sss.luas()
alas_sss = 5
tinggi_sss = 12
miring_sss = 13
print('Alas\t\t = ', alas_sss)
print('Tinggi\t\t = ', tinggi_sss)
print ('Miring\t\t = ',miring_sss)
print('Keliling\t = ',keliling_sss)
print('Luas\t\t = ',luas_sss)

print("============= Segitiga Siku-Siku 2  =============")

sss2 = SegitigaSikuSiku(6,8,10)
keliling_sss2 = sss2.keliling()
luas_sss2 = sss2.luas()
alas_sss2 = 6
tinggi_sss2 = 8
miring_sss2 = 10
print('Alas\t\t = ', alas_sss2)
print('Tinggi\t\t = ', tinggi_sss2)
print ('Miring\t\t = ',miring_sss2)
print('Keliling\t = ',keliling_sss2)
print('Luas\t\t = ',luas_sss2)