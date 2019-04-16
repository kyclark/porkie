#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-04-10
Purpose: Pig Latin
"""

import os
import re
import string
import sys


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} ORD-WAY'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    print(pig(args[0]))


# --------------------------------------------------
def pig(word):
    """Create a Pig Latin version of a word"""

    consonants = re.sub('[aeiouAEIOU]', '', string.ascii_letters)
    match = re.match('^([' + consonants + ']+)(.+)', word)

    pig_word = '-'.join([match.group(2),
                         match.group(1) + 'ay']) if match else word + '-ay'

    return pig_word


# --------------------------------------------------
def test_pig():
    """Tests for the `pig` function"""

    tests = [
        ('mouse', 'ouse-may'),
        ('apple', 'apple-ay'),
        ('chair', 'air-chay'),
        ('street', 'eet-stray'),
        ('BOOK', 'OOK-Bay'),
        ('Creek', 'eek-Cray'),
    ]

    for given, expected in tests:
        assert expected == pig(given)


# --------------------------------------------------
if __name__ == '__main__':
    main()
