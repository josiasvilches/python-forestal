"""
Archivo integrador generado automaticamente
Directorio: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\riego\control
Fecha: 2025-10-21 18:36:35
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\riego\control\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: control_riego_task.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\riego\control\control_riego_task.py
# ================================================================================

"""
Thread controlador de riego (Observer).

Observa sensores y riega automaticamente segun condiciones.
"""

# Standard library
import threading
import time
from typing import TYPE_CHECKING

# Local application
from python_forestacion.patrones.observer.observer import Observer
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.constantes import (
    INTERVALO_CONTROL_RIEGO,
    TEMP_MIN_RIEGO,
    TEMP_MAX_RIEGO,
    HUMEDAD_MAX_RIEGO
)

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion
    from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
    from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
    from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask


class ControlRiegoTask(threading.Thread, Observer[float]):
    """
    Thread daemon controlador de riego automatico.

    Observa sensores de temperatura y humedad, y riega cuando se cumplen condiciones.
    """

    def __init__(
        self,
        sensor_temperatura: 'TemperaturaReaderTask',
        sensor_humedad: 'HumedadReaderTask',
        plantacion: 'Plantacion',
        plantacion_service: 'PlantacionService'
    ):
        """
        Inicializa el controlador de riego.

        Args:
            sensor_temperatura: Sensor de temperatura a observar
            sensor_humedad: Sensor de humedad a observar
            plantacion: Plantacion a regar
            plantacion_service: Servicio para operaciones de riego
        """
        threading.Thread.__init__(self, daemon=True)
        self._plantacion = plantacion
        self._plantacion_service = plantacion_service
        self._detenido = threading.Event()
        
        # Estado de sensores
        self._ultima_temperatura = 20.0
        self._ultima_humedad = 50.0
        
        # Suscribirse a sensores
        sensor_temperatura.agregar_observador(self)
        sensor_humedad.agregar_observador(self)

    def actualizar(self, evento: float) -> None:
        """
        Recibe actualizaciones de sensores (patron Observer).

        Args:
            evento: Valor del sensor (temperatura o humedad)
        """
        # El evento es float, determinar si es temperatura o humedad por rango
        if -25 <= evento <= 50:
            self._ultima_temperatura = evento
        elif 0 <= evento <= 100:
            self._ultima_humedad = evento

    def run(self) -> None:
        """
        Ejecuta control automatico de riego.
        """
        while not self._detenido.is_set():
            self._evaluar_y_regar()
            time.sleep(INTERVALO_CONTROL_RIEGO)

    def _evaluar_y_regar(self) -> None:
        """
        Evalua condiciones y riega si es necesario.
        """
        temperatura = self._ultima_temperatura
        humedad = self._ultima_humedad

        # Condiciones de riego
        if (TEMP_MIN_RIEGO <= temperatura <= TEMP_MAX_RIEGO) and (humedad < HUMEDAD_MAX_RIEGO):
            try:
                print(f"\n[RIEGO AUTO] Temp: {temperatura:.1f}C, Humedad: {humedad:.1f}% - REGANDO")
                self._plantacion_service.regar(self._plantacion)
            except AguaAgotadaException as e:
                print(f"[RIEGO AUTO] {e.get_user_message()}")

    def detener(self) -> None:
        """
        Detiene el thread de forma segura.
        """
        self._detenido.set()

