from django.shortcuts import render,redirect
from .models import Message
from .form import MessageForm

# Create your views here.

# 自定义404和500错误页面

def page_not_found(request,exception):
    return render(request,'404.html',status=404)
def page_error(request):
    return render(request,'500.html',status=500)

def index(request):
    message=Message.objects.all().order_by('-id')
    if request.method=='POST':
        form=MessageForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'index.html',locals())