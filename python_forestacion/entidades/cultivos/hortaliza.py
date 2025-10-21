"""
Entidad base Hortaliza.

Clase base para cultivos horticolas (Lechuga, Zanahoria).
"""

# Standard library
from abc import ABC

# Local application
from python_forestacion.entidades.cultivos.cultivo import Cultivo


class Hortaliza(Cultivo, ABC):
    """
    Clase base abstracta para hortalizas.

    Las hortalizas pueden requerir o no invernadero.
    """

    def __init__(self, agua: int, superficie: float, invernadero: bool):
        """
        Inicializa una hortaliza con sus atributos.

        Args:
            agua: Cantidad inicial de agua en litros
            superficie: Superficie ocupada en metros cuadrados
            invernadero: True si requiere invernadero
        """
        super().__init__(agua, superficie)
        self._invernadero = invernadero

    def get_invernadero(self) -> bool:
        """
        Indica si la hortaliza esta en invernadero.

        Returns:
            True si esta en invernadero
        """
        return self._invernadero

    def set_invernadero(self, invernadero: bool) -> None:
        """
        Establece si la hortaliza esta en invernadero.

        Args:
            invernadero: True si esta en invernadero
        """
        self._invernadero = invernadero