# Generated by Django 4.1 on 2024-03-19 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guestapp', '0004_delete_travelreg'),
        ('Adminapp', '0004_category'),
        ('Serviceapp', '0002_cateringhreg'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cateringhreg',
            new_name='Cateringreg',
        ),
    ]