from django.db import models

# Create your models here.

from django.db import models


class Test(models.Model):
    title = models.CharField(max_length=20)
    context = models.TextField()

    def title_area(self):
        """返回父级区域名"""
        if self.title is None:
            return ''

        return self.title.title

    # 指定方法列显示的名称
    title_area.short_description = '标题'

    def context_area(self):
        """返回父级区域名"""
        if self.context is None:
            return ''

        return self.context.title

    # 指定方法列显示的名称
    context_area.short_description = '内容'


class User(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    age = models.CharField(max_length=3)

    def name_area(self):
        """返回父级区域名"""
        if self.name is None:
            return ''

        return self.name.title

    # 指定方法列显示的名称
    name_area.short_description = '姓名'

    def phone_area(self):
        """返回父级区域名"""
        if self.phone is None:
            return ''

        return self.phone.title

    # 指定方法列显示的名称
    phone_area.short_description = '手机号'

    def age_area(self):
        """返回父级区域名"""
        if self.age is None:
            return ''

        return self.age.title

    # 指定方法列显示的名称
    age_area.short_description = '年龄'
