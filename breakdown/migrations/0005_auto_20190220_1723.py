# Generated by Django 2.1.5 on 2019-02-20 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breakdown', '0004_auto_20190220_1543'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ('ticket_no', '-due_date', 'customer')},
        ),
        migrations.AlterField(
            model_name='breakdown',
            name='image1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='breakdown',
            name='image2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='breakdown',
            name='image3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
