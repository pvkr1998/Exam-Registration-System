# Generated by Django 2.1.2 on 2018-10-19 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20181018_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='password',
            field=models.CharField(max_length=500),
        ),
    ]
