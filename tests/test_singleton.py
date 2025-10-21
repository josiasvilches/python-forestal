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
