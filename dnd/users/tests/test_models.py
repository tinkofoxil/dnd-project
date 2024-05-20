from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Friendship

CustomUser = get_user_model()


class CustomUserModelTest(TestCase):
    @classmethod
    def setUp(self):
        self.user1 = CustomUser.objects.create_user(
            username='user1',
            password='pass1',
            birth_date='1990-01-01'
        )
        self.user2 = CustomUser.objects.create_user(
            username='user2',
            password='pass2',
            birth_date='1992-02-02'
        )

    def test_user_creation(self):
        self.assertEqual(self.user1.username, 'user1')
        self.assertEqual(self.user1.birth_date, '1990-01-01')

    def test_user_registration_date(self):
        self.assertIsNotNone(self.user1.registration_date)


class FriendshipModelTest(TestCase):
    @classmethod
    def setUp(self):
        self.user1 = CustomUser.objects.create_user(
            username='user1',
            password='pass1'
        )
        self.user2 = CustomUser.objects.create_user(
            username='user2',
            password='pass2'
        )
        self.friendship = Friendship.objects.create(
            user=self.user1,
            friend=self.user2
        )

    def test_friendship_creation(self):
        self.assertEqual(self.friendship.user, self.user1)
        self.assertEqual(self.friendship.friend, self.user2)
        self.assertEqual(str(self.friendship), 'user1 - user2')

    def test_unique_together_constraint(self):
        with self.assertRaises(Exception):
            Friendship.objects.create(
                user=self.user1,
                friend=self.user2
            )
