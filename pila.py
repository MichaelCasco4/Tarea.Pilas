# pila.py

class Pila:
    def __init__(self):
        self._sacos = []

    def apilar(self, saco):
        """Agrega un saco encima de la pila (push)."""
        self._sacos.append(saco)

    def descargar(self):
        """Elimina y retorna el saco que está encima (pop)."""
        if self.esta_vacia():
            return None
        return self._sacos.pop()

    def ver_tope(self):
        """Retorna el saco que está encima sin quitarlo (peek)."""
        if self.esta_vacia():
            return None
        return self._sacos[-1]

    def esta_vacia(self):
        """Indica si la pila está vacía."""
        return len(self._sacos) == 0
