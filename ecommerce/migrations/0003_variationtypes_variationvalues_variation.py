# Generated by Django 4.2 on 2023-04-15 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_alter_category_name_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='VariationTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='VariationValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('VariationType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.variationtypes')),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.product')),
                ('variation_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.variationtypes')),
            ],
        ),
    ]
