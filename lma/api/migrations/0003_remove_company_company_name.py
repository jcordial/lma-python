# Generated by Django 3.1.1 on 2020-09-16 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200915_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='company_name',
        ),
    ]
