"""
Create List View for Organization
"""

from rest_framework.generics import ListCreateAPIView
from ..serializers import OrganizationSerializer
from ..models import Organization

class CreateListOrganizationView(ListCreateAPIView): # pylint: disable=R0901
    """This class defines the create and list behavior of organization model."""
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def perform_create(self, serializer): # stam: not sure this is needed
        """Save the post data when creating a new organization."""
        serializer.save()
