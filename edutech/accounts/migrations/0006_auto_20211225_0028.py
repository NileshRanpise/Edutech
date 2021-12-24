# Generated by Django 3.2.4 on 2021-12-24 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_stuimage_teachimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='stuimage',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.student'),
        ),
        migrations.AddField(
            model_name='teachimage',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.teacher'),
        ),
    ]
