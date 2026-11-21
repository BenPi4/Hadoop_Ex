#!/usr/bin/env python
"""mapper.py"""
import sys

def read_input(file):
    for line in file:
        yield line.split()

def main(separator='\t'):
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            # 1. Strip trailing and leading commas and dots
            # 2. Convert word to lowercase
            clean_word = word.strip(',.').lower()
            
            # Print only non-empty words after cleaning
            if clean_word:
                print('%s%s%d' % (clean_word, separator, 1))

if __name__ == "__main__":
    main()
