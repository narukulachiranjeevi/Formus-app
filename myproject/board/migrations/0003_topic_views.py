# Generated by Django 4.2.6 on 2023-10-31 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_rename_essage_post_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
