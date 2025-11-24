from django.urls import path
from . import views

urlpatterns = [
    # API Endpoints
    path('countries/', views.CountryListCreateAPIView.as_view(), name='country-list-api'),
    path('countries/<int:pk>/', views.CountryDetailAPIView.as_view(), name='country-detail-api'),
    
    path('states/', views.StateListCreateAPIView.as_view(), name='state-list-api'),
    path('states/<int:pk>/', views.StateDetailAPIView.as_view(), name='state-detail-api'),
    
    path('districts/', views.DistrictListCreateAPIView.as_view(), name='district-list-api'),
    path('districts/<int:pk>/', views.DistrictDetailAPIView.as_view(), name='district-detail-api'),
    
    path('api/destinations/', views.DestinationListCreateAPIView.as_view(), name='destination-list-api'),
    path('api/destinations/<int:pk>/', views.DestinationDetailAPIView.as_view(), name='destination-detail-api'),
    
    # Template Views
    path('list/', views.DestinationListView.as_view(), name='destination-list-view'),
    path('<int:pk>/', views.DestinationDetailView.as_view(), name='destination-detail-view'),
    path('create/', views.DestinationCreateView.as_view(), name='destination-create'),
    path('<int:pk>/update/', views.DestinationUpdateView.as_view(), name='destination-update'),
    path('<int:pk>/delete/', views.DestinationDeleteView.as_view(), name='destination-delete'),
]