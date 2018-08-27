UK Postcode
===============================

version number: 0.0.1
author: Alisson Silveira

Overview
--------

Validation and formatting for UK Postcodes.

Python Version
--------------
Python >=3.6

Installation / Usage
--------------------

To install use pip:

    $ pip install git://github.com/4lissonsilveira/uk_postcode.git#egg=uk_postcode


Or clone the repo:

    $ git clone https://github.com/4alissonsilveira/uk_postcode.git
    $ python setup.py install
    
Example
-------

```python
from uk_postcode.utils import validate
print(validate('EC1A 1BB'))
True

from uk_postcode.utils import format_postcode
print(format_postcode('EC1A1BB'))
'EC1A 1BB'
```

Tests
-----
    $ pytest
