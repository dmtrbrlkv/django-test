# Generated by Django 2.1.7 on 2019-03-17 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0003_auto_20190317_1533'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Authors',
            new_name='Author',
        ),
    ]
