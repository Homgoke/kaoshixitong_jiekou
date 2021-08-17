import requests
import unittest
from public.cookies import student_cookie

class exam_login(unittest.TestCase):

    def test_Ksxt_0003_00(self):
        '''正常登录-登录状态'''
        cookie=student_cookie()
        url='http://101.200.61.210:8087/api/student/user/message/unreadCount'
        header={'Cookie':cookie}
        result=requests.post(url,headers=header).json()

        result_code=result['code']
        targe_code=1
        result_message=result['message']
        targe_message='成功'

        self.assertEqual(result_code,targe_code)
        self.assertEqual(result_message,targe_message)



