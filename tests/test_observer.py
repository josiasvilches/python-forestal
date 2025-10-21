import unittest

from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.patrones.observer.observer import Observer
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.entidades.terrenos.plantacion import Plantacion


class DummyObservable(Observable[int]):
    def emitir(self, valor: int):
        self.notificar_observadores(valor)


class DummyObserver(Observer[int]):
    def __init__(self):
        self.eventos = []

    def actualizar(self, evento: int) -> None:
        self.eventos.append(evento)


class TestObserverPattern(unittest.TestCase):
    def test_observable_notifica_observer(self):
        observable = DummyObservable()
        observer = DummyObserver()
        observable.agregar_observador(observer)
        observable.emitir(42)
        self.assertEqual(observer.eventos, [42])

    def test_control_riego_evalua_condiciones(self):
        # Crear plantacion simple
        plantacion = Plantacion(nombre="Test", superficie=100.0, agua=100)
        plantacion_service = PlantacionService()

        # Crear sensores reales pero no iniciar threads
        temp = TemperaturaReaderTask()
        hum = HumedadReaderTask()

        # Crear controlador (se suscribe a sensores)
        control = ControlRiegoTask(temp, hum, plantacion, plantacion_service)

        # Simular eventos
        control.actualizar(10.0)   # temperatura
        control.actualizar(20.0)   # humedad

        # Forzar evaluacion
        control._evaluar_y_regar()

        # Debe haber consumido AGUA_MINIMA si condiciones se cumplen
        self.assertLessEqual(plantacion.get_agua_disponible(), 100)


if __name__ == '__main__':
    unittest.main()
