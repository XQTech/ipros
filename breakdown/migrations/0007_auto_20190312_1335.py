# Generated by Django 2.1.5 on 2019-03-12 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('breakdown', '0006_auto_20190307_1717'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ('-jira_id',)},
        ),
        migrations.AddField(
            model_name='breakdowncategory',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='breakdown.BreakdownCategory'),
        ),
        migrations.AlterField(
            model_name='breakdown',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='breakdown.BreakdownCategory'),
        ),
        migrations.AlterField(
            model_name='breakdowncategory',
            name='code',
            field=models.CharField(max_length=20),
        ),
    ]
