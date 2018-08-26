UK Postcode
===============================

version number: 0.0.1
author: Alisson Silveira

Overview
--------

Validation and formatting for UK Postcodes.

Installation / Usage
--------------------

To install use pip:

    $ pip install uk_postalcode


Or clone the repo:

    $ git clone https://github.com/4alisson/uk_postalcode.git
    $ python setup.py install
    
Example
-------

```python
from uk_postcode.utils import validate
print(validate('EC1A 1BB'))
True

from uk_postcode.utils import format
print(format('EC1A1BB'))
'EC1A 1BB'
```

Tests
-----
    $ pytest
