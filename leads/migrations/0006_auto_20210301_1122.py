# Generated by Django 3.1.4 on 2021-03-01 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0005_auto_20210301_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='leads.provider'),
        ),
    ]
