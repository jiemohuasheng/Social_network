# Generated by Django 2.0.1 on 2018-02-27 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_auto_20180227_0848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.AlterField(
            model_name='post',
            name='post_title',
            field=models.CharField(default=None, max_length=50, primary_key=True, serialize=False),
        ),
    ]