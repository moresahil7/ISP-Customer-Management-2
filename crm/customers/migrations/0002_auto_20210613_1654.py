# Generated by Django 3.1.4 on 2021-06-13 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_photo',
            field=models.ImageField(blank=True, default='', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='kYC_document',
            field=models.ImageField(blank=True, default='', upload_to='images'),
        ),
    ]