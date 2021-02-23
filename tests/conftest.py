import pytest
from jsonpath import jsonpath
from requests import request
from common.handle_config import read_config


@pytest.fixture()
def token():
    '''前置条件，登录获取token'''
    response = request(method = 'post',
                       url = read_config.get('env', 'login_host'),
                       data=eval(read_config.get('env', 'login_info'))
                       ).json()
    token = 'Bearer' + ' ' + jsonpath(response, '$..access_token')[0]
    return token
