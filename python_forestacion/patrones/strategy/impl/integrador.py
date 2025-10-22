"""
Archivo integrador generado automaticamente
Directorio: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/patrones/strategy/impl
Fecha: 2025-10-22 09:43:42
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/patrones/strategy/impl/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: absorcion_constante_strategy.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/patrones/strategy/impl/absorcion_constante_strategy.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/3: absorcion_seasonal_strategy.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/patrones/strategy/impl/absorcion_seasonal_strategy.py
# ================================================================================

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

