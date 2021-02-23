import random

import pytest
from requests import request
from common.handle_logging import log
from common.handle_config import read_config
from common.handle_excel import ExcelHandler
from common.handle_path import DATA_FILE
from common.handle_db import MySQLHandler


class TestOrgmanage():

    sheet_data = ExcelHandler(DATA_FILE, 'add_organization')
    test_data = sheet_data.read_data()
    db = MySQLHandler()

    @pytest.mark.parametrize('test_data', test_data)
    def test_login(self, token, test_data):
        expected = eval(test_data['expected'])

        headers = {}
        headers['Authorization'] = token
        actual = request(method = test_data['method'],
                         url = read_config.get('env','host') + test_data['url'],
                         headers = headers,
                         data = eval(test_data['data'].replace('测试name', 'api测试' + str(random.randint(1,99999999))))
                         ).json()  # 发送请求，获得响应数据

        db_check = self.db.find_count('select OrgName from organizationtable where ID = 10')  # 数据库查询添加数据

        row = test_data['case_id'] + 1
        test_result = ''
        try:
            assert db_check == 1
            assert expected['code'] == actual['code']
            assert expected['msg'] == actual['msg']
        except AssertionError as e:
            log.error('用例--{}--执行不通过'.format(test_data['title']))
            test_result = '不通过'
            log.debug('数据库查询预期结果是: 1')
            log.debug('数据库查询实际结果是: {}'.format(db_check))
            log.debug('返回值预期结果是: {}'.format(expected))
            log.debug('返回值实际结果是: {}'.format(actual))
            log.critical(e)
            raise e
        else:
            log.info('用例--{}--执行通过'.format(test_data['title']))
            test_result = '通过'

        finally:
            self.sheet_data.write_data(row=row, column=8, value=str(actual))
            self.sheet_data.write_data(row=row, column=9, value=test_result)