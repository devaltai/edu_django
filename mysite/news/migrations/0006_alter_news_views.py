# Generated by Django 4.0.1 on 2022-01-26 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_news_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='views',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
