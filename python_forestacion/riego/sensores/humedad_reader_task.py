"""
Thread sensor de humedad (Observable).

Lee humedad ambiental y notifica a observadores.
"""

# Standard library
import threading
import time
import random

# Local application
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_HUMEDAD,
    SENSOR_HUMEDAD_MIN,
    SENSOR_HUMEDAD_MAX
)


class HumedadReaderTask(threading.Thread, Observable[float]):
    """
    Thread daemon que lee humedad periodicamente.

    Implementa patron Observer como Observable[float].
    """

    def __init__(self):
        """
        Inicializa el thread sensor de humedad.
        """
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def run(self) -> None:
        """
        Ejecuta lectura continua de humedad.
        """
        while not self._detenido.is_set():
            humedad = self._leer_humedad()
            self.notificar_observadores(humedad)
            time.sleep(INTERVALO_SENSOR_HUMEDAD)

    def _leer_humedad(self) -> float:
        """
        Lee humedad del sensor (simulado).

        Returns:
            Humedad en porcentaje
        """
        return random.uniform(SENSOR_HUMEDAD_MIN, SENSOR_HUMEDAD_MAX)

    def detener(self) -> None:
        """
        Detiene el thread de forma segura.
        """
        self._detenido.set()