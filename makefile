install: 
	poetry install

project:
	poetry run project

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl

lint:
	poetry run flake8 /home/admin/project_tsaregorodtsev_b24-505/project_func/scripts/main_base.py
