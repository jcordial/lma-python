# Generated by Django 3.1.1 on 2020-09-18 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_invoiceitem_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='username',
        ),
    ]