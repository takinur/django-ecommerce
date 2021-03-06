# Generated by Django 4.0.2 on 2022-02-27 11:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Department Name')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Employee Name')),
                ('email', models.EmailField(max_length=100, verbose_name='Employee Email')),
                ('address', models.CharField(max_length=500, verbose_name='Employee Address')),
                ('phone', models.CharField(max_length=20, verbose_name='Employee Phone')),
                ('doj', models.DateField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Date of Joining')),
                ('designation', models.CharField(choices=[('Developer', 'Developer'), ('Network Engineer', 'Network Engineer'), ('Server Admin', 'Server Admin'), ('Manager', 'Manager')], default='Developer', max_length=20, verbose_name='Designation')),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Employee Salary')),
                ('photo', models.FileField(blank=True, default='employee/blank.jpg', upload_to='employee', verbose_name='Employee Photo')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empApp.department')),
            ],
        ),
    ]
