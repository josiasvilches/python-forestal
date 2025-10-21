"""
Estrategia de absorcion constante para hortalizas.

Las hortalizas absorben siempre la misma cantidad de agua.
"""

# Standard library
from datetime import date
from typing import TYPE_CHECKING

# Local application
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """
    Estrategia de absorcion constante.

    Hortalizas absorben siempre la misma cantidad independientemente
    de la estacion o condiciones ambientales.
    """

    def __init__(self, cantidad_constante: int):
        """
        Inicializa estrategia con cantidad fija.

        Args:
            cantidad_constante: Litros a absorber siempre
        """
        self._cantidad_constante = cantidad_constante

    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        """
        Retorna siempre la misma cantidad de agua.

        Args:
            fecha: No utilizada en esta estrategia
            temperatura: No utilizada en esta estrategia
            humedad: No utilizada en esta estrategia
            cultivo: No utilizado en esta estrategia

        Returns:
            Cantidad constante configurada
        """
        return self._cantidad_constante