# Generated by Django 4.2 on 2023-10-28 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mydata', '0004_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_collage_branch',
            name='collage_name',
        ),
        migrations.RemoveField(
            model_name='add_student',
            name='branch_name',
        ),
        migrations.RemoveField(
            model_name='add_student',
            name='collage_name',
        ),
        migrations.DeleteModel(
            name='Add_Collage',
        ),
        migrations.DeleteModel(
            name='Add_Collage_Branch',
        ),
        migrations.DeleteModel(
            name='Add_Student',
        ),
    ]
