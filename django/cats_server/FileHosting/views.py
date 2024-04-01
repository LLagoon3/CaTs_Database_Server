from django.shortcuts import render
from django.http import JsonResponse, Http404
from rest_framework.viewsets import ViewSet

from .models import File, dynamic_upload_path
from .serializers import FileSerializer
from Api.views import DatabaseCRUD, custom_auto_schema_for_create_update, custom_auto_schema_for_list_retrieve_destroy


from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.

class FileViewSet(ViewSet):
    serializer_class = FileSerializer
    db_crud = DatabaseCRUD(File, serializer_class)
    
    def chk_upload_path(self, upload_path, filename):
        if upload_path[-1] == '/': upload_path = upload_path[:-1]
        else: upload_path = upload_path
        return f"{upload_path}/{filename}"
    
    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 200)
    def list(self, request):
        return JsonResponse(self.db_crud.listAll(request), safe = False)
    
    @swagger_auto_schema(
        manual_parameters=[
                    openapi.Parameter('Authorization', openapi.IN_HEADER, description="JWT Access Token ( Use \"Bearer\" Keyword )", type=openapi.TYPE_STRING),
                ],
        responses={200: serializer_class},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'file': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    format=openapi.FORMAT_BINARY
                )
            }
        )
    )
    def create(self, request):
        data =  request.data
        if 'upload_path' not in data.keys(): data['file_name'] = f"{request.FILES['file'].name}"
        else: data['file_name'] = self.chk_upload_path(data['upload_path'], request.FILES['file'].name)
        print(request.data)
        serializer = self.serializer_class(data = data)
        if serializer.is_valid():
            instance = serializer.save()
            instance.file = dynamic_upload_path(instance, data["file_name"])
            return JsonResponse({'detail': 'success'})
        return JsonResponse({"test": serializer.errors})

            

    # def retrieve(self, request, pk=None):
    #     res = self.db_crud.retrieve(request, pk)
    #     return JsonResponse(res['data'])

    # def update(self, request, pk=None):
    #     res = self.db_crud.update(request, pk)
    #     return JsonResponse(res['data'])

    # def destroy(self, request, pk=None):
    #     res = self.db_crud.destroy(request, pk)
    #     return JsonResponse(res['data'], safe = False)
