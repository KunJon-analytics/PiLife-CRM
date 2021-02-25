from django.urls import path
from .views import ProviderListView

app_name = 'providers'

urlpatterns = [
    path('', ProviderListView.as_view(), name='providers')
]