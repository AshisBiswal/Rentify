# Generated by Django 5.0.4 on 2024-05-24 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0010_remove_property_image_propertyimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='price',
            field=models.DecimalField(decimal_places=2, default=500, max_digits=10),
        ),
    ]
