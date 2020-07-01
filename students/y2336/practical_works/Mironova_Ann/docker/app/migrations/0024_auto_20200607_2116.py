# Generated by Django 3.0.6 on 2020-06-07 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20200607_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crew_member',
            name='id_flight',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.flight_information'),
        ),
        migrations.AlterField(
            model_name='flight_information',
            name='id_helicopter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.helicopter'),
        ),
    ]