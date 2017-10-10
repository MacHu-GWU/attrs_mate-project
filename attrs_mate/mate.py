#!/usr/bin/env python
# -*- coding: utf-8 -*-

import attr
import collections


class AttrsClass(object):
    def keys(self):
        return [a.name for a in self.__attrs_attrs__]

    def values(self):
        return [getattr(self, a.name) for a in self.__attrs_attrs__]

    def items(self):
        return list(zip(self.keys(), self.values()))

    def to_dict(self):
        return attr.asdict(self)

    def to_OrderedDict(self):
        return collections.OrderedDict(self.items())
