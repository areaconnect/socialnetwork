# Generated by Django 2.2.6 on 2019-12-09 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='status',
            field=models.CharField(max_length=35),
        ),
    ]
