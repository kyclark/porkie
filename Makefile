VERSION = 0.0.1

.PHONY: doc test tgz test2

tgz:
	git archive --format=tar.gz -o porkie-$(VERSION).tgz --prefix=porkie-$(VERSION)/ master

doc:
	pandoc README.md -o README.pdf

test:
	pytest -v test.py

test2:
	pytest -v pig2.py
