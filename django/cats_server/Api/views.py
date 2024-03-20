from django.shortcuts import render
from django.http import JsonResponse, Http404
from django.db import connection
from rest_framework.viewsets import ViewSet
from rest_framework import status

from .models import User, AttendanceList, ApprovedUser
from .serializers import UserSerializer, AttendanceListSerializer, ApprovedUserSerializer

import json

# Create your views here.
    
class DatabaseCRUD():
    def __init__(self, model_name: str) -> None:
        self.model_name = model_name
        if model_name == 'User':
            self.model = User
            self.serializer = UserSerializer
        elif model_name == 'AttedanceList':
            self.model = AttendanceList
            self.serializer = AttendanceListSerializer
        elif model_name == 'ApprovedUser':
            self.model = ApprovedUser
            self.serializer = ApprovedUserSerializer
        else:
            return {'data': 'Model does not exist'}
        
    def list(self, request):
        # GET 리소스 목록을 반환하는 구현
        print("[{0}][LIST] : ".format(self.model_name), end = "")
        all_objects = self.model.objects.all()
        objects_id_list = list()
        for user in all_objects:
            objects_id_list.append(user.student_id)
        user_student_id_dict = {'user_student_id': objects_id_list}
        print(user_student_id_dict)
        return user_student_id_dict

    def listAll(self, request):
        all_objects = self.model.objects.all()
        objects_dict = dict()
        for object in all_objects:
            serializer_data = self.serializer(object).data
            objects_dict[serializer_data['student_id']] = serializer_data
        return objects_dict

    def create(self, request):
        # POST 새로운 리소스를 생성하는 구현
        print("[{0}][CREATE] : ".format(self.model_name), end = "")
        serializer = self.serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return {'data': serializer.data, 
                    'status': status.HTTP_201_CREATED}
        print(serializer.errors)
        return {'data': serializer.errors, 
                'status': status.HTTP_400_BAD_REQUEST}

    def retrieve(self, request, pk=None):
        # GET 특정 ID의 리소스를 반환하는 구현
        print("[{0}][RETREVE] : ".format(self.model_name), end = "")
        try:
            instance = self.model.objects.get(student_id=pk)
        except self.model.DoesNotExist:
            raise Http404("User does not exist")
        print(self.serializer(instance).data)
        return {'data': self.serializer(instance).data}

    def update(self, request, pk=None):
        # PUT 특정 ID의 리소스를 업데이트하는 구현
        print("[{0}][UPDATE] : ".format(self.model_name), end = "")
        try:
            instance = self.model.objects.get(student_id=pk)
        except self.model.DoesNotExist:
            raise Http404("User does not exist")
        serializer = self.serializer(instance, request.data)
        if serializer.is_valid():
            print(self.serializer(instance).data)
            serializer.save()
            return {'data': self.serializer(instance).data}
        else:
            print(serializer.errors)
            return {'data': serializer.errors}
            
    def destroy(self, request, pk=None):
        # DELETE 특정 ID의 리소스를 삭제하는 구현
        print("[{0}][DELETE] : ".format(self.model_name), end = "")
        try:
            instance = self.model.objects.get(student_id=pk)
        except self.model.DoesNotExist:
            raise Http404("User does not exist")
        print(self.serializer(instance).data)
        instance.delete()
        return {'data': self.serializer(instance).data}
        

class UserViewSet(ViewSet):
    db_crud = DatabaseCRUD('User')
        
    def list(self, request):
        return JsonResponse(self.db_crud.listAll(request), safe = False)

    def create(self, request):
        res = self.db_crud.create(request)
        return JsonResponse(res['data'], status = res['status'])

    def retrieve(self, request, pk=None):
        res = self.db_crud.retrieve(request, pk)
        return JsonResponse(res['data'])

    def update(self, request, pk=None):
        res = self.db_crud.update(request, pk)
        return JsonResponse(res['data'])

    def destroy(self, request, pk=None):
        res = self.db_crud.destroy(request, pk)
        return JsonResponse(res['data'], safe = False)
    

class AttendanceListViewSet(ViewSet):
    db_crud = DatabaseCRUD('AttedanceList')
        
    def list(self, request):
        return JsonResponse(self.db_crud.list(request), safe = False)

    def create(self, request):
        res = self.db_crud.create(request)
        return JsonResponse(res['data'], status = res['status'])

    def retrieve(self, request, pk=None):
        res = self.db_crud.retrieve(request, pk)
        return JsonResponse(res['data'])

    def update(self, request, pk=None):
        res = self.db_crud.update(request, pk)
        return JsonResponse(res['data'])

    def destroy(self, request, pk=None):
        res = self.db_crud.destroy(request, pk)
        return JsonResponse(res['data'], safe = False)
    

class ApprovedUserViewSet(ViewSet):
    db_crud = DatabaseCRUD('ApprovedUser')
        
    def list(self, request):
        return JsonResponse(self.db_crud.list(request), safe = False)

    def create(self, request):
        res = self.db_crud.create(request)
        return JsonResponse(res['data'], status = res['status'])

    def retrieve(self, request, pk=None):
        res = self.db_crud.retrieve(request, pk)
        return JsonResponse(res['data'])

    def update(self, request, pk=None):
        res = self.db_crud.update(request, pk)
        return JsonResponse(res['data'])

    def destroy(self, request, pk=None):
        res = self.db_crud.destroy(request, pk)
        return JsonResponse(res['data'], safe = False)