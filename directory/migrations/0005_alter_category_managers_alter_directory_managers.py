# Generated by Django 4.2 on 2024-03-11 09:38

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0004_alter_category_parent'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='category',
            managers=[
                ('default_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='directory',
            managers=[
                ('default_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
