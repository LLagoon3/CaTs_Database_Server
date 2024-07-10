from django.shortcuts import render
from django.http import JsonResponse, Http404

# from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ViewSet

from Api.views import (
    DatabaseCRUD,
    CustomViewSet,
    custom_auto_schema_for_create_update,
    custom_auto_schema_for_list_retrieve_destroy,
)
from . import models, serializers


class MemberViewSet(ViewSet):
    serializer_class = serializers.MemberSerializer
    db_crud = DatabaseCRUD(models.Member, serializer_class)

    # @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 200)
    def list(self, request):
        return JsonResponse(self.db_crud.listAll(request), safe=False)

    def create(self, request):
        res = self.db_crud.create(request)
        return JsonResponse(res["data"])

    def retrieve(self, request, pk=None):
        res = self.db_crud.retrieve(request, pk)
        return JsonResponse(res["data"])

    def update(self, request, pk=None):
        res = self.db_crud.update(request, pk)
        return JsonResponse(res["data"])

    def destroy(self, request, pk=None):
        res = self.db_crud.destroy(request, pk)
        return JsonResponse(res["data"], safe=False)
