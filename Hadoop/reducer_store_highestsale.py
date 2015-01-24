#! /usr/bin/python

import sys

def reducer():
    """
    Reduce function that obtains the highest sale per store.
    """
    highestSale = 0
    oldStore = None

    for line in sys.admin:
        data = line.strip().split("\t") # remove end of line and split string by tabs in data list


        # check if data contains two items
        # ignore line if not
        if len(data) != 2:
            continue

        # unpack items into appropriate variable names
        thisStore, thisSale = data

        # print out store name and highest sale if new
        # store name is different from previous.
        # This means highest sale for previous store
        # has been obtained.
        if oldStore and (oldStore != thisStore):
            print "{0}\t{1}".format(oldStore, highestSale)
            highestSale = 0

        oldStore = thisStore
        if float(thisSale) > float(highestSale):
            highestSale = float(thisSale)

    # last store and its highest sale printed out
    if oldStore != None:
        print "{0}\t{1}".format(oldStore, highestSale)


def main():
    reducer()
    sys.stdin = sys.__stdin__   # restores default stdin values

main()
