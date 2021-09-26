from django.db import models
from siascraping.classes.parent import Parent

class User(models.Model):
	username = models.CharField(30)
	password = password
	fullname = fullname
	document = document
	expeditionOfDocumentDepartment = expeditionOfDocumentDepartment
	expeditionOfDocumentPlace = expeditionOfDocumentPlace
	sex = sex
	etnicity = etnicity
	personalEmail = personalEmail
	institutionalEmail = institutionalEmail
	cellphoneNumber = cellphoneNumber
	phoneNumber = phoneNumber
	profileImage = profileImage
	birthDate = birthDate
	birthPlace = birthPlace
	nationality = nationality
	bloodType = bloodType
	rhFactor = rhFactor
	eps = eps
	father = father
	mother = mother
	direction = direction
	stratum = stratum
	militarService = militarService
	grades = grades