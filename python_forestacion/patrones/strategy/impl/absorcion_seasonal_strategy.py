"""
Estrategia de absorcion estacional para arboles.

Los arboles absorben mas agua en verano que en invierno.
"""

# Standard library
from datetime import date
from typing import TYPE_CHECKING

# Local application
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.constantes import (
    ABSORCION_SEASONAL_VERANO,
    ABSORCION_SEASONAL_INVIERNO,
    MES_INICIO_VERANO,
    MES_FIN_VERANO
)

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """
    Estrategia de absorcion estacional.

    Arboles absorben:
    - Verano (marzo-agosto): 5 litros
    - Invierno (sept-feb): 2 litros
    """

    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        """
        Calcula absorcion basada en la estacion del anio.

        Args:
            fecha: Fecha actual para determinar estacion
            temperatura: No utilizada en esta estrategia
            humedad: No utilizada en esta estrategia
            cultivo: Cultivo que absorbe

        Returns:
            5 litros en verano, 2 litros en invierno
        """
        mes = fecha.month

        if MES_INICIO_VERANO <= mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO
        else:
            return ABSORCION_SEASONAL_INVIERNO