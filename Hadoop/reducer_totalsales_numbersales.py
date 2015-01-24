#! /usr/bin/python

import sys

def reducer():
    """
    Reduce function that aggregates total value sales and total number of sales from all stores.
    """

    salesTotal = 0
    salesNumber = 0

    for line in sys.stdin:
        cost = line.strip() # remove an newline characters and white spaces

        # try to convert cost variable to float for
        # aggregation.
        # Ignore exception if not valid conversion.
        try:
            cost = float(cost)
            salesTotal += cost
            salesNumber += 1

        except:
            continue

    # Print final result to stdout as tab-delimited total
    # value and total number of sales
    print "{0}\t{1}".format(salesTotal, salesNumber)


def main():
    reducer()
    sys.stdin = sys.__stdin__   # restores default stdin values

main()
