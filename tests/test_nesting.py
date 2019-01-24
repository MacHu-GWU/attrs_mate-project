#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import six
import attr
from attrs_mate import AttrsClass


# --- The correct way to implement nested schema and collection field ---
@attr.s
class Profile(AttrsClass):
    """
    firstname, lastname, ssn are generic data type field.
    """
    firstname = attr.ib(
        validator=attr.validators.optional(
            attr.validators.instance_of(six.string_types)
        ),
        default=None,
    )
    lastname = attr.ib(
        validator=attr.validators.optional(
            attr.validators.instance_of(six.string_types)
        ),
        default=None,
    )
    ssn = attr.ib(
        validator=attr.validators.optional(
            attr.validators.instance_of(six.string_types)
        ),
        default=None,
    )


@attr.s
class Degree(AttrsClass):
    name = attr.ib(
        validator=attr.validators.optional(
            attr.validators.instance_of(six.string_types)
        ),
        default=None,
    )
    year = attr.ib(
        validator=attr.validators.optional(
            attr.validators.instance_of(six.integer_types)
        ),
        default=None,
    )


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


class TestNesting(object):
    def test_from_dict(self):
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
        assert people == people1

    def test_profile_degrees(self):
        people = People()
        people_data = people.to_dict()
        people1 = People.from_dict(people_data)
        assert people == people1
        assert people1.profile.firstname is None
        assert people1.profile.lastname is None
        assert people1.profile.ssn is None
        assert people1.degrees == list()


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
