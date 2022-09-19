# Generated by Django 3.2.13 on 2022-06-15 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('addressid', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('userid', models.PositiveIntegerField(verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user'))),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productid', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSeller',
            fields=[
                ('selling_productid', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('sellerid', models.PositiveIntegerField(verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.seller'))),
                ('productid', models.PositiveIntegerField(verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product'))),
                ('price', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('sellerid', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('gender', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=13)),
            ],
        ),
    ]