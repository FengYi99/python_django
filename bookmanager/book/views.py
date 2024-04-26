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

# 数据的增删改查
# 在pycharm的终端中的shell中执行
# python manage.py shell
# 1. 增加数据
# 方式一：save
from book.models import BookInfo, PeopleInfo
book = BookInfo(
    name='Python入门',
    pub_date = '2000-01-01'
)
book # 查询是否添加成功
book.save()
# 方式二：create，通过模型类.objects.create()保存。
PeopleInfo.objects.create(
    name='django',
    book = book
)
