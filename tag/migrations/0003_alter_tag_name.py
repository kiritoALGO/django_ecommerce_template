# Generated by Django 5.0.7 on 2024-08-14 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0002_alter_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
