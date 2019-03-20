# Generated by Django 2.1.5 on 2019-03-20 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='systemmodule',
            options={'ordering': ('customer', 'name')},
        ),
        migrations.AddField(
            model_name='systemmodule',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.Customer'),
        ),
    ]
