# Generated by Django 2.1.7 on 2019-04-16 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='tutorial',
        ),
        migrations.DeleteModel(
            name='Paper',
        ),
    ]
