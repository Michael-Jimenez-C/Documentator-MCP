from mcp.server.fastmcp import FastMCP
import os
from plantuml import PlantUML

mcp = FastMCP("Documentator-MCP", dependencies=["PlantUML"])

WD = os.environ.get("WD", os.environ.get('HOME'))
ignore_names = os.environ.get("IGNORE_NAMES", "").split(",")

def santize_path(relative_path):
    path = os.path.abspath(relative_path)
    if not path.startswith(os.path.abspath(WD)):
        return WD
    return path

@mcp.tool()
async def get_files(relative_path:str) -> dict:
    path = santize_path(relative_path)
    result_ = os.listdir(path)
    dirs = filter(lambda x: os.path.isdir(os.path.join(path, x)), result_)
    dirs = list(filter(lambda x: x not in ignore_names, dirs))
    
    files = filter(lambda x: x not in dirs+ignore_names, result_)

    return {'directories': dirs, 'files': list(files)}

@mcp.tool()
async def tree(relative_path :str, max_deep:int = 5) -> dict:
    if max_deep <= 0:
        return []
    path = santize_path(relative_path)
    result_ = os.listdir(path)
    dirs = filter(lambda x: os.path.isdir(os.path.join(path, x)), result_)
    dirs = list(filter(lambda x: x not in ignore_names, dirs))
    files_ = []
    if dirs:
        for i in dirs:
            files_.extend(await tree(os.path.join(relative_path, i), max_deep-1))
    
    files = [os.path.join(relative_path, i) for i in filter(lambda x: x not in dirs+ignore_names, result_)]
    files.extend(files_)
    return files

@mcp.tool()
async def read_file(file_relative_path: str) -> str:
    path = santize_path(os.path.join(file_relative_path))
    try:
        return open(path, 'r').read()
    except Exception as e:
        return {'error':str(e), 'path': path, 'relative_path': file_relative_path}

@mcp.tool()
async def write_file(file_relative_path: str, content: str) -> None:
    path = santize_path(os.path.join('./',file_relative_path))
    with open(path, 'w') as f:
        f.write(content)

@mcp.tool()
async def create_dir(relative_path: str) -> None:
    path = santize_path(os.path.join('./',relative_path))
    os.makedirs(path, exist_ok=True)
    return path


@mcp.tool()
async def diagramPlantUML(diagram_code: str, relative_path: str) -> None:
    path = santize_path(relative_path)
    plantuml_client = PlantUML(url='http://www.plantuml.com/plantuml/svg/')
    svg_content = plantuml_client.processes(diagram_code)
    with open(path,'wb') as file:
        file.write(svg_content)
        file.close()
    return path

@mcp.prompt()
def documentation_prompt() -> str:
    return """
    Eres el encargado de documentar el código del proyecto.
    Vas a analizar el codigo del proyecto, y sus dependencias, luego vas a generar una carpeta doc y un archivo DOC.md en donde vas a documentar todo.
    Las secciones obligatorias son: Estructura del proyecto, dependencias, Descripción con la versión de python.
    Las secciones opcionales pero importantes son: CLI, APIs, ENDPOINTS, ENTRYPOINTS, DataClasses, y cualquier otra sección que consideres necesaria.
    La documentación debe ser clara y concisa, y debe incluir ejemplos de uso y cualquier otra información relevantes si estos aparecen en los docstrings.

    Puedes generar diagramas plantuml o mermaid para representar información, los plantuml pueden ser generados, pero los de mermaid se deben generar en un documento para que se procesen manualmente.

    aquellas partes que no puedas completar por tu cuenta en el markdown puedes dejarlo como un comentario.
    """

if __name__ == "__main__":
    mcp.run(transport='stdio')