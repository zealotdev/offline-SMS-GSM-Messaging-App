# Generated by Django 2.2.3 on 2019-08-05 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0011_auto_20190804_1506'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contact', 'verbose_name_plural': 'Contacts'},
        ),
        migrations.RenameField(
            model_name='messagehistory',
            old_name='contacts',
            new_name='recipients',
        ),
    ]