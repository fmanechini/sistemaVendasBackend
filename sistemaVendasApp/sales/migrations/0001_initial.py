# Generated by Django 3.2 on 2021-04-26 01:48

from django.db import migrations, models
import django.db.models.deletion
import sales.models.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Client name')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name of the product or service')),
                ('comission', models.FloatField(validators=[sales.models.validators.validate_comissions], verbose_name='Comission percentage')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Price from product or service')),
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
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.seller')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Product quantity')),
                ('applied_comission', models.FloatField(validators=[sales.models.validators.validate_comissions], verbose_name='Comission percentage applied for certain sale')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.product')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='sales.sale')),
            ],
        ),
    ]
