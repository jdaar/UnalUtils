from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User, Semester, Grade, Parent


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(
            password=make_password(
                validated_data.pop('password')
            ),
            **validated_data
        )
        return user

    def update(self, instance, validated_data):
        if 'user' in validated_data:
            instance.user.password = make_password(
                validated_data.get(
                    'password', instance.user.password)
            )
            instance.save()

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'fullname',
            'document',
            'expeditionOfDocumentDepartment',
            'expeditionOfDocumentPlace',
            'sex',
            'etnicity',
            'email',
            'institutionalEmail',
            'cellphoneNumber',
            'phoneNumber',
            'profileImage',
            'birthDate',
            'birthPlace',
            'nationality',
            'bloodType',
            'rhFactor',
            'eps',
            'direction',
            'stratum',
            'militarService'
        )


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = (
            'user',
            'semesterName'
        )


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = (
            'semester',
            'courseName',
            'courseFinalGrade',
            'courseGradeText'
        )


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = (
            'user',
            'name',
            'typeOfDocument',
            'document'
        )
