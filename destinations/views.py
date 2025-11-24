from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Country, State, District, Destination
from .serializers import (
    CountrySerializer, StateSerializer, DistrictSerializer,
    DestinationListSerializer, DestinationDetailSerializer
)

# API Views
class CountryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'created_at']

class CountryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class StateListCreateAPIView(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['country']
    search_fields = ['name', 'country__name']
    ordering_fields = ['name', 'created_at']

class StateDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class DistrictListCreateAPIView(generics.ListCreateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['state', 'state__country']
    search_fields = ['name', 'state__name', 'state__country__name']
    ordering_fields = ['name', 'created_at']

class DistrictDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class DestinationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['weather', 'state', 'district', 'state__country']
    search_fields = ['place_name', 'description', 'state__name', 'district__name']
    ordering_fields = ['place_name', 'created_at', 'updated_at']
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class DestinationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Template Views
class DestinationListView(ListView):
    model = Destination
    template_name = 'destinations/destination_list.html'
    context_object_name = 'destinations'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        weather = self.request.GET.get('weather')
        country = self.request.GET.get('country')
        state = self.request.GET.get('state')
        
        if search:
            queryset = queryset.filter(place_name__icontains=search) | \
                       queryset.filter(description__icontains=search)
        if weather:
            queryset = queryset.filter(weather=weather)
        if country:
            queryset = queryset.filter(state__country_id=country)
        if state:
            queryset = queryset.filter(state_id=state)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countries'] = Country.objects.all()
        context['states'] = State.objects.all()
        context['weather_choices'] = Destination.WEATHER_CHOICES
        context['search'] = self.request.GET.get('search', '')
        return context

class DestinationDetailView(DetailView):
    model = Destination
    template_name = 'destinations/destination_detail.html'
    context_object_name = 'destination'

class DestinationCreateView(LoginRequiredMixin, CreateView):
    model = Destination
    template_name = 'destinations/destination_form.html'
    fields = ['place_name', 'weather', 'state', 'district', 'google_map_link', 'description', 'image']
    success_url = reverse_lazy('destination-list-view')
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countries'] = Country.objects.all()
        return context

class DestinationUpdateView(LoginRequiredMixin, UpdateView):
    model = Destination
    template_name = 'destinations/destination_form.html'
    fields = ['place_name', 'weather', 'state', 'district', 'google_map_link', 'description', 'image']
    success_url = reverse_lazy('destination-list-view')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countries'] = Country.objects.all()
        context['is_update'] = True
        return context

class DestinationDeleteView(LoginRequiredMixin, DeleteView):
    model = Destination
    template_name = 'destinations/destination_confirm_delete.html'
    success_url = reverse_lazy('destination-list-view')