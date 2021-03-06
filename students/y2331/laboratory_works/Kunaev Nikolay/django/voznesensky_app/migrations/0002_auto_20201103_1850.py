# Generated by Django 2.2.10 on 2020-11-03 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voznesensky_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='address_registration',
            field=models.CharField(max_length=256, verbose_name='Адрес регистрации'),
        ),
        migrations.AlterField(
            model_name='client',
            name='archived_reason',
            field=models.CharField(blank=True, max_length=60, verbose_name='Причина архивации'),
        ),
        migrations.AlterField(
            model_name='client',
            name='balance',
            field=models.IntegerField(default=0, verbose_name='Баланс'),
        ),
        migrations.AlterField(
            model_name='client',
            name='comment',
            field=models.CharField(blank=True, max_length=256, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='client',
            name='comment_addition',
            field=models.CharField(blank=True, max_length=256, verbose_name='Дополнительный комментарий'),
        ),
        migrations.AlterField(
            model_name='client',
            name='discovery_info',
            field=models.CharField(blank=True, max_length=256, verbose_name='Откуда узнал'),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.CharField(blank=True, max_length=60, verbose_name='Адрес электронной почты'),
        ),
        migrations.AlterField(
            model_name='client',
            name='is_archived',
            field=models.BooleanField(default=False, verbose_name='Статус архивации'),
        ),
        migrations.AlterField(
            model_name='client',
            name='permanent_discount',
            field=models.IntegerField(default=0, verbose_name='Постоянная скидка'),
        ),
    ]
