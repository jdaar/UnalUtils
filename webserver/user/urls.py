from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls.conf import path
from . import views

urlpatterns = [
    path('user/create/', views.UserCreate.as_view()),
    path('user/', views.GetUser.as_view()),
    path('semester/', views.SemesterListCreate.as_view()),
    path('grade/', views.GradesListCreate.as_view()),
    path('parent/', views.ParentListCreate.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view())
]
