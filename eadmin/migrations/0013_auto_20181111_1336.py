# Generated by Django 2.1.2 on 2018-11-11 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eadmin', '0012_remove_enrollments_hallticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollments',
            name='examid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eadmin.Exam'),
        ),
    ]
