"""
url configurations for api app
"""

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateListDonorView
from .views import DonorView
from .views import CreateListOrganizationView


urlpatterns = {
    url(
        r'^donors/$',
        CreateListDonorView.as_view(),
        name="create_list_donor"
    ),
    url(
        r'^donor/(?P<primary_key>[0-9]+)/$',
        DonorView.as_view(),
        name="retrieve_update_delete_donor"
    ),
    url(
        r'organizations/$',
        CreateListOrganizationView.as_view(),
        name="create_list_organization"
    )
}

urlpatterns = format_suffix_patterns(urlpatterns)
