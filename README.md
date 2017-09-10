trimpy
=====
[![Build Status](https://travis-ci.org/trimpy/trimpy.svg?style=flat)](https://travis-ci.org/trimpy/trimpy)
[![Appveyor](https://ci.appveyor.com/api/projects/status/github/trimpy/trimpy?branch=dev)](https://www.appveyor.com/)
[![Coverage Status](https://coveralls.io/repos/trimpy/trimpy/badge.svg?branch=dev)](https://coveralls.io/r/trimpy/trimpy?branch=dev)
[![Code Health](https://landscape.io/github/trimpy/trimpy/dev/landscape.svg?style=flat)](https://landscape.io/github/trimpy/trimpy/dev)
[![Join the chat at https://gitter.im/trimpy/trimpy](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/trimpy/trimpy?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

trimpy is a python library for summarizing text

Documentation  and list of algorithms supported should be at a proposed site http://trimpy.org/  
but for now is this README.md
Examples on using trimpy: https://github.com/ravibeta/trimpy/tree/dev/examples  

Dependencies
=============
trimpy has following non optional dependencies:
- Python 2.7 or Python 3
- NetworkX 1.11 
- Scipy 0.18.0 
- Numpy 1.11.1 
- Pandas 0.18.1 
- gensim 2.2.0
- pgmpy 

Download
=========
Currently trimpy is not hosted on pypi or conda.
You can either clone the git repo with:
```
git clone https://github.com/ravibeta/trimpy
```
or download a zip from: https://github.com/ravibeta/trimpy/archive/dev.zip

Installation
=============
To install the dependencies switch to the trimpy directory using:
```
$ cd /path/to/trimpy
```
In the directory run either of the following:

Using pip
```
$ pip install -r requirements.txt  # or requirements-dev.txt if you want to run unittests
```
or conda
```
$ conda install --file requirements.txt  # or requirements-dev.txt
```

Then install using:

```bash
sudo python setup.py install
```

If you face any problems during installation let us know, via issues, mail or at our gitter channel.

Development
============

Code
----

You can check the latest sources from our github repository 
use the command:

    git clone https://github.com/ravibeta/trimpy.git
    
This is merely a proof of concept and open-source so we can use it or modify it in any way.

Contributing
------------
 This is a sealed project because it is specific to the strategies implemented.

Testing
-------

After installation, you can launch the test form trimpy
source directory (you will need to have the ``nose`` package installed):
```bash
$ nosetests -v
```
to see the coverage of existing code use following command
```
$ nosetests --with-coverage --cover-package=trimpy
```

