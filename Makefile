install:
	pip install -r requirements.txt

format:
	black *.py

all: install format