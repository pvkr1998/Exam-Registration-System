# Generated by Django 2.1.2 on 2018-11-05 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eadmin', '0004_exam_examdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='id',
        ),
        migrations.AlterField(
            model_name='enrollments',
            name='hallticket',
            field=models.FileField(null=True, upload_to='documents/hallticket/'),
        ),
        migrations.AlterField(
            model_name='enrollments',
            name='paymentref',
            field=models.FileField(upload_to='documents/payment/'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='examdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='exam',
            name='examid',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
    ]
