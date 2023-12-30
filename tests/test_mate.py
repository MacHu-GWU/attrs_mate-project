# -*- coding: utf-8 -*-

import pytest

import attrs
from attrs_mate.mate import AttrsClass
from collections import OrderedDict


@attrs.define
class User(AttrsClass):
    id = attrs.field()
    name = attrs.field()


@attrs.define
class DBUser(User):
    role = attrs.field()


def test():
    admin = DBUser(id=1, name="Alice", role="admin")
    assert admin.keys() == ["id", "name", "role"]
    assert admin.values() == [1, "Alice", "admin"]
    assert admin.items() == [("id", 1), ("name", "Alice"), ("role", "admin")]
    assert admin.to_dict() == {"id": 1, "name": "Alice", "role": "admin"}
    assert admin.to_OrderedDict() == {
        "id": 1, "name": "Alice", "role": "admin"}
    assert isinstance(admin.to_OrderedDict(), OrderedDict)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
