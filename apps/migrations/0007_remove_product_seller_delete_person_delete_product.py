# Generated by Django 4.1.5 on 2023-02-02 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_product_cartype_product_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='seller',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
