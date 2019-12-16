.PHONY: init collection collect second-pass validate index clobber black clean prune
.SECONDARY:
.DELETE_ON_ERROR:
.SUFFIXES: .json

all: collect second-pass

collect:
	python3 bin/collect.py

black:
	black .

init::
	pip3 install --upgrade -r requirements.txt

prune:
	rm -rf ./var $(VALIDATION_DIR)
