# Generated by Django 5.1.4 on 2024-12-16 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story',
            old_name='id',
            new_name='storyId',
        ),
    ]