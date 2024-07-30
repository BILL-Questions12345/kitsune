# Generated by Django 4.2.14 on 2024-07-30 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0015_auto_20240722_0449"),
    ]

    operations = [
        migrations.AddField(
            model_name="topic",
            name="in_nav",
            field=models.BooleanField(
                default=False, help_text="Whether this topic is shown in navigation menus."
            ),
        ),
        migrations.AlterField(
            model_name="topic",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="topics",
                to="products.product",
            ),
        ),
    ]
