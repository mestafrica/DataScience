#! /usr/bin/python

import sys

def reducer():
    """
    Reduce function that aggregates total sales per store.
    """

    salesTotal = 0
    oldProduct = None

    for line in sys.stdin:
        data = line.strip().split("\t") # remove end of line and split string by tabs in data list

        # check if data contains two items
        # ignore line if not
        if len(data) != 2:
            continue

        # unpack items into appropriate variable names
        thisProduct, thisSale = data

        # print out product name and total sales if current
        # product name is different from previous.
        # This means all of previous product and total sales
        # has been obtained.
        if oldProduct and (oldProduct != thisProduct):
            print "{0}\t{1}".format(oldProduct, salesTotal)

            salesTotal = 0  # reset to zero for next product

        oldProduct = thisProduct
        salesTotal += float(thisSale)

    # last category of product and its total sale printed out
    if oldProduct != None:
        print "{0}\t{1}".format(oldProduct, salesTotal)


def main():
    reducer()
    sys.stdin = sys.__stdin__   # restores default stdin values

main()
