
# Análisis de Orbea Monegros

Este proyecto es un paquete de Python para analizar el evento ciclista Orbea Monegros, incluyendo limpieza de datos, agrupamiento y visualización.

## Características
- Importar y explorar el dataset (EDA).
- Anonimizar nombres de ciclistas.
- Limpiar nombres de clubes y analizar la participación.
- Agrupar tiempos en intervalos de 20 minutos y generar histogramas.
- Identificar y analizar participantes clave, como los del club UCSC.

## Instalación

### Requisitos previos
- Python 3.8 o superior
- `pip` para la gestión de dependencias

### Pasos
1. Clona el repositorio:
   ```bash
   git clone https://github.com/Diego4498/orbea_monegros.git
   cd orbea_monegros
   ```
2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

### Ejecutar el Análisis
Ejecuta el script principal para realizar todas las funcionalidades de forma secuencial:
```bash
python main.py
```

### Opcional: Ejecutar Funciones Específicas
El script `main.py` permite ejecutar partes específicas del análisis de forma interactiva.

### Generar el Histograma
El histograma se guardará automáticamente en el directorio `img/` como `histograma.png`.

## Estructura del Proyecto
```
orbea_monegros/
├── orbea_package/           # Paquete que contiene los módulos principales
│   ├── __init__.py          # Inicializa el paquete
│   ├── eda.py               # Funciones para EDA y limpieza de datos
│   ├── grouping.py          # Funciones para agrupar tiempos y generar histogramas
│   ├── clubs.py             # Funciones para limpiar y analizar clubes
│   └── tests/               # Pruebas unitarias para cada módulo
│       ├── __init__.py      # Inicializa las pruebas
│       ├── test_eda.py      # Pruebas para `eda.py`
│       ├── test_grouping.py # Pruebas para `grouping.py`
│       └── test_clubs.py    # Pruebas para `clubs.py`
├── main.py                  # Script principal para ejecutar el proyecto
├── README.md                # Documentación del proyecto (este archivo)
├── LICENSE                  # Licencia del proyecto
├── requirements.txt         # Lista de dependencias
└── setup.py                 # Opcional: script de instalación
```

## Pruebas

Ejecuta las pruebas unitarias usando `pytest`:
```bash
pytest orbea_package/tests/
```

## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

### Resumen de la Licencia MIT:
- Eres libre de usar, copiar, modificar y distribuir este proyecto.
- Debes incluir el aviso de licencia original en cualquier copia del software.
- El software se proporciona "tal cual", sin garantías de ningún tipo.
