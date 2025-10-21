"""
Patron Observer - Interfaz Observer.

Define el contrato para objetos que observan cambios en Observables.
"""

# Standard library
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class Observer(Generic[T], ABC):
    """
    Interfaz Observer generica tipo-segura.

    Los observadores reciben notificaciones cuando el Observable cambia.

    Type Parameters:
        T: Tipo de evento que puede recibir
    """

    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """
        Metodo llamado cuando el Observable notifica un cambio.

        Args:
            evento: Evento o dato actualizado del tipo T
        """
        pass