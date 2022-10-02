install:
	poetry install

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

brain-games:
	poetry run brain-games

Make lint:
	poetry run flake8 brain_games


