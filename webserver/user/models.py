from django import db
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.


class User(models.Model):

    class Meta:
        db_table = 'user'

    class Sex(models.TextChoices):
        MALE = 'M', _('MALE')
        FEMALE = 'F', _('FEMALE')
        UNDEFINED = 'U', _('UNDEFINED')

    username = models.CharField(32, unique=True)
    password = models.CharField(64)
    fullname = models.CharField(128)
    document = models.IntegerField(unique=True)
    expeditionOfDocumentDepartment = models.CharField(64)
    expeditionOfDocumentPlace = models.CharField(64)
    sex = models.CharField(
        max_length=1,
        choices=Sex.choices,
        default=Sex.UNDEFINED
    )
    etnicity = models.CharField(64)
    personalEmail = models.EmailField(unique=True)
    institutionalEmail = models.EmailField(unique=True)
    cellphoneNumber = models.CharField(32, unique=True)
    phoneNumber = models.CharField(32)
    profileImage = models.CharField(256)
    birthDate = models.CharField(64)
    birthPlace = models.CharField(64)
    nationality = models.CharField(64)
    bloodType = models.CharField(64)
    rhFactor = models.CharField(16)
    eps = models.CharField(64)
    direction = models.CharField(64)
    stratum = models.CharField(32)
    militarService = models.CharField(32)


class Semester(models.Model):

    class Meta:
        db_table = 'user.semester'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    semesterName = models.CharField(6)


class Grade(models.Model):

    class Meta:
        db_table = 'user.semester.grade'

    class GradeText(models.TextChoices):
        AP = 'AP', _('Aprobado')
        RP = 'RP', _('Reprobado')
        ND = 'ND', _('No hay definitiva')

    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    courseName = models.CharField(128)
    courseFinalGrade = models.FloatField(
        default=-1, validators=[MaxValueValidator(5)])
    courseGradeText = models.CharField(
        max_length=2,
        choices=GradeText.choices,
        default=GradeText.ND
    )


class Parent(models.Model):

    class Meta:
        db_table = 'user.parent'

    class Document(models.TextChoices):
        TI = 'TI', _('Tarjeta de identidad')
        CC = 'CC', _('Cedula de ciudadania')
        NI = 'NI', _('No informado')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(256)
    typeOfDocument = models.CharField(
        max_length=2,
        choices=Document.choices,
        default=Document.NI
    )
    document = models.IntegerField(unique=True)
