# Generated by Django 5.0.1 on 2024-02-12 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Netflix', '0002_student_delete_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='place',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]
