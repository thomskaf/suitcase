"""
    indent.py
    ~~~~~~~~~

    :licence: none, Public Domain.
"""
from functools import wraps


def newobj(method):
    @wraps(method)
    def inner(self, *args, **kwargs):
        obj = self.__class__.__new__(self.__class__)
        obj.__dict__ = self.__dict__.copy()
        method(obj, *args, **kwargs)
        return obj
    return inner


class NWord(object):
    def __init__(self, content):
        self.content = content

    @newobj
    def indent(self, spaces=4):
        self.content = " " * spaces + self.content

    @newobj
    def suffix(self, content):
        self.content += " - {}".format(content)

    def __str__(self):
        return self.content


if __name__ == "__main__":
    p = NWord("Foobar")
    q = p.indent(2)
    r = p.indent(4)
    print(q)
    print(r)
