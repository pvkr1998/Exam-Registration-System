# Generated by Django 2.1.2 on 2018-11-22 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('examiner', '0010_auto_20181122_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='examid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eadmin.Exam'),
        ),
    ]
