# Django React App
Basic Django and react app

# Pre-installation
Before installing, please install the prerequisites for this project

| Package | Site | Guide |
| ----------- | ----------- | ----------- |
| mysql | | |
| node | https://nodejs.org/en/download/ |  https://phoenixnap.com/kb/install-node-js-npm-on-windows
| python | https://www.python.org/downloads/ | https://realpython.com/installing-python/
| yarn | after installing node run `npm install --global yarn` | https://classic.yarnpkg.com/en/docs/install/#windows-stable

# File Structure
```
django-react-app/
|
├── app/
|   ├── __init__.py
|   ├── core/
│   |   ├── __init__.py
│   |   ├── settings.py
│   |   ├── urls.py
│   |   └── wsgi.py
|   ├── resources/
|   |   ├── static/
|   |   └── templates/
|   └── test_app/
|       ├── __init__.py
|       ├── migrations/
|       ├── tests/
|       ├── models.py
|       ├── serializers.py
|       └── views.py 
|
├── frontend/
│   ├── components/
│   ├── entrypoints/
│   └── tests/
|
├── .env.example
├── .gitignore
├── db.sqlite3
├── Dockerfile
├── jest.config.js
├── manage.py
├── package.json
├── requirements.txt
├── webpack.config.js
└── yarn.lock
```

# Installation
```
pip install -r requirements.txt
yarn
```

# How To Start
Please copy .env.example into a .env folder, add environment variables values if different.

### Stating Django
This will start the django server up.
```bash
python manage.py runserver
```

### Webpack
This will start a webpack environment that will watch for changes in `frontend/entry/*.jsx` and minify them in `app/resources/static/dist`. Which then can be imported as a script within a flask rendered template. You will have to run this in another terminal if you want both dev environments to be concurrently active.
```bash
yarn dev
```

# Tests
```
python manage.py test   
yarn test
```

# Build and Run Docker Image for Heroku
```bash
docker build -f Dockerfile -t dylan_test_app . 
docker run -e PORT=3000 -p 3000:3000 dylan_test_app 
```