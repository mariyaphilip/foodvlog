# Generated by Django 2.2 on 2023-08-04 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20230804_1210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='pr_avail',
            new_name='accessable_prodts',
        ),
    ]
