# Generated by Django 4.1 on 2023-12-15 08:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="instamojo_id",
            field=models.CharField(max_length=100),
        ),
    ]