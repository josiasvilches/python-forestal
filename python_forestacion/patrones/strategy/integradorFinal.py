"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion/patrones/strategy
Fecha de generacion: 2025-10-21 18:29:27
Total de archivos integrados: 5
Total de directorios procesados: 2
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. __init__.py
#   2. absorcion_agua_strategy.py
#
# DIRECTORIO: impl
#   3. __init__.py
#   4. absorcion_constante_strategy.py
#   5. absorcion_seasonal_strategy.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/5: __init__.py
# Directorio: .
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion/patrones/strategy\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 2/5: absorcion_agua_strategy.py
# Directorio: .
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion/patrones/strategy\absorcion_agua_strategy.py
# ==============================================================================

"""
Patron Strategy - Interfaz para estrategias de absorcion de agua.

Define el contrato que deben cumplir todas las estrategias de absorcion.
"""

# Standard library
from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionAguaStrategy(ABC):
    """
    Interfaz Strategy para algoritmos de absorcion de agua.

    Permite implementar diferentes estrategias de absorcion segun
    el tipo de cultivo (estacional, constante, etc.).
    """

    @abstractmethod
    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        """
        Calcula la cantidad de agua que absorbe un cultivo.

        Args:
            fecha: Fecha actual para determinar estacion
            temperatura: Temperatura ambiental en grados Celsius
            humedad: Humedad ambiental en porcentaje
            cultivo: Cultivo que absorbe agua

        Returns:
            Cantidad de agua absorbida en litros
        """
        pass


################################################################################
# DIRECTORIO: impl
################################################################################

# ==============================================================================
# ARCHIVO 3/5: __init__.py
# Directorio: impl
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion/patrones/strategy\impl\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 4/5: absorcion_constante_strategy.py
# Directorio: impl
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion/patrones/strategy\impl\absorcion_constante_strategy.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 5/5: absorcion_seasonal_strategy.py
# Directorio: impl
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion/patrones/strategy\impl\absorcion_seasonal_strategy.py
# ==============================================================================

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


################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 5
# Generado: 2025-10-21 18:29:27
################################################################################
