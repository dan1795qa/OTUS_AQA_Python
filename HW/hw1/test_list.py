import pytest

mylist = [1, 2, 3]
mytuple = (4, 5, 6)
mydict = {1: 'one', 2: 'two', 3: 'three'}
myset = {7, 8, 9}

@pytest.fixture()
def setup():
    print("-"*50)
    print("Start tests")

    def fin(request):
        print("End test")
        print("-" * 50)
        request.addfinalizer(fin)



class Testlist():

    global mylist

    def test_list_1(self):
        print(mylist.append(0))

    def test_list_2(self):
        print(mylist.count(1))

    def test_list_3(self):
        print(mylist.pop(0))

    def test_list_4(self):
        print(mylist.insert(0, 'Hi'))

    def test_list_5(self):
        print(mylist.extend([11, 22, 33]))

    def test_list_6(self):
        print(mylist.reverse())

    def test_list_7(self):
        print(mylist.index('Hi'))

    def test_list_8(self):
        print(mylist.remove('Hi'))


