# Generated by Django 3.1.4 on 2021-01-01 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbgames', '0003_auto_20210101_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='telephone_number',
            field=models.CharField(blank=True, default=0, max_length=10, null=True),
        ),
    ]
