# Generated by Django 2.2.6 on 2019-11-06 10:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20191106_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='bill_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='billing',
            name='bill_id',
            field=models.CharField(default='lefbzauzem', max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_id',
            field=models.CharField(default='lqknbxsmzw', max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='item_id',
            field=models.CharField(default='rydkgvetlz', max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='login',
            name='login_id',
            field=models.OneToOneField(default='otsjessslo', on_delete=django.db.models.deletion.CASCADE, to='main.CustomUser'),
        ),
        migrations.AlterField(
            model_name='role',
            name='role_id',
            field=models.CharField(default='tjvwvxrkcl', max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='salesandpurchases',
            name='transaction_id',
            field=models.CharField(default='lzckwmpntl', max_length=10, primary_key=True, serialize=False),
        ),
    ]
