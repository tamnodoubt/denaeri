"""
View for Donor
"""

from rest_framework import generics
from ..serializers import DonorSerializer
from ..models import Donor

class CreateListDonorView(generics.ListCreateAPIView): # pylint: disable=R0901
    """Defines create a list behavior for Donor"""
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer

class DonorView(generics.RetrieveUpdateDestroyAPIView): # pylint: disable=R0901
    """Defines get behavior for a single Donor"""
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer
