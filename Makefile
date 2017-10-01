deploy: clean
	python3 setup.py sdist
	twine upload dist/*


clean:
	-rm -rf dist
