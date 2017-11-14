"""
Serializer for Donor model
"""

from rest_framework import serializers
from ..models.donor import Donor

class DonorSerializer(serializers.ModelSerializer):
    """Serializer to map Donor instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""

        model = Donor
        fields = (
            'id', 'username',
            'phone_number', 'email',
            'date_joined', 'first_name',
            'last_name'
        )
        read_only_fields = ('id', 'date_joined')
