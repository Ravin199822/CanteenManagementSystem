# Generated by Django 2.1.15 on 2020-10-11 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Canteen', '0014_ordered_item'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Orders',
        ),
    ]