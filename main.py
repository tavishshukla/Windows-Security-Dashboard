from __future__ import annotations

import platform
import socket
import time

import psutil
from flask import Flask, jsonify, render_template

app = Flask(__name__)
STARTED_AT = time.time()


def snapshot() -> dict:
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    try:
        connections = len(psutil.net_connections(kind="inet"))
    except (psutil.AccessDenied, OSError):
        connections = -1

    return {
        "hostname": socket.gethostname(),
        "os": platform.platform(),
        "python": platform.python_version(),
        "cpu_percent": psutil.cpu_percent(interval=0.2),
        "memory_percent": memory.percent,
        "disk_percent": disk.percent,
        "processes": len(psutil.pids()),
        "network_connections": connections,
        "uptime_seconds": int(time.time() - psutil.boot_time()),
        "dashboard_uptime_seconds": int(time.time() - STARTED_AT),
    }


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/api/status")
def status():
    return jsonify(snapshot())


@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "read_only": True})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)


# Keep Flask debug mode disabled: this is a local read-only dashboard.
