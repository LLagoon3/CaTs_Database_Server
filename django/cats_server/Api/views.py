from django.shortcuts import render
from django.http import JsonResponse, Http404
from django.db import connection

from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import User, UserKakaoInfo, UserFCMToken
from .serializers import UserSerializer, UserKakaoInfoSerializer, UserFCMTokenSerializer

from functools import wraps
import json

# Create your views here.


class DatabaseCRUD:
    def __init__(self, model, serializer) -> None:
        self.model_name = model.name()
        self.model = model
        self.serializer = serializer

    def list(self, request):
        # GET 리소스 목록을 반환하는 구현
        print("[{0}][LIST] : ".format(self.model_name), end="")
        all_objects = self.model.objects.all()
        objects_id_list = list()
        for user in all_objects:
            objects_id_list.append(getattr(user, self.model.pk_name()))
        pk_dict = {self.model.pk_name(): objects_id_list}
        print(pk_dict)
        return pk_dict

    def listQuery(self, query_params):
        # GET params로 전달된 리소스들을 반환하는 구현
        query_set, object_dict = self.model.objects.all(), dict()
        for field, val in query_params.items():
            filter_kwargs = {field: val}
            query_set = query_set.filter(**filter_kwargs)
        for object in query_set:
            serializer_data = self.serializer(object).data
            object_dict[serializer_data[self.model.pk_name()]] = serializer_data
        return object_dict

    def listAll(self, request):
        # GET params이 없을 경우 테이블 전체 반환하는 구현
        if not request.query_params == {}:
            return self.listQuery(request.query_params)
        all_objects = self.model.objects.all()
        objects_dict = dict()
        for object in all_objects:
            serializer_data = self.serializer(object).data
            objects_dict[serializer_data[self.model.pk_name()]] = serializer_data
        return objects_dict

    def create(self, request):
        # POST 새로운 리소스를 생성하는 구현
        print("[{0}][CREATE] : ".format(self.model_name), end="")
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return {"data": serializer.data, "status": status.HTTP_201_CREATED}
        print(serializer.errors)
        return {"data": serializer.errors, "status": status.HTTP_400_BAD_REQUEST}

    def retrieve(self, request, pk=None):
        # GET 특정 ID의 리소스를 반환하는 구현
        print("[{0}][RETREVE] : ".format(self.model_name), end="")
        try:
            pk_kwargs = {self.model.pk_name(): pk}
            instance = self.model.objects.get(**pk_kwargs)
        except self.model.DoesNotExist:
            raise Http404("Object does not exist")
        print(self.serializer(instance).data)
        return {"data": self.serializer(instance).data}

    def update(self, request, pk=None):
        # PUT 특정 ID의 리소스를 업데이트하는 구현
        print("[{0}][UPDATE] : ".format(self.model_name), end="")
        try:
            pk_kwargs = {self.model.pk_name(): pk}
            instance = self.model.objects.get(**pk_kwargs)
        except self.model.DoesNotExist:
            raise Http404("Object does not exist")
        serializer = self.serializer(instance, request.data)
        if serializer.is_valid():
            print(self.serializer(instance).data)
            serializer.save()
            return {"data": self.serializer(instance).data}
        else:
            print(serializer.errors)
            return {"data": serializer.errors}

    def destroy(self, request, pk=None):
        # DELETE 특정 ID의 리소스를 삭제하는 구현
        print("[{0}][DELETE] : ".format(self.model_name), end="")
        try:
            pk_kwargs = {self.model.pk_name(): pk}
            instance = self.model.objects.get(**pk_kwargs)
        except self.model.DoesNotExist:
            raise Http404("Object does not exist")
        print(self.serializer(instance).data)
        instance.delete()
        return {"data": self.serializer(instance).data}


class CustomViewSet:

    def __init__(self, serializer):
        serializer = serializer

    def list(self, request):
        return JsonResponse(self.db_crud.listAll(request), safe=False)

    def create(self, request):
        res = self.db_crud.create(request)
        return JsonResponse(res["data"], status=res["status"])

    def retrieve(self, request, pk=None):
        res = self.db_crud.retrieve(request, pk)
        return JsonResponse(res["data"])

    def update(self, request, pk=None):
        res = self.db_crud.update(request, pk)
        return JsonResponse(res["data"])

    def destroy(self, request, pk=None):
        res = self.db_crud.destroy(request, pk)
        return JsonResponse(res["data"], safe=False)


