#! /usr/bin/python

import sys

def mapper():
    """
    Map function that prints out tab-delimited store name and cost of sale.
    """
    for line in sys.stdin:
        data = line.strip().split("\t") # remove end of line and split string by tabs in data list

        # check whether each split line contains 6 items
        # skip line if it does not
        if len(data) != 6:
            continue

        # unpack data items in appropriate variable names
        date, time, store, product, cost, payment = data

        # print tab-delimited store name and cost to stdout
        print "{0}\t{1}".format(store, cost)


def main():
    mapper()
    sys.stdin = sys.__stdin__   # restores default stdin values
