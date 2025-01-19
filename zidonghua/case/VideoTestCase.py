import unittest
from case.UserTestCase import UserTestCase


class VideoTestCase(unittest.TestCase):
    def setUp(self):
        print('set up')

    def tearDown(self):
        print('tear down')

    def test_1(self):
        print('test1')
        self.assertTrue(1, 2)

    def test_2(self):
        print('test2')
        self.assertEqual(1, 1)


if __name__ == '__main__':
    # 构造测试套件
    suite = unittest.TestSuite()

    # 实例化loader
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(UserTestCase))

    runner = unittest.TextTestRunner(verbosity=2).run(suite)
