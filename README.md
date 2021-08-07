# Django React App
Basic Django and react app

# Pre-installation
Before installing, please install the prerequisites for this project

| Package | Site | Guide |
| ----------- | ----------- | ----------- |
| node | https://nodejs.org/en/download/ |  https://phoenixnap.com/kb/install-node-js-npm-on-windows
| python | https://www.python.org/downloads/ | https://realpython.com/installing-python/
| yarn | after installing node run `npm install --global yarn` | https://classic.yarnpkg.com/en/docs/install/#windows-stable

# Installation
```
pip install -r requirements.txt
yarn
```

# How To Start
## Stating Django
This will start the django server up.
```bash
python app/manage.py runserver localhost:8000
```

## Webpack
This will start a webpack environment that will watch for changes in `frontend/entry/*.jsx` and minify them in `app/resources/static/dist`. Which then can be imported as a script within a flask rendered template. You will have to run this in another terminal if you want both dev environments to be concurrently active.
```bash
yarn dev
```

# Tests
```
ENV="test" python manage.py test   
yarn test
```

# Build and Run Docker Image for AWS
```bash
docker build -f terraform/Dockerfile -t dylan_test_app . 
docker run -p 8000:8000 dylan_test_app 
```

# Build and Run Docker Image for Heroku
```bash
docker build -f Dockerfile -t dylan_test_app . 
docker run -e PORT=3000  -p 3000:3000 dylan_test_app 
```