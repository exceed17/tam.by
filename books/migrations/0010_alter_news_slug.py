# Generated by Django 4.0.6 on 2022-09-30 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_news_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(max_length=70, null=True, unique=True),
        ),
    ]
