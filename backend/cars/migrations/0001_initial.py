# Generated by Django 5.0.6 on 2024-05-15 17:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('car_id', models.AutoField(primary_key=True, serialize=False)),
                ('number_of_owners', models.IntegerField()),
                ('registration_number', models.CharField(max_length=100, unique=True)),
                ('manufacture_year', models.IntegerField()),
                ('number_of_doors', models.IntegerField(default=5)),
                ('mileage', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('car_model_id', models.AutoField(primary_key=True, serialize=False)),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('advertisement_id', models.AutoField(primary_key=True, serialize=False)),
                ('advertisement_date', models.DateTimeField()),
                ('seller_account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.appuser')),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='car_model_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.carmodel'),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('profile_id', models.AutoField(primary_key=True, serialize=False)),
                ('street_name', models.CharField(max_length=100)),
                ('street_number', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=100)),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.appuser')),
            ],
        ),
    ]
