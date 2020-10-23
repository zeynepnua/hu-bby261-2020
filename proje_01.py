import string
cümle = "Elbise çok güzel değil mi ? "
yenicümle = ""
for i in cümle :
  if i not in string.punctuation:
    yenicümle += i
print(yenicümle)
kelime = str(input("kelime giriniz: "))
arama = yenicümle.find(kelime)
if arama > -1 :
 print(arama," = indeks numarası ve cümle içinde var")
elif arama == -1 :
  print("cümle içinde yok")
