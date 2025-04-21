# Documentaci�n del Proyecto: Documentator-MCP

## Estructura del Proyecto
El proyecto tiene la siguiente estructura:

```
main.py
pyproject.toml
README.md
uv.lock
```

## Descripci�n
Este proyecto es una herramienta para documentar autom�ticamente un proyecto utilizando agentes MCP como Claude, Copilot u otros. Est� dise�ado para ejecutarse como un servidor MCP.

- **Nombre del proyecto**: documentator-mcp
- **Versi�n**: 0.1.0
- **Versi�n m�nima de Python requerida**: >= 3.13

## Dependencias
El proyecto utiliza las siguientes dependencias:

- `mcp[cli]>=1.6.0`: Proporciona funcionalidades de cliente MCP.
- `plantuml>=0.3.0`: Para generar diagramas UML.
- `six>=1.17.0`: Biblioteca de compatibilidad entre Python 2 y 3.

Dependencias de desarrollo:
- `documentator-mcp`

## CLI
El proyecto incluye un servidor MCP que se ejecuta con el siguiente comando:

```bash
uv --directory path/documentator-mcp run main.py
```

Variables de entorno importantes:
- `WD`: Directorio de trabajo.
- `IGNORE_NAMES`: Nombres de archivos o carpetas a ignorar, como `.git`, `.venv`, `__pycache__`.

## APIs y Herramientas
El proyecto define varias herramientas MCP:

1. **get_files**: Devuelve los archivos y directorios en una ruta relativa.
2. **tree**: Genera un �rbol de archivos hasta una profundidad m�xima.
3. **read_file**: Lee el contenido de un archivo.
4. **write_file**: Escribe contenido en un archivo.
5. **create_dir**: Crea un directorio.
6. **diagramPlantUML**: Genera diagramas UML y los guarda en formato SVG.

## Ejemplo de Uso
Un ejemplo de c�mo generar un diagrama UML:

```python
from plantuml import PlantUML

plantuml_client = PlantUML(url='http://www.plantuml.com/plantuml/svg/')
diagram_code = """@startuml
Alice -> Bob: Hello
@enduml"""
svg_content = plantuml_client.processes(diagram_code)
with open('diagram.svg', 'wb') as file:
    file.write(svg_content)
```

## ENTRYPOINT
El punto de entrada del proyecto es el archivo `main.py`, que inicializa y ejecuta el servidor MCP.

## ENDPOINTS
El servidor MCP se ejecuta utilizando transporte `stdio`.

## DataClasses
No se identificaron DataClasses en el c�digo proporcionado.

## Notas Adicionales
- El archivo `README.md` proporciona una breve descripci�n del proyecto.
- El archivo `pyproject.toml` define las configuraciones del proyecto y sus dependencias.