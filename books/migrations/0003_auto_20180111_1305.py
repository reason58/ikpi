# Generated by Django 2.0.1 on 2018-01-11 21:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20180108_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_length_pages',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='book_length_words',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='book_pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 11, 21, 5, 45, 891413, tzinfo=utc)),
        ),
    ]
