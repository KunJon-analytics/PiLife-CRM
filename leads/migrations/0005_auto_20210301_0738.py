# Generated by Django 3.1.4 on 2021-03-01 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0004_auto_20210224_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_organiser',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_provider',
            field=models.BooleanField(default=False),
        ),
    ]
