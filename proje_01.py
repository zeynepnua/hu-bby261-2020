cümle = "elbise çok güzel"
kelime = str(input("kelime giriniz: "))
arama = cümle.find(kelime)
if arama > -1 :
 print(arama," = indeks numarası ve cümle içinde var")
elif arama == -1 :
  print("cümle içinde yok")
