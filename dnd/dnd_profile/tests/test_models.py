from django.test import TestCase
from django.contrib.auth import get_user_model
from users.models import CustomUser
from ..models import Profile, Item, Inventory

CustomUser = get_user_model()


class ProfileModelTest(TestCase):
    @classmethod
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='password123'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            name='Test Character',
            age=30,
            race='Эльф',
            class_name='Воин',
            level=1,
            proficiency_bonus=2,
            strength=10,
            dexterity=12,
            constitution=14,
            intelligence=16,
            wisdom=8,
            charisma=10,
            description='A brave warrior',
        )

    def test_profile_creation(self):
        self.assertEqual(self.profile.name, 'Test Character')
        self.assertEqual(self.profile.age, 30)
        self.assertEqual(self.profile.race, 'Эльф')
        self.assertEqual(self.profile.class_name, 'Воин')
        self.assertEqual(self.profile.level, 1)
        self.assertEqual(self.profile.proficiency_bonus, 2)
        self.assertEqual(self.profile.strength, 10)
        self.assertEqual(self.profile.description, 'A brave warrior')
        self.assertEqual(str(self.profile), 'Test Character')


class ItemModelTest(TestCase):
    @classmethod
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='password123'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            name='Test Character',
            age=30,
            race='Эльф',
            class_name='Воин',
            level=1,
            proficiency_bonus=2,
            strength=10,
            dexterity=12,
            constitution=14,
            intelligence=16,
            wisdom=8,
            charisma=10,
            description='A brave warrior',
        )
        self.item = Item.objects.create(
            name='Sword',
            description='A sharp blade',
            character=self.profile
        )

    def test_item_creation(self):
        self.assertEqual(self.item.name, 'Sword')
        self.assertEqual(self.item.description, 'A sharp blade')
        self.assertEqual(self.item.character, self.profile)
        self.assertEqual(str(self.item), 'Sword --- Test Character')


class InventoryModelTest(TestCase):
    @classmethod
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='password123'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            name='Test Character',
            age=30,
            race='Эльф',
            class_name='Воин',
            level=1,
            proficiency_bonus=2,
            strength=10,
            dexterity=12,
            constitution=14,
            intelligence=16,
            wisdom=8,
            charisma=10,
            description='A brave warrior',
        )
        self.item1 = Item.objects.create(
            name='Sword',
            description='A sharp blade',
            character=self.profile
        )
        self.item2 = Item.objects.create(
            name='Shield',
            description='A sturdy shield',
            character=self.profile
        )
        self.inventory = Inventory.objects.create(
            character=self.profile
        )
        self.inventory.item.add(self.item1)
        self.inventory.item.add(self.item2)

    def test_inventory_creation(self):
        self.assertEqual(self.inventory.character, self.profile)
        self.assertEqual(self.inventory.item.count(), 2)
        self.assertIn(self.item1, self.inventory.item.all())
        self.assertIn(self.item2, self.inventory.item.all())
        self.assertEqual(
            str(self.inventory),
            'Инвентарь Test Character: Sword, Shield'
        )
