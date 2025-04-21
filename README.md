## Proyecto de documentador basado en agentes
Una herramienta para documentar un proyecto de forma automatica con claude, copilot u otro mcp client.
Servidor
```js
"mcp-documentator": {
    "command": "uv",
    "args": [
        "--directory",
        "path/documentator-mcp",
        "run",
        "main.py"
    ],
    "env": {
        "WD": "path/documentator-mcp",
        "IGNORE_NAMES": ".git,.venv,.venv,__pycache__"
    }
}
```