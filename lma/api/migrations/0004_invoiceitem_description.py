# Generated by Django 3.1.1 on 2020-09-16 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_company_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceitem',
            name='description',
            field=models.CharField(default='', max_length=150),
        ),
    ]
