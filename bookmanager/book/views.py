from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest
from django.http import HttpResponse

def index(request):
    # return HttpResponse('ok')

    # 模拟数据查询
    context = {
        'name': '书籍列表'
    }
    return render(request, 'book/index.html', context=context)