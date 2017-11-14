"""
Serializer for Donor model
"""

from rest_framework import serializers
from ..models.organization import Organization

class OrganizationSerializer(serializers.ModelSerializer):
    """Serializer to map Donor instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""

        model = Organization
        fields = (
            'id', 'display_name',
            'organization_name', 'website',
            'elevator_pitch', 'address',
            'city', 'state',
            'postal_code', 'date_joined',
            'is_verified_501c3', 'account_status'
        )

        read_only_fields = (
            'id', 'date_joined',
            'is_verified_501c3', 'account_status'
        )
