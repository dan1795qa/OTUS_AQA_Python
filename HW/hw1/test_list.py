import pytest


class Testlist():

    # def __init__(self, mylist):
    #     self.mylist = mylist
    mylist = [1, 2, 3]

    def test_list_1(self, fix_session, fix_module, fix_class, fix_function):
        self.mylist.append(0)
        print("mylist.append(0)")
        print(self.mylist)

    def test_list_2(self, fix_session, fix_module, fix_class, fix_function):
        self.mylist.count(1)
        print("mylist.count(1)")
        print(self.mylist.count(1))
        print(self.mylist)

    def test_list_3(self, fix_session, fix_module, fix_class, fix_function):
        self.mylist.pop(0)
        print("mylist.pop(0)")
        print(self.mylist)

    def test_list_4(self, fix_session, fix_module, fix_class, fix_function):
        self.mylist.insert(0, 44)
        print("mylist.insert(0, 44)")
        print(self.mylist)

    def test_list_5(self, fix_session, fix_module, fix_class, fix_function):
        self.mylist.extend([11, 22, 33])
        print("mylist.extend([11, 22, 33])")
        print(self.mylist)

    def test_list_6(self, fix_session, fix_module, fix_class, fix_function):
        self.mylist.reverse()
        print("mylist.reverse()")
        print(self.mylist)

    def test_list_7(self, fix_session, fix_module, fix_class, fix_function):
        self.mylist.index(11)
        print("mylist.index(11)")
        print(self.mylist.index(11))
        print(self.mylist)

    def test_list_8(self, fix_session, fix_module, fix_class, fix_function):
        self.mylist.remove(44)
        print("mylist.remove(44)")
        print(self.mylist)


