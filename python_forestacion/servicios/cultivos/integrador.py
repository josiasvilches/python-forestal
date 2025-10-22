"""
Archivo integrador generado automaticamente
Directorio: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/servicios/cultivos
Fecha: 2025-10-22 09:43:42
Total de archivos integrados: 8
"""

# ================================================================================
# ARCHIVO 1/8: __init__.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/servicios/cultivos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/8: arbol_service.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/servicios/cultivos/arbol_service.py
# ================================================================================

"""
Servicio base para arboles.

Contiene logica de negocio comun a todos los arboles.
"""

# Standard library
from abc import ABC
from typing import TYPE_CHECKING

# Local application
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.arbol import Arbol


class ArbolService(CultivoService, ABC):
    """
    Servicio base para arboles.

    Los arboles pueden crecer en altura al recibir agua.
    """

    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        """
        Inicializa el servicio de arbol.

        Args:
            estrategia_absorcion: Estrategia de absorcion de agua
        """
        super().__init__(estrategia_absorcion)

    def mostrar_datos(self, arbol: 'Arbol') -> None:
        """
        Muestra datos del arbol incluyendo altura.

        Args:
            arbol: Arbol a mostrar
        """
        super().mostrar_datos(arbol)
        print(f"ID: {arbol.get_id()}")
        print(f"Altura: {arbol.get_altura()} m")

# ================================================================================
# ARCHIVO 3/8: cultivo_service.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/servicios/cultivos/cultivo_service.py
# ================================================================================

"""
Servicio base para cultivos.

Contiene logica de negocio comun a todos los cultivos.
"""

# Standard library
from abc import ABC
from datetime import date
from typing import TYPE_CHECKING

# Local application
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoService(ABC):
    """
    Servicio base abstracto para cultivos.

    Implementa logica comun y delega absorcion a estrategias.
    """

    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        """
        Inicializa el servicio con una estrategia de absorcion.

        Args:
            estrategia_absorcion: Estrategia para calcular absorcion de agua
        """
        self._estrategia_absorcion = estrategia_absorcion

    def absorver_agua(self, cultivo: 'Cultivo') -> int:
        """
        Calcula y aplica absorcion de agua al cultivo.

        Args:
            cultivo: Cultivo que absorbe agua

        Returns:
            Cantidad de agua absorbida en litros
        """
        fecha_actual = date.today()
        temperatura = 20.0
        humedad = 50.0

        agua_absorvida = self._estrategia_absorcion.calcular_absorcion(
            fecha_actual,
            temperatura,
            humedad,
            cultivo
        )

        cultivo.set_agua(cultivo.get_agua() + agua_absorvida)
        return agua_absorvida

    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """
        Muestra datos basicos del cultivo.

        Args:
            cultivo: Cultivo a mostrar
        """
        print(f"Cultivo: {type(cultivo).__name__}")
        print(f"Superficie: {cultivo.get_superficie()} m2")
        print(f"Agua almacenada: {cultivo.get_agua()} L")

# ================================================================================
# ARCHIVO 4/8: cultivo_service_registry.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/servicios/cultivos/cultivo_service_registry.py
# ================================================================================

"""
Registry de servicios de cultivos (Patron Singleton + Registry).

Proporciona acceso centralizado a servicios de cultivos con dispatch polimorfico.
"""

# Standard library
from threading import Lock
from typing import TYPE_CHECKING, Dict, Callable

# Local application
from python_forestacion.servicios.cultivos.pino_service import PinoService
from python_forestacion.servicios.cultivos.olivo_service import OlivoService
from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
from python_forestacion.servicios.cultivos.zanahoria_service import ZanahoriaService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.cultivos.pino import Pino
    from python_forestacion.entidades.cultivos.olivo import Olivo
    from python_forestacion.entidades.cultivos.lechuga import Lechuga
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria


