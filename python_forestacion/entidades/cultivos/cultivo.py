"""
Entidad base Cultivo.

Interfaz base para todos los tipos de cultivos del sistema.
"""

# Standard library
from abc import ABC


class Cultivo(ABC):
    """
    Clase base abstracta para todos los cultivos.

    Define los atributos y comportamientos comunes a todos los cultivos.
    Esta es una entidad (DTO) que solo contiene datos, sin logica de negocio.
    """

    _contador_id = 0

    def __init__(self, agua: int, superficie: float):
        """
        Inicializa un cultivo con sus atributos basicos.

        Args:
            agua: Cantidad inicial de agua en litros
            superficie: Superficie ocupada en metros cuadrados
        """
        Cultivo._contador_id += 1
        self._id = Cultivo._contador_id
        self._agua = agua
        self._superficie = superficie

    def get_id(self) -> int:
        """
        Obtiene el ID unico del cultivo.

        Returns:
            ID del cultivo
        """
        return self._id

    def get_agua(self) -> int:
        """
        Obtiene la cantidad de agua almacenada.

        Returns:
            Agua en litros
        """
        return self._agua

    def set_agua(self, agua: int) -> None:
        """
        Establece la cantidad de agua almacenada.

        Args:
            agua: Nueva cantidad de agua en litros
        """
        self._agua = agua

    def get_superficie(self) -> float:
        """
        Obtiene la superficie ocupada por el cultivo.

        Returns:
            Superficie en metros cuadrados
        """
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        """
        Establece la superficie ocupada.

        Args:
            superficie: Nueva superficie en metros cuadrados
        """
        self._superficie = superficie