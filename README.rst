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

Usage::

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


Quick Links
------------------------------------------------------------------------------

- .. image:: https://img.shields.io/badge/Link-Document-red.svg
      :target: http://www.wbh-doc.com.s3.amazonaws.com/attrs_mate/index.html

- .. image:: https://img.shields.io/badge/Link-API_Reference_and_Source_Code-red.svg
      :target: http://www.wbh-doc.com.s3.amazonaws.com/attrs_mate/py-modindex.html

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