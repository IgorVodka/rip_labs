# Generated by Django 2.1.2 on 2018-10-13 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab_4', '0006_remove_teacher_subjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='subjects',
            field=models.ManyToManyField(to='lab_4.Subject'),
        ),
    ]
