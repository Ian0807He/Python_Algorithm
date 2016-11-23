class SingleObject(object):
    _shared_state = {}
    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj
