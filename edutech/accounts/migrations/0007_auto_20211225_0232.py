# Generated by Django 3.2.4 on 2021-12-24 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20211225_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teachimage',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='teachimage',
            name='user',
        ),
        migrations.DeleteModel(
            name='StuImage',
        ),
        migrations.DeleteModel(
            name='TeachImage',
        ),
    ]