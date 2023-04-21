from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from . import views


router = routers.SimpleRouter()
router.register(r'profile', views.ProfileViewSet)
router.register(r'game', views.GameViewSet)
router.register(r'user/(?P<user_id>\d+)/profiles', views.MyProfilesViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
