# Generated by Django 2.2 on 2023-08-04 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20230804_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='avail',
        ),
        migrations.AddField(
            model_name='products',
            name='pr_avail',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
