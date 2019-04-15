VERSION = 0.0.1

.PHONY: doc test tgz

tgz:
	git archive --format=tar.gz -o porkie-$(VERSION).tgz --prefix=$(VERSION) master

doc:
	pandoc README.md -o README.pdf

test:
	pytest -v test.py
