# Generated by Django 4.2 on 2023-05-09 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=100, null=True),
        ),
    ]