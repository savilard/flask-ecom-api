.PHONY: install
install:
		poetry install --no-dev

.PHONY: dev_install
dev_install:
		poetry install

.PHONY: lint
lint:
		poetry run mypy flask_ecom_api/
		poetry run flake8 flask_ecom_api/
		poetry run isort flask_ecom_api/

.PHONY: unit
unit:
	poetry run pytest .

.PHONY: test
test: lint unit
