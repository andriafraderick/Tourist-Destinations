from rest_framework import serializers
from .models import Country, State, District, Destination
from django.contrib.auth.models import User

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'created_at']
        read_only_fields = ['created_at']

class StateSerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source='country.name', read_only=True)
    
    class Meta:
        model = State
        fields = ['id', 'name', 'country', 'country_name', 'created_at']
        read_only_fields = ['created_at']

class DistrictSerializer(serializers.ModelSerializer):
    state_name = serializers.CharField(source='state.name', read_only=True)
    country_name = serializers.CharField(source='state.country.name', read_only=True)
    
    class Meta:
        model = District
        fields = ['id', 'name', 'state', 'state_name', 'country_name', 'created_at']
        read_only_fields = ['created_at']

class DestinationListSerializer(serializers.ModelSerializer):
    state_name = serializers.CharField(source='state.name', read_only=True)
    district_name = serializers.CharField(source='district.name', read_only=True)
    country_name = serializers.CharField(source='state.country.name', read_only=True)
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)
    
    class Meta:
        model = Destination
        fields = [
            'id', 'place_name', 'weather', 'state', 'state_name', 
            'district', 'district_name', 'country_name', 'google_map_link',
            'description', 'image', 'created_by', 'created_by_username',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_by', 'created_at', 'updated_at']

class DestinationDetailSerializer(serializers.ModelSerializer):
    state_name = serializers.CharField(source='state.name', read_only=True)
    district_name = serializers.CharField(source='district.name', read_only=True)
    country_name = serializers.CharField(source='state.country.name', read_only=True)
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)
    state_obj = StateSerializer(source='state', read_only=True)
    district_obj = DistrictSerializer(source='district', read_only=True)
    
    class Meta:
        model = Destination
        fields = [
            'id', 'place_name', 'weather', 'state', 'state_name', 'state_obj',
            'district', 'district_name', 'district_obj', 'country_name',
            'google_map_link', 'description', 'image', 'created_by',
            'created_by_username', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_by', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']