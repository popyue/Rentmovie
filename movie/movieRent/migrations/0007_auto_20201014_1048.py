# Generated by Django 3.1.1 on 2020-10-14 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieRent', '0006_auto_20201014_1046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movieproduct',
            options={'ordering': ('movie_name',)},
        ),
        migrations.AddField(
            model_name='movieproduct',
            name='slug',
            field=models.SlugField(default=None, max_length=200),
        ),
        migrations.AlterIndexTogether(
            name='movieproduct',
            index_together={('id', 'slug')},
        ),
    ]
