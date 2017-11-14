"""
admin setup
"""

from django.contrib import admin
from .models.organization import Organization
from .models.donor import Donor

admin.site.register(Organization)
admin.site.register(Donor)
