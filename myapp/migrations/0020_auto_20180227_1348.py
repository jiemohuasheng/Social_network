# Generated by Django 2.0.1 on 2018-02-27 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_auto_20180227_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_info',
            name='post_user',
            field=models.ForeignKey(default=None, on_delete=None, to='myapp.User_info'),
        ),
    ]
