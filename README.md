# Track API

This tiny application is a gateway that provides a tracking script and processes incoming requests from the client-side. Tracker collects elementary browser data, transforms information into the structured JSON, and pushes the JSON to a local/remote MongoDB database.

**Requirements:**

- Python >= 3.6
- MongoDB >= 4.0

## How to run:

**Step #1:** Create virtualenv:

> virtualenv .venv

**Step #2:** Activate env:

> source ./.venv/bin/activate

**Step #3:** Install requirements:

> pip install -r ./requirements.txt

**Step #4:** Copy .env-sample and save as .env  
**Step #5:** Replace database credentials and TRACK_HOSTNAME in .env  
**Step #6:** Run application:

> python app.py

## Deployment:

As the application is built around Flask (Python single-treaded framework), the simplest way to increase application performance is to run Tracker using multiple workers. For that reason, we recommend you using Nginx as a proxy server, and Gunicorn as the application server.

**Start Tracker API with single gunicorn worker (small VMs):**  
gunicorn -w 1 -b 127.0.0.1:5005 app:app

**Start Tracker API with N workers:**  
gunicorn -w N -b 127.0.0.1:5005 app:app

## Integration:

Add the following code right before the end of the `<body>` tag:

```
<script src="https://yourfancydomain.com/scripts/collection" defer=""></script>
```

## Routes:

- /ping, Methods: "GET" - Route is required for alive-tracking
- /scripts/collection, Methods: "GET" - Route serves tracking script (cached since app initialization)
- /demo, Methods: "GET" - Route shows demo page, which contains data Tracking API collects
- /data/push, Methods: "POST", "OPTIONS" - Route is a gateway, that processes data from the tracking script (sent from the client-side)

## Contact:

- Project email: brwsr.rsrch at gmail.com
- Maintainer's email: konstantin.lebejko at gmail.com
