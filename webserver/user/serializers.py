from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User, Semester, Grade, Parent
from .scraping import SiaConnection


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        siaConnection = SiaConnection(
            validated_data['username'], validated_data['password'])
        userSia = siaConnection.getUserDataAndCreateUser()
        parents = userSia.pop('parents')
        user = User.objects.create_user(
            username=validated_data.pop('username'),
            password=make_password(
                validated_data.pop('password')
            ),
            **userSia
        )
        for parent in parents:
            Parent.objects.create(
                user=user,
                name=parent['name'],
                typeOfDocument=parent['typeOfDocument'],
                document=parent['document']
            )
        for semester in siaConnection.getGradesDataAndCreateGrades():
            createdSemester = Semester.objects.create(
                user=user,
                semesterName=semester['semester']
            )
            if semester['grades'] != []:
                for grade in semester['grades']:
                    Grade.objects.create(
                        user=user,
                        semester=createdSemester,
                        courseName=grade['courseName'],
                        courseFinalGrade=-
                        1 if grade['courseGrade'] == 'APROBADA' else grade['courseGrade'],
                        courseGradeText='AP' if grade['courseAprobed'] else 'RP'
                    )
        siaConnection.terminate()
        return user

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
        read_only_fields = (
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
