# Generated by Django 4.0.6 on 2022-09-13 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_remove_news_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='photo',
            field=models.ImageField(default=1, upload_to='photos/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
