# Generated by Django 2.2.3 on 2019-07-22 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20190723_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
