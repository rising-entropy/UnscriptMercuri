# Generated by Django 3.1.1 on 2020-11-21 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercuri', '0005_auto_20201121_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='shift',
            field=models.CharField(default='Morning', max_length=20),
        ),
    ]