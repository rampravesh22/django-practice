# Generated by Django 4.0.5 on 2022-07-22 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_section_section_section_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='section', to='core.student'),
        ),
    ]