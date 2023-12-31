# Generated by Django 4.1 on 2023-12-15 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "uid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                ("update_at", models.DateField(auto_now_add=True)),
                ("is_paid", models.BooleanField(default=False)),
                ("instamojo_id", models.CharField(max_length=150)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="carts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PizaaCategory",
            fields=[
                (
                    "uid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                ("update_at", models.DateField(auto_now_add=True)),
                ("category_name", models.CharField(max_length=100)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Pizza",
            fields=[
                (
                    "uid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                ("update_at", models.DateField(auto_now_add=True)),
                ("pizza_name", models.CharField(max_length=100)),
                ("price", models.IntegerField(default=100)),
                ("image", models.ImageField(upload_to="pizza")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pizzas",
                        to="app.pizaacategory",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CartItems",
            fields=[
                (
                    "uid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                ("update_at", models.DateField(auto_now_add=True)),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cart_items",
                        to="app.cart",
                    ),
                ),
                (
                    "pizaa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.pizza"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
