from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.SimpleRouter()
router.register(r'profile', views.ProfileViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
]
