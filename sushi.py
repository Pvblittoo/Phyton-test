total=0
pikachu=0
otaku=0
pulpo=0
anguila=0
descuento=0.9
ts=int(input("cuanto sushi desea llevar "))

for i in range (ts):
    print("que tipo de sushi desea llevar 1.pikachu roll 4500 2.otaku roll 5000 3. pulpo venenoso roll 5200 4.anguila electrica roll 4800")
    op=int(input())
    if op ==1:
        print("Usted lleva pikachu roll")
        total=total+4500
        pikachu=pikachu+1
    if op==2 :
        print("usted lleva otaku roll")
        total=total+5000
        otaku=otaku+1
    if op==3:
        print("usted lleva pulpo venenoso roll")
        total=total+5200
        pulpo=pulpo+1
    if op==4 :
        print ("usted lleva anguila electrica roll")
        total=total+4800
        anguila=anguila+1

ds=int(input("tiene desuento? 1.si 2.no"))
if ds==1:
    print("ingrese su codigo de descuento")
    dcto=str(input())
    while dcto !="soy otaku":
        print("descuento erroneo")
        print("ingrese su codigo de descuento")
        dcto=str(input())
        if dcto=="x":
            break
    if dcto=="soy otaku":
        total=total*descuento
        print("su descuento ha sido aplicado")       
else:
    print
      


    



boleta=total*1.19
print("su total mas iva es ",boleta)

