"""
URLs dispatcher
"""

import logging
from django.urls import path
from . import views

logger = logging.getLogger(__name__)

urlpatterns = [
    path('', views.HelloView.as_view(), name="index"),
]
