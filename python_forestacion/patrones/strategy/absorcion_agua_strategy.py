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