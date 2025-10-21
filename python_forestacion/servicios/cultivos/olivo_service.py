"""
Servicio para Olivo.

Logica de negocio especifica para cultivos de tipo Olivo.
"""

# Standard library
from typing import TYPE_CHECKING

# Local application
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_OLIVO

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.olivo import Olivo


class OlivoService(ArbolService):
    """
    Servicio para cultivos tipo Olivo.

    Implementa logica especifica de olivos (crecimiento lento, absorcion estacional).
    """

    def __init__(self):
        """
        Inicializa servicio con estrategia estacional.
        """
        super().__init__(AbsorcionSeasonalStrategy())

    def absorver_agua(self, olivo: 'Olivo') -> int:
        """
        Absorbe agua y hace crecer el olivo.

        Args:
            olivo: Olivo que absorbe agua

        Returns:
            Cantidad de agua absorbida
        """
        agua_absorvida = super().absorver_agua(olivo)
        
        # Olivo crece lentamente al recibir agua
        altura_actual = olivo.get_altura()
        olivo.set_altura(altura_actual + CRECIMIENTO_OLIVO)
        
        return agua_absorvida

    def mostrar_datos(self, olivo: 'Olivo') -> None:
        """
        Muestra datos del olivo incluyendo tipo de aceituna.

        Args:
            olivo: Olivo a mostrar
        """
        super().mostrar_datos(olivo)
        print(f"Tipo de aceituna: {olivo.get_tipo_aceituna().value}")