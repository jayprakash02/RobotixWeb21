# Robotix Web 2.O

This repository contains a backkend of [Robotix Club NITRR Website](https://robotix.nitrr.ac.in).
## Backend development workflow

### Installation
```
python -m venv robo
source robo/bin/activate
pip install -r requirements.txt
python manage.py runserver
```
### Migrations
```
python manage.py makemigrations
python manage.py migrate
```
### Start Server
```
python manage.py runserver
```