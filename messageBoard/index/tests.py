from django.test import TestCase
from django.test import Client
from .models import Message
# Create your tests here.

class MessageTest(TestCase):
    # 添加数据
    def setUp(self):
        Message.objects.create(name='张三',content='测试数据')
        Message.objects.create(name='李四',content='测试数据1')

    # 编写测试用例
    def test_Message(self):
        # 编写用例
        info=Message.objects.get(name='张三')
        # 判断测试用例的执行结果
        self.assertIsNotNone(info.timestamp)

    # 编写测试用例
    def test_post(self):
        # 编写用例
        c=Client()
        data={'name':'王五','content':'测试数据2'}
        response=c.post('/',data=data)
        status_code=response.status_code
        info=Message.objects.get(name='王五')
        # 判断测试用例的执行结果
        self.assertEqual(status_code,302)
        self.assertIsNotNone(info.content,'测试数据2')