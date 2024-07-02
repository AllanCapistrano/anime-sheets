from deprecated import deprecated


@deprecated(version='1.2.1', reason="You should use another function")
def some_old_function(x, y):
    return x + y


class SomeClass(object):
    @deprecated(version='1.3.0', reason="This method is deprecated")
    def some_old_method(self, x, y):
        return x + y


some_old_function(12, 34)
obj = SomeClass()
obj.some_old_method(5, 8)