# Generated by Django 4.0.5 on 2022-06-21 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_alter_data_modified_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
