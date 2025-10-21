"""
Excepcion para superficie insuficiente en plantacion.
"""

# Standard library
from typing import TYPE_CHECKING

# Local application
from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import (
    MSG_SUPERFICIE_INSUFICIENTE_USER,
    MSG_SUPERFICIE_INSUFICIENTE_TECH
)


class SuperficieInsuficienteException(ForestacionException):
    """
    Excepcion lanzada cuando no hay suficiente superficie para plantar.

    Args:
        superficie_requerida: Superficie necesaria en m2
        superficie_disponible: Superficie disponible en m2
    """

    def __init__(self, superficie_requerida: float, superficie_disponible: float):
        """
        Inicializa la excepcion con detalles de superficie.

        Args:
            superficie_requerida: Superficie que se necesita
            superficie_disponible: Superficie que hay disponible
        """
        self._superficie_requerida = superficie_requerida
        self._superficie_disponible = superficie_disponible

        user_msg = MSG_SUPERFICIE_INSUFICIENTE_USER
        tech_msg = MSG_SUPERFICIE_INSUFICIENTE_TECH.format(
            requerida=superficie_requerida,
            disponible=superficie_disponible
        )

        super().__init__(user_msg, tech_msg)

    def get_superficie_requerida(self) -> float:
        """
        Obtiene la superficie requerida.

        Returns:
            Superficie requerida en m2
        """
        return self._superficie_requerida

    def get_superficie_disponible(self) -> float:
        """
        Obtiene la superficie disponible.

        Returns:
            Superficie disponible en m2
        """
        return self._superficie_disponible