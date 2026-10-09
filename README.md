# Windows Security Dashboard

A local, read-only dashboard for basic Windows/system telemetry.

## Shows
CPU, memory, disk usage, process count, network connection count, and OS information.

## Run
```bash
pip install -r requirements.txt
python main.py
```
Then open http://127.0.0.1:5000

It only reads telemetry. It does not change firewall, registry, processes, or security settings.
