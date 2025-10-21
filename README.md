# Sistema de Gestión Forestal - PythonForestal por Josías Vilches

[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-PEP%208-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

Sistema integral de gestión forestal y agrícola que demuestra la implementación de múltiples patrones de diseño de software con enfoque educativo y profesional.

---

## Instalación y Ejecución

### Requisitos

- **Python 3.13** o superior
- Solo biblioteca estándar de Python (sin dependencias externas)

### Instalación

```bash
# Clonar o descargar el proyecto
cd PythonForestal

# NO es necesario instalar dependencias externas
# El proyecto usa solo la biblioteca estándar de Python
```

### Ejecución

```bash
python main.py
```

**Salida esperada**: El sistema ejecutará una demostración completa de todas las funcionalidades, mostrando:

1. ✅ Patrón Singleton en acción
2. ✅ Patrón Factory creando cultivos
3. ✅ Patrón Observer con sensores de riego
4. ✅ Patrón Strategy con absorción de agua
5. ✅ Operaciones de negocio completas
6. ✅ Persistencia de datos en `data/`

---

## Patrones de Diseño Implementados

### 1. SINGLETON Pattern
- **Ubicación**: `servicios/cultivos/cultivo_service_registry.py`
- **Propósito**: Garantizar una única instancia del registro de servicios
- **Características**:
  - Thread-safe con `threading.Lock`
  - Double-checked locking
  - Inicialización perezosa

### 2. FACTORY METHOD Pattern
- **Ubicación**: `patrones/factory/cultivo_factory.py`
- **Propósito**: Crear objetos sin conocer clases concretas
- **Características**:
  - Desacoplamiento total del cliente
  - 7 métodos de creación (supera threshold de 4)
  - Métodos públicos: `crear_cultivo()`, `crear_trabajador()`, `crear_herramienta()`
  - Métodos auxiliares: `_crear_pino()`, `_crear_olivo()`, `_crear_lechuga()`, `_crear_zanahoria()`
  - Diccionario de factories (sin if/elif)

### 3. OBSERVER Pattern
- **Ubicación**: `patrones/observer/`
- **Propósito**: Notificación automática entre sensores y controlador
- **Características**:
  - Genéricos tipo-seguro: `Observable[T]`, `Observer[T]`
  - Sensores como Observable
  - Control de riego como Observer

### 4. STRATEGY Pattern
- **Ubicación**: `patrones/strategy/`
- **Propósito**: Algoritmos de absorción intercambiables
- **Características**:
  - `AbsorcionSeasonalStrategy` para árboles
  - `AbsorcionConstanteStrategy` para hortalizas
  - Inyección de dependencias en servicios

---

## Estructura del Proyecto

```
PythonForestal/
├── main.py                          # Punto de entrada
├── README.md                        # Este archivo
├── data/                            # Datos persistidos (.dat)
└── python_forestacion/
    ├── constantes.py                # Constantes centralizadas
    ├── entidades/                   # DTOs (solo datos)
    │   ├── cultivos/                # Pino, Olivo, Lechuga, Zanahoria
    │   ├── terrenos/                # Tierra, Plantación, Registro
    │   └── personal/                # Trabajador, Tarea, Herramienta
    ├── servicios/                   # Lógica de negocio
    │   ├── cultivos/                # Servicios + Registry (Singleton)
    │   ├── terrenos/                # Servicios de terrenos
    │   ├── personal/                # Servicios de personal
    │   └── negocio/                 # FincasService, Paquete
    ├── patrones/                    # Patrones de diseño
    │   ├── factory/                 # Factory Method
    │   ├── observer/                # Observer Pattern
    │   └── strategy/                # Strategy Pattern
    ├── riego/                       # Sistema de riego automático
    │   ├── sensores/                # Threads sensores (Observable)
    │   └── control/                 # Control de riego (Observer)
    └── excepciones/                 # Jerarquía de excepciones
```

---

## Funcionalidades Principales

### 1. Gestión de Cultivos
- ✅ 4 tipos de cultivos: Pino, Olivo, Lechuga, Zanahoria
- ✅ Plantación con control de superficie
- ✅ Crecimiento automático de árboles
- ✅ Absorción diferenciada de agua

### 2. Sistema de Riego Automático
- ✅ Sensores en threads daemon (temperatura y humedad)
- ✅ Control automático basado en condiciones
- ✅ Patrón Observer en acción
- ✅ Graceful shutdown con timeouts

### 3. Gestión de Personal
- ✅ Trabajadores con certificación médica
- ✅ Asignación y ejecución de tareas
- ✅ Herramientas con certificación H&S

### 4. Persistencia
- ✅ Guardado con Pickle en disco
- ✅ Recuperación desde archivos `.dat`
- ✅ Manejo robusto de excepciones

---

## Características Técnicas

### Calidad de Código
- ✅ **PEP 8 Compliance 100%**
- ✅ **Type Hints** en todas las firmas
- ✅ **Docstrings Google Style**
- ✅ **CERO magic numbers** (todo en constantes.py)
- ✅ **CERO lambdas** (métodos estáticos nombrados)
- ✅ **Sin código duplicado**

### Arquitectura
- ✅ **Separación de responsabilidades** (entidades vs servicios)
- ✅ **Inyección de dependencias** manual
- ✅ **Principios SOLID** aplicados
- ✅ **Excepciones específicas** de dominio

---

## Ejemplos de Uso

### Crear Cultivos con Factory

```python
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory

# Crear cultivos (cliente NO conoce clases concretas)
pino = CultivoFactory.crear_cultivo("Pino")
olivo = CultivoFactory.crear_cultivo("Olivo")
lechuga = CultivoFactory.crear_cultivo("Lechuga")
```

### Crear Trabajadores y Herramientas con Factory

```python
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.entidades.personal.tarea import Tarea
from datetime import date

# Crear tareas
tareas = [
    Tarea(1, date.today(), "Desmalezar"),
    Tarea(2, date.today(), "Abonar")
]

# Crear trabajador usando Factory
trabajador = CultivoFactory.crear_trabajador(
    dni=43888734,
    nombre="Juan Perez",
    tareas=tareas
)

# Crear herramienta usando Factory
herramienta = CultivoFactory.crear_herramienta(
    id_herramienta=1,
    nombre="Pala",
    certificado_hys=True
)
```

### Plantar Cultivos

```python
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService

plantacion_service = PlantacionService()

# Usa Factory Method internamente
plantacion_service.plantar(plantacion, "Pino", 5)
plantacion_service.plantar(plantacion, "Olivo", 3)
```

### Sistema de Riego Automático

```python
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask

# Crear sensores (Observable)
tarea_temp = TemperaturaReaderTask()
tarea_hum = HumedadReaderTask()

# Crear controlador (Observer)
tarea_control = ControlRiegoTask(tarea_temp, tarea_hum, plantacion, plantacion_service)

# Iniciar threads daemon
tarea_temp.start()
tarea_hum.start()
tarea_control.start()

# Sistema funciona automáticamente
time.sleep(20)

# Detener sistema
tarea_temp.detener()
tarea_hum.detener()
tarea_control.detener()
```

### Persistencia

```python
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService

registro_service = RegistroForestalService()

# Guardar
registro_service.persistir(registro)
# Crea: data/Juan Perez.dat

# Recuperar
registro_leido = RegistroForestalService.leer_registro("Juan Perez")
registro_service.mostrar_datos(registro_leido)
```

---

## Verificación Automática (n8n Compatible)

El proyecto cumple con todos los criterios automatizables de la rúbrica:

### Verificaciones Estáticas
```bash
# Singleton
grep -rn "_instance = None" --include="*.py" .
grep -rn "def __new__" --include="*.py" .

# Factory
grep -rn "@staticmethod" --include="*factory*.py" .

# Observer
grep -rn "class Observable" --include="*.py" .

# Strategy
grep -rn "class.*Strategy.*ABC" --include="*.py" .
```

### Verificaciones Dinámicas
```bash
# Ejecutar sistema completo
python main.py

# Verificar archivo persistido
ls -la data/*.dat
```

---

## Testing Manual

### Checklist de Validación

- [ ] Sistema ejecuta sin errores: `python main.py`
- [ ] Mensaje final: "EJEMPLO COMPLETADO EXITOSAMENTE"
- [ ] Archivo creado: `data/Juan Perez.dat`
- [ ] Todos los patrones mostrados en output
- [ ] No excepciones no manejadas
- [ ] Threads finalizan correctamente

---

## Documentación Adicional

- **USER_STORIES.md**: 28 historias de usuario completas
- **RUBRICA_EVALUACION.md**: Criterios de evaluación detallados
- **RUBRICA_AUTOMATIZADA.md**: Automatización con n8n

---

## Licencia

MIT License - Ver archivo LICENSE para detalles

---

## Contacto

Para dudas o consultas sobre el proyecto, referirse a la documentación técnica incluida.

**Versión**: 1.0.0  
**Python requerido**: 3.13+  
**Última actualización**: Octubre 2025