pilihan = int(input("Masukan Pilihan : 1.Ganjil | 2.Genap : "))
awal = int(input("Masukan Nilai Awal : "))
akhir = int(input("Masukan Nilai Akhir : "))

if pilihan == 1:
    for x in range (awal,akhir):
        if x % 2 == 1:
            print(x)
else:
    for x in range (awal,akhir):
        if x % 2 == 0:
            print(x)

#Tampilkan bilangan ganjil, Genap

print("=================")
print("bilangan ganjil dan genap adalah")
print("ganjil,genap")

#perintah stack append

stack=[]
stack.append("ganjil")
stack.append("genap")

print("Tampilkan stack")
print(stack)