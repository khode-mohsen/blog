# Generated by Django 2.1.3 on 2018-11-12 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181112_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]