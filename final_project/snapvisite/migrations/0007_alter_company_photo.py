# Generated by Django 4.0.4 on 2022-05-08 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snapvisite', '0006_alter_company_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='company_photo/<django.db.models.fields.CharField>'),
        ),
    ]