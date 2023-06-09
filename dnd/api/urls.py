from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework import routers

from . import views


router = routers.SimpleRouter()
router.register(r'profile', views.ProfileViewSet)
router.register(r'game', views.GameViewSet)
router.register(r'user/(?P<user_id>\d+)/profiles', views.MyProfilesViewSet)
router.register('users/friends', views.FriendsListViewSet, basename='friends')
router.register(
    r'users/(?P<user_id>\d+)/friend',
    views.FriendsCreateDestroyViewSet,
    basename='add_delete_friend'
)
router.register('party', views.GameViewSet, basename='party')
router.register(
    r'party/(?P<game_id>\d+)/join',
    views.GameUserViewSet,
    basename='party_join'
)
router.register(
    'users/invitation',
    views.InvitationReadViewSet,
    basename='invitation_requests'
)
router.register(
    r'party/(?P<game_id>\d+)/users/(?P<user_id>\d+)/invite',
    views.InvitationCreateViewSet,
    basename='send_invite'
)

schema_view = get_schema_view(
    openapi.Info(
        title="DND API",
        default_version='v1.0',
        description="Документация для DND API",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    path(
        'api/v1/redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
