# Generated by Django 2.1.7 on 2019-05-02 05:46

import apps.order_service.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_service', '0008_auto_20190502_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderservice',
            name='file',
            field=models.FileField(blank=True, default=None, upload_to=apps.order_service.models.user_directory_path, verbose_name='فایل'),
        ),
    ]
