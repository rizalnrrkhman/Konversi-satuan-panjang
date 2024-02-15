print ("Aplikasi Konversi Satuan Panjang")
print ("================================")
print ("Menu Pilihan Satuan Panjang")
print ("1. Km")
print ("2. Hm")
print ("3. Dam")
print ("4. M")
print ("5. Dm")
print ("6. Cm")
print ("7. Mm")
print ('\n')

satuan = input ("Pilihlah Satuan Konversinya : ")
if satuan == "Km":
  km = float(input("Masukan Nilai Kmnya : "))
  hasilhm  = 10 * km
  hasildam = 100 * km
  hasilm   = 1000 * km
  hasildm  = 10000 * km
  hasilcm  = 100000 * km
  hasilmm  = 1000000 * km

  print ("Hasilnya Sebaga Berikut")
  print (f"Hm   = {hasilhm}")
  print (f"Dam  = {hasildam}")
  print (f"M    = {hasilm}")
  print (f"Dm   = {hasildm}")
  print (f"Cm   = {hasilcm}")
  print (f"Mm   = {hasilmm}")

  print ('\n')
  print ("Semoga Membantu Terimakasih")

elif satuan == "Hm":
  hm = float (input("Masukan Nilai Hmnya : "))
  hasilkm1   = hm / 10
  hasildam1  = hm * 10
  hasilm1    = hm * 100
  hasildm1   = hm * 1000
  hasilcm1   = hm * 10000
  hasilmm1   = hm * 100000

  print ("Hasilnya Sebaga Berikut")
  print (f"Km   = {hasilkm1}")
  print (f"Dam  = {hasildam1}")
  print (f"M    = {hasilm1}")
  print (f"Dm   = {hasildm1}")
  print (f"Cm   = {hasilcm1}")
  print (f"Mm   = {hasilmm1}")

  print ('\n')
  print ("Semoga Membantu Terimakasih")

elif satuan == "Dam":
  Dam = float (input("Masukan Nilai Damnya : "))
  hasilkm2   = Dam / 100
  hasilhm2   = Dam / 10
  hasilm2    = Dam * 10
  hasildm2   = Dam * 100
  hasilcm2   = Dam * 1000
  hasilmm2   = Dam * 10000

  print ("Hasilnya Sebaga Berikut")
  print (f"Km   = {hasilkm2}")
  print (f"Hm   = {hasilhm2}")
  print (f"M    = {hasilm2}")
  print (f"Dm   = {hasildm2}")
  print (f"Cm   = {hasilcm2}")
  print (f"Mm   = {hasilmm2}")

  print ('\n')
  print ("Semoga Membantu Terimakasih")

elif satuan == "M":
  m = float (input("Masukan Nilai Mnya : "))
  hasilkm3   = m / 1000
  hasilhm3   = m / 100
  hasildam3  = m / 10
  hasilcm3   = m * 100
  hasildm3   = m * 10
  hasilmm3   = m * 1000

  print ("Hasilnya Sebaga Berikut")
  print (f"Km   = {hasilkm3}")
  print (f"Hm   = {hasilhm3}")
  print (f"M    = {hasilm2}")
  print (f"Dm   = {hasildm2}")
  print (f"Cm   = {hasilcm2}")
  print (f"Mm   = {hasilmm2}")

  print ('\n')
  print ("Semoga Membantu Terimakasih")

elif satuan == "Dm":
  dm = float (input("Masukan Nilai Dmnya : "))
  hasilkm4   = dm / 10000
  hasilhm4   = dm / 1000
  hasildam4  = dm / 100
  hasilm4    = dm / 10
  hasilcm4   = dm * 10
  hasilmm4   = dm * 100

  print ("Hasilnya Sebaga Berikut")
  print (f"Km   = {hasilkm4}")
  print (f"Hm   = {hasilhm4}")
  print (f"Dam  = {hasildam4}")
  print (f"M    = {hasilm4}")
  print (f"Cm   = {hasilcm4}")
  print (f"Mm   = {hasilmm4}")

  print ('\n')
  print ("Semoga Membantu Terimakasih")

elif satuan == "Cm":
  cm = float (input("Masukan Nilai Cmnya : "))
  hasilkm5   = cm / 100000
  hasilhm5   = cm / 10000
  hasildam5  = cm / 1000
  hasilm5    = cm / 100
  hasildm5   = cm / 10
  hasilmm5   = cm * 10

  print ("Hasilnya Sebagai Berikut")
  print (f"Km   = {hasilkm5}")
  print (f"Hm   = {hasildm5}")
  print (f"Dam  = {hasildam5}")
  print (f"M    = {hasilm5}")
  print (f"Dm   = {hasildm5}")
  print (f"Mm   = {hasilmm5}")

  print ('\n')
  print ("Semoga Membantu Terimakasih")

elif satuan == "Mm":
  mm = float (input("Masukan Nilai Mmnya : "))
  hasilkm6   = mm / 1000000
  hasilhm6   = mm / 100000
  hasildam6  = mm / 10000
  hasilm6    = mm / 1000
  hasildm6   = mm / 100
  hasilcm6   = mm / 10

  print ("Hasilnya Sebagai Berikut")
  print (f"Km   = {hasilkm6}")
  print (f"Hm   = {hasilhm6}")
  print (f"Dam  = {hasildam6}")
  print (f"M    = {hasilm6}")
  print (f"Dm   = {hasildm6}")
  print (f"Cm   = {hasilcm6}")

  print ('\n')
  print ("Semoga Membantu Terimakasih")

else:
  print ("Coba Lagi")