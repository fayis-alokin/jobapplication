# Generated by Django 3.2.12 on 2022-10-19 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20221019_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdetails',
            name='linkedin',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]