SHELL:=/bin/bash

build:
	docker-compose build

init:
	docker-compose up -d
	docker exec -it moviedatabase_web_1 python manage.py makemigrations
	docker exec -it moviedatabase_web_1 python manage.py migrate
	docker exec -it moviedatabase_web_1 python manage.py collectstatic --noinput
	docker-compose stop

bash:
	docker exec -it moviedatabase_web_1 bash

stop:
	docker-compose stop

clean:
	docker stop moviedatabase_web_1
	docker stop moviedatabase_db_1
	docker rm moviedatabase_web_1
	docker rm moviedatabase_db_1
	docker rmi moviedatabase_web
