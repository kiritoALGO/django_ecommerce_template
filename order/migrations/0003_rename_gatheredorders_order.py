# Generated by Django 5.0.4 on 2024-08-20 06:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_initial'),
        ('orderItem', '0005_rename_gathered_orders_orderitem_order'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GatheredOrders',
            new_name='Order',
        ),
    ]
