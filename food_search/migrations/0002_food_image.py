# Generated by Django 4.2 on 2023-05-26 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='food_images'),
        ),
    ]
