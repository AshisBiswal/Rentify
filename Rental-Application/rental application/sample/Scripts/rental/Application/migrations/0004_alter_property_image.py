# Generated by Django 5.0.4 on 2024-05-20 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0003_property_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]