import pytest


@pytest.fixture(scope='session')
def fix_session(request):
    print("\nStart session tests")
    def fin():
        print(f"End session test {request.scope}")
        print("-" * 50)

    request.addfinalizer(fin)


@pytest.fixture(scope='module')
def fix_module(request):
    print(f"Start test {request.scope}")

    def fin():
        print(f"End test {request.scope}")
        print("-" * 50)

    request.addfinalizer(fin)

@pytest.fixture(scope='class')
def fix_class(request):
    print(f"Start test {request.scope}")

    def fin():
        print(f"Finalize test {request.scope}")
        print("-" * 50)

    request.addfinalizer(fin)

# @pytest.fixture()
# def fix_function(request):
#     print(f"Start test")
#
#     def fin():
#         print(f"Finalize test")
#         print("-" * 50)
#
#     request.addfinalizer(fin)


@pytest.fixture()
def fix_function():
    print('\n')
    print("-" * 50)
    print("Start function test")

    yield

    print("Finalize function test")
    print("-" * 50)

