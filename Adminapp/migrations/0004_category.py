# Generated by Django 4.1 on 2024-02-27 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0003_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('categoryid', models.AutoField(primary_key=True, serialize=False)),
                ('categoryname', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('desc', models.CharField(max_length=50)),
            ],
        ),
    ]