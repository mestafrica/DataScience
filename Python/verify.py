"""
This is a slightly modified script taken from the Havard CS 109 Installation Instructions IPython Notebook.
http://nbviewer.ipython.org/github/cs109/2014/blob/master/homework/HW0.ipynb
"""

# Numpy is a library for working with Arrays
try:
    import numpy as np
    print "Numpy version:        %6.6s (need at least 1.7.1)" % np.__version__
except:
    print "Numpy version: NOT INSTALLED!!!"

# SciPy implements many different numerical algorithms
try:
    import scipy as sp
    print "SciPy version:        %6.6s (need at least 0.12.0)" % sp.__version__
except:
    print "SciPy version: NOT INSTALLED!!!"

# Pandas makes working with data tables easier
try:
    import pandas as pd
    print "Pandas version:       %6.6s (need at least 0.11.0)" % pd.__version__
except:
    print "Pandas: NOT INSTALLED!!!"

# Module for plotting
try:
    import matplotlib
    print "Matplotlib version:    %6.6s (need at least 1.2.1)" % matplotlib.__version__
except:
    print "Matplotlib: NOT INSTALLED!!!"

#IPython is what you are using now to run the notebook
try:
    import IPython
    print "IPython version:      %6.6s (need at least 1.0)" %   IPython.__version__
except:
    print "IPython: NOT INSTALLED!!!"

# SciKit Learn implements several Machine Learning algorithms
try:
    import sklearn
    print "Scikit-Learn version: %6.6s (need at least 0.13.1)" % sklearn.__version__
except:
    print "Scikit-Learn: NOT INSTALLED!!!"

print "\n\n"
print "EXTRA PYTHON LIBRARIES"
# Requests is a library for getting data from the Web
try:
    import requests
    print "requests version:     %6.6s (need at least 1.2.3)" % requests.__version__
except:
    print "requests: NOT INSTALLED!!!"

# Networkx is a library for working with networks
try:
    import networkx as nx
    print "NetworkX version:     %6.6s (need at least 1.7)" % nx.__version__
except:
    print "Networkx: NOT INSTALLED!!!"

#BeautifulSoup is a library to parse HTML and XML documents
try:
    import bs4
    print "BeautifulSoup version:   %6.6s (need at least 4.0)" % bs4.__version__
except:
    print "BeautifulSoup: NOT INSTALLED!!!"

#MrJob is a library to run map reduce jobs on Amazon's computers
try:
    import mrjob
    print "Mr Job version:       %6.6s (need at least 0.4)" % mrjob.__version__
except:
    print "Mr Job: NOT INSTALLED!!!"

#Pattern has lots of tools for working with data from the internet
try:
    import pattern
    print "Pattern version:      %6.6s (need at least 2.6)" % pattern.__version__
except:
    print "Pattern: NOT INSTALLED!!!"

#Seaborn is a nice library for visualizations
try:
    import seaborn
    print "Seaborn version:      %6.6s (need at least 0.3.1)" % seaborn.__version__
except:
    print "Seaborn: NOT INSTALLED!!!"
