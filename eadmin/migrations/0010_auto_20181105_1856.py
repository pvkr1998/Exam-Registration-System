# Generated by Django 2.1.2 on 2018-11-05 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_applicant'),
        ('eadmin', '0009_auto_20181105_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollments',
            name='paymentref',
            field=models.FileField(upload_to='documents/payment/'),
        ),
        migrations.AlterUniqueTogether(
            name='enrollments',
            unique_together={('roll_no', 'examid')},
        ),
    ]
