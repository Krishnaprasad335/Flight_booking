# Generated by Django 5.1.1 on 2024-09-24 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_ticket',
            name='booking_status',
            field=models.CharField(default='available', max_length=20),
        ),
    ]
