from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("Documentator-MCP")

WD = os.environ.get("WD", os.environ.get('HOME'))
ignore_names = os.environ.get("IGNORE_NAMES", "").split(",")

def santize_path(relative_path):
    path = os.path.abspath(relative_path)
    if not path.startswith(WD):
        return WD
    return path

@mcp.tool()
async def get_files(relative_path) -> dict:
    path = santize_path(relative_path)
    result_ = os.listdir(path)
    dirs = filter(lambda x: os.path.isdir(os.path.join(path, x)), result_)
    dirs = list(filter(lambda x: x not in ignore_names, dirs))
    
    files = filter(lambda x: x not in dirs+ignore_names, result_)

    return {'directories': dirs, 'files': list(files)}

@mcp.tool()
async def tree(relative_path, max_deep = 5) -> dict:
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
    return open(santize_path(file_relative_path), 'r').read()

@mcp.tool()
async def write_file(file_relative_path: str, content: str) -> None:
    with open(santize_path(file_relative_path), 'w') as f:
        f.write(content)

if __name__ == "__main__":
    mcp.run(transport='stdio')