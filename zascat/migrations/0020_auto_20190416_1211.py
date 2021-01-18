# Generated by Django 2.0 on 2019-04-16 09:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('zascat', '0019_auto_20190404_1655'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prepimages',
            old_name='src',
            new_name='base_img',
        ),
        migrations.AlterField(
            model_name='prep',
            name='prep_date',
            field=models.DateField(default=datetime.datetime(2019, 4, 16, 9, 11, 46, 829432, tzinfo=utc), verbose_name='Дата добавления (изменения)'),
        ),
    ]
