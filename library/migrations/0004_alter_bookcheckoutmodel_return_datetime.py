# Generated by Django 4.1.2 on 2022-10-18 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_bookcheckoutmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcheckoutmodel',
            name='return_datetime',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
