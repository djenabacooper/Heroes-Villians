# Generated by Django 4.1.7 on 2023-03-02 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='super',
            old_name='secondary_abiity',
            new_name='secondary_ability',
        ),
    ]
