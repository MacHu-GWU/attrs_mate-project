
.. image:: https://github.com/MacHu-GWU/attrs_mate-project/workflows/CI/badge.svg
    :target: https://github.com/MacHu-GWU/attrs_mate-project/actions?query=workflow:CI

.. image:: https://codecov.io/gh/MacHu-GWU/attrs_mate-project/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/MacHu-GWU/attrs_mate-project

.. image:: https://img.shields.io/pypi/v/attrs_mate.svg
    :target: https://pypi.python.org/pypi/attrs_mate

.. image:: https://img.shields.io/pypi/l/attrs_mate.svg
    :target: https://pypi.python.org/pypi/attrs_mate

.. image:: https://img.shields.io/pypi/pyversions/attrs_mate.svg
    :target: https://pypi.python.org/pypi/attrs_mate

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/attrs_mate-project

------

.. image:: https://img.shields.io/badge/Link-Document-orange.svg
      :target: https://attrs_mate.readthedocs.io/index.html

.. image:: https://img.shields.io/badge/Link-API-orange.svg
      :target: https://attrs_mate.readthedocs.io/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Source_Code-blue.svg
      :target: https://attrs_mate.readthedocs.io/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Install-blue.svg
      :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
      :target: https://github.com/MacHu-GWU/attrs_mate-project

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
      :target: https://github.com/MacHu-GWU/attrs_mate-project/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
      :target: https://github.com/MacHu-GWU/attrs_mate-project/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
      :target: https://pypi.org/pypi/attrs_mate#files


Welcome to ``attrs_mate`` Documentation
==============================================================================

.. contents::
    :class: this-will-duplicate-information-and-it-is-still-useful-here
    :depth: 1
    :local:


`attrs <https://www.attrs.org/en/stable/index.html>`_ makes writing class a lot of more fun!

``attrs_mate`` aims to bring more features to ``attrs``, less code, and better code pattern.


Usage1: More Utility Methods
------------------------------------------------------------------------------

.. code-block:: python

    from attrs_mate import attr, AttrsClass

    @attr.s
    class User(AttrsClass):
        id = attr.ib()
        name = attr.ib()

    user = User(id=1, name="Alice")
    user.keys() # ["id", "name"]
    user.values() # [1, "Alice"]
    user.items() # [("id", 1), ("name": "Alice")]
    user.to_dict() # {"id": 1, "name": "Alice"}
    user.to_OrderedDict() # OrderedDict([("id", 1), ("name": "Alice")])


Usage2: Allow attrs to construct complex object from dict data.
------------------------------------------------------------------------------

**Plus, this is an example of nesting schema**.

.. code-block:: python

    import attr
    from attrs_mate import AttrsClass


    @attr.s
    class Profile(AttrsClass):
        """
        firstname, lastname, ssn are generic data type field.
        """
        firstname = AttrsClass.ib_str() # default String Validator
        lastname = AttrsClass.ib_str()
        ssn = AttrsClass.ib_str()


    @attr.s
    class Degree(AttrsClass):
        name = AttrsClass.ib_str()
        year = AttrsClass.ib_int() # default Integer Validator


    @attr.s
    class People(AttrsClass):
        """
        - ``profile`` is nested field.
        - ``degrees`` is collection type field.
        """
        id = AttrsClass.ib_int()
        profile = Profile.ib_nested() # default Nested Schema Validator and Converter
        degrees = Degree.ib_list() # default Nested Schema Validator and Converter

    >>> people = People(
        id=1,
        profile=Profile(
            firstname="David",
            lastname="John",
            ssn="123-45-6789",
        ),
        degrees=[
            Degree(name="Bachelor", year=2004),
            Degree(name="Master", year=2006),
        ],
    )

    >>> people_data = people.to_dict()
    >>> people_data
    {
        'id': 1,
        'profile': {
            'lastname': 'John', 'ssn': '123-45-6789', 'firstname': 'David'
        },
        'degrees': [
            {'name': 'Bachelor', 'year': 2004},
            {'name': 'Master', 'year': 2006}
        ]
    }

    >>> people = People.from_dict(people_data)
    >>> people
    People(id=1, profile=Profile(firstname='David', lastname='John', ssn='123-45-6789'), degrees=[Degree(name='Bachelor', year=2004), Degree(name='Master', year=2006)])

Or you can just pass nested schema in dictionary, it works the same:

.. code-block:: python

    >>> people = People(
        id=1,
        profile=dict(
            firstname="David",
            lastname="John",
            ssn="123-45-6789",
        ),
        degrees=[
            dict(name="Bachelor", year=2004),
            dict(name="Master", year=2006),
        ],
    )


Usage3: Cached Instance and Property Attribute
------------------------------------------------------------------------------

.. code-block:: python

    from attrs_mate import attr, LazyClass

    @attr.s
    class User(LazyClass): # instance are cached
        id = attr.ib()
        lastname = attr.ib()
        firstname = attr.ib()
        uuid_called_count = attr.ib(default=0)
        fullname_called_count = attr.ib(default=0)

        @LazyClass.lazyproperty
        def uuid(self):
            self.uuid_called_count += 1
            return self.id

        @LazyClass.lazyproperty
        def fullname(self): # property method are cached
            self.fullname_called_count += 1
            return "{} {}".format(self.lastname, self.firstname)

    >>> user1 = User.lazymake(id=1, lastname="David", firstname="John")
    >>> user1.fullname_called_count
    0 # initially, fullname never been called
    >>> user1.fullname
    David John
    >>> user1.fullname_called_count
    1 # called once
    >>> user1.fullname
    David John
    >>> user1.fullname_called_count
    1 # User.fullname() not been called

    # use factory method to create new instance
    >>> user2 = User.lazymake(id=1, lastname="David", firstname="Kim")
    >>> id(user1) == id(user2)
    True # since
    >>> user2.firstname == "John"
    True
    >>> user2.fullname_called_count
    1 # already been called once, because it is actually user1


.. _install:

Install
------------------------------------------------------------------------------

``attrs_mate`` is released on PyPI, so all you need is:

.. code-block:: console

    $ pip install attrs_mate

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade attrs_mate
