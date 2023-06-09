# Generated by Django 4.1.1 on 2023-01-03 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('price', models.IntegerField(default=0)),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('details', models.TextField(blank=True, default='', max_length=500, null=True)),
                ('img', models.ImageField(upload_to='media/img/item')),
                ('slug', models.SlugField()),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.category')),
            ],
        ),
    ]
