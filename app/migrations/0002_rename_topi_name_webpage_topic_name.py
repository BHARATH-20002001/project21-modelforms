# Generated by Django 4.2.7 on 2024-01-09 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webpage',
            old_name='topi_name',
            new_name='topic_name',
        ),
    ]