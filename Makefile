APP_FILE=docker-compose/app.yaml
STORAGE_FILE=docker-compose/storage.yaml


.PHONY = help up_app down_app migration migrate lint format

# Defines the default target that `make` will to try to make, or in the case of a phony target, execute the specified commands
# This target is executed whenever we just type `make`
.DEFAULT_GOAL = help

# The @ makes sure that the command itself isn't echoed in the terminal
help:
	@echo "---------------HELP-----------------"
	@echo "To migration the project type make migration"
	@echo "To migrate the project type make migrate"
	@echo "To lint the project type make lint"
	@echo "To format the project type make format"	
	@echo "To up_app the project type make up_app"	
	@echo "To down_app the project type make down_app"	
	@echo "------------------------------------"

up_app:
	docker-compose --env-file example.env -f ${APP_FILE} -f ${STORAGE_FILE} up --build

down_app:
	docker-compose -f ${APP_FILE} -f ${STORAGE_FILE} down 

migration:
	alembic revision --autogenerate -m "initial migration"

migrate:
	alembic upgrade head

lint:
	poetry run ruff check --fix .

format:
	poetry run ruff format .






