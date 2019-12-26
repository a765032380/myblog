# Generated by Django 2.2.7 on 2019-12-11 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_comments_number',
            field=models.IntegerField(verbose_name='评论数量'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_context',
            field=models.CharField(max_length=100, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_image',
            field=models.CharField(max_length=100, verbose_name='封面'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_praise_number',
            field=models.IntegerField(verbose_name='点赞数量'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_share_number',
            field=models.IntegerField(verbose_name='分享数量'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_title',
            field=models.CharField(max_length=100, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_url',
            field=models.CharField(max_length=100, verbose_name='地址'),
        ),
    ]
