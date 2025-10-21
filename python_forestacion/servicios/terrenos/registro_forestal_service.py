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