"""
Servicio para Pino.

Logica de negocio especifica para cultivos de tipo Pino.
"""

# Standard library
from typing import TYPE_CHECKING

# Local application
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_PINO

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.pino import Pino


class PinoService(ArbolService):
    """
    Servicio para cultivos tipo Pino.

    Implementa logica especifica de pinos (crecimiento, absorcion estacional).
    """

    def __init__(self):
        """
        Inicializa servicio con estrategia estacional.
        """
        super().__init__(AbsorcionSeasonalStrategy())

    def absorver_agua(self, pino: 'Pino') -> int:
        """
        Absorbe agua y hace crecer el pino.

        Args:
            pino: Pino que absorbe agua

        Returns:
            Cantidad de agua absorbida
        """
        agua_absorvida = super().absorver_agua(pino)
        
        # Pino crece al recibir agua
        altura_actual = pino.get_altura()
        pino.set_altura(altura_actual + CRECIMIENTO_PINO)
        
        return agua_absorvida

    def mostrar_datos(self, pino: 'Pino') -> None:
        """
        Muestra datos del pino incluyendo variedad.

        Args:
            pino: Pino a mostrar
        """
        super().mostrar_datos(pino)
        print(f"Variedad: {pino.get_variedad()}")