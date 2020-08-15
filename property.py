class Property:

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if not doc:
            doc = self.fget.__doc__
        self.__doc__ = doc

    def __set__(self, instance, value):
        if not self.fset:
            raise AttributeError("can't set attribute")
        self.fset(instance, value)

    def __get__(self, instance, owner):
        if not self.fset:
            raise AttributeError("can't get attribute")
        return self.fget(instance)

    def __delete__(self, instance):
        if not self.fset:
            raise AttributeError("can't delete attribute")
        self.fdel(instance)

    def setter(self, fset):
        self.fset = fset
        return self

    def getter(self, fget):
        self.fget = fget
        return self

    def deleter(self, fdel):
        self.fdel = fdel
        return self


class Foo:

    def __init__(self, age):
        self.__age = age

    @Property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 100:
            raise ValueError
        self.__age = age

    @age.deleter
    def age(self):
        del self.__age


if __name__ == '__main__':
    obj = Foo(age=21)
    print(obj.age)  # 21
    obj.age = 10
    print(obj.age)  # 10
    del obj.age
    print(obj.age)  # raise
