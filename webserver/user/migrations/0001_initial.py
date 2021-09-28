# Generated by Django 3.2.7 on 2021-09-26 23:14

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=64)),
                ('fullname', models.CharField(max_length=128)),
                ('document', models.IntegerField(unique=True)),
                ('expeditionOfDocumentDepartment', models.CharField(max_length=64)),
                ('expeditionOfDocumentPlace', models.CharField(max_length=64)),
                ('sex', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE'), ('U', 'UNDEFINED')], default='U', max_length=1)),
                ('etnicity', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254, unique=True)),
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
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semesterName', models.CharField(max_length=7)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user.semester.grade',
            },
        ),
    ]
