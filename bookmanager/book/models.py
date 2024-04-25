from django.db import models

class BookInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name='书籍名称')
    pub_date = models.DateField(verbose_name='出版日期', null=True)
    readcount = models.IntegerField(default=0, verbose_name='阅读量')
    commentcount = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'bookinfo' # 指明数据库表名
        verbose_name = '图书' # 在admin站点显示的名称

    # 重写str方法，让admin显示书籍名称
    def __str__(self):
        return self.name
class PeopleInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female'),
    )
    name = models.CharField(max_length=20, verbose_name='姓名')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    description = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    # 外键约束
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name