# Generated by Django 2.0.1 on 2018-03-20 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20180319_0857'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_content', models.CharField(default=None, max_length=500)),
                ('msg_publish_date', models.DateField(blank=True, default=None, null=True)),
                ('msg_publish_time', models.TimeField(blank=True, default=None, null=True)),
                ('msg_reciever', models.ForeignKey(on_delete=None, related_name='msg_reciever', to='myapp.User_info')),
                ('msg_sender', models.ForeignKey(on_delete=None, related_name='msg_sender', to='myapp.User_info')),
            ],
        ),
    ]
