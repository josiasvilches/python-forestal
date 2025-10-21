"""
Entidad Lechuga.

Cultivo horticola de tipo Lechuga con variedad especifica.
"""

# Local application
from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import (
    AGUA_INICIAL_LECHUGA,
    SUPERFICIE_LECHUGA
)


class Lechuga(Hortaliza):
    """
    Cultivo tipo Lechuga.

    Hortaliza de hoja verde que requiere invernadero.
    """

    def __init__(self, variedad: str):
        """
        Inicializa una Lechuga con su variedad.

        Args:
            variedad: Variedad de lechuga (Crespa, Mantecosa, Morada, etc.)
        """
        super().__init__(
            agua=AGUA_INICIAL_LECHUGA,
            superficie=SUPERFICIE_LECHUGA,
            invernadero=True
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        """
        Obtiene la variedad de la lechuga.

        Returns:
            Variedad de la lechuga
        """
        return self._variedad

    def set_variedad(self, variedad: str) -> None:
        """
        Establece la variedad de la lechuga.

        Args:
            variedad: Nueva variedad
        """
        self._variedad = variedad