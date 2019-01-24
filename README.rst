
.. image:: https://travis-ci.org/MacHu-GWU/attrs_mate-project.svg?branch=master
    :target: https://travis-ci.org/MacHu-GWU/attrs_mate-project?branch=master

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


.. image:: https://img.shields.io/badge/Link-Document-blue.svg
      :target: https://attrs_mate.readthedocs.io/index.html

.. image:: https://img.shields.io/badge/Link-API-blue.svg
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

`attrs <https://www.attrs.org/en/stable/index.html>`_ might be the second widely used python library for developers (First is ``requests``). It is the ultimate weapon for writing class.

``attrs_mate`` aims to bring more features to ``attrs``, and better code pattern.


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
        firstname = attr.ib(default=None)
        lastname = attr.ib(default=None)
        ssn = attr.ib(default=None)


    @attr.s
    class Degree(AttrsClass):
        name = attr.ib(default=None)
        year = attr.ib(default=None)


    @attr.s
    class People(AttrsClass):
        """
        - ``profile`` is nested field.
        - ``degrees`` is collection type field.
        """
        id = attr.ib(default=None)
        profile = attr.ib(
            converter=Profile.from_dict,
            validator=attr.validators.optional(
                attr.validators.instance_of(Profile)
            ),
            factory=Profile,
        )
        degrees = attr.ib(
            converter=lambda degrees: [
                Degree.from_dict(degree) for degree in degrees],
            factory=list,
        )

    people = People(
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
