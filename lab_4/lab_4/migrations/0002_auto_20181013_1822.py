# Generated by Django 2.1.2 on 2018-10-13 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab_4', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='subject',
        ),
        migrations.AddField(
            model_name='subject',
            name='subject',
            field=models.ManyToManyField(to='lab_4.Teacher'),
        ),
    ]