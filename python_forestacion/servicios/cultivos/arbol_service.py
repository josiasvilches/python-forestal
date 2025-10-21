"""
Servicio base para arboles.

Contiene logica de negocio comun a todos los arboles.
"""

# Standard library
from abc import ABC
from typing import TYPE_CHECKING

# Local application
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.arbol import Arbol


class ArbolService(CultivoService, ABC):
    """
    Servicio base para arboles.

    Los arboles pueden crecer en altura al recibir agua.
    """

    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        """
        Inicializa el servicio de arbol.

        Args:
            estrategia_absorcion: Estrategia de absorcion de agua
        """
        super().__init__(estrategia_absorcion)

    def mostrar_datos(self, arbol: 'Arbol') -> None:
        """
        Muestra datos del arbol incluyendo altura.

        Args:
            arbol: Arbol a mostrar
        """
        super().mostrar_datos(arbol)
        print(f"ID: {arbol.get_id()}")
        print(f"Altura: {arbol.get_altura()} m")