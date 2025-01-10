# Generated by Django 5.1.4 on 2025-01-10 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersettings',
            name='alert_light_level',
            field=models.FloatField(default=100.0),
        ),
        migrations.AlterField(
            model_name='usersettings',
            name='humidity_threshold',
            field=models.FloatField(default=100.0),
        ),
        migrations.AlterField(
            model_name='usersettings',
            name='soil_moisture_threshold',
            field=models.FloatField(default=100.0),
        ),
        migrations.AlterField(
            model_name='usersettings',
            name='temp_threshold',
            field=models.FloatField(default=100.0),
        ),
    ]