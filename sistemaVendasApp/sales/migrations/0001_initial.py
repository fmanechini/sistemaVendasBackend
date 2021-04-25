# Generated by Django 3.2 on 2021-04-25 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nome do Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Product quantity')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name of the product or service')),
                ('comission', models.FloatField(verbose_name='Comission percentage')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name of the seller')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_datetime', models.DateTimeField(verbose_name='Date and time of the sale')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.client')),
                ('items', models.ManyToManyField(to='sales.Item')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.seller')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.product'),
        ),
    ]