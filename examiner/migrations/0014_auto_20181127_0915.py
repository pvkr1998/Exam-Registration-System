# Generated by Django 2.1.2 on 2018-11-27 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examiner', '0013_auto_20181126_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='examid',
            field=models.CharField(max_length=15),
        ),
    ]
