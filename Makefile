FULL_DIR=$(shell pwd)
PYTHON_EXECUTABLE=${FULL_DIR}/.venv/bin/python
BACKEND_DIR=src/
INPUT_DIR=$(BACKEND_DIR)/static/input
OUTPUT_DIR=$(BACKEND_DIR)/static/output
DEPLOYMENT_DIR=${FULL_DIR}/deployment

run:
	cd $(BACKEND_DIR) && $(PYTHON_EXECUTABLE) manage.py runserver

generate-key:
	$(PYTHON_EXECUTABLE) -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

test:
	cd $(BACKEND_DIR) && pytest

redis:
	docker run --rm --name redis-server -p 6379:6379 -v ${FULL_DIR}/tmp:/data redis

notification:
	${PYTHON_EXECUTABLE} random_notifications.py

superuser:
	cd $(BACKEND_DIR) && $(PYTHON_EXECUTABLE) manage.py createsuperuser

migrations:
	cd $(BACKEND_DIR) && $(PYTHON_EXECUTABLE) manage.py makemigrations

migrations-dry-run:
	cd $(BACKEND_DIR) && $(PYTHON_EXECUTABLE) manage.py makemigrations --dry-run

migrate:
	cd $(BACKEND_DIR) &&  $(PYTHON_EXECUTABLE) manage.py makemigrations && $(PYTHON_EXECUTABLE) manage.py migrate
