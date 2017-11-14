"""
url configurations for api app
"""

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateListDonorView
from .views import CreateListOrganizationView


urlpatterns = {
    url(r'^donor/$', CreateListDonorView.as_view(), name="create_list_donot"),
    url(r'organization/$', CreateListOrganizationView.as_view(), name="create_list_organization")
}

urlpatterns = format_suffix_patterns(urlpatterns)
