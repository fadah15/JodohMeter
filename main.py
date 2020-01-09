import random #ramdomangka#

print ("Selamat datang di aplikasi Jodoh Meter")
loop = True
loopmaster = True

while loopmaster:
  print("")
  print ("Pilih Menu :")
  menu = input ("1. Kalkulator Cinta 2. Hitung Weton (1/2) : ")
  print("")
  if menu == "1" :
    while loop:
      print("")
      pria = input("Masukkan nama Pria : ")
      wanita= input("Masukkan nama Wanita : ")

      print ("==================================")
      print ("Nama Pria : ", pria)
      print ("Nama Wanita :", wanita )

      confirm = input ("Apakah nama yang dimasukkan sudah benar? y/n : ")

      if confirm == "y" :
        loop = False

    match = random.randrange(0,100)

    print("")
    print("MATCH METER", match,"%")
    print("")

    if match > 80 :
      print ("Ndang Rabi")
    else :
      if match > 60 :
        print ("Pikir-Pikir")
      else : 
          if match > 40 :
            print ("Yaaakinn...!")
          else :
              if match > 20 :
                print ("cari lagi")
              else :
                print ("putus aja")
  else :
    print ("Silahkan Hitung Weton Anda dan Pasangan")
    print ("")
    print("Hari :")
    print ("Minggu: 5,", "Senin: 4,", "Selasa: 3,", "Rabu: 7,", "Kamis: 8,", "Jumat: 6,", "Sabtu: 9")
    print ("")
    print("Pasaran :")
    print("Legi: 5,", "Pahing: 9,", "Pon: 7,", "Wage: 4,", "Kliwon: 8 ")


    print("==========================")
    a = input ("Hari laki-laki : ")
    b = input ("Pasaran laki-laki :")
    c = input ("Hari perempuan :")
    d = input ("Pasaran perempuan :")

    jumlah = int(a) + int(b) + int(c) + int(d)
    print ("Jumlah : ",jumlah)

    loop3 = True
    pembagi=10
    print("")
    print("Ramalan Weton :")
    while loop3:

      hasil = jumlah%pembagi

      if hasil == 1 :
        print ("Wasesa Segara")
        loop3 = False
      elif hasil == 2 :
        print ("Tunggak Semi")
        loop3 = False
      elif hasil == 3 :
        print ("Satria Wibawa")
        loop3 = False
      elif hasil == 4 :
        print ("Sumur Sinaba")
        loop3 = False
      elif hasil == 5 :
        print ("Satria Wirang")
        loop3 = False
      elif hasil == 6 :
        print ("Bumi Kepetak")
        loop3 = False
      elif hasil == 7 :
        print ("Lebu Ketiup Angin")
        loop3 = False
      else :
        pembagi = 7


  print ("")
  lagi = input ("Mau mencoba lagi ? (y/n) : ")
  if lagi == 'n' :
    loopmaster = False
  else :
    loop = True
    
