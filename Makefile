run:
	@pipenv run python index.py

lint:
	@pipenv run flake8 .

setup:
	@pip install pipenv
	@pipenv install --dev
