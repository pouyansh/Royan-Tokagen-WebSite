# Generated by Django 2.1.7 on 2019-09-02 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20190728_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='file',
            field=models.FileField(blank=True, default=None, null=True, upload_to='', verbose_name='فایل'),
        ),
    ]