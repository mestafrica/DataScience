# Python for Data Science

  I am supposed to say something smart about using Python for Data Science over here.  Well, I do not have any but there are always opinions online. Check out this [Quora](http://www.quora.com/Why-is-Python-a-language-of-choice-for-data-scientists).

## Installation

### Installing Python

Most unix-based systems such as Ubuntu, Debian and OS X normally come install with Python. We will use Python 2.6 or above BUT NOT Python 3.0 and above. To check the version of Python on your system, type `python --version` into your terminal.

**The installation instructions below are geared toward Debian/Ubuntu OS. OS X will be added soon.**

### Essential Libraries
+ Dependencies

  The essential data science Python libraries depend on a few libraries which we will install first:

  ```
  sudo apt-get install python-dev build-essential python-setuptools \
                        libatlas-dev libatlas3gf-base
  sudo apt-get update
  ```

+ **[Pip](https://pip.pypa.io/en/latest/user_guide.html)**

  Pip is a library for easy installation of Python libraries.

  ```
  sudo apt-get install python-pip
  sudo apt-get update
  ```

+ **[Numpy](http://www.numpy.org/)**

  Numerical Python package for scientific computing in Python. Many scientific and analytical libraries are built on top of this.

  ```
  sudo pip install numpy
  ```

+ **[SciPy](http://scipy.org/scipylib/index.html)**

  Collection of packages to tackle different standard problem domains in scientific computing.

  ```
  sudo pip install scipy
  ```

  If you run into any errors, type the following:
  ```
  sudo apt-get install gfortran libopenblas-dev liblapack-dev
  ```


+ **[Pandas](http://pandas.pydata.org/)**

  rich data structures and functions for working with structured data

  ```
  sudo pip install pandas
  ```

+ **[Matplotlib](http://matplotlib.org/)**

  Python library for plot and 2D data visualisations

  ```
  sudo pip install matplotlib
  ```

+ **[IPython and IPython-Notebook](http://ipython.org/)**

  Python environment for interactive and exploratory computing. It accelerates writing, testing and debugging of Python code.

  ```
  sudo pip install ipython
  ```

+ **[Scikit-learn](http://scikit-learn.org/stable/)**

  ```
  sudo pip install --user --install-option="--prefix=" -U scikit-learn
  ```

### Extra Libraries

  These are additional libraries that you do not need to get started with doing Data Science in Python but will be useful for special tasks you will want to achieve such as working with networks, creating visualisations and getting data from the internet

+ Requests: a library for getting data from the Web

  ```
  sudo pip install requests
  ```

+ **Networkx**: a library for working with networks
  ```
  sudo pip install networkx
  ```

+ **Beautiful Soup**: a library to parse HTML and XML documents
  ```
  sudo pip install beautifulsoup4
  ```

+ **MrJob**: a library to run map reduce jobs on Amazon's computers
 ```
 sudo pip install mrjob
 ```

+ **Pattern**: a library with lots of tools for working with data from the internet
  ```
  sudo pip install pattern
  ```
+  **Seaborn**: a nice library for visualizations
  ```
  sudo pip install seaborn
  ```
