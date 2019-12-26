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
    password = models.CharField(max_length=20, verbose_name='密码', default='')

    class Meta:
        verbose_name_plural = '用户'


class Video(models.Model):
    video_title = models.CharField(max_length=100, verbose_name='标题')
    video_context = models.CharField(max_length=100, verbose_name='内容')
    video_image = models.CharField(max_length=100, verbose_name='封面')
    video_file = models.FileField(upload_to='video/', default='', verbose_name='视频文件')
    video_praise_number = models.IntegerField(verbose_name='点赞数量')
    video_comments_number = models.IntegerField(verbose_name='评论数量')
    video_share_number = models.IntegerField(verbose_name='分享数量')

    class Meta:
        verbose_name_plural = '视频'


class News(models.Model):
    title = models.CharField(max_length=100,verbose_name='标题')
    date = models.CharField(max_length=200,verbose_name='日期')
    url = models.CharField(max_length=100,verbose_name='新闻地址')
    thumbnail_pic_s = models.ImageField(max_length=100,verbose_name='图片地址1')
    thumbnail_pic_s02 = models.ImageField(max_length=100,verbose_name='图片地址2')
    thumbnail_pic_s03 = models.ImageField(max_length=100,verbose_name='图片地址3')
    category = models.CharField(max_length=100,verbose_name='新闻类型')
    uniquekey = models.CharField(max_length=100,verbose_name='')
    author_name = models.CharField(max_length=100,verbose_name='')

    class Meta:
        verbose_name_plural = '新闻'


class Joke(models.Model):
    content = models.CharField(max_length=10000,verbose_name='内容')
    hashId = models.CharField(max_length=200,verbose_name='hashId')
    unixTime = models.CharField(max_length=100,verbose_name='')
    updateTime = models.CharField(max_length=100,verbose_name='更新时间')
    url = models.CharField(max_length=1000,verbose_name='图片地址')

    class Meta:
        verbose_name_plural = '聚合笑话'