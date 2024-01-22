# -*- coding: utf-8 -*-

import typing as T
import pytest

import attrs
from attrs_mate import AttrsClass


# --- The correct way to implement nested schema and collection field ---
@attrs.define
class Profile(AttrsClass):
    """
    firstname, lastname, ssn are generic data type field.
    """

    firstname = AttrsClass.ib_str()
    lastname = AttrsClass.ib_str()
    ssn = AttrsClass.ib_str()


@attrs.define
class Degree(AttrsClass):
    name = AttrsClass.ib_str()
    year = AttrsClass.ib_int()


@attrs.define
class People(AttrsClass):
    """
    - ``profile`` is nested field.
    - ``degrees`` is collection type field.
    """

    id = AttrsClass.ib_int()
    profile = Profile.ib_nested()
    degrees = Degree.ib_list_of_nested()


class TestNesting:
    def test_from_dict1(self):
        """
        constructor data is generic dict
        """
        people = People(
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
        people_data = people.to_dict()
        people1 = People.from_dict(people_data)
        people1_data = people1.to_dict()
        assert people == people1
        assert people_data == people1_data

    def test_from_dict2(self):
        """
        constructor data is already object
        """
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
        people1 = People.from_dict(people_data)
        people1_data = people1.to_dict()
        assert people == people1
        assert people_data == people1_data

    def test_from_dict3(self):
        """
        nested value is None.
        """
        people = People(
            id=1,
            profile=None,
            degrees=None,
        )
        people_data = people.to_dict()
        people1 = People.from_dict(people_data)
        people1_data = people1.to_dict()
        assert people == people1
        assert people_data == people1_data

    def test_profile_degrees_default_value(self):
        people = People(id=1)
        assert people.profile is None
        assert people.degrees == list()

        people_data = people.to_dict()
        people1 = People.from_dict(people_data)
        assert people == people1
        assert people1.profile is None
        assert people1.degrees == list()

    def test_ib_map_of_nested(self):
        @attrs.define
        class Record(AttrsClass):
            record_id: str = AttrsClass.ib_str()

        @attrs.define
        class Batch(AttrsClass):
            batch_id: str = AttrsClass.ib_str()
            records: T.Dict[str, Record] = Record.ib_map_of_nested(key_type=str, value_nullable=True)

        batch = Batch(
            batch_id="b-1",
            records={"r-1": Record(record_id="r-1")},
        )
        batch_data = batch.to_dict()
        batch1 = Batch.from_dict(batch_data)
        batch1_data = batch.to_dict()
        assert batch == batch1
        assert batch_data == batch1_data

        batch = Batch(
            batch_id="b-1",
            records={"r-1": None},
        )
        batch_data = batch.to_dict()
        batch1 = Batch.from_dict(batch_data)
        batch1_data = batch.to_dict()
        assert batch == batch1
        assert batch_data == batch1_data

        batch = Batch(
            batch_id="b-1",
            records=None,
        )
        batch_data = batch.to_dict()
        batch1 = Batch.from_dict(batch_data)
        batch1_data = batch.to_dict()
        assert batch == batch1
        assert batch_data == batch1_data


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
