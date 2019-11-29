from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from blog import models


# Register your models here.


class TestAdmin(ModelAdmin):
    # 显示顶部的选项
    actions_on_top = True
    # 显示底部的选项
    actions_on_bottom = True
    # 列表页面要显示属性
    list_display = ["title", "context"]
    # 过滤的属性
    # list_filter = ["age", "birthday"]
    # 分页的每页数量
    list_per_page = 10
    # 增加和修改的属性
    # fields = ["name", "nickname"]
    # 注意，fields 和 fieldsets 不能同时出现
    # fieldsets = [
    #     ("必填", {"fields": ["age", "birthday"]}),
    #     ("选写", {"fields": ["name", "nickname"]})
    # ]


class UserAdmin(ModelAdmin):
    # 显示顶部的选项
    actions_on_top = True
    # 显示底部的选项
    actions_on_bottom = True
    # 列表页面要显示属性
    list_display = ["name", "phone", 'age', 'signature', 'email']
    # 过滤的属性
    # list_filter = ["age", "birthday"]
    # 分页的每页数量
    list_per_page = 10
    # 增加和修改的属性
    # fields = ["name", "nickname"]
    # 注意，fields 和 fieldsets 不能同时出现
    # fieldsets = [
    #     ("必填", {"fields": ["age", "birthday"]}),
    #     ("选写", {"fields": ["name", "nickname"]})
    # ]


admin.site.site_header = 'MyBlog'
admin.site.site_title = 'GLL'
admin.site.register(models.Test, TestAdmin)
admin.site.register(models.User, UserAdmin)
