# Generated by Django 4.2.5 on 2023-10-12 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='qte',
            field=models.IntegerField(default=1, verbose_name='Quantity product'),
        ),
    ]
