import requests
import unittest

class exam_zhuce(unittest.TestCase):
    def test_Ksxt_0001(self):
        '''正常注册'''
        exam_url='http://101.200.61.210:8087/api/student/user/register'
        exam_header={'Content-Type':'application/json'}
        exam_body={"userName": "xiaoxiaoxiao啊 @1234", "password": "123456", "userLevel": 1}
        exam_result=requests.post(exam_url,headers=exam_header,json=exam_body)
        resule_message=exam_result.json()["message"]
        targe_message='成功'

        self.assertEqual(resule_message,targe_message)

    def test_Ksxt_0002(self):
        '''重复注册'''
        exam_url = 'http://101.200.61.210:8087/api/student/user/register'
        exam_header = {'Content-Type': 'application/json'}
        exam_body = {"userName": "xiaoxiaoxiao", "password": "123456", "userLevel": 1}
        exam_result = requests.post(exam_url, headers=exam_header, json=exam_body)
        resule_message = exam_result.json()["message"]
        targe_message = '用户已存在'

        self.assertEqual(resule_message, targe_message)

    def test_Ksxt_0003(self):
        '''不输入用户名注册'''
        exam_url = 'http://101.200.61.210:8087/api/student/user/register'
        exam_header = {'Content-Type': 'application/json'}
        exam_body = {"userName": "", "password": "123456", "userLevel": 1}
        exam_result = requests.post(exam_url, headers=exam_header, json=exam_body)
        resule_message = exam_result.json()["message"]
        targe_message = '【userName : must not be blank】'

        self.assertEqual(resule_message, targe_message)

    def test_Ksxt_0004(self):
        '''输入用户名超长'''
        exam_url = 'http://101.200.61.210:8087/api/student/user/register'
        exam_header = {'Content-Type': 'application/json'}
        exam_body = {"userName": "abc123123123123123123123123123123123123123123"
                                 "1231231231231231231231231231231231231231231231"
                                 "2312312312312312312312312312312312312312312312"
                                 "3123123123123123123123123123123123123123123123"
                                 "1231231231231231231231231231231231231231231231"
                                 "2312312312312312312312312312312312312312312312"
                                 "3123123123123123123123123123123123123123123",
                     "password": "123456", "userLevel": 1}
        exam_result = requests.post(exam_url, headers=exam_header, json=exam_body)
        resule_message = exam_result.json()["message"]
        targe_message = '用户名不能超过限定长度'

        self.assertIn(resule_message, targe_message)




