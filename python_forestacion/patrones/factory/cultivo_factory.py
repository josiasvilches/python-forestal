"""
Patron Factory Method - Fabrica de cultivos.

Centraliza la creacion de cultivos sin exponer clases concretas al cliente.
"""

# Standard library
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoFactory:
    """
    Factory Method para crear cultivos.

    Encapsula la logica de creacion de diferentes tipos de cultivos,
    permitiendo al cliente crear cultivos sin conocer sus clases concretas.
    """

    @staticmethod
    def crear_cultivo(especie: str) -> 'Cultivo':
        """
        Crea un cultivo del tipo especificado.

        Args:
            especie: Nombre de la especie a crear

        Returns:
            Instancia de Cultivo del tipo solicitado

        Raises:
            ValueError: Si la especie es desconocida
        """
        factories = {
            "Pino": CultivoFactory._crear_pino,
            "Olivo": CultivoFactory._crear_olivo,
            "Lechuga": CultivoFactory._crear_lechuga,
            "Zanahoria": CultivoFactory._crear_zanahoria
        }

        if especie not in factories:
            raise ValueError(f"Especie desconocida: {especie}")

        return factories[especie]()

    @staticmethod
    def _crear_pino() -> 'Cultivo':
        """
        Crea una instancia de Pino.

        Returns:
            Pino con variedad por defecto
        """
        from python_forestacion.entidades.cultivos.pino import Pino
        from python_forestacion.constantes import VARIEDAD_PINO_DEFAULT
        return Pino(variedad=VARIEDAD_PINO_DEFAULT)

    @staticmethod
    def _crear_olivo() -> 'Cultivo':
        """
        Crea una instancia de Olivo.

        Returns:
            Olivo con tipo de aceituna Arbequina
        """
        from python_forestacion.entidades.cultivos.olivo import Olivo
        from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
        return Olivo(tipo_aceituna=TipoAceituna.ARBEQUINA)

    @staticmethod
    def _crear_lechuga() -> 'Cultivo':
        """
        Crea una instancia de Lechuga.

        Returns:
            Lechuga con variedad por defecto
        """
        from python_forestacion.entidades.cultivos.lechuga import Lechuga
        from python_forestacion.constantes import VARIEDAD_LECHUGA_DEFAULT
        return Lechuga(variedad=VARIEDAD_LECHUGA_DEFAULT)

    @staticmethod
    def _crear_zanahoria() -> 'Cultivo':
        """
        Crea una instancia de Zanahoria.

        Returns:
            Zanahoria (no baby carrot por defecto)
        """
        from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
        return Zanahoria(is_baby_carrot=False)