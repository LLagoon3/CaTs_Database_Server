from rest_framework import serializers
from .models import RestaurantInfo

class RestaurantInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantInfo
        fields = '__all__'