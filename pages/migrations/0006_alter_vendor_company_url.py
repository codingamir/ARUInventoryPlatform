# Generated by Django 5.0.2 on 2024-03-18 01:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0005_vendor_company_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vendor",
            name="company_url",
            field=models.URLField(default=""),
        ),
    ]
