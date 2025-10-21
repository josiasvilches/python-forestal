"""
Entidad Zanahoria.

Cultivo horticola de tipo Zanahoria (regular o baby carrot).
"""

# Local application
from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import (
    AGUA_INICIAL_ZANAHORIA,
    SUPERFICIE_ZANAHORIA
)


class Zanahoria(Hortaliza):
    """
    Cultivo tipo Zanahoria.

    Hortaliza de raiz que puede ser regular o baby carrot.
    """

    def __init__(self, is_baby_carrot: bool):
        """
        Inicializa una Zanahoria.

        Args:
            is_baby_carrot: True si es baby carrot, False si es regular
        """
        super().__init__(
            agua=AGUA_INICIAL_ZANAHORIA,
            superficie=SUPERFICIE_ZANAHORIA,
            invernadero=False
        )
        self._is_baby_carrot = is_baby_carrot

    def is_baby_carrot(self) -> bool:
        """
        Indica si es baby carrot.

        Returns:
            True si es baby carrot, False si es regular
        """
        return self._is_baby_carrot

    def set_baby_carrot(self, is_baby_carrot: bool) -> None:
        """
        Establece si es baby carrot.

        Args:
            is_baby_carrot: True para baby carrot, False para regular
        """
        self._is_baby_carrot = is_baby_carrot