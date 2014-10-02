clean:
	find . -name *.pyc -delete
	rm -rf classymq/__pycache__
	rm -rf build/*


build: clean
	python setup.py build

release: clean 
	python setup.py sdist upload

test: clean
	trial classymq.tests

.PHONY: build

