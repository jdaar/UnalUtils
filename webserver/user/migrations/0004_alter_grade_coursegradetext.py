# Generated by Django 3.2.7 on 2021-09-26 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='courseGradeText',
            field=models.CharField(choices=[('AP', 'Aprobado'), ('RP', 'Reprobado'), ('ND', 'No hay definitiva')], default='ND', max_length=12),
        ),
    ]