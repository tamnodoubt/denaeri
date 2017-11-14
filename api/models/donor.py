"""
Donor model for api app
"""

from django.db import models

class Donor(models.Model):
    """ A user of the donor app """

    username = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=30)
    email = models.CharField(max_length=200)
    date_joined = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + ": " + self.username
