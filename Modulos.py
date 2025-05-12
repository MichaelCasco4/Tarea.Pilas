class Tarea:
    #Representa la tarea que es entregada por un estudiante 
    def __init__(self, descripcion):
        self.descripcion = descripcion

    def __str__(self):
        return self.descripcion
    
class PilaTareas:
    #Implementa una pila de tareas usando una lista interna 
    def __init__(self):
        self.pila = []

    def push(self, tarea):
        #Agrega una nueva tarea a la pila 
        self.pila.append(tarea)
        print(f"Tarea {tarea} agregada correctamente. \n")

    def pop(self):
        #Elimina y muestra la ultima tarea entregada 
        if not self.esta_vacia():
            tarea = self.pila.pop()
            print(f"Tarea {tarea} revisada. \n")
            return tarea
        #Si no hay ninguna, mensaje de advertencia 
        else:
            print("No hay ninguna tarea por revisar. \n")
            return None
        
    def peek(self):
        #Muestra la ultima tarea agregada sin eliminarla
        if not self.esta_vacia():
            tarea = self.pila[-1]
            print(f"Siguiente tarea a revisar es: {tarea}. \n")
            return tarea
        
        else:
            print("No hay tareas para revisar. \n")
            return None
    #Verifica si la ultima pila esta vacia  
    def esta_vacia(self):
        return len(self.pila) == 0
    


        
