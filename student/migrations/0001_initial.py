# Generated by Django 2.0.7 on 2018-07-03 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tName', models.CharField(default='python', max_length=20)),
                ('tAge', models.IntegerField(default=0, max_length=5)),
                ('tImage', models.CharField(default='http://itaem.oss-cn-shenzhen.aliyuncs.com/20180509083509.jpg?Expires=4679469344&OSSAccessKeyId=LTAIATBJKsu6vu4R&Signature=PJkwOp9DVhtYu3Xkka0MnZVfnP0%3D', max_length=300)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
    ]
