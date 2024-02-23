# Generated by Django 5.0.2 on 2024-02-22 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('product_name', models.CharField(max_length=30)),
                ('product_category', models.CharField(max_length=30)),
                ('product_price', models.IntegerField()),
                ('product_manifacturing_date', models.DateField()),
                ('product_manifactured_by', models.CharField(max_length=40)),
            ],
        ),
    ]
