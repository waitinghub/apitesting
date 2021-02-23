
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目根目录
CASE_PATH = os.path.join(BASE_PATH, 'tests')  # 用例脚本所在目录
DATA_PATH = os.path.join(BASE_PATH, 'data')  # 用例数据目录
CONF_PATH = os.path.join(BASE_PATH, 'config')  # 配置文件路径
REPORT_PATH = os.path.join(BASE_PATH, 'report')  # 测试报告路径
LOG_PATH = os.path.join(BASE_PATH, 'logs')  # 日志目录路径

CONF_FILE = os.path.join(CONF_PATH,'config.ini')  # ini文件路径
DATA_FILE = os.path.join(DATA_PATH,'apicases.xlsx')  # data文件路径
