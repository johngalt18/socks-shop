# Generated by Django 2.2.6 on 2019-10-28 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socks_shop', '0003_auto_20191028_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socks',
            name='color',
            field=models.CharField(max_length=30, null=True, verbose_name='Цвет'),
        ),
    ]
