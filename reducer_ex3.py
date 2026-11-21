#!/usr/bin/env python
"""reducer.py"""
from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    data = read_mapper_output(sys.stdin, separator=separator)
    word_counts = []
    
    # Aggregate total counts for each word
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            word_counts.append((current_word, total_count))
        except ValueError:
            pass

    # Sort words by total count in descending order
    word_counts.sort(key=itemgetter(1), reverse=True)

    # Print only the top 3 highest scoring words
    for word, count in word_counts[:3]:
        print("%s%s%d" % (word, separator, count))

if __name__ == "__main__":
    main()
