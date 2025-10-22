"""
Archivo integrador generado automaticamente
Directorio: /home/josiasvilches/cursada/disenosistemas/python-forestal
Fecha: 2025-10-22 09:43:42
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: buscar_paquete.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/buscar_paquete.py
# ================================================================================

"""
Script para buscar el paquete python_forestacion desde el directorio raiz del proyecto.
Incluye funcionalidad para integrar archivos Python en cada nivel del arbol de directorios.
"""
import os
import sys
from datetime import datetime


def buscar_paquete(directorio_raiz: str, nombre_paquete: str) -> list:
    """
    Busca un paquete Python en el directorio raiz y subdirectorios.

    Args:
        directorio_raiz: Directorio desde donde iniciar la busqueda
        nombre_paquete: Nombre del paquete a buscar

    Returns:
        Lista de rutas donde se encontro el paquete
    """
    paquetes_encontrados = []

    for raiz, directorios, archivos in os.walk(directorio_raiz):
        # Verificar si el directorio actual es el paquete buscado
        nombre_dir = os.path.basename(raiz)

        if nombre_dir == nombre_paquete:
            # Verificar que sea un paquete Python (contiene __init__.py)
            if '__init__.py' in archivos:
                paquetes_encontrados.append(raiz)
                print(f"[+] Paquete encontrado: {raiz}")
            else:
                print(f"[!] Directorio encontrado pero no es un paquete Python: {raiz}")

    return paquetes_encontrados


def obtener_archivos_python(directorio: str) -> list:
    """
    Obtiene todos los archivos Python en un directorio (sin recursion).

    Args:
        directorio: Ruta del directorio a examinar

    Returns:
        Lista de rutas completas de archivos .py
    """
    archivos_python = []
    try:
        for item in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, item)
            if os.path.isfile(ruta_completa) and item.endswith('.py'):
                # Excluir archivos integradores para evitar recursion infinita
                if item not in ['integrador.py', 'integradorFinal.py']:
                    archivos_python.append(ruta_completa)
    except PermissionError:
        print(f"[!] Sin permisos para leer: {directorio}")

    return sorted(archivos_python)


def obtener_subdirectorios(directorio: str) -> list:
    """
    Obtiene todos los subdirectorios inmediatos de un directorio.

    Args:
        directorio: Ruta del directorio a examinar

    Returns:
        Lista de rutas completas de subdirectorios
    """
    subdirectorios = []
    try:
        for item in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, item)
            if os.path.isdir(ruta_completa):
                # Excluir directorios especiales
                if not item.startswith('.') and item not in ['__pycache__', 'venv', '.venv']:
                    subdirectorios.append(ruta_completa)
    except PermissionError:
        print(f"[!] Sin permisos para leer: {directorio}")

    return sorted(subdirectorios)


def leer_contenido_archivo(ruta_archivo: str) -> str:
    """
    Lee el contenido de un archivo Python.

    Args:
        ruta_archivo: Ruta completa del archivo

    Returns:
        Contenido del archivo como string
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except Exception as error:
        print(f"[!] Error al leer {ruta_archivo}: {error}")
        return f"# Error al leer este archivo: {error}\n"


def crear_archivo_integrador(directorio: str, archivos_python: list) -> bool:
    """
    Crea un archivo integrador.py con el contenido de todos los archivos Python.

    Args:
        directorio: Directorio donde crear el archivo integrador
        archivos_python: Lista de rutas de archivos Python a integrar

    Returns:
        True si se creo exitosamente, False en caso contrario
    """
    if not archivos_python:
        return False

    ruta_integrador = os.path.join(directorio, 'integrador.py')

    try:
        with open(ruta_integrador, 'w', encoding='utf-8') as integrador:
            # Encabezado
            integrador.write('"""\n')
            integrador.write(f"Archivo integrador generado automaticamente\n")
            integrador.write(f"Directorio: {directorio}\n")
            integrador.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador.write(f"Total de archivos integrados: {len(archivos_python)}\n")
            integrador.write('"""\n\n')

            # Integrar cada archivo
            for idx, archivo in enumerate(archivos_python, 1):
                nombre_archivo = os.path.basename(archivo)
                integrador.write(f"# {'=' * 80}\n")
                integrador.write(f"# ARCHIVO {idx}/{len(archivos_python)}: {nombre_archivo}\n")
                integrador.write(f"# Ruta: {archivo}\n")
                integrador.write(f"# {'=' * 80}\n\n")

                contenido = leer_contenido_archivo(archivo)
                integrador.write(contenido)
                integrador.write("\n\n")

        print(f"[OK] Integrador creado: {ruta_integrador}")
        print(f"     Archivos integrados: {len(archivos_python)}")
        return True

    except Exception as error:
        print(f"[!] Error al crear integrador en {directorio}: {error}")
        return False


