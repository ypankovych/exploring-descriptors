class Super:

    def __init__(self, __type, __obj):
        self.__obj = __obj
        self.__type = __type

    def __getattr__(self, item):
        start_type = type(self.__obj)
        mro = iter(start_type.__mro__)

        for cls in mro:
            if cls is self.__type:
                break

        for cls in mro:
            if item in cls.__dict__:
                attr = cls.__dict__[item]
                if hasattr(attr, "__get__"):
                    attr = attr.__get__(self.__obj)
                return attr
        raise AttributeError(item)


class A:
    def foo(self):
        return "A"


class B(A):
    def foo(self):
        return "B" + Super(B, self).foo()


class C(B):
    def foo(self):
        return "C" + Super(C, self).foo()


if __name__ == '__main__':
    print(C().foo())  # CBA
