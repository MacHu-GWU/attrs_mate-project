# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx


def test():
    import attrs_mate

    _ = attrs_mate.attr
    _ = attrs_mate.attrs
    _ = attrs_mate.AttrsClass
    _ = attrs_mate.LazyClass

    _ = attrs_mate.AttrsClass.ib_generic
    _ = attrs_mate.AttrsClass.ib_str
    _ = attrs_mate.AttrsClass.ib_int
    _ = attrs_mate.AttrsClass.ib_float
    _ = attrs_mate.AttrsClass.ib_bool
    _ = attrs_mate.AttrsClass.ib_date
    _ = attrs_mate.AttrsClass.ib_datetime
    _ = attrs_mate.AttrsClass.ib_list
    _ = attrs_mate.AttrsClass.ib_tuple
    _ = attrs_mate.AttrsClass.ib_set
    _ = attrs_mate.AttrsClass.ib_dict
    _ = attrs_mate.AttrsClass.ib_list_of_generic
    _ = attrs_mate.AttrsClass.ib_list_of_str
    _ = attrs_mate.AttrsClass.ib_list_of_int
    _ = attrs_mate.AttrsClass.ib_list_of_float
    _ = attrs_mate.AttrsClass.ib_list_of_bool
    _ = attrs_mate.AttrsClass.ib_list_of_date
    _ = attrs_mate.AttrsClass.ib_list_of_datetime
    _ = attrs_mate.AttrsClass.ib_dict_of_generic
    _ = attrs_mate.AttrsClass.ib_nested
    _ = attrs_mate.AttrsClass.ib_list_of_nested


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
