"""
View for Donor
"""

from rest_framework.generics import ListCreateAPIView
from ..serializers import DonorSerializer
from ..models import Donor

class CreateDonorView(ListCreateAPIView): # pylint: disable=R0901
    """This class defines the create behavior of our rest api."""
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()
