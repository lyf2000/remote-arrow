import os

import netifaces
import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from service import ArrowControlAdapter

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

    ip_list = []
    for interface in netifaces.interfaces():
        if interface in ["eth0", "wlp2s0"] or interface.startswith("enp"):
            for link in netifaces.ifaddresses(interface).get(netifaces.AF_INET, {}):
                ip_addr = link.get("addr", None)
                # ignore loopback address
                if ip_addr and ip_addr != "127.0.0.1":
                    ip_list.append(ip_addr)
    print("Try to connect to one of the following in your phone")
    print([ip + f":{port}" for ip in ip_list], sep="\n")
    uvicorn.run(app, host=host, port=port)
