from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Countries"
        ordering = ['name']
    
    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='states')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
        unique_together = ['name', 'country']
    
    def __str__(self):
        return f"{self.name}, {self.country.name}"

class District(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='districts')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
        unique_together = ['name', 'state']
    
    def __str__(self):
        return f"{self.name}, {self.state.name}"

class Destination(models.Model):
    WEATHER_CHOICES = [
        ('tropical', 'Tropical'),
        ('dry', 'Dry'),
        ('temperate', 'Temperate'),
        ('continental', 'Continental'),
        ('polar', 'Polar'),
        ('mediterranean', 'Mediterranean'),
        ('subtropical', 'Subtropical'),
    ]
    
    place_name = models.CharField(max_length=200)
    weather = models.CharField(max_length=50, choices=WEATHER_CHOICES)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='destinations')
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='destinations')
    google_map_link = models.URLField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='destinations/', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='destinations')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.place_name