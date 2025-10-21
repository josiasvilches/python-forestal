"""
Excepcion para agua agotada en plantacion.
"""

# Local application
from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import (
    MSG_AGUA_AGOTADA_USER,
    MSG_AGUA_AGOTADA_TECH
)


class AguaAgotadaException(ForestacionException):
    """
    Excepcion lanzada cuando no hay suficiente agua para regar.

    Args:
        agua_requerida: Agua necesaria en litros
        agua_disponible: Agua disponible en litros
    """

    def __init__(self, agua_requerida: int, agua_disponible: int):
        """
        Inicializa la excepcion con detalles de agua.

        Args:
            agua_requerida: Agua que se necesita
            agua_disponible: Agua que hay disponible
        """
        self._agua_requerida = agua_requerida
        self._agua_disponible = agua_disponible

        user_msg = MSG_AGUA_AGOTADA_USER
        tech_msg = MSG_AGUA_AGOTADA_TECH.format(
            requerida=agua_requerida,
            disponible=agua_disponible
        )

        super().__init__(user_msg, tech_msg)

    def get_agua_requerida(self) -> int:
        """
        Obtiene el agua requerida.

        Returns:
            Agua requerida en litros
        """
        return self._agua_requerida

    def get_agua_disponible(self) -> int:
        """
        Obtiene el agua disponible.

        Returns:
            Agua disponible en litros
        """
        return self._agua_disponible