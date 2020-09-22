# api.browser-research.com

Open-source API for browser data gathering

## Steps to run

- > virtualenv .venv
- Activate env and make sure that virtualenv is using Python 3
- > pip install -r .\requirements.txt
- Copy .env-sample and save as .env
- Replace database credentials in .env
- > python app.py

## Deploy in production
- Two workers (small servers) > gunicorn -w 2 -b 127.0.0.1:4000 app:app
- Five workers (powerful VMs) > gunicorn -w 5 -b 127.0.0.1:4000 app:app
