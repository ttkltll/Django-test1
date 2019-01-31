# from django.shortcuts import render

# Create your views here.
#from django.shortcuts import render
from django.http import HttpResponse
#from booktest.models import BookInfo # 导入图书模型类
#from django.template import loader,RequestContext


def index(request):
    # 进行处理，和M和T进行交互。。。
     return HttpResponse('老铁，没毛病')
    # return my_render(request, 'booktest/index.html')
    # return render(request, 'booktest/index.html', {'content':'hello world', 'list':list(range(1,10))})


# http://127.0.0.1:8000/index2
def index2(request):
    return HttpResponse('hello python')


