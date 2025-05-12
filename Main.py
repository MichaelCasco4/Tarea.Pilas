"""Una oficina de atención ciudadana en una alcaldía municipal en Nicaragua recibe documentos para 
revisión. Por cada solicitud, se apilan los documentos entregados en el orden en que llegan. El 
personal debe revisar el último documento entregado primero. Se debe simular el proceso de 
revisión, utilizando una pila, y permitir agregar nuevos documentos, eliminar el último revisado y 
mostrar los pendientes."""

from Pila import Pila
from Documento import Documento

def menu():
    opc = None
    pila = Pila()
    
    while opc != 5:
        
        print("-"*25)
        print("Alcaldia Municipal")
        print("1. Agregar Documento")
        print("2. Revisar Documento")
        print("3. Visualizar Documentos")
        print("4.Salir")
        print("-"*25)

        try:
            opc = int(input("Digite una opción:"))

            if opc < 1 or opc > 4:
                print("Numero invalido!")
                continue

        except ValueError:
            print("Su numero es invalido!")
            continue

        match opc:
            case 1:
                Nombre = input("Digite el nombre del documento que desea insertar:")
                cuerpo = input("Digite el cuerpo del documento:")
                documento = Documento(Nombre, cuerpo)
                pila.push(documento)
                print("\nDocumento añadido!")
            case 2:
                if pila.vacia() is False:
                    print("La pila esta vacia!")
                    continue
                else:
                    documentoEliminado = str(pila.pop())
                    print("Usted ha revisado el siguiente documento:" + " " + documentoEliminado)
            case 3:
                print("\nDocumentos")
                print("-"*25)
                pila.imprimir()
            case 4:
                print("Usted esta saliendo!")
                break
        
menu()