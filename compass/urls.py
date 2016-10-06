"""
URLs dispatcher
"""

import logging
from django.conf.urls import url
from . import views

logger = logging.getLogger(__name__)

urlpatterns = [
    url(r'^$', views.HelloView.as_view(), name="index"),
]
