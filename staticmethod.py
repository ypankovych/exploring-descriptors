class StaticMethod:

    def __init__(self, method):
        self.method = method

    def __get__(self, instance, owner):
        return self.method


class Foo:

    @StaticMethod
    def bar():
        return "Hello, world!"


if __name__ == '__main__':
    print(Foo.bar())  # Hello, world!
    print(Foo().bar())  # Hello, world!
