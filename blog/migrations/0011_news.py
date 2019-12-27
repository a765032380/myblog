# Generated by Django 2.2.7 on 2019-12-26 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20191226_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('date', models.CharField(max_length=200, verbose_name='日期')),
                ('url', models.CharField(max_length=100, verbose_name='新闻地址')),
                ('thumbnail_pic_s', models.ImageField(upload_to='', verbose_name='图片地址1')),
                ('thumbnail_pic_s02', models.ImageField(upload_to='', verbose_name='图片地址2')),
                ('thumbnail_pic_s03', models.ImageField(upload_to='', verbose_name='图片地址3')),
                ('category', models.CharField(max_length=100, verbose_name='新闻类型')),
                ('uniquekey', models.CharField(max_length=100, verbose_name='')),
                ('author_name', models.CharField(max_length=100, verbose_name='')),
            ],
            options={
                'verbose_name_plural': '新闻',
            },
        ),
    ]