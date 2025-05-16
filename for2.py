import time






palabra=input("ingrese una frase")
cont=0
vocales=0
cons=0
for i in palabra.lower():
    print(i)
    cont=cont+1
    print(cont,i)
   
    if i in "aeiou":
        vocales=vocales+1
    else:
        cons=cons+1
       
    print("los caracteres de la palabra son", cont)
    print("las vocales son"(vocales))
    print("las consonantes son"(cons))