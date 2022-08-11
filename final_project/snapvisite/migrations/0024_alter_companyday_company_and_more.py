# Generated by Django 4.0.4 on 2022-05-19 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snapvisite', '0023_alter_companyday_company_alter_companyday_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyday',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snapvisite.company'),
        ),
        migrations.AlterUniqueTogether(
            name='companyday',
            unique_together={('company', 'date')},
        ),
    ]