"""
Models for api app
"""

from django.db import models

class User(models.Model):
    """ A user of the donor app """

    username = models.CharField(max_length=200)
