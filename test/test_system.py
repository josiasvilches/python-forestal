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
