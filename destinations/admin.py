from django.contrib import admin
from .models import Country, State, District, Destination

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    ordering = ['name']

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'created_at']
    list_filter = ['country']
    search_fields = ['name', 'country__name']
    ordering = ['country', 'name']

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name', 'state', 'get_country', 'created_at']
    list_filter = ['state__country', 'state']
    search_fields = ['name', 'state__name', 'state__country__name']
    ordering = ['state', 'name']
    
    def get_country(self, obj):
        return obj.state.country.name
    get_country.short_description = 'Country'

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['place_name', 'weather', 'district', 'state', 'created_by', 'created_at']
    list_filter = ['weather', 'state__country', 'state', 'created_at']
    search_fields = ['place_name', 'description', 'district__name', 'state__name']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('place_name', 'weather', 'description', 'image')
        }),
        ('Location', {
            'fields': ('state', 'district', 'google_map_link')
        }),
        ('Metadata', {
            'fields': ('created_by', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )