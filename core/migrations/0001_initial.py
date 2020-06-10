# Generated by Django 3.0.7 on 2020-06-09 16:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('cpf', models.CharField(max_length=11, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(11), django.core.validators.MaxLengthValidator(11)])),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_pmt', models.DateField()),
                ('salary', models.FloatField()),
                ('deduction', models.FloatField()),
                ('cpf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Employee')),
            ],
        ),
    ]
