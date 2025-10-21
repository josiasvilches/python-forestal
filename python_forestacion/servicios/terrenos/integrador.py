"""
Archivo integrador generado automaticamente
Directorio: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\servicios\terrenos
Fecha: 2025-10-21 18:36:35
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\servicios\terrenos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: plantacion_service.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\servicios\terrenos\plantacion_service.py
# ================================================================================

"""
Servicio para Plantacion.

Logica de negocio para plantaciones agricolas.
"""

# Standard library
from typing import TYPE_CHECKING

# Local application
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.constantes import AGUA_MINIMA

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class PlantacionService:
    """
    Servicio para gestion de plantaciones.

    Proporciona operaciones como plantar, regar, cosechar y fumigar.
    """

    def __init__(self):
        """
        Inicializa el servicio con factory y registry.
        """
        self._factory = CultivoFactory()
        self._registry = CultivoServiceRegistry.get_instance()

    def plantar(self, plantacion: 'Plantacion', especie: str, cantidad: int) -> None:
        """
        Planta cultivos de una especie especifica.

        Args:
            plantacion: Plantacion donde plantar
            especie: Tipo de cultivo a plantar
            cantidad: Cantidad de cultivos

        Raises:
            SuperficieInsuficienteException: Si no hay superficie suficiente
        """
        # Crear cultivo de muestra para calcular superficie
        cultivo_muestra = self._factory.crear_cultivo(especie)
        superficie_requerida = cultivo_muestra.get_superficie() * cantidad
        superficie_disponible = plantacion.get_superficie() - plantacion.get_superficie_ocupada()

        if superficie_requerida > superficie_disponible:
            raise SuperficieInsuficienteException(superficie_requerida, superficie_disponible)

        # Plantar cultivos
        for i in range(cantidad):
            cultivo = self._factory.crear_cultivo(especie)
            plantacion.agregar_cultivo(cultivo)

        # Actualizar superficie ocupada
        nueva_superficie_ocupada = plantacion.get_superficie_ocupada() + superficie_requerida
        plantacion.set_superficie_ocupada(nueva_superficie_ocupada)

        print(f"{cantidad} {especie}(s) plantado(s) exitosamente")

    def regar(self, plantacion: 'Plantacion') -> None:
        """
        Riega todos los cultivos de la plantacion.

        Args:
            plantacion: Plantacion a regar

        Raises:
            AguaAgotadaException: Si no hay agua suficiente
        """
        agua_disponible = plantacion.get_agua_disponible()
        
        if agua_disponible < AGUA_MINIMA:
            raise AguaAgotadaException(AGUA_MINIMA, agua_disponible)

        # Consumir agua de la plantacion
        plantacion.set_agua_disponible(agua_disponible - AGUA_MINIMA)

        # Cada cultivo absorbe agua segun su estrategia
        cultivos = plantacion.get_cultivos()
        for cultivo in cultivos:
            self._registry.absorber_agua(cultivo)

        print(f"Plantacion regada. Agua restante: {plantacion.get_agua_disponible()} L")

    def cosechar(self, plantacion: 'Plantacion') -> None:
        """
        Cosecha todos los cultivos de la plantacion.

        Args:
            plantacion: Plantacion a cosechar
        """
        cultivos = plantacion.get_cultivos()
        cantidad = len(cultivos)

        # Vaciar lista de cultivos
        plantacion.set_cultivos([])
        plantacion.set_superficie_ocupada(0.0)

        print(f"Cosechados {cantidad} cultivos")

    def fumigar(self, plantacion: 'Plantacion', plaguicida: str) -> None:
        """
        Fumiga la plantacion con un plaguicida.

        Args:
            plantacion: Plantacion a fumigar
            plaguicida: Tipo de plaguicida a aplicar
        """
        print(f"Fumigando plantacion con: {plaguicida}")

    def mostrar_cultivos(self, plantacion: 'Plantacion') -> None:
        """
        Muestra todos los cultivos de la plantacion.

        Args:
            plantacion: Plantacion a mostrar
        """
        cultivos = plantacion.get_cultivos()
        print(f"\nCantidad de cultivos plantados: {len(cultivos)}")
        
        if len(cultivos) > 0:
            print("Listado de Cultivos plantados")
            print("_" * 28)
            print()
            
            for cultivo in cultivos:
                self._registry.mostrar_datos(cultivo)
                print()

# ================================================================================
# ARCHIVO 3/4: registro_forestal_service.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\servicios\terrenos\registro_forestal_service.py
# ================================================================================

"""
Servicio para RegistroForestal.

