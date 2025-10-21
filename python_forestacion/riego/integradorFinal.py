"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion/riego
Fecha de generacion: 2025-10-21 18:29:59
Total de archivos integrados: 6
Total de directorios procesados: 3
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. __init__.py
#
# DIRECTORIO: control
#   2. __init__.py
#   3. control_riego_task.py
#
# DIRECTORIO: sensores
#   4. __init__.py
#   5. humedad_reader_task.py
#   6. temperatura_reader_task.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/6: __init__.py
# Directorio: .
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion/riego\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: control
################################################################################

# ==============================================================================
# ARCHIVO 2/6: __init__.py
# Directorio: control
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion/riego\control\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 3/6: control_riego_task.py
# Directorio: control
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion/riego\control\control_riego_task.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: sensores
################################################################################

# ==============================================================================
# ARCHIVO 4/6: __init__.py
# Directorio: sensores
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion/riego\sensores\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 5/6: humedad_reader_task.py
# Directorio: sensores
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion/riego\sensores\humedad_reader_task.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 6/6: temperatura_reader_task.py
# Directorio: sensores
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion/riego\sensores\temperatura_reader_task.py
# ==============================================================================

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


################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 6
# Generado: 2025-10-21 18:29:59
################################################################################
