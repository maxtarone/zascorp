# Generated by Django 2.0 on 2019-04-04 13:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('zascat', '0018_auto_20190404_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prep',
            name='prep_date',
            field=models.DateField(default=datetime.datetime(2019, 4, 4, 13, 55, 53, 581140, tzinfo=utc), verbose_name='Дата добавления (изменения)'),
        ),
    ]
