from django.shortcuts import render
from django.http import JsonResponse, Http404

from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import RestaurantInfo
from .serializers import RestaurantInfoSerializer
from Api.views import DatabaseCRUD, custom_auto_schema_for_create_update, custom_auto_schema_for_list_retrieve_destroy


# Create your views here.
class RestaurantInfoViewSet(ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = RestaurantInfoSerializer
    db_crud = DatabaseCRUD(RestaurantInfo, RestaurantInfoSerializer)
    
    @custom_auto_schema_for_create_update(serializer_class, 201)
    def create(self, request):
        res = self.db_crud.create(request)
        return JsonResponse(res['data'], status = res['status'])
    
    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 200)
    def retrieve(self, request, pk=None):
        restaurantInfoObj = RestaurantInfo.objects.filter(date=pk)
        serializer = RestaurantInfoSerializer(restaurantInfoObj, many=True)
        return JsonResponse(serializer.data, safe=False)
    
        