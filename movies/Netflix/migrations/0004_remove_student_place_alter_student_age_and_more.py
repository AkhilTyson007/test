# Generated by Django 5.0.1 on 2024-02-12 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Netflix', '0003_student_place_alter_student_mobile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='place',
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='student',
            name='mobile',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
