# Generated by Django 2.1.5 on 2019-03-20 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breakdown', '0010_auto_20190318_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breakdown',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
