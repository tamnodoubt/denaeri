"""
url configurations for api app
"""

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateListDonorView

urlpatterns = {
    url(r'^donor/$', CreateListDonorView.as_view(), name="create"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
