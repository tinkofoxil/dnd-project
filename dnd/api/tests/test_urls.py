from django.test import SimpleTestCase
from django.urls import reverse, resolve
from rest_framework.test import APITestCase

from .. import views


class TestUrls(SimpleTestCase):

    def test_profile_url(self):
        url = reverse('profile-list')
        self.assertEqual(resolve(url).func.__name__, views.ProfileViewSet.__name__)

    def test_friends_list_url(self):
        url = reverse('friends-list')
        self.assertEqual(resolve(url).func.__name__, views.FriendsListViewSet.__name__)

    def test_add_delete_friend_url(self):
        url = reverse('add_delete_friend-list', args=[1])
        self.assertEqual(resolve(url).func.__name__, views.FriendsCreateDestroyViewSet.__name__)

    def test_party_url(self):
        url = reverse('party-list')
        self.assertEqual(resolve(url).func.__name__, views.GameViewSet.__name__)

    def test_party_join_url(self):
        url = reverse('party_join-list', args=[1])
        self.assertEqual(resolve(url).func.__name__, views.GameUserViewSet.__name__)

    def test_send_invite_url(self):
        url = reverse('send_invite-list', args=[1, 1])
        self.assertEqual(resolve(url).func.__name__, views.InvitationCreateViewSet.__name__)

    def test_profile_item_url(self):
        url = reverse('profile_item-list', args=[1])
        self.assertEqual(resolve(url).func.__name__, views.ItemViewSet.__name__)


class TestApiAuthUrls(APITestCase):

    def test_redoc_url(self):
        url = reverse('schema-redoc')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
