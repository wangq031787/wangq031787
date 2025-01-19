import os
import unittest

def load_all_case():
    '''加载指定路径全部测试用例'''
    print(os.getcwd())
    case_path=os.path.join(os.getcwd(),'case')
    print(case_path)
    discouver=unittest.defaultTestLoader.discover(case_path,pattern='*.py',top_level_dir=None)
    print(discouver)
    return discouver
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(load_all_case())