def procesar_directorio_recursivo(directorio: str, nivel: int = 0, archivos_totales: list = None) -> list:
    """
    Procesa un directorio de forma recursiva, creando integradores en cada nivel.
    Utiliza DFS (Depth-First Search) para llegar primero a los niveles mas profundos.

    Args:
        directorio: Directorio a procesar
        nivel: Nivel de profundidad actual (para logging)
        archivos_totales: Lista acumulativa de todos los archivos procesados

    Returns:
        Lista de todos los archivos Python procesados en el arbol
    """
    if archivos_totales is None:
        archivos_totales = []

    indentacion = "  " * nivel
    print(f"{indentacion}[INFO] Procesando nivel {nivel}: {os.path.basename(directorio)}")

    # Obtener subdirectorios
    subdirectorios = obtener_subdirectorios(directorio)

    # Primero, procesar recursivamente todos los subdirectorios (DFS)
    for subdir in subdirectorios:
        procesar_directorio_recursivo(subdir, nivel + 1, archivos_totales)

    # Despues de procesar subdirectorios, procesar archivos del nivel actual
    archivos_python = obtener_archivos_python(directorio)

    if archivos_python:
        print(f"{indentacion}[+] Encontrados {len(archivos_python)} archivo(s) Python")
        crear_archivo_integrador(directorio, archivos_python)
        # Agregar archivos a la lista total
        archivos_totales.extend(archivos_python)
    else:
        print(f"{indentacion}[INFO] No hay archivos Python en este nivel")

    return archivos_totales


