from django.shortcuts import render
from django.http import JsonResponse, Http404
from rest_framework.viewsets import ViewSet

from .models import File
from .serializers import FileSerializer
# Create your views here.

class FileViewSet(ViewSet):
    
    def list(self, request):
        return JsonResponse(self.db_crud.listAll(request), safe = False)

    def create(self, request):
        file = request.FILES['file']
        print(FileSerializer(request.data).data)
        print(type(file))

    def retrieve(self, request, pk=None):
        res = self.db_crud.retrieve(request, pk)
        return JsonResponse(res['data'])

    def update(self, request, pk=None):
        res = self.db_crud.update(request, pk)
        return JsonResponse(res['data'])

    def destroy(self, request, pk=None):
        res = self.db_crud.destroy(request, pk)
        return JsonResponse(res['data'], safe = False)
