# Generated by Django 4.2 on 2023-04-16 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_variationtypes_variationvalues_variation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='variationtypes',
            options={'verbose_name': 'Variation Type', 'verbose_name_plural': 'Variation Types'},
        ),
        migrations.AlterModelOptions(
            name='variationvalues',
            options={'verbose_name': 'Variation Value', 'verbose_name_plural': 'Variation Values'},
        ),
        migrations.AddField(
            model_name='variation',
            name='variation_value',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.variationvalues'),
            preserve_default=False,
        ),
    ]