# -*- coding: utf-8 -*-

"""
This module implements:

- :class:`AttrsClass`
- :class:`LazyClass`
"""

from typing import TypeVar, List, Union, Dict, OrderedDict, Any, Optional
import warnings
import collections
from datetime import date, datetime

import attr
import attr.validators as vs
import attrs


T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


@attrs.define
class AttrsClass:
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

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert to dictionary.
        """
        return attr.asdict(self)

    def to_OrderedDict(self) -> OrderedDict[str, Any]:
        """
        Convert to ordered dictionary.
        """
        return attr.asdict(self, dict_factory=collections.OrderedDict)

    @classmethod
    def from_dict(
        cls,
        dct_or_obj: Union[Dict[str, Any], "AttrsClass", None],
    ) -> Union["AttrsClass", None]:
        """
        Construct an instance from dictionary data.
        """
        if isinstance(dct_or_obj, cls):
            return dct_or_obj
        elif dct_or_obj is None:
            return None
        elif isinstance(dct_or_obj, dict):
            return cls(**dct_or_obj)
        else:  # pragma: no cover
            raise TypeError

    @classmethod
    def from_list(
        cls,
        list_of_dct_or_obj: List[Union[Dict[str, Any], "AttrsClass", None]],
    ) -> List[Union["AttrsClass", None]]:
        """
        Construct list of instance from list of dictionary data.
        """
        if isinstance(list_of_dct_or_obj, list):
            return [cls.from_dict(item) for item in list_of_dct_or_obj]
        elif list_of_dct_or_obj is None:
            return list()
        else:  # pragma: no cover
            raise TypeError

    @classmethod
    def from_mapper(
        cls,
        map_of_dct_or_obj: Optional[
            Dict[str, Union[Dict[str, Any], "AttrsClass", None]]
        ],
    ) -> Optional[Dict[str, Union[Dict[str, Any], "AttrsClass", None]]]:
        """
        Construct dict of instance from dict of :class:`AttrsClass` liked data.
        It could be a dictionary, an instance of this class, or None.
        """
        if isinstance(map_of_dct_or_obj, dict):
            return {k: cls.from_dict(v) for k, v in map_of_dct_or_obj.items()}
        elif map_of_dct_or_obj is None:
            return None
        else:  # pragma: no cover
            raise TypeError

    # --------------------------------------------------------------------------
    # Generic Type
    # --------------------------------------------------------------------------
    @classmethod
    def ib_generic(cls, type_: T, nullable=True, **kwargs):
        if "validator" not in kwargs:
            if nullable:
                kwargs["validator"] = vs.optional(vs.instance_of(type_))
            else:
                kwargs["validator"] = vs.instance_of(type_)
        return attr.field(**kwargs)

    @classmethod
    def ib_str(cls, nullable=True, **kwargs):
        """ """
        return cls.ib_generic(str, nullable=nullable, **kwargs)

    @classmethod
    def ib_int(cls, nullable=True, **kwargs):
        """ """
        return cls.ib_generic(int, nullable=nullable, **kwargs)

    @classmethod
    def ib_float(cls, nullable=True, **kwargs):
        """ """
        return cls.ib_generic(float, nullable=nullable, **kwargs)

    @classmethod
    def ib_bool(cls, nullable=True, **kwargs):
        """ """
        return cls.ib_generic(bool, nullable=nullable, **kwargs)

    @classmethod
    def ib_date(cls, nullable=True, **kwargs):
        """ """
        return cls.ib_generic(date, nullable=nullable, **kwargs)

    @classmethod
    def ib_datetime(cls, nullable=True, **kwargs):
        """ """
        return cls.ib_generic(datetime, nullable=nullable, **kwargs)

    # --------------------------------------------------------------------------
    # Collection Type
    # --------------------------------------------------------------------------
    @classmethod
    def ib_list(cls, nullable=True, **kwargs):
        """ """
        return cls.ib_generic(list, nullable=nullable, **kwargs)

    @classmethod
    def ib_tuple(cls, nullable=True, **kwargs):
        """ """
        return cls.ib_generic(tuple, nullable=nullable, **kwargs)

    @classmethod
    def ib_set(cls, nullable=True, **kwargs):
        """ """
        return cls.ib_generic(set, nullable=nullable, **kwargs)

    @classmethod
    def ib_dict(cls, nullable=True, **kwargs):
        """ """
        return cls.ib_generic(dict, nullable=nullable, **kwargs)

    # --------------------------------------------------------------------------
    # List of Generic Type
    # --------------------------------------------------------------------------
    @classmethod
    def ib_list_of_generic(cls, member_type: T, nullable=True, **kwargs):
        if "validator" not in kwargs:
            if nullable:
                kwargs["validator"] = vs.optional(
                    vs.deep_iterable(
                        member_validator=vs.instance_of(member_type),
                        iterable_validator=vs.instance_of(list),
                    )
                )
            else:
                kwargs["validator"] = vs.deep_iterable(
                    member_validator=vs.instance_of(member_type),
                    iterable_validator=vs.instance_of(list),
                )

        return attr.field(**kwargs)

    @classmethod
    def ib_list_of_str(cls, nullable=True, **kwargs):
        """ """
        return cls.ib_list_of_generic(str, nullable=nullable, **kwargs)

    @classmethod
    def ib_list_of_int(cls, nullable=True, **kwargs):
        """ """
        return cls.ib_list_of_generic(int, nullable=nullable, **kwargs)

    @classmethod
    def ib_list_of_float(cls, nullable=True, **kwargs):
        """ """
        return cls.ib_list_of_generic(float, nullable=nullable, **kwargs)

    @classmethod
    def ib_list_of_bool(cls, nullable=True, **kwargs):
        """ """
        return cls.ib_list_of_generic(bool, nullable=nullable, **kwargs)

    @classmethod
    def ib_list_of_date(cls, nullable=True, **kwargs):
        """ """
        return cls.ib_list_of_generic(date, nullable=nullable, **kwargs)

    @classmethod
    def ib_list_of_datetime(cls, nullable=True, **kwargs):
        """ """
        return cls.ib_list_of_generic(datetime, nullable=nullable, **kwargs)

    # --------------------------------------------------------------------------
    # Dict of Generic Type
    # --------------------------------------------------------------------------
    @classmethod
    def ib_dict_of_generic(
        cls,
        key_type: K,
        value_type: V,
        nullable=True,
        value_nullable=True,
        **kwargs,
    ):
        """ """
        if "validator" not in kwargs:
            if value_nullable:
                key_validator = vs.optional(vs.instance_of(key_type))
                value_validator = vs.optional(vs.instance_of(value_type))
            else:
                key_validator = vs.instance_of(key_type)
                value_validator = vs.instance_of(value_type)
            if nullable:
                kwargs["validator"] = vs.optional(
                    vs.deep_mapping(
                        key_validator=key_validator,
                        value_validator=value_validator,
                    )
                )
            else:
                kwargs["validator"] = vs.deep_mapping(
                    key_validator=key_validator,
                    value_validator=value_validator,
                )

        return attr.field(**kwargs)

    # --------------------------------------------------------------------------
    # Nested Type
    # --------------------------------------------------------------------------
    @classmethod
    def ib_nested(cls, **kwargs):
        """
        Declare a field that is another :class:`AttrsClass`.

        .. note::

            nested object has default value ``None``, so it has to put it after
            those attribute doesn't has default value.
        """
        if "converter" not in kwargs:
            kwargs["converter"] = cls.from_dict
        if "validator" not in kwargs:
            kwargs["validator"] = vs.optional(vs.instance_of(cls))
        if "default" not in kwargs:
            kwargs["default"] = None
        return attr.field(**kwargs)

    @classmethod
    def ib_list_of_nested(cls, **kwargs):
        """
        Declare a field that is a list of other :class:`AttrsClass`.
        """
        if "converter" not in kwargs:
            kwargs["converter"] = cls.from_list
        if "validator" not in kwargs:
            kwargs["validator"] = vs.deep_iterable(
                member_validator=vs.instance_of(cls),
                iterable_validator=vs.instance_of(list),
            )
        if "factory" not in kwargs:
            kwargs["factory"] = list
        return attr.field(**kwargs)

    @classmethod
    def ib_map_of_nested(
        cls,
        key_type: K,
        nullable=True,
        value_nullable=True,
        **kwargs,
    ):
        """
        Declare a field that is a mapper that key is any hashable value and
         value is instance of :class:`AttrsClass`.
        """
        if "converter" not in kwargs:
            kwargs["converter"] = cls.from_mapper
        if "validator" not in kwargs:
            if value_nullable:
                key_validator = vs.optional(vs.instance_of(key_type))
                value_validator = vs.optional(vs.instance_of(cls))
            else:  # pragma: no cover
                key_validator = vs.instance_of(key_type)
                value_validator = vs.instance_of(cls)
            if nullable:
                kwargs["validator"] = vs.optional(
                    vs.deep_mapping(
                        key_validator=key_validator,
                        value_validator=value_validator,
                    )
                )
            else:  # pragma: no cover
                kwargs["validator"] = vs.deep_mapping(
                    key_validator=key_validator,
                    value_validator=value_validator,
                )
        if "factory" not in kwargs:
            kwargs["factory"] = dict
        return attr.field(**kwargs)


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

    .. deprecated:: 1.2.X

        introduced cached property >=3.8, which is better than this
        if <3.7, you can use https://pypi.org/project/cached-property/
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
            warnings.warn(
                "deprecated, will be removed in 1.2.X, use cached_property instead",
                DeprecationWarning,
            )
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
