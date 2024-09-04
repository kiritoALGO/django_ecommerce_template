# Generated by Django 5.0.4 on 2024-08-31 18:10

from django.db import migrations

def set_initial_order_id(apps, schema_editor):
    schema_editor.execute("UPDATE sqlite_sequence SET seq = 999 WHERE name = 'order_order'")


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_order_id'),
    ]

    operations = [
        migrations.RunPython(set_initial_order_id),
    ]