from django.urls.conf import path
from . import views

urlpatterns = [
    path('user/create', views.UserCreate.as_view()),
    path('user/get', views.GetUser.as_view()),
    path('semester/', views.SemesterListCreate.as_view()),
    path('grade/', views.GradesListCreate.as_view()),
    path('parent/', views.ParentListCreate.as_view())
]
