import requests
import unittest
class exam_login(unittest.TestCase):
    def test_Ksxt_0002_01(self):
        '''正常登录'''
        self.exam_url = 'http://101.200.61.210:8087/api/user/login'
        self.exam_header = {"Content-Type": "application/json"}
        self.exam_body = {"userName": "xiaoxiaoxiao啊 @123", "password": "123456", "remember": False}
        self.result = requests.post(self.exam_url, json=self.exam_body, headers=self.exam_header)
        result_message = self.result.json()['message']
        target_message = '成功'
        result_name = self.result.json()['response']['userName']
        target_name = self.exam_body['userName']

        self.assertEqual(result_message, target_message)
        self.assertEqual(result_name, target_name)

    def test_Ksxt_002_02(self):
        '''不输入账号登录'''
        self.exam_url = 'http://101.200.61.210:8087/api/user/login'
        self.exam_header = {"Content-Type": "application/json"}
        self.exam_body = {"userName": "", "password": "123456", "remember": False}
        self.result = requests.post(self.exam_url, json=self.exam_body, headers=self.exam_header)
        print(self.result.json())
        result_message = self.result.json()['message']
        target_message = '用户名或密码错误'
        result_code = self.result.json()['code']
        target_name = 402

        self.assertEqual(result_message, target_message)
        self.assertEqual(result_code, target_name)

    def test_Ksxt_002_03(self):
        '''输入不存在的账户登录'''
        self.exam_url = 'http://101.200.61.210:8087/api/user/login'
        self.exam_header = {"Content-Type": "application/json"}
        self.exam_body = {"userName": "xiaoxiaoxiao1123", "password": "123456", "remember": False}
        self.result = requests.post(self.exam_url, json=self.exam_body, headers=self.exam_header)
        print(self.result.json())
        result_message = self.result.json()['message']
        target_message = '用户名或密码错误'
        result_code = self.result.json()['code']
        target_name = 402

        self.assertEqual(result_message, target_message)
        self.assertEqual(result_code, target_name)

    def test_Ksxt_002_04(self):
        '''输入一个字符长度的账户'''
        self.exam_url = 'http://101.200.61.210:8087/api/user/login'
        self.exam_header = {"Content-Type": "application/json"}
        self.exam_body = {"userName": "x", "password": "123456", "remember": False}
        self.result = requests.post(self.exam_url, json=self.exam_body, headers=self.exam_header)
        result_message = self.result.json()['message']
        target_message = '成功'
        result_name = self.result.json()['response']['userName']
        target_name = self.exam_body['userName']

        self.assertEqual(result_message, target_message)
        self.assertEqual(result_name, target_name)














