# Generated by Django 2.1.7 on 2019-12-30 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0015_auto_20190728_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='field_names',
            field=models.CharField(blank=True, default=None, max_length=300, null=True, verbose_name='نام فیلدها'),
        ),
    ]