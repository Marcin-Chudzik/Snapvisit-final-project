# Generated by Django 4.0.4 on 2022-05-08 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snapvisite', '0005_alter_timeslot_company_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='snapvisite.address'),
        ),
    ]
