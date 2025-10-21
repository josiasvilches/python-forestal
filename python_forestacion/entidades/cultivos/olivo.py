"""
Entidad Olivo.

Cultivo arboreo de tipo Olivo con tipo de aceituna.
"""

# Local application
from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
from python_forestacion.constantes import (
    AGUA_INICIAL_OLIVO,
    SUPERFICIE_OLIVO,
    ALTURA_INICIAL_ARBOL
)


class Olivo(Arbol):
    """
    Cultivo tipo Olivo.

    Arbol olivicola con tipo de aceituna especifico.
    """

    def __init__(self, tipo_aceituna: TipoAceituna):
        """
        Inicializa un Olivo con su tipo de aceituna.

        Args:
            tipo_aceituna: Tipo de aceituna del olivo
        """
        super().__init__(
            agua=AGUA_INICIAL_OLIVO,
            superficie=SUPERFICIE_OLIVO,
            altura=ALTURA_INICIAL_ARBOL
        )
        self._tipo_aceituna = tipo_aceituna

    def get_tipo_aceituna(self) -> TipoAceituna:
        """
        Obtiene el tipo de aceituna.

        Returns:
            Tipo de aceituna
        """
        return self._tipo_aceituna

    def set_tipo_aceituna(self, tipo_aceituna: TipoAceituna) -> None:
        """
        Establece el tipo de aceituna.

        Args:
            tipo_aceituna: Nuevo tipo de aceituna
        """
        self._tipo_aceituna = tipo_aceituna