.PHONY: test unit full-test clean setup stage deploy


SRC=auto_release_workflow
PKG=$(SRC)


#
# testing
#
test:
	pytest . --durations=10


update-deps:
	pip-compile -U > /dev/null
	pip-compile > /dev/null
	git --no-pager diff requirements.txt

#
# update deps in windows OS
#
update-deps-win:
	pip-compile -U
	git --no-pager diff requirements.txt


release:
	git push --tags
	rm -rf /tmp/olapy
	git clone . /tmp/olapy
	cd /tmp/olapy ; python setup.py sdist
	cd /tmp/olapy ; python setup.py sdist upload