# Generated by Django 2.1.2 on 2018-10-20 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundraiser', '0005_auto_20181020_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='edudonationreq',
            name='note',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
