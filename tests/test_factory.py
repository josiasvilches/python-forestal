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