Logica de negocio para registros forestales (persistencia).
"""

# Standard library
import pickle
import os
from typing import TYPE_CHECKING

# Local application
from python_forestacion.excepciones.persistencia_exception import (
    PersistenciaException,
    TipoOperacionPersistencia
)
from python_forestacion.excepciones.mensajes_exception import (
    MSG_PERSISTENCIA_ERROR_ESCRITURA_USER,
    MSG_PERSISTENCIA_ERROR_ESCRITURA_TECH,
    MSG_PERSISTENCIA_ERROR_LECTURA_USER,
    MSG_PERSISTENCIA_ERROR_LECTURA_TECH,
    MSG_PERSISTENCIA_ARCHIVO_NO_ENCONTRADO_USER,
    MSG_PERSISTENCIA_ARCHIVO_NO_ENCONTRADO_TECH,
    MSG_PROPIETARIO_VACIO
)
from python_forestacion.constantes import DIRECTORIO_DATA, EXTENSION_DATA

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal


class RegistroForestalService:
    """
    Servicio para gestion de registros forestales.

    Proporciona operaciones de persistencia y mostracion de registros.
    """

    def mostrar_datos(self, registro: 'RegistroForestal') -> None:
        """
        Muestra todos los datos del registro forestal.

        Args:
            registro: Registro a mostrar
        """
        print("\nREGISTRO FORESTAL")
        print("=" * 17)
        print(f"Padron:      {registro.get_id_padron()}")
        print(f"Propietario: {registro.get_propietario()}")
        print(f"Avaluo:      {registro.get_avaluo()}")
        
        tierra = registro.get_tierra()
        print(f"Domicilio:   {tierra.get_domicilio()}")
        print(f"Superficie: {tierra.get_superficie()}")
        
        plantacion = registro.get_plantacion()
        cultivos = plantacion.get_cultivos()
        print(f"Cantidad de cultivos plantados: {len(cultivos)}")
        
        if len(cultivos) > 0:
            print("Listado de Cultivos plantados")
            print("_" * 28)
            print()
            
            from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
            registry = CultivoServiceRegistry.get_instance()
            
            for cultivo in cultivos:
                registry.mostrar_datos(cultivo)
                print()

    def persistir(self, registro: 'RegistroForestal') -> None:
        """
        Persiste un registro forestal en disco usando Pickle.

        Args:
            registro: Registro a persistir

        Raises:
            PersistenciaException: Si ocurre error al guardar
        """
        propietario = registro.get_propietario()
        
        # Crear directorio si no existe
        if not os.path.exists(DIRECTORIO_DATA):
            os.makedirs(DIRECTORIO_DATA)
        
        nombre_archivo = os.path.join(DIRECTORIO_DATA, f"{propietario}{EXTENSION_DATA}")
        
        file_handle = None
        try:
            file_handle = open(nombre_archivo, 'wb')
            pickle.dump(registro, file_handle)
            print(f"Registro de {propietario} persistido exitosamente en {nombre_archivo}")
        
        except Exception as e:
            tech_msg = MSG_PERSISTENCIA_ERROR_ESCRITURA_TECH.format(archivo=nombre_archivo)
            raise PersistenciaException(
                MSG_PERSISTENCIA_ERROR_ESCRITURA_USER,
                tech_msg,
                nombre_archivo,
                TipoOperacionPersistencia.ESCRITURA
            ) from e
        
        finally:
            if file_handle is not None:
                file_handle.close()

    @staticmethod
    def leer_registro(propietario: str) -> 'RegistroForestal':
        """
        Lee un registro forestal desde disco.

        Args:
            propietario: Nombre del propietario

        Returns:
            Registro forestal deserializado

        Raises:
            ValueError: Si el propietario es vacio
            PersistenciaException: Si ocurre error al leer
        """
        if not propietario or propietario.strip() == "":
            raise ValueError(MSG_PROPIETARIO_VACIO)
        
        nombre_archivo = os.path.join(DIRECTORIO_DATA, f"{propietario}{EXTENSION_DATA}")
        
        if not os.path.exists(nombre_archivo):
            tech_msg = MSG_PERSISTENCIA_ARCHIVO_NO_ENCONTRADO_TECH.format(archivo=nombre_archivo)
            raise PersistenciaException(
                MSG_PERSISTENCIA_ARCHIVO_NO_ENCONTRADO_USER,
                tech_msg,
                nombre_archivo,
                TipoOperacionPersistencia.LECTURA
            )
        
        file_handle = None
        try:
            file_handle = open(nombre_archivo, 'rb')
            registro = pickle.load(file_handle)
            print(f"Registro de {propietario} recuperado exitosamente desde {nombre_archivo}")
            return registro
        
        except Exception as e:
            tech_msg = MSG_PERSISTENCIA_ERROR_LECTURA_TECH.format(archivo=nombre_archivo)
            raise PersistenciaException(
                MSG_PERSISTENCIA_ERROR_LECTURA_USER,
                tech_msg,
                nombre_archivo,
                TipoOperacionPersistencia.LECTURA
            ) from e
        
        finally:
            if file_handle is not None:
                file_handle.close()

# ================================================================================
# ARCHIVO 4/4: tierra_service.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\servicios\terrenos\tierra_service.py
# ================================================================================

"""
Servicio para Tierra.

Logica de negocio para terrenos catastrales.
"""

# Local application
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.constantes import AGUA_INICIAL_PLANTACION


class TierraService:
    """
    Servicio para gestion de terrenos.

    Proporciona operaciones de negocio sobre terrenos catastrales.
    """

    def crear_tierra_con_plantacion(
        self,
        id_padron_catastral: int,
        superficie: float,
        domicilio: str,
        nombre_plantacion: str
    ) -> Tierra:
        """
        Crea un terreno con una plantacion asociada.

        Args:
            id_padron_catastral: ID del padron catastral
            superficie: Superficie en metros cuadrados
            domicilio: Domicilio del terreno
            nombre_plantacion: Nombre de la plantacion

        Returns:
            Tierra creada con plantacion asociada
        """
        tierra = Tierra(
            id_padron_catastral=id_padron_catastral,
            superficie=superficie,
            domicilio=domicilio
        )

        plantacion = Plantacion(
            nombre=nombre_plantacion,
            superficie=superficie,
            agua=AGUA_INICIAL_PLANTACION
        )

        tierra.set_finca(plantacion)

        return tierra

