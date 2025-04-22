#USO DEL FOR
# num=int(input("ingrese un numero"))
# for i in range(num):
#     print(i)
# num=int(input("ingrese un numero"))
# for i in range(10):
#     print(num,"x",i+1,"="(i+1)*num)
 

cant=int(input("ingrese un numero de nptas"))
suma=0
for i in range(cant):
    print("INGRESE LA NOTA",i+1)
    nota=float(input())
    suma=suma+nota
prom=suma/cant
print("el promedio es",round (prom))
if prom>=4:
    print("aprobo")
else:
    print("Reprobo")