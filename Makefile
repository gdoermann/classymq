clean:
	find . -name *.pyc -delete
	rm -rf classymq/__pycache__


build: clean
	python setup.py build

release: clean 
	python setup.py sdist upload


.PHONY: build

