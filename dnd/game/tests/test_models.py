from django.test import TestCase
from django.contrib.auth import get_user_model
from users.models import CustomUser
from ..models import Game, Invitation, GameUser

CustomUser = get_user_model()


class GameModelTest(TestCase):
    @classmethod
    def setUp(self):
        self.game = Game.objects.create(
            name='Test Game'
        )

    def test_game_creation(self):
        self.assertEqual(self.game.name, 'Test Game')
        self.assertEqual(self.game.status, 'created')
        self.assertIsNone(self.game.start_time)
        self.assertIsNone(self.game.finish_time)
        self.assertEqual(str(self.game), 'Test Game')


class InvitationModelTest(TestCase):
    @classmethod
    def setUp(self):
        self.sender = CustomUser.objects.create_user(
            username='sender',
            password='password123'
        )
        self.recipient = CustomUser.objects.create_user(
            username='recipient',
            password='password123'
        )
        self.game = Game.objects.create(
            name='Test Game'
        )
        self.invitation = Invitation.objects.create(
            sender=self.sender,
            recipient=self.recipient,
            game=self.game
        )

    def test_invitation_creation(self):
        self.assertEqual(self.invitation.sender, self.sender)
        self.assertEqual(self.invitation.recipient, self.recipient)
        self.assertEqual(self.invitation.game, self.game)
        self.assertEqual(str(self.invitation), f'{self.sender} --- {self.recipient}')


class GameUserModelTest(TestCase):
    @classmethod
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='password123'
        )
        self.game = Game.objects.create(
            name='Test Game'
        )
        self.game_user = GameUser.objects.create(
            user=self.user,
            game=self.game
        )

    def test_game_user_creation(self):
        self.assertEqual(self.game_user.user, self.user)
        self.assertEqual(self.game_user.game, self.game)
        self.assertEqual(str(self.game_user), f'{self.user} --- {self.game}')

    def test_game_players(self):
        self.game.players.add(self.user)
        self.assertIn(self.user, self.game.players.all())
