# Windows Security Dashboard

A local, read-only system security dashboard built with Python, Flask, and psutil.

It displays basic system telemetry in a browser without changing Windows security settings.

## Features

- CPU usage
- Memory usage
- Disk usage
- Process count
- Network connection count
- Operating system information
- Browser-based dashboard
- Automatic dashboard refresh
- Read-only operation

## Requirements

- Windows recommended
- Python **3.11 or newer**
- Git
- A web browser

## 1. Install Python

Download Python:

https://www.python.org/downloads/

During Windows installation, enable:

**Add Python to PATH**

Check that it worked:

```bat
python --version
```

## 2. Install Git

Download Git:

https://git-scm.com/downloads

Check:

```bat
git --version
```

## 3. Clone the repository

```bat
git clone https://github.com/tavishshukla/Windows-Security-Dashboard.git
cd Windows-Security-Dashboard
```

## 4. Create a virtual environment

```bat
python -m venv .venv
.venv\\Scripts\\activate
```

## 5. Install dependencies

Upgrade pip:

```bat
python -m pip install --upgrade pip
```

Install the project requirements:

```bat
python -m pip install -r requirements.txt
```

You normally do not need to download pip separately because it is included with Python.

## 6. Start the dashboard

Run:

```bat
python main.py
```

You should see Flask start on:

```
http://127.0.0.1:5000
```

Open that address in your browser.

## 7. Use the dashboard

The page displays current telemetry and refreshes automatically.

The backend API is:

```
http://127.0.0.1:5000/api/status
```

Opening that endpoint directly shows the current telemetry as JSON.

## 8. Stop the dashboard

Return to the terminal and press:

```
Ctrl+C
```

## 9. Run tests

If tests are present in the repository, run:

```bat
python -m pytest
```

## What the dashboard measures

### CPU

Current CPU utilization reported by psutil.

### Memory

Current percentage of system memory in use.

### Disk

Current disk usage percentage for the system filesystem.

### Processes

Number of processes visible to psutil.

### Network connections

Number of network connections visible to psutil.

Some operating systems may restrict access to certain connection information. The application handles that case without modifying the system.

## Project structure

```
Windows-Security-Dashboard/
├── main.py
├── requirements.txt
├── README.md
└── templates/
    └── index.html
```

## Troubleshooting

### Python is not recognized

Reinstall Python and make sure **Add Python to PATH** is enabled. Then open a new Command Prompt.

### Flask is missing

Make sure the virtual environment is active and run:

```bat
python -m pip install -r requirements.txt
```

### Port 5000 is already in use

Another local application may already be using port 5000. Stop that authorized local application before running this dashboard.

## Security model

This dashboard is read-only. It does not:

- Change the Windows firewall
- Kill processes
- Modify the registry
- Change passwords
- Change security policies
- Disable antivirus
- Modify network settings

It is intended for local defensive monitoring and cybersecurity learning.
