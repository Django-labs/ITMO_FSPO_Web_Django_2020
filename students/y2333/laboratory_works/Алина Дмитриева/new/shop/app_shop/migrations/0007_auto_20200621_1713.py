# Generated by Django 3.0.7 on 2020-06-21 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0006_auto_20200621_1507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='selling',
            old_name='price_sell',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='selling',
            name='quantity',
        ),
    ]
