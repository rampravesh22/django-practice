# Generated by Django 4.0.5 on 2022-07-22 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_section'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='section',
            new_name='section_name',
        ),
    ]