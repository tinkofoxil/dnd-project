from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import CustomUser


class ProfileViewSetTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='password123'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_profile(self):
        url = reverse('profile-list')
        data = {
            "name": "Test Profile",
            "age": 25,
            "race": "Эльф",
            "class_name": "Волшебник",
            "level": 1,
            "proficiency_bonus": 2,
            "strength": 10,
            "dexterity": 10,
            "constitution": 10,
            "intelligence": 10,
            "wisdom": 10,
            "charisma": 10,
            "description": "Test description"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Test Profile')
