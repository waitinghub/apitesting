
import pytest
from requests import request

from common.handle_excel import ExcelHandler
from common.handle_path import DATA_FILE
from common.handle_config import read_config
from common.handle_logging import log


class TestLogin():

    sheet_data = ExcelHandler(DATA_FILE, 'login')  # 获取login sheet
    test_data = sheet_data.read_data()  # 读取sheet下测试数据

    @pytest.mark.parametrize('test_data', test_data)
    def test_login(self, test_data):
        expected = eval(test_data['expected'])
        actual = request(method = test_data['method'],
                         url = read_config.get('env','host') + test_data['url'],
                         data = eval(test_data['data'])
                         ).json()  # 发送请求，获得响应数据

        row = test_data['case_id'] + 1 # 获取测试用例所在行
        test_result = ''  # 初始化测试结果
        try:
            assert expected['code'] == actual['code']
            assert expected['msg'] == actual['msg']
        except AssertionError as e:
            log.error('用例--{}--执行不通过'.format(test_data['title']))
            test_result = '不通过'
            log.debug('返回值预期结果是：{}'.format(expected))
            log.debug('返回值实际结果是：{}'.format(actual))
            log.critical(e)
            raise e
        else:
            log.info('用例--{}--执行通过'.format(test_data['title']))
            test_result = '通过'

        finally:
            self.sheet_data.write_data(row=row, column=8, value=str(actual))  # 将实际结果写入excel
            self.sheet_data.write_data(row=row, column=9, value=test_result)  # 将测试结果写入excel
