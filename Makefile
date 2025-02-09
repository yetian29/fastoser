.PHONY = help migrations migrate

# Defines the default target that `make` will to try to make, or in the case of a phony target, execute the specified commands
# This target is executed whenever we just type `make`
.DEFAULT_GOAL = help

# The @ makes sure that the command itself isn't echoed in the terminal
help:
	@echo "---------------HELP-----------------"
	@echo "To migration the project type make migration"
	@echo "To migrate the project type make migrate"
	@echo "------------------------------------"

migration:
	alembic revision --autogenerate -m "initial migration"

migrate:
	alembic upgrade head



