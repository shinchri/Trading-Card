# Generated by Django 4.1.1 on 2022-09-29 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_cart_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, max_length=5),
        ),
    ]
