# Generated by Django 2.2.3 on 2019-07-22 23:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20190723_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 23, 1, 45, 30, 910124)),
        ),
    ]