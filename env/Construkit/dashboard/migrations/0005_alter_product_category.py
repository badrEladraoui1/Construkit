# Generated by Django 4.2.5 on 2023-09-16 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Building Materials', 'Building Materials'), ('Tools and Equipmen', 'Tools and Equipmen'), ('Heavy Machinery Parts', 'Heavy Machinery Parts')], max_length=100, null=True),
        ),
    ]
