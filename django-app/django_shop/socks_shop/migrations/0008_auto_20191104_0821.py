# Generated by Django 2.2.6 on 2019-11-04 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socks_shop', '0007_auto_20191103_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socks',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Описание'),
        ),
    ]
