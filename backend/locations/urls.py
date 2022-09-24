from django.urls import path
from locations.views import LocationView

urlpatterns = [
    path('locations/', LocationView.as_view(), name='locations')
]
