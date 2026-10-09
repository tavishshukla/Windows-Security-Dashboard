# Windows Security Dashboard

A local, read-only system telemetry dashboard built with Python, Flask, and psutil.

## Features

- CPU usage
- Memory usage
- Disk usage
- Process count
- Network connection count
- Hostname and OS information
- Python version
- System uptime
- Dashboard uptime
- Auto-refreshing browser UI
- JSON status API
- Health endpoint
- Read-only operation

## Requirements

- Windows recommended
- Python **3.11 or newer**
- Git
- A web browser

## Setup

Install Python from https://www.python.org/downloads/ and Git from https://git-scm.com/downloads/.

Verify:

```bat
python --version
git --version
```

Clone:

```bat
git clone https://github.com/tavishshukla/Windows-Security-Dashboard.git
cd Windows-Security-Dashboard
```

Create the virtual environment:

```bat
python -m venv .venv
.venv\\Scripts\\activate
```

Install:

```bat
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run

```bat
python main.py
```

Open:

```
http://127.0.0.1:5000
```

The dashboard refreshes every 3 seconds.

## API endpoints

### Status

```
http://127.0.0.1:5000/api/status
```

Returns the current telemetry as JSON.

### Health

```
http://127.0.0.1:5000/api/health
```

Returns a simple health response confirming that the dashboard is running in read-only mode.

## Stop

Press `Ctrl+C` in the terminal.

## What it measures

- CPU utilization
- Memory utilization
- System disk utilization
- Visible process count
- Visible network connection count
- Hostname
- OS/platform
- Python version
- System uptime

Some network connection information may be restricted by the operating system. The application handles that without changing system settings.

## Project structure

```
Windows-Security-Dashboard/
├── main.py
├── requirements.txt
├── README.md
└── templates/
    └── index.html
```

## Security model

This dashboard is read-only. It does not change the firewall, kill processes, modify the registry, change passwords, disable antivirus, or modify network settings.

## API endpoints

The dashboard exposes two local read-only endpoints: `/api/status` for current telemetry and `/api/health` for basic health/read-only status. Both are available only through the local Flask server.

## Process telemetry

The local read-only `/api/processes` endpoint returns up to 20 visible processes, ordered by memory usage. Access-denied processes are skipped rather than changing system permissions.

`http://127.0.0.1:5000/api/processes`
