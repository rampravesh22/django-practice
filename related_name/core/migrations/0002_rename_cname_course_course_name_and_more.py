# Generated by Django 4.0.5 on 2022-07-22 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='cname',
            new_name='course_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='sname',
            new_name='student_name',
        ),
        migrations.AlterField(
            model_name='course',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='core.student'),
        ),
    ]
