# Generated by Django 4.2 on 2023-05-24 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_diary_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='diary_images/'),
        ),
    ]
