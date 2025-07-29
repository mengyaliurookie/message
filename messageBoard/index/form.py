from django import forms
from .models import *

# 定义模型表单
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'