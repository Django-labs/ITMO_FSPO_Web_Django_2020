# Generated by Django 3.1.2 on 2020-11-01 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('izdat_app', '0002_book_customer_edition_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='year_of_publication',
            field=models.IntegerField(),
        ),
    ]