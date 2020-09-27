# Track API

This tiny application is a gateway that provides a tracking script and processes incoming requests from the client-side. Tracker collects elementary browser data, transforms information into the structured JSON, and pushes the JSON to a local/remote MongoDB database.

**Requirements:**

- Python >3.4
- MongoDB >4.0

## Steps to run:

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

As the application is built around Flask (Python single-treaded framework), the simplest way to increase application performance is to run Tracker using multiple workers. For that reason, we recommend you using Nginx as a proxy server, and Gunicorn as the application server. The example of Nginx configuration you may find in nginx.conf-sample. Also, remember to change ENV value at .env from DEVELOPMENT to PRODUCTION.

**Start Tracker API with single gunicorn worker (small VMs):**  
gunicorn -w 1 -b 127.0.0.1:5005 app:app

**Start Tracker API with N workers:**  
gunicorn -w N -b 127.0.0.1:5005 app:app

## Integration:

Add the following code right before the end of the `<body>` tag:

```
<script src="https://track.browser-research.com/scripts/collection" defer=""></script>
```

## Notes:

- For config example of systemctl service check systemctl.service-sample
- The deployment post is 5005, while development is 5000
- Application is deployed at https://track.browser-research.com
- Single Tracker instance consumes as less as 35MB of RAM, what makes it possible to deploy application at tiny VMs (with as less as 256MB of RAM).

## Contact

For any inquiries drop a line to brwsr.rsrch@gmail.com
