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

.. image:: https://img.shields.io/badge/Star_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/attrs_mate-project


Welcome to ``attrs_mate`` Documentation
==============================================================================

Usage: more utility methods.

.. code-block:: python

    import attr
    from attrs_mate import AttrsClass

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


Feature: allow attrs to load complex object from dict data.

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
            convert=Profile.from_dict,
            factory=Profile,
        )
        degrees = attr.ib(
            convert=lambda degrees: [
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
    people_data = people.to_dict()

    # {
    #     'id': 1,
    #     'profile': {
    #         'lastname': 'John', 'ssn': '123-45-6789', 'firstname': 'David'
    #     },
    #     'degrees': [
    #         {'name': 'Bachelor', 'year': 2004},
    #         {'name': 'Master', 'year': 2006}
    #     ]
    # }
    print(people_data)

    people = People.from_dict(people_data)
    # People(id=1, profile=Profile(firstname='David', lastname='John', ssn='123-45-6789'), degrees=[Degree(name='Bachelor', year=2004), Degree(name='Master', year=2006)])
    print(people)


Quick Links
------------------------------------------------------------------------------

- .. image:: https://img.shields.io/badge/Link-Document-red.svg
      :target: https://attrs_mate.readthedocs.io/index.html

- .. image:: https://img.shields.io/badge/Link-API_Reference_and_Source_Code-red.svg
      :target: https://attrs_mate.readthedocs.io/py-modindex.html

- .. image:: https://img.shields.io/badge/Link-Install-red.svg
      :target: `install`_

- .. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
      :target: https://github.com/MacHu-GWU/attrs_mate-project

- .. image:: https://img.shields.io/badge/Link-Submit_Issue_and_Feature_Request-blue.svg
      :target: https://github.com/MacHu-GWU/attrs_mate-project/issues

- .. image:: https://img.shields.io/badge/Link-Download-blue.svg
      :target: https://pypi.python.org/pypi/attrs_mate#downloads


.. _install:

Install
------------------------------------------------------------------------------

``attrs_mate`` is released on PyPI, so all you need is:

.. code-block:: console

    $ pip install attrs_mate

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade attrs_mate