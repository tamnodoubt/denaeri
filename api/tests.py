"""
Tests for api app
"""

from django.test import TestCase
from .models import User

class UserModelTestCase(TestCase):
    """ Test suite for User model """

    def setUp(self):
        """ define reusable test variables """
        self.expected_username = "stam"
        self.expected_phone_number = "9785008493"
        self.user = User(
            username=self.expected_username,
            phone_number=self.expected_phone_number
        )
        return

    def test_that_user_has_username(self):
        """ tests that the user has a username """
        self.assertEqual(self.user.username, self.expected_username)
        return

    def test_that_can_create_user(self):
        """ tests that a user can be created and saved """
        count_before_save = User.objects.count()
        self.user.save()
        count_after_save = User.objects.count()

        self.assertEqual(count_after_save - count_before_save, 1)
        return

    def test_that_user_has_phone_number(self):
        """ test that a user has a phone number """
        self.assertEqual(self.user.phone_number, self.expected_phone_number)
        return
