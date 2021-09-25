# Generated by Django 3.2.7 on 2021-09-25 18:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=64)),
                ('fullname', models.CharField(max_length=128)),
                ('document', models.IntegerField(unique=True)),
                ('expeditionOfDocumentDepartment', models.CharField(max_length=64)),
                ('expeditionOfDocumentPlace', models.CharField(max_length=64)),
                ('sex', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE'), ('U', 'UNDEFINED')], default='U', max_length=1)),
                ('etnicity', models.CharField(max_length=64)),
                ('personalEmail', models.EmailField(max_length=254, unique=True)),
                ('institutionalEmail', models.EmailField(max_length=254, unique=True)),
                ('cellphoneNumber', models.CharField(max_length=32, unique=True)),
                ('phoneNumber', models.CharField(max_length=32)),
                ('profileImage', models.CharField(max_length=256)),
                ('birthDate', models.CharField(max_length=64)),
                ('birthPlace', models.CharField(max_length=64)),
                ('nationality', models.CharField(max_length=64)),
                ('bloodType', models.CharField(max_length=64)),
                ('rhFactor', models.CharField(max_length=16)),
                ('eps', models.CharField(max_length=64)),
                ('direction', models.CharField(max_length=64)),
                ('stratum', models.CharField(max_length=32)),
                ('militarService', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semesterName', models.CharField(max_length=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'user.semester',
            },
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('typeOfDocument', models.CharField(choices=[('TI', 'Tarjeta de identidad'), ('CC', 'Cedula de ciudadania'), ('NI', 'No informado')], default='NI', max_length=2)),
                ('document', models.IntegerField(unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'user.parent',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=128)),
                ('courseFinalGrade', models.FloatField(default=-1, validators=[django.core.validators.MaxValueValidator(5)])),
                ('courseGradeText', models.CharField(choices=[('AP', 'Aprobado'), ('RP', 'Reprobado'), ('ND', 'No hay definitiva')], default='ND', max_length=2)),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.semester')),
            ],
            options={
                'db_table': 'user.semester.grade',
            },
        ),
    ]