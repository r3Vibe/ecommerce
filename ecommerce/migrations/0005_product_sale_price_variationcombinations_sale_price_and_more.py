# Generated by Django 4.2 on 2023-04-21 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_variationcombinations_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='variationcombinations',
            name='sale_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='variationcombinations',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
