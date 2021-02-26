from django.urls import path
from .views import (
    ProviderListView, ProviderCreateView, ProviderDetailView, 
    ProviderUpdateView, ProviderDeleteView
)

app_name = 'providers'

urlpatterns = [
    path('', ProviderListView.as_view(), name='provider-list'),
    path('<int:pk>/', ProviderDetailView.as_view(), name='provider-detail'),
    path('<int:pk>/update/', ProviderUpdateView.as_view(), name='provider-update'),
    path('<int:pk>/delete/', ProviderDeleteView.as_view(), name='provider-delete'),
    path('create/', ProviderCreateView.as_view(), name='provider-create')
]