from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):

    class Meta:
        db_table = 'user'

    class Sex(models.TextChoices):
        MALE = 'M', _('MALE')
        FEMALE = 'F', _('FEMALE')
        UNDEFINED = 'U', _('UNDEFINED')

    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=64)
    fullname = models.CharField(max_length=128)
    document = models.IntegerField(unique=True)
    expeditionOfDocumentDepartment = models.CharField(max_length=64)
    expeditionOfDocumentPlace = models.CharField(max_length=64)
    sex = models.CharField(
        max_length=1,
        choices=Sex.choices,
        default=Sex.UNDEFINED
    )
    etnicity = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    institutionalEmail = models.EmailField(unique=True)
    cellphoneNumber = models.CharField(max_length=32, unique=True)
    phoneNumber = models.CharField(max_length=32)
    profileImage = models.CharField(max_length=256)
    birthDate = models.CharField(max_length=64)
    birthPlace = models.CharField(max_length=64)
    nationality = models.CharField(max_length=64)
    bloodType = models.CharField(max_length=64)
    rhFactor = models.CharField(max_length=16)
    eps = models.CharField(max_length=64)
    direction = models.CharField(max_length=64)
    stratum = models.CharField(max_length=32)
    militarService = models.CharField(max_length=32)

    objects = UserManager()

    # Django specifics
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'institutionalEmail',
                       'sex', 'document', 'nationality']


class Semester(models.Model):

    class Meta:
        db_table = 'user.semester'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    semesterName = models.CharField(max_length=7)


class Grade(models.Model):

    class Meta:
        db_table = 'user.semester.grade'

    class GradeText(models.TextChoices):
        AP = 'AP', _('Aprobado')
        RP = 'RP', _('Reprobado')
        ND = 'ND', _('No hay definitiva')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    courseName = models.CharField(max_length=128)
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
    name = models.CharField(max_length=256)
    typeOfDocument = models.CharField(
        max_length=2,
        choices=Document.choices,
        default=Document.NI
    )
    document = models.IntegerField(unique=True)
