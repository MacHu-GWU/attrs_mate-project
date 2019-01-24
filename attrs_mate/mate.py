# -*- coding: utf-8 -*-

"""
This module implements:

- :class:`AttrsClass`
- :class:`LazyClass`
"""

import attr
import collections


class AttrsClass(object):
    """
    A mixins class provideing more utility methods.
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
        return attr.asdict(self, dict_factory=collections.OrderedDict)

    @classmethod
    def from_dict(cls, dct_or_obj):
        """
        Construct an instance from dictionary data.
        """
        if isinstance(dct_or_obj, cls):
            return dct_or_obj
        else:
            return cls(**dct_or_obj)


DictClass = dict
"""
This might work too::

    import weakref
    DictClass = weakref.WeakValueDictionary
"""


class LazyClass(AttrsClass):
    """
    Inheriting from this class gives you a factory method
    :meth:`LazyClass.lazymake`. It allows you to use the same API as the default
    ``__init__(*args, **kwargs)``, but using cache.

    You can implement your own ``uuid(self)`` property method like this. The
    uuid value will be used as the key for new instance::

        class MyClass(LazyClass):
            ...

            @LazyClass.lazyproperty
            def uuid(self):
                return ...

    :class:`LazyClass.lazyproperty` is a decorator which is similar to
    the built-in ``property`` decorator, **but the returned value
    are automatically cached, and will be called only once**.

    Reference:

    - 8.10 使用延迟计算属性: https://python-cookbook-3rd-edition.readthedocs.io/zh_CN/latest/c08/p10_using_lazily_computed_properties.html
    - 8.25 创建缓存实例: https://python-cookbook-3rd-edition.readthedocs.io/zh_CN/latest/c08/p25_creating_cached_instances.html
    """
    _instance_cache = DictClass()

    class lazyproperty(object):
        """
        decorator for cached property method.

        Usage Example::

            class User(object):
                def __init__(self, firstname, lastname):
                    self.firstname = firstname
                    self.lastname = lastname

                @LazyClass.lazyproperty
                def fullname(self):
                    return "{} {}".format(self.lastname, self.firstname)
        """

        def __init__(self, func):
            self.func = func

        def __get__(self, instance, cls):
            if instance is None:  # pragma: no cover
                return self
            else:
                value = self.func(instance)
                setattr(instance, self.func.__name__, value)
                return value

    @lazyproperty
    def uuid(self):
        """
        Return the custom uuid.

        :return: str / int, any hashable object.
        """
        msg = "You have to implement the uuid property method!"
        raise NotImplementedError(msg)

    @lazyproperty
    def _classname(self):
        """
        Returns class name string.
        """
        return self.__class__.__name__

    @classmethod
    def lazymake(cls, *args, **kwargs):
        """
        A factory method to make an object, prefer to use cache.

        :param args: same argument as ``Class.__init__(*args, **kwargs)``
        :param kwargs: same argument as ``Class.__init__(*args, **kwargs)``
        """
        obj = cls(*args, **kwargs)
        try:
            if obj.uuid in cls._instance_cache[obj._classname]:
                return cls._instance_cache[obj._classname][obj.uuid]
            else:
                cls._instance_cache[obj._classname][obj.uuid] = obj
                return obj
        except KeyError:
            cls._instance_cache[obj._classname] = DictClass([(obj.uuid, obj)])
            return obj
