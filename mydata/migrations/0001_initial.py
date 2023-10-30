# Generated by Django 4.2 on 2023-10-28 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Collage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collage_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Add_Collage_Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=100)),
                ('collage_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mydata.add_collage')),
            ],
        ),
        migrations.CreateModel(
            name='Add_Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_age', models.IntegerField()),
                ('branch_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mydata.add_collage_branch')),
                ('collage_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mydata.add_collage')),
            ],
        ),
    ]
