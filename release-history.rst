.. _release_history:

Release and Version History
==============================================================================


1.0.3 (TODO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


1.0.2 (2022-03-24)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- add :meth:`attrs_mate.mate.AttrsClass.ib_generic`
- add :meth:`attrs_mate.mate.AttrsClass.ib_list_of_generic`
- add :meth:`attrs_mate.mate.AttrsClass.ib_dict_of_generic`


1.0.1 (2022-03-24)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- more typed field with validators.

**Miscellaneous**

- widely use the new API ``@attr.define`` and ``attr.field`` to class definition.


1.0.0 (2021-06-24)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Use type hint

**Minor Improvements**

- More test case for nested object

**Miscellaneous**

- Drop support for Python2.7, only tested on Python3.6 +
- move CI from travis to GitHub CI
- add test on windows


0.0.5 (2019-08-22)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- add ``AttrClss.ib_str()``, ``AttrClss.ib_int()``, ``AttrClss.ib_nested()``, ``AttrClss.ib_list_of_nested()``

**Miscellaneous**

- requires attrs >= 19.1.0 to make ``attr.validators.deep_iterable`` works


0.0.4 (2019-02-07)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- remove reference to newly initiated object if the object is already in cache.


0.0.3 (2019-01-24)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- add LazyClass, support cached instance, cached property
- use attrs >= 17.4.0

**Minor Improvements**

- improve document


0.0.2 (2017-09-05)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- allow read complex object from dict data. good support for nesting.

**Miscellaneous**

- use readthedoc to host document.



0.0.1 (2017-10-10)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- First release