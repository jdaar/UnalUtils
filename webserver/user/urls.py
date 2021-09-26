from django.urls.conf import path
from . import views

urlpatterns = [
    path('', views.UserListCreate.as_view()),
    path('semester/', views.SemesterListCreate.as_view()),
    path('grade/', views.GradesListCreate.as_view()),
    path('parent/', views.ParentListCreate.as_view())
]