class CultivoServiceRegistry:
    """
    Registry Singleton de servicios de cultivos.

    Implementa:
    - Patron Singleton: Una sola instancia compartida
    - Patron Registry: Dispatch polimorfico sin isinstance()
    """

    _instance = None
    _lock = Lock()

    def __new__(cls):
        """
        Crea o retorna la instancia unica (thread-safe).

        Returns:
            Instancia unica del registry
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._inicializar_servicios()
        return cls._instance

    def _inicializar_servicios(self) -> None:
        """
        Inicializa los servicios y registros una sola vez.
        """
        # Servicios especificos
        self._pino_service = PinoService()
        self._olivo_service = OlivoService()
        self._lechuga_service = LechugaService()
        self._zanahoria_service = ZanahoriaService()

        # Registry de handlers (evita isinstance cascades)
        from python_forestacion.entidades.cultivos.pino import Pino
        from python_forestacion.entidades.cultivos.olivo import Olivo
        from python_forestacion.entidades.cultivos.lechuga import Lechuga
        from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

        self._absorber_agua_handlers: Dict[type, Callable] = {
            Pino: self._absorber_agua_pino,
            Olivo: self._absorber_agua_olivo,
            Lechuga: self._absorber_agua_lechuga,
            Zanahoria: self._absorber_agua_zanahoria
        }

        self._mostrar_datos_handlers: Dict[type, Callable] = {
            Pino: self._mostrar_datos_pino,
            Olivo: self._mostrar_datos_olivo,
            Lechuga: self._mostrar_datos_lechuga,
            Zanahoria: self._mostrar_datos_zanahoria
        }

    @classmethod
    def get_instance(cls) -> 'CultivoServiceRegistry':
        """
        Obtiene la instancia unica del registry.

        Returns:
            Instancia del registry
        """
        if cls._instance is None:
            cls()
        return cls._instance

    def absorber_agua(self, cultivo: 'Cultivo') -> int:
        """
        Absorbe agua usando dispatch polimorfico.

        Args:
            cultivo: Cultivo que absorbe agua

        Returns:
            Cantidad de agua absorbida

        Raises:
            ValueError: Si el tipo de cultivo no esta registrado
        """
        tipo = type(cultivo)
        if tipo not in self._absorber_agua_handlers:
            raise ValueError(f"Tipo de cultivo no registrado: {tipo}")
        return self._absorber_agua_handlers[tipo](cultivo)

    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """
        Muestra datos usando dispatch polimorfico.

        Args:
            cultivo: Cultivo a mostrar

        Raises:
            ValueError: Si el tipo de cultivo no esta registrado
        """
        tipo = type(cultivo)
        if tipo not in self._mostrar_datos_handlers:
            raise ValueError(f"Tipo de cultivo no registrado: {tipo}")
        self._mostrar_datos_handlers[tipo](cultivo)

    def _absorber_agua_pino(self, cultivo: 'Pino') -> int:
        """Handler para absorber agua de Pino."""
        return self._pino_service.absorver_agua(cultivo)

    def _absorber_agua_olivo(self, cultivo: 'Olivo') -> int:
        """Handler para absorber agua de Olivo."""
        return self._olivo_service.absorver_agua(cultivo)

    def _absorber_agua_lechuga(self, cultivo: 'Lechuga') -> int:
        """Handler para absorber agua de Lechuga."""
        return self._lechuga_service.absorver_agua(cultivo)

    def _absorber_agua_zanahoria(self, cultivo: 'Zanahoria') -> int:
        """Handler para absorber agua de Zanahoria."""
        return self._zanahoria_service.absorver_agua(cultivo)

    def _mostrar_datos_pino(self, cultivo: 'Pino') -> None:
        """Handler para mostrar datos de Pino."""
        self._pino_service.mostrar_datos(cultivo)

    def _mostrar_datos_olivo(self, cultivo: 'Olivo') -> None:
        """Handler para mostrar datos de Olivo."""
        self._olivo_service.mostrar_datos(cultivo)

    def _mostrar_datos_lechuga(self, cultivo: 'Lechuga') -> None:
        """Handler para mostrar datos de Lechuga."""
        self._lechuga_service.mostrar_datos(cultivo)

    def _mostrar_datos_zanahoria(self, cultivo: 'Zanahoria') -> None:
        """Handler para mostrar datos de Zanahoria."""
        self._zanahoria_service.mostrar_datos(cultivo)

# ================================================================================
# ARCHIVO 5/8: lechuga_service.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/servicios/cultivos/lechuga_service.py
# ================================================================================

"""
Servicio para Lechuga.

