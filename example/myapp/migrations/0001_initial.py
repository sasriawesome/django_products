# Generated by Django 3.0.5 on 2020-04-07 16:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_products.Product')),
                ('sn', models.CharField(blank=True, max_length=150, null=True, verbose_name='serial number')),
                ('stock_on_hand', models.IntegerField(default=0, verbose_name='stock on hand')),
                ('stock_on_delivery', models.IntegerField(default=0, verbose_name='stock on delivery')),
                ('stock_on_request', models.IntegerField(default=0, verbose_name='stock on request')),
                ('min_stock', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='min stock')),
                ('max_stock', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='max stock')),
            ],
            options={
                'verbose_name': 'Book',
            },
            bases=('django_products.product', models.Model),
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_products.Product')),
                ('sn', models.CharField(blank=True, max_length=150, null=True, verbose_name='serial number')),
                ('stock_on_hand', models.IntegerField(default=0, verbose_name='stock on hand')),
                ('stock_on_delivery', models.IntegerField(default=0, verbose_name='stock on delivery')),
                ('stock_on_request', models.IntegerField(default=0, verbose_name='stock on request')),
                ('min_stock', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='min stock')),
                ('max_stock', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='max stock')),
            ],
            options={
                'verbose_name': 'Music',
            },
            bases=('django_products.product', models.Model),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_products.Product')),
                ('sn', models.CharField(blank=True, max_length=150, null=True, verbose_name='serial number')),
                ('stock_on_hand', models.IntegerField(default=0, verbose_name='stock on hand')),
                ('stock_on_delivery', models.IntegerField(default=0, verbose_name='stock on delivery')),
                ('stock_on_request', models.IntegerField(default=0, verbose_name='stock on request')),
                ('min_stock', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='min stock')),
                ('max_stock', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='max stock')),
            ],
            options={
                'verbose_name': 'Video',
            },
            bases=('django_products.product', models.Model),
        ),
    ]
