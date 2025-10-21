"""
Entidad Plantacion.

Representa una plantacion con cultivos y trabajadores.
"""

# Standard library
from typing import TYPE_CHECKING, List

# Local application
from python_forestacion.excepciones.mensajes_exception import (
    MSG_SUPERFICIE_INVALIDA,
    MSG_AGUA_INVALIDA
)

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.personal.trabajador import Trabajador


class Plantacion:
    """
    Plantacion agricola con cultivos y trabajadores.

    Contiene la lista de cultivos plantados y trabajadores asignados.
    """

    def __init__(self, nombre: str, superficie: float, agua: int):
        """
        Inicializa una plantacion.

        Args:
            nombre: Nombre identificatorio de la plantacion
            superficie: Superficie maxima en metros cuadrados
            agua: Agua disponible inicial en litros

        Raises:
            ValueError: Si superficie o agua son invalidas
        """
        if superficie <= 0:
            raise ValueError(MSG_SUPERFICIE_INVALIDA)
        if agua < 0:
            raise ValueError(MSG_AGUA_INVALIDA)

        self._nombre = nombre
        self._superficie = superficie
        self._agua_disponible = agua
        self._cultivos: List['Cultivo'] = []
        self._trabajadores: List['Trabajador'] = []
        self._superficie_ocupada = 0.0

    def get_nombre(self) -> str:
        """
        Obtiene el nombre de la plantacion.

        Returns:
            Nombre de la plantacion
        """
        return self._nombre

    def set_nombre(self, nombre: str) -> None:
        """
        Establece el nombre de la plantacion.

        Args:
            nombre: Nuevo nombre
        """
        self._nombre = nombre

    def get_superficie(self) -> float:
        """
        Obtiene la superficie maxima.

        Returns:
            Superficie en metros cuadrados
        """
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        """
        Establece la superficie maxima.

        Args:
            superficie: Nueva superficie

        Raises:
            ValueError: Si la superficie no es mayor a cero
        """
        if superficie <= 0:
            raise ValueError(MSG_SUPERFICIE_INVALIDA)
        self._superficie = superficie

    def get_agua_disponible(self) -> int:
        """
        Obtiene el agua disponible.

        Returns:
            Agua en litros
        """
        return self._agua_disponible

    def set_agua_disponible(self, agua: int) -> None:
        """
        Establece el agua disponible.

        Args:
            agua: Nueva cantidad de agua

        Raises:
            ValueError: Si el agua es negativa
        """
        if agua < 0:
            raise ValueError(MSG_AGUA_INVALIDA)
        self._agua_disponible = agua

    def get_cultivos(self) -> List['Cultivo']:
        """
        Obtiene la lista de cultivos (defensive copy).

        Returns:
            Copia de la lista de cultivos
        """
        return self._cultivos.copy()

    def set_cultivos(self, cultivos: List['Cultivo']) -> None:
        """
        Establece la lista de cultivos.

        Args:
            cultivos: Nueva lista de cultivos
        """
        self._cultivos = cultivos.copy()

    def agregar_cultivo(self, cultivo: 'Cultivo') -> None:
        """
        Agrega un cultivo a la plantacion.

        Args:
            cultivo: Cultivo a agregar
        """
        self._cultivos.append(cultivo)

    def eliminar_cultivo(self, cultivo: 'Cultivo') -> None:
        """
        Elimina un cultivo de la plantacion.

        Args:
            cultivo: Cultivo a eliminar
        """
        if cultivo in self._cultivos:
            self._cultivos.remove(cultivo)

    def get_trabajadores(self) -> List['Trabajador']:
        """
        Obtiene la lista de trabajadores (defensive copy).

        Returns:
            Copia de la lista de trabajadores
        """
        return self._trabajadores.copy()

    def set_trabajadores(self, trabajadores: List['Trabajador']) -> None:
        """
        Establece la lista de trabajadores.

        Args:
            trabajadores: Nueva lista de trabajadores
        """
        self._trabajadores = trabajadores.copy()

    def get_superficie_ocupada(self) -> float:
        """
        Obtiene la superficie ocupada por cultivos.

        Returns:
            Superficie ocupada en metros cuadrados
        """
        return self._superficie_ocupada

    def set_superficie_ocupada(self, superficie_ocupada: float) -> None:
        """
        Establece la superficie ocupada.

        Args:
            superficie_ocupada: Nueva superficie ocupada
        """
        self._superficie_ocupada = superficie_ocupada