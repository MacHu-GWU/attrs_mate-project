# -*- coding: utf-8 -*-

import pytest
from datetime import date, datetime
import attr
from attrs_mate.mate import AttrsClass


@attr.define
class Invalid:
    pass


def test_ib_generic():
    @attr.define
    class Data(AttrsClass):
        ib_str = AttrsClass.ib_str()
        ib_int = AttrsClass.ib_int()
        ib_float = AttrsClass.ib_float()
        ib_bool = AttrsClass.ib_bool()
        ib_date = AttrsClass.ib_date()
        ib_datetime = AttrsClass.ib_datetime()

    data = Data(
        ib_str="s",
        ib_int=1,
        ib_float=3.14,
        ib_bool=True,
        ib_date=date.today(),
        ib_datetime=datetime.now(),
    )
    invalid = Invalid()

    with pytest.raises(TypeError):
        attr.evolve(data, ib_str=invalid)

    with pytest.raises(TypeError):
        attr.evolve(data, ib_int=invalid)

    with pytest.raises(TypeError):
        attr.evolve(data, ib_float=invalid)

    with pytest.raises(TypeError):
        attr.evolve(data, ib_bool=invalid)

    with pytest.raises(TypeError):
        attr.evolve(data, ib_date=invalid)

    with pytest.raises(TypeError):
        attr.evolve(data, ib_datetime=invalid)

    # None is OK
    data = Data(
        ib_str=None,
        ib_int=None,
        ib_float=None,
        ib_bool=None,
        ib_date=None,
        ib_datetime=None,
    )

    # None is NOT OK
    @attr.define
    class DataNotNullable(AttrsClass):
        v = AttrsClass.ib_str(nullable=False)

    with pytest.raises(TypeError):
        DataNotNullable(v=None)


def test_ib_collection():
    @attr.define
    class Data(AttrsClass):
        ib_list = AttrsClass.ib_list()
        ib_tuple = AttrsClass.ib_tuple()
        ib_set = AttrsClass.ib_set()
        ib_dict = AttrsClass.ib_dict()

    data = Data(
        ib_list=[1, 2],
        ib_tuple=(1, 2),
        ib_set={1, 2},
        ib_dict={"a": 1, "b": 2},
    )
    invalid = Invalid()

    with pytest.raises(TypeError):
        attr.evolve(data, ib_list=invalid)

    with pytest.raises(TypeError):
        attr.evolve(data, ib_tuple=invalid)

    with pytest.raises(TypeError):
        attr.evolve(data, ib_set=invalid)

    with pytest.raises(TypeError):
        attr.evolve(data, ib_dict=invalid)

    # None is OK
    data = Data(
        ib_list=None,
        ib_tuple=None,
        ib_set=None,
        ib_dict=None,
    )

    # None is NOT OK
    @attr.define
    class DataNotNullable(AttrsClass):
        v = AttrsClass.ib_list(nullable=False)

    with pytest.raises(TypeError):
        DataNotNullable(v=None)


def test_ib_list_of_generic():
    @attr.define
    class Data(AttrsClass):
        ib_str = AttrsClass.ib_list_of_str()
        ib_int = AttrsClass.ib_list_of_int()
        ib_float = AttrsClass.ib_list_of_float()
        ib_bool = AttrsClass.ib_list_of_bool()
        ib_date = AttrsClass.ib_list_of_date()
        ib_datetime = AttrsClass.ib_list_of_datetime()

    data = Data(
        ib_str=["s", ],
        ib_int=[1, ],
        ib_float=[3.14, ],
        ib_bool=[True, ],
        ib_date=[date.today(), ],
        ib_datetime=[datetime.now(), ],
    )
    invalid = Invalid()

    with pytest.raises(TypeError):
        attr.evolve(data, ib_str=invalid)

    with pytest.raises(TypeError):
        attr.evolve(data, ib_int=invalid)

    with pytest.raises(TypeError):
        attr.evolve(data, ib_float=invalid)

    with pytest.raises(TypeError):
        attr.evolve(data, ib_bool=invalid)

    with pytest.raises(TypeError):
        attr.evolve(data, ib_date=invalid)

    with pytest.raises(TypeError):
        attr.evolve(data, ib_datetime=invalid)

    data = Data(
        ib_str=None,
        ib_int=None,
        ib_float=None,
        ib_bool=None,
        ib_date=None,
        ib_datetime=None,
    )

    @attr.define
    class DataNotNullable(AttrsClass):
        v = AttrsClass.ib_list_of_str(nullable=False)

    with pytest.raises(TypeError):
        DataNotNullable(v=None)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])