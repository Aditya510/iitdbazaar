# Generated by Django 2.1.7 on 2019-03-04 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='data_posted',
            new_name='date_posted',
        ),
    ]
