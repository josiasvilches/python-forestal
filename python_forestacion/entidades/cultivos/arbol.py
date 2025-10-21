"""
Entidad base Arbol.

Clase base para cultivos arboreos (Pino, Olivo).
"""

# Standard library
from abc import ABC

# Local application
from python_forestacion.entidades.cultivos.cultivo import Cultivo


class Arbol(Cultivo, ABC):
    """
    Clase base abstracta para arboles.

    Los arboles tienen altura adicional a los atributos de cultivo.
    """

    def __init__(self, agua: int, superficie: float, altura: float):
        """
        Inicializa un arbol con sus atributos.

        Args:
            agua: Cantidad inicial de agua en litros
            superficie: Superficie ocupada en metros cuadrados
            altura: Altura del arbol en metros
        """
        super().__init__(agua, superficie)
        self._altura = altura

    def get_altura(self) -> float:
        """
        Obtiene la altura del arbol.

        Returns:
            Altura en metros
        """
        return self._altura

    def set_altura(self, altura: float) -> None:
        """
        Establece la altura del arbol.

        Args:
            altura: Nueva altura en metros
        """
        self._altura = altura