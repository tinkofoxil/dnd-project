from django.urls import path

from . import views

urlpatterns = [
    path('api/v1/profile_list/', views.ProfileAPIList.as_view()),
    path('api/v1/profile_list/<int:pk>/', views.ProfileAPIUpdate.as_view())
]
