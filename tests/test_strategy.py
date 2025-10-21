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
