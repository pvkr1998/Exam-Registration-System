# Generated by Django 2.1.2 on 2018-11-04 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eadmin', '0003_enrollments'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='examdate',
            field=models.DateField(auto_now=True),
        ),
    ]
