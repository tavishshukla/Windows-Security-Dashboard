from __future__ import annotations
import platform
import psutil
from flask import Flask, jsonify, render_template

app = Flask(__name__)

def snapshot() -> dict:
    memory, disk = psutil.virtual_memory(), psutil.disk_usage("/")
    try:
        connections = len(psutil.net_connections(kind="inet"))
    except (psutil.AccessDenied, OSError):
        connections = -1
    return {
        "os": platform.platform(),
        "cpu_percent": psutil.cpu_percent(interval=0.2),
        "memory_percent": memory.percent,
        "disk_percent": disk.percent,
        "processes": len(psutil.pids()),
        "network_connections": connections,
    }

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/api/status")
def status():
    return jsonify(snapshot())

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