def custom_auto_schema_for_list_retrieve_destroy(serializer_class, status_code):
    def decorator(func):
        @swagger_auto_schema(
            manual_parameters=[
                openapi.Parameter(
                    "Authorization",
                    openapi.IN_HEADER,
                    description='JWT Access Token ( Use "Bearer" Keyword )',
                    type=openapi.TYPE_STRING,
                ),
            ],
            responses={status_code: serializer_class},
        )
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator


def custom_auto_schema_for_create_update(serializer_class, status_code):
    def decorator(func):
        @swagger_auto_schema(
            manual_parameters=[
                openapi.Parameter(
                    "Authorization",
                    openapi.IN_HEADER,
                    description='JWT Access Token ( Use "Bearer" Keyword )',
                    type=openapi.TYPE_STRING,
                ),
            ],
            query_serializer=serializer_class,
            responses={status_code: serializer_class},
        )
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator


class UserViewSet(ViewSet, CustomViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    db_crud = DatabaseCRUD(User, serializer_class)
    testdeco = staticmethod(
        custom_auto_schema_for_list_retrieve_destroy(serializer_class, 200)
    )

    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 200)
    def list(self, request):
        return JsonResponse(self.db_crud.listAll(request), safe=False)

    @custom_auto_schema_for_create_update(serializer_class, 201)
    def create(self, request):
        res = self.db_crud.create(request)
        return JsonResponse(res["data"], status=res["status"])

    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 200)
    def retrieve(self, request, pk=None):
        res = self.db_crud.retrieve(request, pk)
        return JsonResponse(res["data"])

    @custom_auto_schema_for_create_update(serializer_class, 200)
    def update(self, request, pk=None):
        res = self.db_crud.update(request, pk)
        return JsonResponse(res["data"])

    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 204)
    def destroy(self, request, pk=None):
        res = self.db_crud.destroy(request, pk)
        return JsonResponse(res["data"], safe=False)


class UserKakaoInfoViewSet(ViewSet, CustomViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserKakaoInfoSerializer
    db_crud = DatabaseCRUD(UserKakaoInfo, serializer_class)

    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 200)
    def list(self, request):
        return JsonResponse(self.db_crud.listAll(request), safe=False)

    @custom_auto_schema_for_create_update(serializer_class, 201)
    def create(self, request):
        res = self.db_crud.create(request)
        return JsonResponse(res["data"], status=res["status"])

    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 200)
    def retrieve(self, request, pk=None):
        res = self.db_crud.retrieve(request, pk)
        return JsonResponse(res["data"])

    @custom_auto_schema_for_create_update(serializer_class, 200)
    def update(self, request, pk=None):
        res = self.db_crud.update(request, pk)
        return JsonResponse(res["data"])

    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 204)
    def destroy(self, request, pk=None):
        res = self.db_crud.destroy(request, pk)
        return JsonResponse(res["data"], safe=False)


class UserFCMTokenViewSet(ViewSet, CustomViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserFCMTokenSerializer
    db_crud = DatabaseCRUD(UserFCMToken, serializer_class)

    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 200)
    def list(self, request):
        return JsonResponse(self.db_crud.listAll(request), safe=False)

    @custom_auto_schema_for_create_update(serializer_class, 201)
    def create(self, request):
        res = self.db_crud.create(request)
        return JsonResponse(res["data"], status=res["status"])

    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 200)
    def retrieve(self, request, pk=None):
        res = self.db_crud.retrieve(request, pk)
        return JsonResponse(res["data"])

    @custom_auto_schema_for_create_update(serializer_class, 200)
    def update(self, request, pk=None):
        res = self.db_crud.update(request, pk)
        return JsonResponse(res["data"])

    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 204)
    def destroy(self, request, pk=None):
        res = self.db_crud.destroy(request, pk)
        return JsonResponse(res["data"], safe=False)
