"""
Archivo integrador generado automaticamente
Directorio: /home/josiasvilches/cursada/disenosistemas/python-forestal/tests
Fecha: 2025-10-22 09:43:42
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/tests/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/6: test_factory.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/tests/test_factory.py
# ================================================================================

import unittest

from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
from python_forestacion.constantes import (
    VARIEDAD_PINO_DEFAULT,
    VARIEDAD_LECHUGA_DEFAULT
)
from python_forestacion.entidades.personal.tarea import Tarea
from datetime import date


class TestCultivoFactory(unittest.TestCase):
    def test_crear_cultivo_pino(self):
        cultivo = CultivoFactory.crear_cultivo("Pino")
        self.assertIsInstance(cultivo, Pino)
        self.assertEqual(cultivo.get_variedad(), VARIEDAD_PINO_DEFAULT)

    def test_crear_cultivo_olivo(self):
        cultivo = CultivoFactory.crear_cultivo("Olivo")
        self.assertIsInstance(cultivo, Olivo)
        self.assertEqual(cultivo.get_tipo_aceituna(), TipoAceituna.ARBEQUINA)

    def test_crear_cultivo_lechuga(self):
        cultivo = CultivoFactory.crear_cultivo("Lechuga")
        self.assertIsInstance(cultivo, Lechuga)
        self.assertEqual(cultivo.get_variedad(), VARIEDAD_LECHUGA_DEFAULT)
        self.assertTrue(cultivo.get_invernadero())

    def test_crear_cultivo_zanahoria(self):
        cultivo = CultivoFactory.crear_cultivo("Zanahoria")
        self.assertIsInstance(cultivo, Zanahoria)
        self.assertFalse(cultivo.is_baby_carrot())

    def test_crear_cultivo_desconocido(self):
        with self.assertRaises(ValueError):
            CultivoFactory.crear_cultivo("Desconocido")

    def test_crear_trabajador(self):
        tareas = [Tarea(1, date.today(), "Probar")] 
        trabajador = CultivoFactory.crear_trabajador(12345678, "Juan Perez", tareas)
        self.assertEqual(trabajador.get_dni(), 12345678)
        self.assertEqual(trabajador.get_nombre(), "Juan Perez")
        self.assertEqual(len(trabajador.get_tareas()), 1)

    def test_crear_trabajador_validaciones(self):
        tareas = []
        with self.assertRaises(ValueError):
            CultivoFactory.crear_trabajador(0, "Nombre", tareas)
        with self.assertRaises(ValueError):
            CultivoFactory.crear_trabajador(123, "   ", tareas)

    def test_crear_herramienta(self):
        herramienta = CultivoFactory.crear_herramienta(1, "Pala", True)
        self.assertEqual(herramienta.get_id_herramienta(), 1)
        self.assertEqual(herramienta.get_nombre(), "Pala")
        self.assertTrue(herramienta.tiene_certificado_hys())

    def test_crear_herramienta_validaciones(self):
        with self.assertRaises(ValueError):
            CultivoFactory.crear_herramienta(0, "Pala", True)
        with self.assertRaises(ValueError):
            CultivoFactory.crear_herramienta(1, " ", True)


if __name__ == '__main__':
    unittest.main()


# ================================================================================
# ARCHIVO 3/6: test_observer.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/tests/test_observer.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 4/6: test_singleton.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/tests/test_singleton.py
# ================================================================================

import unittest

from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory


class TestSingletonRegistry(unittest.TestCase):
    def test_unica_instancia(self):
        a = CultivoServiceRegistry()
        b = CultivoServiceRegistry.get_instance()
        self.assertIs(a, b)

    def test_dispatch_absorber_agua(self):
        registry = CultivoServiceRegistry.get_instance()
        cultivo = CultivoFactory.crear_cultivo("Lechuga")
        agua_antes = cultivo.get_agua()
        absorbida = registry.absorber_agua(cultivo)
        self.assertIsInstance(absorbida, int)
        self.assertGreaterEqual(cultivo.get_agua(), agua_antes)

    def test_mostrar_datos_no_registrado(self):
        class Dummy:
            pass
        registry = CultivoServiceRegistry.get_instance()
        with self.assertRaises(ValueError):
            registry.mostrar_datos(Dummy())


if __name__ == '__main__':
    unittest.main()


# ================================================================================
# ARCHIVO 5/6: test_strategy.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/tests/test_strategy.py
# ================================================================================

import unittest
from datetime import date

from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
from python_forestacion.servicios.cultivos.pino_service import PinoService
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.constantes import (
    ABSORCION_SEASONAL_VERANO,
    ABSORCION_SEASONAL_INVIERNO,
    ABSORCION_LECHUGA
)


class TestStrategy(unittest.TestCase):
    def test_absorcion_seasonal_verano_invierno(self):
        strat = AbsorcionSeasonalStrategy()
        # Mes 3 (marzo) => verano hemisferio sur
        verano = strat.calcular_absorcion(date(2025, 3, 21), 20.0, 50.0, CultivoFactory.crear_cultivo("Pino"))
        # Mes 9 (septiembre) => invierno hemisferio sur
        invierno = strat.calcular_absorcion(date(2025, 9, 21), 10.0, 40.0, CultivoFactory.crear_cultivo("Pino"))
        self.assertEqual(verano, ABSORCION_SEASONAL_VERANO)
        self.assertEqual(invierno, ABSORCION_SEASONAL_INVIERNO)

    def test_absorcion_constante(self):
        strat = AbsorcionConstanteStrategy(ABSORCION_LECHUGA)
        litros = strat.calcular_absorcion(date.today(), 20.0, 50.0, CultivoFactory.crear_cultivo("Lechuga"))
        self.assertEqual(litros, ABSORCION_LECHUGA)

    def test_integracion_servicios(self):
        # Lechuga (constante)
        svc_lechuga = LechugaService()
        lechuga = CultivoFactory.crear_cultivo("Lechuga")
        agua_antes = lechuga.get_agua()
        absorbed = svc_lechuga.absorver_agua(lechuga)
        self.assertEqual(absorbed, ABSORCION_LECHUGA)
        self.assertEqual(lechuga.get_agua(), agua_antes + ABSORCION_LECHUGA)

        # Pino (estacional) no verificamos valor exacto, pero debe ser int y sumar agua
        svc_pino = PinoService()
        pino = CultivoFactory.crear_cultivo("Pino")
        agua_antes = pino.get_agua()
        absorbed = svc_pino.absorver_agua(pino)
        self.assertIsInstance(absorbed, int)
        self.assertGreaterEqual(pino.get_agua(), agua_antes + ABSORCION_SEASONAL_INVIERNO)


if __name__ == '__main__':
    unittest.main()


# ================================================================================
# ARCHIVO 6/6: test_system.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/tests/test_system.py
# ================================================================================

import os
import unittest
from datetime import date

from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.constantes import DIRECTORIO_DATA, EXTENSION_DATA, AGUA_MINIMA


class TestSistemaServicios(unittest.TestCase):
    def setUp(self):
        self.tierra_service = TierraService()
        self.plantacion_service = PlantacionService()
        self.terreno = self.tierra_service.crear_tierra_con_plantacion(
            id_padron_catastral=99,
            superficie=100.0,
            domicilio="Test",
            nombre_plantacion="TestPlantacion"
        )
        self.plantacion = self.terreno.get_finca()

    def test_plantar_y_validar_superficie(self):
        # Plantar 10 lechugas (0.1 m2 c/u) => 1 m2
        self.plantacion_service.plantar(self.plantacion, "Lechuga", 10)
        self.assertEqual(len(self.plantacion.get_cultivos()), 10)
        self.assertAlmostEqual(self.plantacion.get_superficie_ocupada(), 1.0)

        # Intentar exceder superficie
        with self.assertRaises(SuperficieInsuficienteException):
            self.plantacion_service.plantar(self.plantacion, "Pino", 1000)

    def test_regar_y_excepciones(self):
        # Dejar poca agua y forzar excepcion de agua
        self.plantacion.set_agua_disponible(AGUA_MINIMA - 1)
        with self.assertRaises(AguaAgotadaException):
            self.plantacion_service.regar(self.plantacion)

        # Ahora agua suficiente
        self.plantacion.set_agua_disponible(AGUA_MINIMA)
        self.plantacion_service.regar(self.plantacion)
        self.assertGreaterEqual(self.plantacion.get_agua_disponible(), 0)

    def test_persistencia_registro(self):
        registro = RegistroForestal(
            id_padron=99,
            tierra=self.terreno,
            plantacion=self.plantacion,
            propietario="TestOwner",
            avaluo=123.45
        )

        service = RegistroForestalService()
        service.persistir(registro)

        # Archivo debe existir
        path = os.path.join(DIRECTORIO_DATA, f"TestOwner{EXTENSION_DATA}")
        self.assertTrue(os.path.exists(path))

        # Leer registro
        leido = RegistroForestalService.leer_registro("TestOwner")
        self.assertEqual(leido.get_id_padron(), 99)
        self.assertEqual(leido.get_propietario(), "TestOwner")

        # Cleanup
        try:
            os.remove(path)
            os.rmdir(DIRECTORIO_DATA)
        except Exception:
            pass


if __name__ == '__main__':
    unittest.main()


