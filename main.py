"""
Sistema de Gestion Forestal - Demostracion Completa.

Este modulo demuestra el funcionamiento completo del sistema,
incluyendo los 4 patrones de diseno implementados.
"""

# Standard library
import time
from datetime import date

# Local application
from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService
from python_forestacion.servicios.personal.trabajador_service import TrabajadorService
from python_forestacion.servicios.negocio.fincas_service import FincasService
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask
from python_forestacion.constantes import THREAD_JOIN_TIMEOUT


def imprimir_separador(titulo: str = "") -> None:
    """
    Imprime un separador visual.

    Args:
        titulo: Titulo opcional para el separador
    """
    print("\n" + "=" * 70)
    if titulo:
        print(f"         {titulo}")
        print("=" * 70)


def imprimir_seccion(titulo: str) -> None:
    """
    Imprime titulo de seccion.

    Args:
        titulo: Titulo de la seccion
    """
    print("\n" + "-" * 70)
    print(f"  {titulo}")
    print("-" * 70)


def main():
    """
    Funcion principal que ejecuta la demostracion completa del sistema.
    """
    imprimir_separador("SISTEMA DE GESTION FORESTAL - PATRONES DE DISENO")

    # ========================================================================
    # PATRON SINGLETON: CultivoServiceRegistry
    # ========================================================================
    imprimir_seccion("PATRON SINGLETON: Inicializando servicios")
    
    registry1 = CultivoServiceRegistry()
    registry2 = CultivoServiceRegistry.get_instance()
    
    if registry1 is registry2:
        print("[OK] Todos los servicios comparten la misma instancia del Registry")
    else:
        print("[ERROR] Singleton no funciona correctamente")

    # ========================================================================
    # CREACION DE TERRENO Y PLANTACION
    # ========================================================================
    imprimir_seccion("1. Creando tierra con plantacion...")
    
    tierra_service = TierraService()
    terreno = tierra_service.crear_tierra_con_plantacion(
        id_padron_catastral=1,
        superficie=10000.0,
        domicilio="Agrelo, Mendoza",
        nombre_plantacion="Finca del Madero"
    )
    
    plantacion = terreno.get_finca()
    print(f"Terreno creado: Padron {terreno.get_id_padron_catastral()}")
    print(f"Plantacion: {plantacion.get_nombre()}")
    print(f"Superficie disponible: {plantacion.get_superficie()} m2")
    print(f"Agua disponible: {plantacion.get_agua_disponible()} L")

    # ========================================================================
    # CREAR REGISTRO FORESTAL
    # ========================================================================
    imprimir_seccion("2. Creando registro forestal...")
    
    registro = RegistroForestal(
        id_padron=1,
        tierra=terreno,
        plantacion=plantacion,
        propietario="Juan Perez",
        avaluo=50309233.55
    )
    print("Registro forestal creado exitosamente")

    # ========================================================================
    # PATRON FACTORY: Plantar cultivos
    # ========================================================================
    imprimir_seccion("PATRON FACTORY: Plantando cultivos")
    
    plantacion_service = PlantacionService()
    
    print("\nPlantando cultivos usando Factory Method:")
    plantacion_service.plantar(plantacion, "Pino", 5)
    plantacion_service.plantar(plantacion, "Olivo", 5)
    plantacion_service.plantar(plantacion, "Lechuga", 5)
    plantacion_service.plantar(plantacion, "Zanahoria", 5)
    
    print(f"\nSuperficie ocupada: {plantacion.get_superficie_ocupada()} m2")
    print(f"Cultivos plantados: {len(plantacion.get_cultivos())}")

    # ========================================================================
    # PATRON OBSERVER + STRATEGY: Sistema de riego automatizado
    # ========================================================================
    imprimir_seccion("PATRON OBSERVER + STRATEGY: Iniciando riego automatizado")
    
    print("\nCreando sensores (Observable)...")
    tarea_temp = TemperaturaReaderTask()
    tarea_hum = HumedadReaderTask()
    
    print("Creando controlador de riego (Observer)...")
    tarea_control = ControlRiegoTask(
        sensor_temperatura=tarea_temp,
        sensor_humedad=tarea_hum,
        plantacion=plantacion,
        plantacion_service=plantacion_service
    )
    
    print("\nIniciando threads daemon...")
    tarea_temp.start()
    tarea_hum.start()
    tarea_control.start()
    
    print("Sistema de riego automatico activo por 20 segundos...")
    print("(Los cultivos absorben agua segun su estrategia: Seasonal para arboles, Constante para hortalizas)")
    
    time.sleep(20)
    
    print("\nDeteniendo sistema de riego...")
    tarea_temp.detener()
    tarea_hum.detener()
    tarea_control.detener()
    
    tarea_temp.join(timeout=THREAD_JOIN_TIMEOUT)
    tarea_hum.join(timeout=THREAD_JOIN_TIMEOUT)
    tarea_control.join(timeout=THREAD_JOIN_TIMEOUT)
    
    print("Sistema de riego detenido correctamente")

    # ========================================================================
    # GESTION DE TRABAJADORES
    # ========================================================================
    imprimir_seccion("3. Gestionando trabajadores")
    
    # Crear tareas
    tareas = [
        Tarea(1, date.today(), "Desmalezar"),
        Tarea(2, date.today(), "Abonar"),
        Tarea(3, date.today(), "Marcar surcos")
    ]
    
    # PATRON FACTORY: Crear trabajador usando Factory Method
    print("\nCreando trabajador y herramienta usando Factory Method:")
    from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
    
    trabajador = CultivoFactory.crear_trabajador(
        dni=43888734,
        nombre="Juan Perez",
        tareas=tareas
    )
    print(f"Trabajador creado: {trabajador.get_nombre()} (DNI: {trabajador.get_dni()})")
    
    # Crear herramienta usando Factory Method
    herramienta = CultivoFactory.crear_herramienta(
        id_herramienta=1,
        nombre="Pala",
        certificado_hys=True
    )
    print(f"Herramienta creada: {herramienta.get_nombre()} (Certificado H&S: {herramienta.tiene_certificado_hys()})")
    
    # Asignar trabajadores a plantacion
    plantacion.set_trabajadores([trabajador])
    print(f"\nTrabajador {trabajador.get_nombre()} asignado a plantacion")
    
    # Asignar apto medico
    trabajador_service = TrabajadorService()
    trabajador_service.asignar_apto_medico(
        trabajador=trabajador,
        apto=True,
        fecha_emision=date.today(),
        observaciones="Estado de salud: excelente"
    )
    
    # Ejecutar tareas
    print("\nEjecutando tareas del dia:")
    trabajador_service.trabajar(
        trabajador=trabajador,
        fecha=date.today(),
        util=herramienta
    )

    # ========================================================================
    # OPERACIONES DE NEGOCIO
    # ========================================================================
    imprimir_seccion("4. Operaciones de negocio de alto nivel")
    
    fincas_service = FincasService()
    fincas_service.add_finca(registro)
    
    # Fumigar
    fincas_service.fumigar(id_padron=1, plaguicida="insecto organico")
    
    # Cosechar y empaquetar por tipo
    print("\nCosechando cultivos por tipo:")
    caja_lechugas = fincas_service.cosechar_yempaquetar(Lechuga)
    caja_lechugas.mostrar_contenido_caja()
    
    caja_pinos = fincas_service.cosechar_yempaquetar(Pino)
    caja_pinos.mostrar_contenido_caja()

    # ========================================================================
    # PERSISTENCIA
    # ========================================================================
    imprimir_seccion("5. Persistencia de datos")
    
    registro_service = RegistroForestalService()
    
    print("\nPersistiendo registro forestal...")
    registro_service.persistir(registro)
    
    print("\nRecuperando registro desde disco...")
    registro_leido = RegistroForestalService.leer_registro("Juan Perez")
    registro_service.mostrar_datos(registro_leido)

    # ========================================================================
    # FIN DE DEMOSTRACION
    # ========================================================================
    imprimir_separador("EJEMPLO COMPLETADO EXITOSAMENTE")
    print("  [OK] SINGLETON   - CultivoServiceRegistry (instancia unica)")
    print("  [OK] FACTORY     - Creacion de cultivos, trabajadores y herramientas")
    print("  [OK] OBSERVER    - Sistema de sensores y eventos")
    print("  [OK] STRATEGY    - Algoritmos de absorcion de agua")
    imprimir_separador()


if __name__ == "__main__":
    main()