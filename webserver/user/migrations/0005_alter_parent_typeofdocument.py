# Generated by Django 3.2.7 on 2021-09-26 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_grade_coursegradetext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='typeOfDocument',
            field=models.CharField(choices=[('TI', 'Tarjeta de identidad'), ('CC', 'Cedula de ciudadania'), ('NI', 'No informado')], default='NI', max_length=32),
        ),
    ]
