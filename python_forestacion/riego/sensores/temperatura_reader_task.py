"""
Thread sensor de temperatura (Observable).

Lee temperatura ambiental y notifica a observadores.
"""

# Standard library
import threading
import time
import random

# Local application
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_TEMPERATURA,
    SENSOR_TEMP_MIN,
    SENSOR_TEMP_MAX
)


class TemperaturaReaderTask(threading.Thread, Observable[float]):
    """
    Thread daemon que lee temperatura periodicamente.

    Implementa patron Observer como Observable[float].
    """

    def __init__(self):
        """
        Inicializa el thread sensor de temperatura.
        """
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def run(self) -> None:
        """
        Ejecuta lectura continua de temperatura.
        """
        while not self._detenido.is_set():
            temperatura = self._leer_temperatura()
            self.notificar_observadores(temperatura)
            time.sleep(INTERVALO_SENSOR_TEMPERATURA)

    def _leer_temperatura(self) -> float:
        """
        Lee temperatura del sensor (simulado).

        Returns:
            Temperatura en grados Celsius
        """
        return random.uniform(SENSOR_TEMP_MIN, SENSOR_TEMP_MAX)

    def detener(self) -> None:
        """
        Detiene el thread de forma segura.
        """
        self._detenido.set()