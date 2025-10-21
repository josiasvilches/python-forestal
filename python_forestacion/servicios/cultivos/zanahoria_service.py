"""
Servicio para Zanahoria.

Logica de negocio especifica para cultivos de tipo Zanahoria.
"""

# Standard library
from typing import TYPE_CHECKING

# Local application
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_ZANAHORIA

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria


class ZanahoriaService(CultivoService):
    """
    Servicio para cultivos tipo Zanahoria.

    Implementa logica especifica de zanahorias (absorcion constante).
    """

    def __init__(self):
        """
        Inicializa servicio con estrategia constante.
        """
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_ZANAHORIA))

    def mostrar_datos(self, zanahoria: 'Zanahoria') -> None:
        """
        Muestra datos de la zanahoria incluyendo si es baby carrot.

        Args:
            zanahoria: Zanahoria a mostrar
        """
        super().mostrar_datos(zanahoria)
        tipo = "Baby carrot" if zanahoria.is_baby_carrot() else "Regular"
        print(f"Tipo: {tipo}")