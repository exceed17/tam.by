# Generated by Django 4.0.6 on 2022-09-30 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_category_alter_accidents_time_create_news_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
