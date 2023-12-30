# -*- coding: utf-8 -*-

import pytest

from collections import OrderedDict

import attrs
from attrs_mate.mate import AttrsClass

try:
    from functools import cached_property
except ImportError:
    from cached_property import cached_property


@attrs.define(
    slots=False,
)
class User(AttrsClass):
    id = attrs.field()
    name = attrs.field()


@attrs.define(
    slots=False, # to use cached_property, you have to disable slots
)
class DBUser(User):
    role = attrs.field()

    @cached_property
    def desc(self) -> str:
        return f"{self.id} {self.name} {self.role}"


def test():
    admin = DBUser(id=1, name="Alice", role="admin")
    assert admin.keys() == ["id", "name", "role"]
    assert admin.values() == [1, "Alice", "admin"]
    assert admin.items() == [("id", 1), ("name", "Alice"), ("role", "admin")]
    assert admin.to_dict() == {"id": 1, "name": "Alice", "role": "admin"}
    assert admin.to_OrderedDict() == {"id": 1, "name": "Alice", "role": "admin"}
    assert isinstance(admin.to_OrderedDict(), OrderedDict)

    assert admin.desc == "1 Alice admin"


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
