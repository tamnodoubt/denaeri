"""
Tests for api app
"""

from django.test import TestCase
from django.utils import timezone
from ..models import Donor

class DonorModelTestCase(TestCase):
    """ Test suite for User model """

    def setUp(self):
        """ define reusable test variables """
        self.expected_username = "stam"
        self.expected_phone_number = "9785008493"
        self.expected_email = "stam@denaeri.com"
        self.expected_first_name = "stephen"
        self.expected_last_name = "tam"
        self.donor = Donor(
            username=self.expected_username,
            phone_number=self.expected_phone_number,
            email=self.expected_email,
            first_name=self.expected_first_name,
            last_name=self.expected_last_name
        )
        return

    def test_that_user_has_username(self):
        """ tests that the user has a username """
        self.assertEqual(self.donor.username, self.expected_username)
        return

    def test_that_can_create_user(self):
        """ tests that a user can be created and saved """
        count_before_save = Donor.objects.count()
        self.donor.save()
        count_after_save = Donor.objects.count()

        self.assertEqual(count_after_save - count_before_save, 1)
        return

    def test_that_user_has_phone_number(self):
        """ test that a user has a phone number """
        self.assertEqual(self.donor.phone_number, self.expected_phone_number)
        return

    def test_that_user_has_email(self):
        """ test that a user has an email """
        self.assertEqual(self.donor.email, self.expected_email)
        return

    def test_that_user_has_date_joined(self):
        """ test that a user has a join date """
        now = timezone.now()
        self.donor.save()

        self.assertGreater(self.donor.date_joined, now)
        return

    def test_that_user_has_first_name(self):
        """ test that a user has a first name """
        self.assertEqual(self.donor.first_name, self.expected_first_name)
        return

    def test_that_user_has_last_name(self):
        """ test that a user has a last name """
        self.assertEqual(self.donor.last_name, self.expected_last_name)
        return
