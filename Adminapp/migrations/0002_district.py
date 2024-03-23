# Generated by Django 4.1 on 2024-02-23 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('districtid', models.AutoField(primary_key=True, serialize=False)),
                ('districtname', models.CharField(max_length=50)),
                ('stateid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Adminapp.state')),
            ],
        ),
    ]
