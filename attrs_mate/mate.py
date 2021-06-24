# -*- coding: utf-8 -*-

"""
This module implements:

- :class:`AttrsClass`
- :class:`LazyClass`
"""

import attr
import collections


@attr.s
class AttrsClass(object):
    """
    A mixins class provideing more utility methods.
    """

    @classmethod
    def keys(cls):
        """
        Fieldname list.
        """
        return [field.name for field in attr.fields(cls)]

    def values(self):
        """
        Value list.
        """
        return [getattr(self, field_name) for field_name in self.keys()]

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

        :type dct_or_obj: Union[dict, None]
        :rtype: cls
        """
        if isinstance(dct_or_obj, cls):
            return dct_or_obj
        elif dct_or_obj is None:
            return None
        elif isinstance(dct_or_obj, dict):
            return cls(**dct_or_obj)
        else:  # pragma: no cover
            return TypeError

    @classmethod
    def _from_list(cls, list_of_dct_or_obj):
        """
        Construct list of instance from list of dictionary data.

        :type list_of_dct_or_obj: Union[List[cls], List[dict], None]
        :rtype: List[cls]
        """
        if isinstance(list_of_dct_or_obj, list):
            return [cls.from_dict(item) for item in list_of_dct_or_obj]
        elif list_of_dct_or_obj is None:
            return list()
        else:  # pragma: no cover
            return TypeError

    @classmethod
    def ib_str(cls, **kwargs):
        if "validator" not in kwargs:
            kwargs["validator"] = attr.validators.optional(
                attr.validators.instance_of(str)
            )
        return attr.ib(**kwargs)

    @classmethod
    def ib_int(cls, **kwargs):
        if "validator" not in kwargs:
            kwargs["validator"] = attr.validators.optional(
                attr.validators.instance_of(int)
            )
        return attr.ib(**kwargs)

    # complex object
    @classmethod
    def ib_nested(cls, **kwargs):
        if "converter" not in kwargs:
            kwargs["converter"] = cls.from_dict
        if "validator" not in kwargs:
            kwargs["validator"] = attr.validators.optional(
                attr.validators.instance_of(cls)
            )
        if "default" not in kwargs:
            kwargs["default"] = None
        return attr.ib(**kwargs)

    @classmethod
    def ib_list_of_nested(cls, **kwargs):
        if "converter" not in kwargs:
            kwargs["converter"] = cls._from_list
        if "validator" not in kwargs:
            kwargs["validator"] = attr.validators.deep_iterable(
                member_validator=attr.validators.instance_of(cls),
                iterable_validator=attr.validators.instance_of(list),
            )
        if "factory" not in kwargs:
            kwargs["factory"] = list
        return attr.ib(**kwargs)


DictClass = dict
"""
This might work too::

    import weakref
    DictClass = weakref.WeakValueDictionary
"""


@attr.s
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
                obj_from_cache = cls._instance_cache[obj._classname][obj.uuid]
                del obj
                return obj_from_cache
            else:
                cls._instance_cache[obj._classname][obj.uuid] = obj
                return obj
        except KeyError:
            cls._instance_cache[obj._classname] = DictClass([(obj.uuid, obj)])
            return obj
