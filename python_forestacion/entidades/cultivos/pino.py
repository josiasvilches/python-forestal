"""
Entidad Pino.

Cultivo arboreo de tipo Pino con variedad especifica.
"""

# Local application
from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import (
    AGUA_INICIAL_PINO,
    SUPERFICIE_PINO,
    ALTURA_INICIAL_ARBOL
)


class Pino(Arbol):
    """
    Cultivo tipo Pino.

    Arbol maderable con diferentes variedades posibles.
    """

    def __init__(self, variedad: str):
        """
        Inicializa un Pino con su variedad.

        Args:
            variedad: Variedad de pino (Parana, Elliott, Taeda, etc.)
        """
        super().__init__(
            agua=AGUA_INICIAL_PINO,
            superficie=SUPERFICIE_PINO,
            altura=ALTURA_INICIAL_ARBOL
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        """
        Obtiene la variedad del pino.

        Returns:
            Variedad del pino
        """
        return self._variedad

    def set_variedad(self, variedad: str) -> None:
        """
        Establece la variedad del pino.

        Args:
            variedad: Nueva variedad
        """
        self._variedad = variedad