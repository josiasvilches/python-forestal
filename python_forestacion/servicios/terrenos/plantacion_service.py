"""
Servicio para Plantacion.

Logica de negocio para plantaciones agricolas.
"""

# Standard library
from typing import TYPE_CHECKING

# Local application
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.constantes import AGUA_MINIMA

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class PlantacionService:
    """
    Servicio para gestion de plantaciones.

    Proporciona operaciones como plantar, regar, cosechar y fumigar.
    """

    def __init__(self):
        """
        Inicializa el servicio con factory y registry.
        """
        self._factory = CultivoFactory()
        self._registry = CultivoServiceRegistry.get_instance()

    def plantar(self, plantacion: 'Plantacion', especie: str, cantidad: int) -> None:
        """
        Planta cultivos de una especie especifica.

        Args:
            plantacion: Plantacion donde plantar
            especie: Tipo de cultivo a plantar
            cantidad: Cantidad de cultivos

        Raises:
            SuperficieInsuficienteException: Si no hay superficie suficiente
        """
        # Crear cultivo de muestra para calcular superficie
        cultivo_muestra = self._factory.crear_cultivo(especie)
        superficie_requerida = cultivo_muestra.get_superficie() * cantidad
        superficie_disponible = plantacion.get_superficie() - plantacion.get_superficie_ocupada()

        if superficie_requerida > superficie_disponible:
            raise SuperficieInsuficienteException(superficie_requerida, superficie_disponible)

        # Plantar cultivos
        for i in range(cantidad):
            cultivo = self._factory.crear_cultivo(especie)
            plantacion.agregar_cultivo(cultivo)

        # Actualizar superficie ocupada
        nueva_superficie_ocupada = plantacion.get_superficie_ocupada() + superficie_requerida
        plantacion.set_superficie_ocupada(nueva_superficie_ocupada)

        print(f"{cantidad} {especie}(s) plantado(s) exitosamente")

    def regar(self, plantacion: 'Plantacion') -> None:
        """
        Riega todos los cultivos de la plantacion.

        Args:
            plantacion: Plantacion a regar

        Raises:
            AguaAgotadaException: Si no hay agua suficiente
        """
        agua_disponible = plantacion.get_agua_disponible()
        
        if agua_disponible < AGUA_MINIMA:
            raise AguaAgotadaException(AGUA_MINIMA, agua_disponible)

        # Consumir agua de la plantacion
        plantacion.set_agua_disponible(agua_disponible - AGUA_MINIMA)

        # Cada cultivo absorbe agua segun su estrategia
        cultivos = plantacion.get_cultivos()
        for cultivo in cultivos:
            self._registry.absorber_agua(cultivo)

        print(f"Plantacion regada. Agua restante: {plantacion.get_agua_disponible()} L")

    def cosechar(self, plantacion: 'Plantacion') -> None:
        """
        Cosecha todos los cultivos de la plantacion.

        Args:
            plantacion: Plantacion a cosechar
        """
        cultivos = plantacion.get_cultivos()
        cantidad = len(cultivos)

        # Vaciar lista de cultivos
        plantacion.set_cultivos([])
        plantacion.set_superficie_ocupada(0.0)

        print(f"Cosechados {cantidad} cultivos")

    def fumigar(self, plantacion: 'Plantacion', plaguicida: str) -> None:
        """
        Fumiga la plantacion con un plaguicida.

        Args:
            plantacion: Plantacion a fumigar
            plaguicida: Tipo de plaguicida a aplicar
        """
        print(f"Fumigando plantacion con: {plaguicida}")

    def mostrar_cultivos(self, plantacion: 'Plantacion') -> None:
        """
        Muestra todos los cultivos de la plantacion.

        Args:
            plantacion: Plantacion a mostrar
        """
        cultivos = plantacion.get_cultivos()
        print(f"\nCantidad de cultivos plantados: {len(cultivos)}")
        
        if len(cultivos) > 0:
            print("Listado de Cultivos plantados")
            print("_" * 28)
            print()
            
            for cultivo in cultivos:
                self._registry.mostrar_datos(cultivo)
                print()