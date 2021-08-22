from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_on_email(self):
        """Test creating a new user with an email """
        email = "test@gmail.com"
        password = "Test12345"

        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_normalized_email(self):
        """Test normalized email while creating user"""
        email = "test123@Gmail.com"
        user = get_user_model().objects.create_user(email=email, password="Test12345")
        self.assertEqual(user.email, email.lower())
