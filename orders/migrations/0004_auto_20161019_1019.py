# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 10:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20161018_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Additional_Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('isChoosen', models.BooleanField()),
                ('image', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Sauce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='dish',
        ),
        migrations.RenameField(
            model_name='dish',
            old_name='price',
            new_name='totalPrice',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='dish_name',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='dish_picture',
        ),
        migrations.AddField(
            model_name='dish',
            name='deliveryTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='dish',
            name='orderTime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.AddField(
            model_name='dish',
            name='addIngredients',
            field=models.ManyToManyField(to='orders.Additional_Ingredient'),
        ),
        migrations.AddField(
            model_name='dish',
            name='pasta',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='orders.Pasta'),
        ),
        migrations.AddField(
            model_name='dish',
            name='sauce',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='orders.Sauce'),
        ),
    ]
