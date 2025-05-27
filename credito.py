deuda=100000
cupo=2000000
total=0
p_comprados=[]
while True:
    try:
        op=int(input(f"""¿Que operacion desea realizar?
                     1.Pagar deuda actual{deuda}
                     2.consultar cupo disponible
                     3.comprar algun otro producto
                     4.salir 
                     5.VER LISTADO DE PRODUCTOS QUE LLEVA
                     6.PAGAR"""))
        match op:
            case 1:
                try:
                    print(deuda)
                    p_deuda=int(input("cuanto desea pagar de su deuda actual"))
                    deuda=deuda-p_deuda
                    print("su deuda actual es",deuda)
                except Exception:
                    print("ingrese un valor valido")
            case 3:
                productos=int(input("""Los productos disponibles a comprar son 
                                    1.SMART TV SAMSUNG QLED 8K 90'$700.000
                                    2.PLAYSTATION 5 PRO MAX ULTRA $600.000
                                    3.SILLA GAMER CORSAIR $200.000
                                    4.NIKE AIR FORCE ONE DE ORO $1.000.000
                                    5.SALIR """))
                match productos:
                    case 1:
                        print("usted lleva una smart tv samsung qled 8k de 90 pulgadas")
                        cupo=cupo-700000
                        total=total+700000
                        p_comprados.append("smart tv")
                        print("su cupo restante es",cupo)
                    case 2:
                        print("usted lleva playstation 5 pro max ultra")
                        cupo=cupo-600000
                        total=total+600000
                        p_comprados.append("playstation 5 pro max ")
                        print("su cupo restante es",cupo)
                    case 3:
                        print("usted lleva silla gamer corsair")
                        cupo=cupo-200000
                        total=total+200000
                        p_comprados.append("silla corsair")
                        print("su cupo rastante es ",cupo)
                    case 4:
                        print("usted lleva air force one de oro")
                        cupo=cupo-1000000
                        total=total+1000000
                        p_comprados.append("air force one de oro")
                        print("su cupo deisponible es",cupo)   
                    case 5:
                        print("saliendo...")
                        break 
            case 2:
                print("su cupo disponible es",cupo)
            case 4:
                print("saliendo...")
                break
            case 5:
                for i in (p_comprados):
                    print(i)
            case 6:
                print(f"su total es{total}y su total con iva es{total*1.19}")
                print("su cupo restante sera de",cupo)
    except Exception:
        print("Ingrese un valor valido")