# Generated by Django 4.0.5 on 2022-10-01 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.RemoveField(
            model_name='order',
            name='transaction_id',
        ),
    ]