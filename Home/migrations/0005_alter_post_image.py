# Generated by Django 3.2.4 on 2021-09-03 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
