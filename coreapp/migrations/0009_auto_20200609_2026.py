# Generated by Django 3.0.7 on 2020-06-09 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0008_auto_20200609_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='salary',
            name='date_pmt',
            field=models.DateField(),
        ),
    ]
