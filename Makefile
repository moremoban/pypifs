all: test

install_test:
	pip install -r tests/requirements.txt

test:
	bash test.sh

lint:
	bash lint.sh

format:
	isort -y $(find pypifs -name "*.py"|xargs echo) $(find tests -name "*.py"|xargs echo)
	black -l 79 pypifs
	black -l 79 tests

git-diff-check:
	git diff --exit-code
