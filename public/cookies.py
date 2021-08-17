import requests
import requests.utils



def csv_cookie(file_name):
    exam_url = 'http://101.200.61.210:8087/api/user/login'
    exam_header = {"Content-Type": "application/json"}

    with open(file_name,'r',encoding='utf-8') as csv_file:
        for line in csv_file:
            line=line.strip()
            line_list=line.split(',')
            username=line_list[0]
            password=line_list[1]
            exam_body = {"userName": username, "password": password , "remember": False}
            result=requests.post(exam_url,json=exam_body,headers=exam_header,timeout=1)
            cookies=requests.utils.dict_from_cookiejar(result.cookies)["SESSION"]
            print(cookies)
            with open('../ksxt_cookies.csv','a',encoding='utf-8') as ksxt_cookie:
                ksxt_cookie.write(cookies+'\n')

def student_cookie():
    exam_url = 'http://101.200.61.210:8087/api/user/login'
    exam_header = {"Content-Type": "application/json"}
    exam_body={"userName": 'student', "password": '123456' , "remember": False}
    exam_result=requests.post(exam_url,json=exam_body,headers=exam_header)
    student_cookie=requests.utils.dict_from_cookiejar(exam_result.cookies)["SESSION"]
    cookies='SESSION='+student_cookie
    return cookies





if __name__=='__main__':
     csv_cookie('../ksxt.csv')
     student_cookie()
















