# Generated by Django 2.1.7 on 2019-04-18 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_auto_20190418_0330'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='has_form',
            field=models.BooleanField(default=False, verbose_name='آیا فرم ثبت سفارش دارد؟'),
        ),
    ]