
class TestSet():
    myset = {7, 8, 9}

    def test_set_1(self, fix_session, fix_module, fix_class, fix_function):
        self.myset.add(10)
        print("myset.add(10)")
        print(self.myset)