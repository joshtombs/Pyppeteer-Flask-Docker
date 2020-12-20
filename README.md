# Pyppeteer-Flask-Docker
After having some trouble setting up a simple Python web scraping application, I realized that
there were some quirks required to setting up a Flask application, that ran Pyppeteer - all of
which was deployed in a Docker application. The purpose of this repository is to show the bare
minimum needed to achieve that goal.

Simply build:

```
docker build -t pyppeteer-app .
```

And then run:

```
docker run --rm --security-opt seccomp=chrome.json --init -p 9090:8080 -e PORT=8080 pyppeteer-app
```
