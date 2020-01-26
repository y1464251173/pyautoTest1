import unittest
from BSTestRunner import BSTestRunner
import time

# 定义测试用例的目录为当前目录中的 test_case/目录
test_dir = "./test_case"

suit = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == "__main__":
    # 生成 HTML 格式的测试报告
    # fp = open("./test_reports/result.html", "wb")

    # 测试报告存放路径
    report_dir = './test_reports'

    # 定义报告的文件命名方式
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name = report_dir + '/' + now + "result.html"

    # 运行用例并生成报告
    fp = open(report_name, 'wb')
    runner = BSTestRunner(
        stream=fp,
        title="百度搜索测试报告",
        description="运行环境：Windows 10，Chrome 浏览器"
    )
    runner.run(suit)
    fp.close()
