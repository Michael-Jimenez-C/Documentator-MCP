# Documentation for Documentator-MCP

## Project Structure
The project has the following structure:
```
main.py
pyproject.toml
README.md
uv.lock
```

## Dependencies
The project uses the following dependencies:
- `mcp[cli]>=1.6.0`: Provides CLI tools for MCP.

### Development Dependencies
- `documentator-mcp`: Included as a development dependency.

## Description
This project, `documentator-mcp`, is designed to work with Python version `>=3.13`. It provides tools for managing and documenting MCP-based projects.

## APIs and Tools
The project defines several tools and APIs using the `mcp` framework:

### Tools
1. **get_files(relative_path: str) -> dict**
   - Retrieves a list of directories and files in the specified relative path.

2. **tree(relative_path: str, max_deep: int = 5) -> dict**
   - Recursively lists files and directories up to a specified depth.

3. **read_file(file_relative_path: str) -> str**
   - Reads the content of a file.

4. **write_file(file_relative_path: str, content: str) -> None**
   - Writes content to a file.

5. **create_dir(relative_path: str) -> None**
   - Creates a directory at the specified relative path.

6. **diagram(diagram_type: str, diagram_code: str, path: str) -> None**
   - Generates and saves a diagram using Mermaid.

### Prompt
The project includes a prompt for generating documentation:
```python
@mcp.prompt()
def documentation_prompt() -> str:
    return """
    Eres el encargado de documentar el c�digo del proyecto.
    Vas a analizar el codigo del proyecto, y sus dependencias, luego vas a generar una carpeta doc y un archivo DOC.md en donde vas a documentar todo.
    Las secciones obligatorias son: Estructura del proyecto, dependencias, Descripci�n con la versi�n de python.
    Las secciones opcionales pero importantes son: CLI, APIs, ENDPOINTS, ENTRYPOINTS, DataClasses, y cualquier otra secci�n que consideres necesaria.
    La documentaci�n debe ser clara y concisa, y debe incluir ejemplos de uso y cualquier otra informaci�n relevantes si estos aparecen en los docstrings.

    Puedes generar imagenes, las cuales van a estar guardadas en una carpeta doc_images.

    Puedes documentar utilizando mermaid para un diagrama, no hagas diagramas de clases.

    aquellas partes que no puedas completar por tu cuenta en el markdown puedes dejarlo como un comentario.
    """
```

## Entry Point
The entry point for the project is `main.py`, which initializes and runs the MCP server using the `mcp.run()` method.

## Examples
### Example Usage of `get_files`
```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Documentator-MCP")

@mcp.tool()
async def get_files(relative_path: str) -> dict:
    # Implementation here
    pass
```

### Example Usage of `diagram`
```python
from mermaid.graph import Graph

diag = Graph("sequenceDiagram", "Alice->>Bob: Hello Bob")
diag.save("diagram.png")
```

## Additional Notes
- The project uses environment variables such as `WD` and `IGNORE_NAMES` for configuration.
- The `santize_path` function ensures paths are within the working directory.

## TEST PROMPT

```
Solo utilizando herramientas del mcp-documentator, Eres el encargado de documentar el código del proyecto.
Vas a analizar el codigo del proyecto, y sus dependencias, luego vas a generar una carpeta doc y un archivo DOC.md en donde vas a documentar todo.
Las secciones obligatorias son: Estructura del proyecto, dependencias, Descripción con la versión de python.
Las secciones opcionales pero importantes son: CLI, APIs, ENDPOINTS, ENTRYPOINTS, DataClasses, y cualquier otra sección que consideres necesaria.
La documentación debe ser clara y concisa, y debe incluir ejemplos de uso y cualquier otra información relevantes si estos aparecen en los docstrings.
```