# Generated by Django 3.0.3 on 2020-04-19 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0006_auto_20200419_0436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='time_frame',
            field=models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], max_length=20),
        ),
    ]
