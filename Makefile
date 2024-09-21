.PHONY: release
release:
	rm -rf dist
	scripts/git_tag.sh
	python setup.py sdist bdist_wheel
	twine upload dist/*

.PHONY: docs
docs:
	rm -rf docs/build/html
	@cd docs && sphinx-apidoc -f -e -o source/ ../python_package/
	@cd docs && make html && make html

.PHONY: doxygen
doxygen:
	rm -rf docs/html
	doxygen Doxyfile

.PHONY: test
test:
	python setup.py test

.PHONY: coverage
coverage:
	coverage run --source python_package setup.py test && coverage html && coverage report -m

.PHONY: tdd
tdd:
	coverage run --source python_package setup.py test && coverage report -m

.PHONY: lint
lint:
	flake8 python_package/ && pylint python_package/ && flake8 tests/ && pylint tests/

.PHONY: alltests
alltests:
	flake8 python_package/ && pylint python_package/ && flake8 tests/ && pylint tests/ && coverage run --source python_package setup.py test && coverage report -m
