# Generated by Django 2.1.5 on 2019-04-01 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breakdown', '0011_auto_20190320_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='breakdowncategory',
            name='tips',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]