"""
Servicio para Lechuga.

Logica de negocio especifica para cultivos de tipo Lechuga.
"""

# Standard library
from typing import TYPE_CHECKING

# Local application
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_LECHUGA

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.lechuga import Lechuga


class LechugaService(CultivoService):
    """
    Servicio para cultivos tipo Lechuga.

    Implementa logica especifica de lechugas (absorcion constante).
    """

    def __init__(self):
        """
        Inicializa servicio con estrategia constante.
        """
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_LECHUGA))

    def mostrar_datos(self, lechuga: 'Lechuga') -> None:
        """
        Muestra datos de la lechuga incluyendo variedad e invernadero.

        Args:
            lechuga: Lechuga a mostrar
        """
        super().mostrar_datos(lechuga)
        print(f"Variedad: {lechuga.get_variedad()}")
        print(f"Invernadero: {lechuga.get_invernadero()}")