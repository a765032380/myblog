from django.db import models

# Create your models here.

from django.db import models


class Test(models.Model):
    title = models.CharField(max_length=20, verbose_name='标题')
    context = models.TextField(verbose_name='内容')

    class Meta:
        verbose_name_plural = '测试'


class User(models.Model):
    name = models.CharField(max_length=20, verbose_name='姓名')
    phone = models.CharField(max_length=11, verbose_name='手机号')
    age = models.CharField(max_length=3, verbose_name='年龄')
    signature = models.TextField(verbose_name='个性签名', default='')
    email = models.TextField(verbose_name='邮箱', default='')
    password = models.CharField(max_length=20, verbose_name='密码',default='')

    class Meta:
        verbose_name_plural = '用户'
