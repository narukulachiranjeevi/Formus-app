# Generated by Django 4.2.6 on 2023-10-30 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='essage',
            new_name='message',
        ),
    ]