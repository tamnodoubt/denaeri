"""
View for Donor
"""

from rest_framework import generics
from ..serializers import DonorSerializer
from ..models import Donor

class CreateDonorView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()
