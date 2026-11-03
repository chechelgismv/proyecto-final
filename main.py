"""Servidor local para abrir el Diario ambiental en el navegador."""

from __future__ import annotations

import os
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


# Ruta del proyecto que se podrá servir al navegador.
ROOT = Path(__file__).resolve().parent
# Dirección local y puerto configurable del servidor.
HOST = "127.0.0.1"
PORT = int(os.environ.get("PORT", "8000"))


# Inicia el servidor local y sirve los archivos del proyecto desde el navegador.
def main() -> None:
    handler = partial(SimpleHTTPRequestHandler, directory=str(ROOT))
    server = ThreadingHTTPServer((HOST, PORT), handler)
    print(f"Diario ambiental disponible en http://localhost:{PORT}")
    print("Presioná Ctrl+C para detener el servidor.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nCerrando el servidor...")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
