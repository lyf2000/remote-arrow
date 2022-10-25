import os

# import netifaces
import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from service import ArrowControlAdapter, get_ip

app = FastAPI()


@app.get("/")
def index():
    return FileResponse("templates/control_page.html", media_type="text/html")


@app.get("/favicon.ico")
def favicon():
    return FileResponse("templates/favicon.ico")


ACTIONS_ENABLED = ["up", "down", "left", "right"]


@app.get("/{cmd}")
def get_cmd(cmd):
    if cmd not in ACTIONS_ENABLED:
        raise HTTPException(status_code=400, detail="No such command available")

    ArrowControlAdapter.click_keyb(cmd)


if __name__ == "__main__":
    cwd = os.path.dirname(os.path.abspath(__file__))
    app.mount("/templates", StaticFiles(directory=os.path.join(cwd, "templates")))

    host = "0.0.0.0"
    port = 8000

    print("Try to connect to this ip addr in your phone:")
    ip = f"{get_ip()}:{port}"
    print(ip)
    uvicorn.run(app, host=host, port=port)
