# Generated by Django 5.0 on 2023-12-15 12:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('contact_details', models.TextField()),
                ('address', models.TextField()),
                ('vendor_code', models.CharField(max_length=20, unique=True)),
                ('on_time_delivery_rate', models.FloatField(blank=True, null=True)),
                ('quality_rating_avg', models.FloatField(blank=True, null=True)),
                ('average_response_time', models.FloatField(blank=True, null=True)),
                ('fulfillment_rate', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_number', models.CharField(max_length=20, unique=True)),
                ('order_date', models.DateTimeField()),
                ('delivery_date', models.DateTimeField(blank=True, null=True)),
                ('items', models.CharField(max_length=1000)),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
                ('quality_rating', models.FloatField(blank=True, null=True)),
                ('issue_date', models.DateTimeField(auto_now_add=True)),
                ('acknowledgment_date', models.DateTimeField(blank=True, null=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_orders', to='vendor_api.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('on_time_delivery_rate', models.FloatField()),
                ('quality_rating_avg', models.FloatField()),
                ('average_response_time', models.FloatField()),
                ('fulfillment_rate', models.FloatField()),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor_api.vendor')),
            ],
        ),
    ]
