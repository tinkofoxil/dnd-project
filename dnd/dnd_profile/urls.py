from django.urls import path

from . import views

urlpatterns = [
    path('api/v1/profile_list/', views.ProfileAPIView.as_view()),
]
