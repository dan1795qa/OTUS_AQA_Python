
class TestDict():


    mydict = {1: 'one', 2: 'two', 3: 'three'}

    def test_dict_1(self, fix_session, fix_module, fix_class, fix_function):
        self.mydict.get(1)
        print("mydict.get(1)")
        print(self.mydict)