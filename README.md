# Movie Database

### Description
Simple website provided by [http://www.omdbapi.com/](http://www.omdbapi.com/). User can logged and save result to 
favourite list.

In project used Python 3.

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
* `admin/` - Django-admin page

## API URLs:
* `api/` - API
