from functools import partial


class ClassMethod:

    def __init__(self, method):
        self.method = method

    def __get__(self, instance, owner):
        return partial(self.method, owner)


class Foo:
    name = "Yaroslav"

    @ClassMethod
    def bar(cls):
        return cls.name


if __name__ == '__main__':
    obj = Foo()
    print(obj.bar())  # Yaroslav
    print(Foo.bar())  # Yaroslav
