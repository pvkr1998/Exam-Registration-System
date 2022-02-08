# Generated by Django 2.1.2 on 2018-10-30 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0008_applicant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('courseid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('coursename', models.CharField(max_length=40)),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Examiner')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('paymentref', models.CharField(max_length=50)),
                ('courseid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eadmin.Course')),
                ('roll_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Applicant')),
            ],
        ),
    ]