# Django Course

### Env setup

```bash
python3 -m venv .venv
source .venv/bin/activate
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config
pip install django mysqlclient
django-admin startproject dcrm .
python manage.py startapp website
# Install and Create DB
docker container run -d --name dcrm-db -e MYSQL_ROOT_PASSWORD=password123 -p 3306:3306 mysql:8.0.34
docker exec -it dcrm-db bash
mysql -u root -p
# CREATE DATABASE dcrm;
# update settings.py under dcrm folder - add website under INSTALLED_APPS and configure database
# install mysql client UI
docker container run -d --name adminer -p 8080:8080 adminer

# Make migrations, create superuser and start app
python manage.py migrate
python manage.py createsuperuser #admin #password
python manage.py runserver
```

### App

-
