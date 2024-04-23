from django.db import models

class BookInfo(models.Model):
    name = models.CharField(max_length=10)

    # 重写str方法，让admin显示书籍名称
    def __str__(self):
        return self.name
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
