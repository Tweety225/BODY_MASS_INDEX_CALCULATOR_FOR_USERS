# BMI Calculator

This repository provides a small FastAPI backend and a lightweight HTML/CSS frontend to calculate Body Mass Index (BMI).

Quickstart
---------

Install dependencies and run locally:

```bash
python -m pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Open http://localhost:8000 in your browser.

Docker
------

Build and run with Docker:

```bash
docker build -t bmi-app .
docker run -p 8000:80 bmi-app
```

Project structure
-----------------

```
.
├─ app/
│  ├─ api/
│  │  └─ v1/
│  │     ├─ bmi.py
│  │     ├─ health.py
│  │     └─ routes.py
│  ├─ core/
│  │  └─ config.py
│  ├─ services/
│  │  └─ bmi.py
│  ├─ templates/
│  └─ main.py
├─ static/
├─ tests/
└─ requirements.txt
```

Endpoints
---------

- `GET /` - lightweight HTML UI
- `POST /api/v1/bmi/` - JSON API: `{ "weight_kg": 70, "height_m": 1.75 }`
- `GET /api/v1/healthz/` - readiness/health check

Testing
-------

Run unit tests with `pytest`:

```bash
pytest -q
```

Render deployment
-----------------

You can deploy to Render either by using the included `render.yaml` (recommended) or by creating a Web Service manually:

With `render.yaml`:

1. Connect your GitHub/GitLab repo to Render.
2. Push this repository and Render will create a `bmi-app` web service using `render.yaml`.

Manual setup:

1. Create a new Web Service on Render.
2. Set the Build Command to:

```bash
pip install -r requirements.txt
```

3. Set the Start Command to:

```bash
gunicorn -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:$PORT --workers 2 --log-level info
```

Render will use `/readyz` for the health check as configured in `render.yaml`.

