import pytest


# from pmxbot.conftest
@pytest.fixture(scope='session', autouse=True)
def init_config():
	__import__('pmxbot').config = {}


# from pmxbot.tests.conftest
@pytest.fixture(params=['mongodb', 'sqlite'])
def db_uri(request):
	if request.param == 'mongodb':
		return request.getfuncargvalue('mongodb_uri')
	return 'sqlite:pmxbot.sqlite'
