from django.urls.conf import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.index),
    path('user/', views.index)
]
