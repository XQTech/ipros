# Generated by Django 2.1.5 on 2019-03-12 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suplog', '0003_auto_20190307_1745'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customerstaff',
            options={'ordering': ('company', 'name')},
        ),
        migrations.AlterModelOptions(
            name='suplog',
            options={'ordering': ('-sup_ed_time', '-sup_st_time')},
        ),
    ]
