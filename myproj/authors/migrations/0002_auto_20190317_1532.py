# Generated by Django 2.1.7 on 2019-03-17 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AuthorsModel',
            new_name='Authors',
        ),
        migrations.AlterModelOptions(
            name='authors',
            options={'verbose_name': 'Authors', 'verbose_name_plural': 'Authors'},
        ),
        migrations.RenameField(
            model_name='authors',
            old_name='email_address',
            new_name='email',
        ),
    ]