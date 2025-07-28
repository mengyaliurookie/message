from django.db import models

# Create your models here.

class Message(models.Model):
    id=models.AutoField('序号',primary_key=True)
    name=models.CharField('名称',max_length=50)
    content=models.TextField('信息内容')
    timestamp=models.DateTimeField('反馈时间',auto_now=True)