Logica de negocio especifica para cultivos de tipo Lechuga.
"""

# Standard library
from typing import TYPE_CHECKING

# Local application
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_LECHUGA

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.lechuga import Lechuga


class LechugaService(CultivoService):
    """
    Servicio para cultivos tipo Lechuga.

    Implementa logica especifica de lechugas (absorcion constante).
    """

    def __init__(self):
        """
        Inicializa servicio con estrategia constante.
        """
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_LECHUGA))

    def mostrar_datos(self, lechuga: 'Lechuga') -> None:
        """
        Muestra datos de la lechuga incluyendo variedad e invernadero.

        Args:
            lechuga: Lechuga a mostrar
        """
        super().mostrar_datos(lechuga)
        print(f"Variedad: {lechuga.get_variedad()}")
        print(f"Invernadero: {lechuga.get_invernadero()}")

# ================================================================================
# ARCHIVO 6/8: olivo_service.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/servicios/cultivos/olivo_service.py
# ================================================================================

"""
Servicio para Olivo.

Logica de negocio especifica para cultivos de tipo Olivo.
"""

# Standard library
from typing import TYPE_CHECKING

# Local application
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_OLIVO

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.olivo import Olivo


class OlivoService(ArbolService):
    """
    Servicio para cultivos tipo Olivo.

    Implementa logica especifica de olivos (crecimiento lento, absorcion estacional).
    """

    def __init__(self):
        """
        Inicializa servicio con estrategia estacional.
        """
        super().__init__(AbsorcionSeasonalStrategy())

    def absorver_agua(self, olivo: 'Olivo') -> int:
        """
        Absorbe agua y hace crecer el olivo.

        Args:
            olivo: Olivo que absorbe agua

        Returns:
            Cantidad de agua absorbida
        """
        agua_absorvida = super().absorver_agua(olivo)
        
        # Olivo crece lentamente al recibir agua
        altura_actual = olivo.get_altura()
        olivo.set_altura(altura_actual + CRECIMIENTO_OLIVO)
        
        return agua_absorvida

    def mostrar_datos(self, olivo: 'Olivo') -> None:
        """
        Muestra datos del olivo incluyendo tipo de aceituna.

        Args:
            olivo: Olivo a mostrar
        """
        super().mostrar_datos(olivo)
        print(f"Tipo de aceituna: {olivo.get_tipo_aceituna().value}")

# ================================================================================
# ARCHIVO 7/8: pino_service.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/servicios/cultivos/pino_service.py
# ================================================================================

"""
Servicio para Pino.

Logica de negocio especifica para cultivos de tipo Pino.
"""

# Standard library
from typing import TYPE_CHECKING

# Local application
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_PINO

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.pino import Pino


class PinoService(ArbolService):
    """
    Servicio para cultivos tipo Pino.

    Implementa logica especifica de pinos (crecimiento, absorcion estacional).
    """

    def __init__(self):
        """
        Inicializa servicio con estrategia estacional.
        """
        super().__init__(AbsorcionSeasonalStrategy())

    def absorver_agua(self, pino: 'Pino') -> int:
        """
        Absorbe agua y hace crecer el pino.

        Args:
            pino: Pino que absorbe agua

        Returns:
            Cantidad de agua absorbida
        """
        agua_absorvida = super().absorver_agua(pino)
        
        # Pino crece al recibir agua
        altura_actual = pino.get_altura()
        pino.set_altura(altura_actual + CRECIMIENTO_PINO)
        
        return agua_absorvida

    def mostrar_datos(self, pino: 'Pino') -> None:
        """
        Muestra datos del pino incluyendo variedad.

        Args:
            pino: Pino a mostrar
        """
        super().mostrar_datos(pino)
        print(f"Variedad: {pino.get_variedad()}")

# ================================================================================
# ARCHIVO 8/8: zanahoria_service.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/servicios/cultivos/zanahoria_service.py
# ================================================================================

"""
Servicio para Zanahoria.

Logica de negocio especifica para cultivos de tipo Zanahoria.
"""

# Standard library
from typing import TYPE_CHECKING

# Local application
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_ZANAHORIA

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria


class ZanahoriaService(CultivoService):
    """
    Servicio para cultivos tipo Zanahoria.

    Implementa logica especifica de zanahorias (absorcion constante).
    """

    def __init__(self):
        """
        Inicializa servicio con estrategia constante.
        """
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_ZANAHORIA))

    def mostrar_datos(self, zanahoria: 'Zanahoria') -> None:
        """
        Muestra datos de la zanahoria incluyendo si es baby carrot.

        Args:
            zanahoria: Zanahoria a mostrar
        """
        super().mostrar_datos(zanahoria)
        tipo = "Baby carrot" if zanahoria.is_baby_carrot() else "Regular"
        print(f"Tipo: {tipo}")

