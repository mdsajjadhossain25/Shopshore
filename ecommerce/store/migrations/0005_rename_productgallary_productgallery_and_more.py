# Generated by Django 4.2.4 on 2023-09-30 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_productgallary'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductGallary',
            new_name='ProductGallery',
        ),
        migrations.AlterModelOptions(
            name='productgallery',
            options={'verbose_name': 'productgallery', 'verbose_name_plural': 'product gallery'},
        ),
    ]
