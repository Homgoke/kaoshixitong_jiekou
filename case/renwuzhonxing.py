import requests
import unittest
from public.cookies import student_cookie
class exam_renwuzhonxing(unittest.TestCase):

    def test_Ksxt_0004(self):
        exam_url='http://101.200.61.210:8087/api/student/dashboard/task'
        exam_header={"Cookie":student_cookie()}
        exam_result=requests.post(exam_url,headers=exam_header).json()
        result_code=exam_result['code']
        targe_code=1
        result_message=exam_result['message']
        targe_message='成功'

        self.assertEqual(result_code,targe_code)
        self.assertEqual(result_message,targe_message)