# Clase que representa la pila de donantes
class PilaDonantes:
    def __init__(self):
        self.pila = []  # Lista para almacenar los donantes
    
    def push(self, donante):
        # Agrega un nuevo donante al final de la pila
        self.pila.append(donante)
        print(f"Donante '{donante}' registrado.")

    def pop(self):
        # Elimina el último donante registrado (el tope de la pila)
        if self.pila:
            eliminado = self.pila.pop()
            print(f"Donante '{eliminado}' eliminado del registro.")
        else:
            print("No hay donantes en la pila para eliminar.")

    def mostrar_donante_actual(self):
        # Muestra el donante que está en proceso (último agregado)
        if self.pila:
            print(f"Donante actual en proceso: {self.pila[-1]}")
        else:
            print("No hay donantes en proceso.")