# -*- coding: utf-8 -*-

import pytest
from attrs_mate import attr, LazyClass


@attr.define
class User(LazyClass):
    """
    This also works::

        class User(LazyClass):
            def __init__(self, id, lastname, firstname,
                         uuid_called_count=0, fullname_called_count=0):
                self.id = id
                self.lastname = lastname
                self.firstname = firstname
                self.uuid_called_count = uuid_called_count
                self.fullname_called_count = fullname_called_count
    """
    id = attr.field()
    lastname = attr.field()
    firstname = attr.field()
    uuid_called_count = attr.field(default=0)
    fullname_called_count = attr.field(default=0)

    @LazyClass.lazyproperty
    def uuid(self):
        self.uuid_called_count += 1
        return self.id

    @LazyClass.lazyproperty
    def fullname(self):
        self.fullname_called_count += 1
        return "{} {}".format(self.lastname, self.firstname)


class TestLazyClassSampleUsage:
    def test(self):
        user1 = User.lazymake(id=1, lastname="David", firstname="John")
        assert user1.fullname_called_count == 0
        _ = user1.fullname
        assert user1.fullname_called_count == 1
        _ = user1.fullname
        assert user1.fullname_called_count == 1

        user2 = User.lazymake(id=1, lastname="David", firstname="Kim")
        assert id(user1) == id(user2)
        assert user2.firstname == "John"
        assert user2.fullname_called_count == 1
        _ = user2.fullname
        assert user2.fullname_called_count == 1

        user3 = User.lazymake(id=2, lastname="David", firstname="John")
        assert user3.fullname_called_count == 0


@attr.define
class Foo(LazyClass):
    id = attr.field()


class TestLazyClassWrongUsage:
    def test(self):
        with pytest.raises(NotImplementedError):
            foo = Foo.lazymake(id=1)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
