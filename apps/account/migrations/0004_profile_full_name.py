# Generated by Django 2.2.6 on 2019-11-25 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20191122_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='full_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
