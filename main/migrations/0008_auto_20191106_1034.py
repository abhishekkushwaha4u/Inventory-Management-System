# Generated by Django 2.2.6 on 2019-11-06 05:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20191106_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='bill_id',
            field=models.CharField(default='atzuoxgibs', max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_id',
            field=models.CharField(default='pjzbpdxptp', max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='item_id',
            field=models.CharField(default='ooifqwinbl', max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='login',
            name='login_id',
            field=models.OneToOneField(default='fxsygyhnwd', on_delete=django.db.models.deletion.CASCADE, to='main.CustomUser'),
        ),
        migrations.AlterField(
            model_name='role',
            name='role_id',
            field=models.CharField(default='uvxdjidjiw', max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='salesandpurchases',
            name='transaction_date',
            field=models.DateField(default=datetime.date(2019, 11, 6)),
        ),
        migrations.AlterField(
            model_name='salesandpurchases',
            name='transaction_id',
            field=models.CharField(default='rqqaltnnqq', max_length=10, primary_key=True, serialize=False),
        ),
    ]
