#!/usr/bin/env python
# -*- coding: utf-8 -*-

import attr
import collections


class AttrsClass(object):
    """
    Provides more utility methods.
    """

    def keys(self):
        """
        Fieldname list.
        """
        return [a.name for a in self.__attrs_attrs__]

    def values(self):
        """
        Value list.
        """
        return [getattr(self, a.name) for a in self.__attrs_attrs__]

    def items(self):
        """
        Fieldname and value pair list.
        """
        return list(zip(self.keys(), self.values()))

    def to_dict(self):
        """
        Convert to dictionary.
        """
        return attr.asdict(self)

    def to_OrderedDict(self):
        """
        Convert to ordered dictionary.
        """
        return collections.OrderedDict(self.items())

    @classmethod
    def from_dict(cls, dct_or_obj):
        """
        Construct an instance from dictionary data.
        """
        if isinstance(dct_or_obj, cls):
            return dct_or_obj
        else:
            return cls(**dct_or_obj)
