import pytest


@pytest.fixture(scope='session')
def fix_session():
    print("-"*50)
    print("Start tests")

    def fin(request):
        print("End test")
        print("-" * 50)
        request.addfinalizer(fin)


@pytest.fixture(scope='module')
def fix_module(request):
    print("-" * 50)
    print(f"Start test {request.scope}")

    def fin(request):
        print(f"End test {request.scope}")
        print("-" * 50)
        request.addfinalizer(fin)

@pytest.fixture(scope='class')
def fix_class(request):
    print("-" * 50)
    print(f"Start test {request.scope}")

    def fin(request):
        print(f"Filalize test {request.scope}")
        print("-" * 50)
        request.addfinalizer(fin)


@pytest.fixture()
def fix_function():
    print("-"*50)
    print("Start function test")

    yield

    print("-" * 50)
    print("Finalize function test")