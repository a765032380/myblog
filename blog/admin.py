from django.contrib import admin

# Register your models here.
from django.contrib import admin
from blog import models

# Register your models here.

admin.site.register(models.Test)
admin.site.register(models.User)