import pytest

class TestTuple():

    mytuple = (4, 5, 6)


    def test_tuple_1(self, fix_session, fix_module, fix_class, fix_function):
        self.mytuple.count(5)
        print("mytuple.count(5)")
        print(self.mytuple)

    def test_tuple_2(self, fix_session, fix_module, fix_class, fix_function):
        self.mytuple.index(4)
        print("mytuple.index(4)")
        print(self.mytuple)