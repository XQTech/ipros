# Generated by Django 2.1.5 on 2019-01-23 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breakdown', '0002_auto_20190123_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='ticket_no',
            field=models.CharField(default='', max_length=10),
        ),
    ]
