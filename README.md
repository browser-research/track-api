# api.browser-research.com

Open-source API for browser data gathering

## Steps to run

- virtualenv .venv
- Activate env and make sure that virtualenv is using Python 3
- pip install -r .\requirements.txt
- Copy .env-sample and save as .env
- Replace database credentials in .env
- Replace API_HOSTNAME in .env with localhost (make sure that port matches) or production domain
- python app.py
- Replace 127.0.0.1 to localhost to avoid CORS issues

## Deploy in production

- One worker (tiny servers) > gunicorn -w 1 -b 127.0.0.1:5005 app:app
- Five workers (powerful VMs) > gunicorn -w 5 -b 127.0.0.1:5005 app:app
