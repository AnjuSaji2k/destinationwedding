# Generated by Django 4.1 on 2024-03-21 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guestapp', '0005_customerreg'),
        ('Adminapp', '0007_rename_image_subcategory_subimage'),
        ('Serviceapp', '0004_destinationreg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Serviceregistration',
            fields=[
                ('serviceid', models.AutoField(primary_key=True, serialize=False)),
                ('servicename', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('desc', models.CharField(max_length=100)),
                ('categoryid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Adminapp.category')),
                ('locationid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Adminapp.location')),
                ('providerid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Guestapp.servicereg')),
            ],
        ),
    ]
