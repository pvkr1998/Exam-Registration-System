# Generated by Django 2.1.2 on 2018-10-18 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicant',
            old_name='name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='applicant',
            name='id',
        ),
        migrations.AlterField(
            model_name='applicant',
            name='roll_no',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
    ]
