# Pig Latin

Make a "Pig Latin" version of a given word with the following rules:

1. If the word begins with consonants, e.g., "k" or "ch", move them to the end of the word and append "ay" so that "mouse" becomes "ouse-may" and "chair" becomes "air-chay."
2. If the word begins with a vowel, simple append "-ay" to the end, so "apple" is "apple-ay."

# Examples

````
$ ./pig.py
Usage: pig.py ORD-WAY
$ ./pig.py foo
oo-fay
$ ./pig.py oof
oof-ay
$ ./pig.py hello
ello-hay
````

# Test

To execute the test suite, run `make test` or `pytest -v test.py`.

# Author

Ken Youens-Clark <kyclark@email.arizona.edu>
