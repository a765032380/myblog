# Generated by Django 2.2.7 on 2019-12-12 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20191211_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video_file',
            field=models.FileField(default='', upload_to='video/', verbose_name='视频文件'),
        ),
    ]