def crear_integrador_final(directorio_raiz: str, archivos_totales: list) -> bool:
    """
    Crea un archivo integradorFinal.py con TODO el codigo fuente de todas las ramas.

    Args:
        directorio_raiz: Directorio donde crear el archivo integrador final
        archivos_totales: Lista completa de todos los archivos Python procesados

    Returns:
        True si se creo exitosamente, False en caso contrario
    """
    if not archivos_totales:
        print("[!] No hay archivos para crear el integrador final")
        return False

    ruta_integrador_final = os.path.join(directorio_raiz, 'integradorFinal.py')

    # Organizar archivos por directorio para mejor estructura
    archivos_por_directorio = {}
    for archivo in archivos_totales:
        directorio = os.path.dirname(archivo)
        if directorio not in archivos_por_directorio:
            archivos_por_directorio[directorio] = []
        archivos_por_directorio[directorio].append(archivo)

    try:
        with open(ruta_integrador_final, 'w', encoding='utf-8') as integrador_final:
            # Encabezado principal
            integrador_final.write('"""\n')
            integrador_final.write("INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO\n")
            integrador_final.write("=" * 76 + "\n")
            integrador_final.write(f"Directorio raiz: {directorio_raiz}\n")
            integrador_final.write(f"Fecha de generacion: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador_final.write(f"Total de archivos integrados: {len(archivos_totales)}\n")
            integrador_final.write(f"Total de directorios procesados: {len(archivos_por_directorio)}\n")
            integrador_final.write("=" * 76 + "\n")
            integrador_final.write('"""\n\n')

            # Tabla de contenidos
            integrador_final.write("# " + "=" * 78 + "\n")
            integrador_final.write("# TABLA DE CONTENIDOS\n")
            integrador_final.write("# " + "=" * 78 + "\n\n")

            contador_global = 1
            for directorio in sorted(archivos_por_directorio.keys()):
                dir_relativo = os.path.relpath(directorio, directorio_raiz)
                integrador_final.write(f"# DIRECTORIO: {dir_relativo}\n")
                for archivo in sorted(archivos_por_directorio[directorio]):
                    nombre_archivo = os.path.basename(archivo)
                    integrador_final.write(f"#   {contador_global}. {nombre_archivo}\n")
                    contador_global += 1
                integrador_final.write("#\n")

            integrador_final.write("\n\n")

            # Contenido completo organizado por directorio
            contador_global = 1
            for directorio in sorted(archivos_por_directorio.keys()):
                dir_relativo = os.path.relpath(directorio, directorio_raiz)

                # Separador de directorio
                integrador_final.write("\n" + "#" * 80 + "\n")
                integrador_final.write(f"# DIRECTORIO: {dir_relativo}\n")
                integrador_final.write("#" * 80 + "\n\n")

                # Procesar cada archivo del directorio
                for archivo in sorted(archivos_por_directorio[directorio]):
                    nombre_archivo = os.path.basename(archivo)

                    integrador_final.write(f"# {'=' * 78}\n")
                    integrador_final.write(f"# ARCHIVO {contador_global}/{len(archivos_totales)}: {nombre_archivo}\n")
                    integrador_final.write(f"# Directorio: {dir_relativo}\n")
                    integrador_final.write(f"# Ruta completa: {archivo}\n")
                    integrador_final.write(f"# {'=' * 78}\n\n")

                    contenido = leer_contenido_archivo(archivo)
                    integrador_final.write(contenido)
                    integrador_final.write("\n\n")

                    contador_global += 1

            # Footer
            integrador_final.write("\n" + "#" * 80 + "\n")
            integrador_final.write("# FIN DEL INTEGRADOR FINAL\n")
            integrador_final.write(f"# Total de archivos: {len(archivos_totales)}\n")
            integrador_final.write(f"# Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador_final.write("#" * 80 + "\n")

        print(f"\n[OK] Integrador final creado: {ruta_integrador_final}")
        print(f"     Total de archivos integrados: {len(archivos_totales)}")
        print(f"     Total de directorios procesados: {len(archivos_por_directorio)}")

        # Mostrar tamanio del archivo
        tamanio = os.path.getsize(ruta_integrador_final)
        if tamanio < 1024:
            tamanio_str = f"{tamanio} bytes"
        elif tamanio < 1024 * 1024:
            tamanio_str = f"{tamanio / 1024:.2f} KB"
        else:
            tamanio_str = f"{tamanio / (1024 * 1024):.2f} MB"
        print(f"     Tamanio del archivo: {tamanio_str}")

        return True

    except Exception as error:
        print(f"[!] Error al crear integrador final: {error}")
        return False


def integrar_arbol_directorios(directorio_raiz: str) -> None:
    """
    Inicia el proceso de integracion para todo el arbol de directorios.

    Args:
        directorio_raiz: Directorio raiz desde donde comenzar
    """
    print("\n" + "=" * 80)
    print("INICIANDO INTEGRACION DE ARCHIVOS PYTHON")
    print("=" * 80)
    print(f"Directorio raiz: {directorio_raiz}\n")

    # Procesar directorios y obtener lista de todos los archivos
    archivos_totales = procesar_directorio_recursivo(directorio_raiz)

    print("\n" + "=" * 80)
    print("INTEGRACION POR NIVELES COMPLETADA")
    print("=" * 80)

    # Crear integrador final con todos los archivos
    if archivos_totales:
        print("\n" + "=" * 80)
        print("CREANDO INTEGRADOR FINAL")
        print("=" * 80)
        crear_integrador_final(directorio_raiz, archivos_totales)

    print("\n" + "=" * 80)
    print("PROCESO COMPLETO FINALIZADO")
    print("=" * 80)


def main():
    """Funcion principal del script."""
    # Obtener el directorio raiz del proyecto (donde esta este script)
    directorio_raiz = os.path.dirname(os.path.abspath(__file__))

    # Verificar argumentos de linea de comandos
    if len(sys.argv) > 1:
        comando = sys.argv[1].lower()

        if comando == "integrar":
            # Modo de integracion de archivos
            if len(sys.argv) > 2:
                directorio_objetivo = sys.argv[2]
                if not os.path.isabs(directorio_objetivo):
                    directorio_objetivo = os.path.join(directorio_raiz, directorio_objetivo)
            else:
                directorio_objetivo = directorio_raiz

            if not os.path.isdir(directorio_objetivo):
                print(f"[!] El directorio no existe: {directorio_objetivo}")
                return 1

            integrar_arbol_directorios(directorio_objetivo)
            return 0

        elif comando == "help" or comando == "--help" or comando == "-h":
            print("Uso: python buscar_paquete.py [COMANDO] [OPCIONES]")
            print("")
            print("Comandos disponibles:")
            print("  (sin argumentos)     Busca el paquete python_forestacion")
            print("  integrar [DIR]       Integra archivos Python en el arbol de directorios")
            print("                       DIR: directorio raiz (por defecto: directorio actual)")
            print("  help                 Muestra esta ayuda")
            print("")
            print("Ejemplos:")
            print("  python buscar_paquete.py")
            print("  python buscar_paquete.py integrar")
            print("  python buscar_paquete.py integrar python_forestacion")
            return 0

        else:
            print(f"[!] Comando desconocido: {comando}")
            print("    Use 'python buscar_paquete.py help' para ver los comandos disponibles")
            return 1

    # Modo por defecto: buscar paquete
    print(f"[INFO] Buscando desde: {directorio_raiz}")
    print(f"[INFO] Buscando paquete: python_forestacion")
    print("")

    # Buscar el paquete
    paquetes = buscar_paquete(directorio_raiz, "python_forestacion")

    print("")
    if paquetes:
        print(f"[OK] Se encontraron {len(paquetes)} paquete(s):")
        for paquete in paquetes:
            print(f"  - {paquete}")

            # Mostrar estructura basica del paquete
            print(f"    Contenido:")
            try:
                contenido = os.listdir(paquete)
                for item in sorted(contenido)[:10]:  # Mostrar primeros 10 items
                    ruta_item = os.path.join(paquete, item)
                    if os.path.isdir(ruta_item):
                        print(f"      [DIR]  {item}")
                    else:
                        print(f"      [FILE] {item}")
                if len(contenido) > 10:
                    print(f"      ... y {len(contenido) - 10} items mas")
            except PermissionError:
                print(f"      [!] Sin permisos para leer el directorio")
    else:
        print("[!] No se encontro el paquete python_forestacion")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

# ================================================================================
# ARCHIVO 2/3: evaluador.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/evaluador.py
# ================================================================================

#!/usr/bin/env python3
"""
Script helper para evaluacion automatizada.
Uso: python evaluador_automatico.py --proyecto /path/to/proyecto --config config.json
"""

import json
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Any

class EvaluadorAutomatico:
    def __init__(self, proyecto_path: str, config_path: str):
        self.proyecto_path = Path(proyecto_path)
        self.config = self._cargar_config(config_path)
        self.resultados = []

    def _cargar_config(self, config_path: str) -> Dict:
        with open(config_path, 'r') as f:
            return json.load(f)

    def ejecutar_comando(self, comando: str) -> Dict[str, Any]:
        """Ejecuta comando y retorna resultado."""
        try:
            resultado = subprocess.run(
                comando,
                shell=True,
                cwd=self.proyecto_path,
                capture_output=True,
                text=True,
                timeout=30
            )
            return {
                'exitcode': resultado.returncode,
                'stdout': resultado.stdout,
                'stderr': resultado.stderr,
                'exito': resultado.returncode == 0
            }
        except subprocess.TimeoutExpired:
            return {
                'exitcode': -1,
                'stdout': '',
                'stderr': 'Timeout',
                'exito': False
            }

    def evaluar_criterio(self, criterio: Dict) -> Dict:
        """Evalua un criterio individual."""
        resultado_cmd = self.ejecutar_comando(criterio['comando'])

        # Contar coincidencias
        coincidencias = resultado_cmd['stdout'].count('\n')

        # Evaluar segun threshold
        inverted = criterio.get('inverted', False)
        if inverted:
            pasado = coincidencias <= criterio['threshold']
        else:
            pasado = coincidencias >= criterio['threshold']

        return {
            'id': criterio['id'],
            'categoria': criterio['categoria'],
            'pasado': pasado,
            'coincidencias': coincidencias,
            'threshold': criterio['threshold'],
            'puntaje_max': criterio['puntaje'],
            'puntaje_obtenido': criterio['puntaje'] if pasado else 0,
            'peso': criterio['peso'],
            'output': resultado_cmd['stdout'][:500]  # Primeros 500 chars
        }

    def evaluar_todos(self) -> Dict:
        """Evalua todos los criterios."""
        for criterio in self.config['evaluacion']['criterios']:
            resultado = self.evaluar_criterio(criterio)
            self.resultados.append(resultado)

        # Calcular totales
        puntaje_total = sum(r['puntaje_obtenido'] for r in self.resultados)
        puntaje_maximo = self.config['evaluacion']['puntaje_maximo']
        porcentaje = (puntaje_total / puntaje_maximo) * 100

        # Determinar calificacion
        if porcentaje >= 90:
            calificacion = 'Excelente'
        elif porcentaje >= 80:
            calificacion = 'Muy Bueno'
        elif porcentaje >= 70:
            calificacion = 'Bueno'
        elif porcentaje >= 60:
            calificacion = 'Suficiente'
        else:
            calificacion = 'Insuficiente'

        return {
            'puntaje_total': puntaje_total,
            'puntaje_maximo': puntaje_maximo,
            'porcentaje': round(porcentaje, 2),
            'calificacion': calificacion,
            'aprobado': porcentaje >= 70,
            'criterios_pasados': sum(1 for r in self.resultados if r['pasado']),
            'criterios_fallados': sum(1 for r in self.resultados if not r['pasado']),
            'resultados': self.resultados
        }

    def generar_reporte_json(self, output_path: str):
        """Genera reporte en formato JSON."""
        resumen = self.evaluar_todos()
        with open(output_path, 'w') as f:
            json.dump(resumen, f, indent=2)

    def generar_reporte_markdown(self, output_path: str):
        """Genera reporte en formato Markdown."""
        resumen = self.evaluar_todos()

        markdown = f"""# Reporte de Evaluacion Automatizada

**Proyecto**: {self.proyecto_path.name}
**Fecha**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Resumen

- **Puntaje Total**: {resumen['puntaje_total']}/{resumen['puntaje_maximo']}
- **Porcentaje**: {resumen['porcentaje']}%
- **Calificacion**: {resumen['calificacion']}
- **Estado**: {'APROBADO' if resumen['aprobado'] else 'NO APROBADO'}

## Detalles

| Criterio | Categoria | Pasado | Puntaje | Peso |
|----------|-----------|--------|---------|------|
"""
        for r in self.resultados:
            estado = '✓' if r['pasado'] else '✗'
            markdown += f"| {r['id']} | {r['categoria']} | {estado} | {r['puntaje_obtenido']}/{r['puntaje_max']} | {r['peso']} |\n"

        with open(output_path, 'w') as f:
            f.write(markdown)


if __name__ == '__main__':
    import argparse
    from datetime import datetime

    parser = argparse.ArgumentParser(description='Evaluador automatico de proyectos')
    parser.add_argument('--proyecto', required=True, help='Path al proyecto')
    parser.add_argument('--config', required=True, help='Path al archivo de configuracion')
    parser.add_argument('--output-json', help='Path para reporte JSON')
    parser.add_argument('--output-md', help='Path para reporte Markdown')

    args = parser.parse_args()

    evaluador = EvaluadorAutomatico(args.proyecto, args.config)

    if args.output_json:
        evaluador.generar_reporte_json(args.output_json)
        print(f"Reporte JSON generado: {args.output_json}")

    if args.output_md:
        evaluador.generar_reporte_markdown(args.output_md)
        print(f"Reporte Markdown generado: {args.output_md}")

    # Imprimir resumen en consola
    resumen = evaluador.evaluar_todos()
    print(f"\n=== RESUMEN ===")
    print(f"Puntaje: {resumen['puntaje_total']}/{resumen['puntaje_maximo']} ({resumen['porcentaje']}%)")
    print(f"Calificacion: {resumen['calificacion']}")
    print(f"Estado: {'APROBADO' if resumen['aprobado'] else 'NO APROBADO'}")

    sys.exit(0 if resumen['aprobado'] else 1)

# ================================================================================
# ARCHIVO 3/3: main.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/main.py
# ================================================================================

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

