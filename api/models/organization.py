"""
Organization model for api app
"""

from django.db import models

class Organization(models.Model):
    """ An organization partner """

    OPEN = "Op"
    CLOSED = "Cl"
    CREATING = "Cr"
    VERIFYING = "Ve"
    ACCOUNT_STATUS_CHOICES = (
        (OPEN, "Open"),
        (CLOSED, "Closed"),
        (CREATING, "Creating"),
        (VERIFYING, "Verifying")
    )

    display_name = models.CharField(max_length=200)
    organization_name = models.CharField(max_length=200)
    website = models.CharField(max_length=400)
    elevator_pitch = models.TextField(blank=False)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    postal_code = models.CharField(max_length=20)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_verified_501c3 = models.BooleanField(default=False)
    account_status = models.CharField(
        max_length=2,
        choices=ACCOUNT_STATUS_CHOICES,
        default=CREATING
    )

    def __str__(self):
        return str(self.id) + ": " + self.display_name
