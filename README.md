# Movie Database

### Description
Simple website provided by API [http://www.omdbapi.com/](http://www.omdbapi.com/). User can logged and save result to 
favourite list.

In backend used _Python 3 with Django 2_. In front part used:
_html + css(bootstrap) + jquery_


## Quick local start

* Install all packages from [requirements.txt](requirements.txt)
* Run in command line:

```
python manage.py makemigrations app
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Urls
* `http://127.0.0.1:8000/` - home page
* `login/` - login page
* `search/` - search movie page
* `favourite/` - favourite movie page
* `admin/` - Django-admin page

## Docker-compose
- for a docker please use _settings/developer.py_