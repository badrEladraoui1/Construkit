# Generated by Django 4.2.5 on 2023-09-07 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_product_category_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Order'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'product'},
        ),
    ]
