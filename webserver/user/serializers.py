from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User, Semester, Grade, Parent
from .scraping import SiaConnection


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        userSia = SiaConnection(
            validated_data['username'], validated_data['password']).getUserDataAndCreateUser()
        user = User.objects.create_user(
            username=validated_data.pop('username'),
            password=make_password(
                validated_data.pop('password')
            ),
            **userSia
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
