# Generated by Django 4.0.6 on 2022-09-13 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_news_most_important'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='photo',
            field=models.ImageField(default=1, upload_to='photos/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
