# Generated by Django 2.2 on 2023-07-24 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20230724_1136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
