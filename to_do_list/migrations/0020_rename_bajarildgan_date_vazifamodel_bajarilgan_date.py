# Generated by Django 4.2 on 2023-07-26 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0019_rename_date_bajarildi_vazifamodel_bajarildgan_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vazifamodel',
            old_name='bajarildgan_date',
            new_name='bajarilgan_date',
        ),
    ]
