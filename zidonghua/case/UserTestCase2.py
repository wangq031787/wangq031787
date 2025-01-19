# -*-coding: UTF-8 -*-
import unittest
from case.UserTestCase import UserTestCase
class UserTestCase2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('初始化')

    @classmethod
    def tearDownClass(cls):
        print('资源清理')


    def test_1(self):
        print('test1')
        self.assertTrue(1, 2)

    def test_2(self):
        print('test2')
        self.assertEqual(1,1)
    # @unittest.skip('跳过')
    def test_3(self):
        print('test3')
        self.assertEqual(1,1)



if __name__ == '__main__':
    # unittest.main()

    # 构造一个测试套件
    suite = unittest.TestSuite()
    # 类名（方法名）
    suite.addTest(UserTestCase2('test_1'))

    suite.addTest(UserTestCase1('test_2'))
    # 运行套件
    unittest.TextTestRunner(verbosity=2).run(suite)



















