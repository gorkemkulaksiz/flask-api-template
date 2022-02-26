# flask-api-template

A Flask API template I use for my projects. This is by no means a production-ready template, just my idea of a starting point.

## Overview

This template is made to be used with these:

Database:
* MySQL 5.7+
* MariaDB 10+

Libraries:
* [Flask-SQLAlchemy](https://github.com/pallets/flask-sqlalchemy/)
* [Flask-Migrate](https://github.com/miguelgrinberg/flask-migrate)
* [marshmallow](https://github.com/marshmallow-code/marshmallow)
* [flask-smorest](https://github.com/marshmallow-code/flask-smorest)
* [PyJWT](https://github.com/jpadilla/pyjwt)

## Usage

### .env File

It's nicer to have a dotenv file instead of hard-coding configuration variables. Use the default `.env.example` file to create your own `.env` file before attempting to run the application server.

### Getting Started

```bash
# Setting up the virtual environment
# Using the bundled venv module for Python 3.3+
$ python3 -m venv env
$ source ./env/bin/activate

# Install dependencies
(env)$ pip install -r requirements.txt

# Start the application server
# --reload (optional/development): restarts workers when code changes
(env)$ gunicorn -w 4 --reload -b 0.0.0.0:8080 wsgi:app
```

## Contributing

If you have any suggestions for how this template could be improved, or see something wrong, feel free to open an issue.