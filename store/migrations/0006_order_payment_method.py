# Generated by Django 4.2 on 2024-09-12 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_remove_coupon_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('PayPal', 'PayPal'), ('Credit/Debit Card', 'Credit/Debit Card')], default=None, max_length=100, null=True),
        ),
    ]
