"""
Archivo integrador generado automaticamente
Directorio: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/patrones/observer
Fecha: 2025-10-22 09:43:42
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/patrones/observer/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: observable.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/patrones/observer/observable.py
# ================================================================================

"""
Patron Observer - Clase Observable.

Clase base para objetos que pueden ser observados.
"""

# Standard library
from abc import ABC
from typing import Generic, TypeVar, List

# Local application
from python_forestacion.patrones.observer.observer import Observer

T = TypeVar('T')


class Observable(Generic[T], ABC):
    """
    Clase Observable generica tipo-segura.

    Mantiene una lista de observadores y los notifica cuando ocurren cambios.

    Type Parameters:
        T: Tipo de evento que puede notificar
    """

    def __init__(self):
        """
        Inicializa lista de observadores vacia.
        """
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        """
        Agrega un observador a la lista.

        Args:
            observador: Observador a agregar
        """
        if observador not in self._observadores:
            self._observadores.append(observador)

    def eliminar_observador(self, observador: Observer[T]) -> None:
        """
        Elimina un observador de la lista.

        Args:
            observador: Observador a eliminar
        """
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notificar_observadores(self, evento: T) -> None:
        """
        Notifica a todos los observadores con el evento.

        Args:
            evento: Evento o dato a notificar del tipo T
        """
        for observador in self._observadores:
            observador.actualizar(evento)

# ================================================================================
# ARCHIVO 3/3: observer.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/patrones/observer/observer.py
# ================================================================================

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

