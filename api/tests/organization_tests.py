"""
Tests for organization model
"""

from django.test import TestCase
from django.utils import timezone
from ..models import Organization

class OrganizationModelTestCase(TestCase):
    """ Organization model test case """

    expected_display_name = "mock org"
    expected_organization_name = "mock org co"
    expected_website = "www.website.com"
    expected_elevator_pitch = "Mock org is here to mock you."
    expected_address = "42 mock st"
    expected_city = "Mock"
    expected_state = "MO"
    expected_postal_code = "01982-000"
    expected_date_joined = timezone.now()
    expected_is_verified_501c3 = True
    expected_account_status = Organization.OPEN

    def setUp(self):
        self.organization = Organization(
            display_name=self.expected_display_name,
            organization_name=self.expected_organization_name,
            website=self.expected_website,
            elevator_pitch=self.expected_elevator_pitch,
            address=self.expected_address,
            city=self.expected_city,
            state=self.expected_state,
            postal_code=self.expected_postal_code,
            date_joined=self.expected_date_joined,
            is_verified_501c3=self.expected_is_verified_501c3,
            account_status=self.expected_account_status
        )

    def test_can_create_organization(self):
        """ test that an organization can be created """

        before_save_count = Organization.objects.count()
        self.organization.save()
        after_save_count = Organization.objects.count()

        self.assertEqual(after_save_count - before_save_count, 1)
        return

    def test_account_status_choices(self):
        """ test that account status choices are correct """

        self.assertEqual(
            Organization.ACCOUNT_STATUS_CHOICES[0],
            (Organization.OPEN, "Open")
        )
        self.assertEqual(
            Organization.ACCOUNT_STATUS_CHOICES[1],
            (Organization.CLOSED, "Closed")
        )
        self.assertEqual(
            Organization.ACCOUNT_STATUS_CHOICES[2],
            (Organization.CREATING, "Creating")
        )
        self.assertEqual(
            Organization.ACCOUNT_STATUS_CHOICES[3],
            (Organization.VERIFYING, "Verifying")
        )

        return
