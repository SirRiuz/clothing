

# Django
from django.urls import path


# Views
from .views import *



urlpatterns = [
    path('provider/',GetDataProvider.as_view()),
    path('provider-register/',Provider.as_view())
]
