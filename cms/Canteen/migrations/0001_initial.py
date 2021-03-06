# Generated by Django 2.1.15 on 2020-10-09 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iid', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=10)),
                ('desc', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'items',
            },
        ),
    ]
