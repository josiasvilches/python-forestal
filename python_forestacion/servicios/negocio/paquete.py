"""
Clase Paquete generica tipo-segura.

Representa un paquete de cultivos empaquetados.
"""

# Standard library
from typing import Generic, TypeVar, List

T = TypeVar('T')


class Paquete(Generic[T]):
    """
    Paquete generico tipo-seguro para empaquetar cultivos.

    Type Parameters:
        T: Tipo de cultivo contenido en el paquete
    """

    _contador_id = 0

    def __init__(self, tipo_contenido: type):
        """
        Inicializa un paquete vacio.

        Args:
            tipo_contenido: Clase del tipo de cultivo contenido
        """
        Paquete._contador_id += 1
        self._id_paquete = Paquete._contador_id
        self._tipo_contenido = tipo_contenido
        self._contenido: List[T] = []

    def agregar(self, item: T) -> None:
        """
        Agrega un item al paquete.

        Args:
            item: Item a agregar
        """
        self._contenido.append(item)

    def get_contenido(self) -> List[T]:
        """
        Obtiene el contenido del paquete.

        Returns:
            Lista de items contenidos
        """
        return self._contenido.copy()

    def get_cantidad(self) -> int:
        """
        Obtiene la cantidad de items.

        Returns:
            Cantidad de items en el paquete
        """
        return len(self._contenido)

    def get_tipo_contenido(self) -> type:
        """
        Obtiene el tipo de contenido.

        Returns:
            Clase del tipo contenido
        """
        return self._tipo_contenido

    def get_id_paquete(self) -> int:
        """
        Obtiene el ID del paquete.

        Returns:
            ID unico del paquete
        """
        return self._id_paquete

    def mostrar_contenido_caja(self) -> None:
        """
        Muestra el contenido del paquete.
        """
        print("\nContenido de la caja:")
        print(f"  Tipo: {self._tipo_contenido.__name__}")
        print(f"  Cantidad: {self.get_cantidad()}")
        print(f"  ID Paquete: {self._id_paquete}")