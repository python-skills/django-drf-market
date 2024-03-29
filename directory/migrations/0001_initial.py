# Generated by Django 4.2 on 2024-02-22 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31)),
                ('logo', models.ImageField(upload_to='categories/')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Directory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('slug', models.CharField(max_length=31, unique=True)),
                ('logo', models.ImageField(upload_to='directories/')),
                ('description', models.CharField(max_length=511)),
                ('link', models.CharField(max_length=127)),
                ('is_active', models.BooleanField(default=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(to='startup.category')),
            ],
            options={
                'verbose_name': 'Directory',
                'verbose_name_plural': 'Directories',
            },
        ),
    ]
