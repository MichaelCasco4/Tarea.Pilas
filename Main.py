"""En una panadería tradicional en León, los panes recién horneados se apilan en una bandeja. El 
primero que se vende es el último que se colocó. Simula el proceso de agregar panes a la bandeja 
(push), vender uno (pop), y visualizar qué tipo de pan está listo para vender (peek). """

from Pila import Pila
from Pan import Pan

def menu():
    opc = None
    pila = Pila()

    while opc != 5:
        print("="*25)
        print("1.Agregar panes")
        print("2.Vender pan")
        print("3.Pan listo")
        print("4.Salir")
        print("="*25)

        try:
            opc = int(input("Digite su opción:"))
        except ValueError:
            print("Su número es invalido!")

        match opc:
            case 1:
                tipoDePan = input("Digite el tipo de pan:")

                if tipoDePan:
                    pan = Pan(tipoDePan)

                    pila.push(pan)
                    print("Su pan" + " " +tipoDePan + " " + "ha sido añadido!")
                else:
                    print("Este campo no puede estar vacio")

                

            case 2:
                if pila.vacia() is False:
                    print("La pila esta vacia")
                else:
                    panVendido = str(pila.pop())
                    print("Usted ha vendido el siguiente pan:" + panVendido)

            case 3: 
                pan = pila.peek()


                if pan is False:
                    print("No hay panes!")
                    continue
                else:
                    pan = str(pan)
                    print(pan)
            
            case 4:
                print("Saliendo del programa")
                break

menu()
