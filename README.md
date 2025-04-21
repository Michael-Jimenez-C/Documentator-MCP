## Proyecto de documentador basado en agentes
Una herramienta para documentar un proyecto de forma automatica con claude, copilot u otro mcp client.


# Servidor
Busca en tu cliente la opción de mcp, y agrega esta linea.

```json
{
    "mcp": {

        "inputs": [],
        "servers": {
            "mcp-documentator": {
                "command": "uv",
                "args": [
                    "--directory",
                    "C:/Users/micha/OneDrive/Documentos/GitHub/documentator-mcp",
                    "run",
                    "main.py"
                ],
                "env": {
                    "WD": "C:/Users/micha/OneDrive/Documentos/GitHub/documentator-mcp",
                    "IGNORE_NAMES": ".git,.venv,.venv,__pycache__"
                }
            }
        }
    }
}
```