from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.SimpleRouter()
router.register(r'profile', views.ProfileViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    #path('api/v1/profile/', views.ProfileViewSet.as_view({'get': 'list'})),
    #path('api/v1/profile/<int:pk>/', views.ProfileViewSet.as_view({'put': 'update'}))
]
