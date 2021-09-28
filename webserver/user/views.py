from .serializers import GradeSerializer, ParentSerializer, SemesterSerializer
from .models import Grade, Parent, Semester
from .serializers import UserSerializer
from .models import User
from django.shortcuts import get_list_or_404, render, get_object_or_404
from rest_framework import generics

# Create your views here.


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GetUser(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        queryset = self.get_queryset()
        filter = {'username': self.request.query_params.get('username')}
        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj


class GradesListCreate(generics.ListCreateAPIView):
    serializer_class = GradeSerializer

    def get_queryset(self):
        userid = User.objects.get(
            username=self.request.query_params.get('username')).id
        return get_list_or_404(Grade.objects.filter(user_id=1))


class SemesterListCreate(generics.ListCreateAPIView):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer


class ParentListCreate(generics.ListCreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
