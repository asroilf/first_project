# Generated by Django 4.2 on 2023-07-26 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0018_delete_bajarildimodel_vazifamodel_date_bajarildi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vazifamodel',
            old_name='date_bajarildi',
            new_name='bajarildgan_date',
        ),
    ]
