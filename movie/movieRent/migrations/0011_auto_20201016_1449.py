# Generated by Django 3.1.1 on 2020-10-16 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieRent', '0010_auto_20201014_1658'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='CATEGORY',
        ),
        migrations.AlterModelTable(
            name='movie',
            table='MOVIE',
        ),
    ]
