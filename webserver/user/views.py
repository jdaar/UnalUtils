from .serializers import GradeSerializer, ParentSerializer, SemesterSerializer
from .models import Grade, Parent, Semester
from .serializers import UserSerializer
from .models import User
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import generics, permissions

# Create your views here.


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class GetUser(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        filter = {'username': self.request.user.username}
        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj


class GradesListCreate(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        userid = User.objects.get(
            username=self.request.user.username).id
        return get_list_or_404(Grade.objects.filter(user_id=userid))


class SemesterListCreate(generics.ListCreateAPIView):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        userid = User.objects.get(
            username=self.request.user.username).id
        return get_list_or_404(Grade.objects.filter(user_id=userid))


class ParentListCreate(generics.ListCreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        userid = User.objects.get(
            username=self.request.user.username).id
        return get_list_or_404(Grade.objects.filter(user_id=userid))
