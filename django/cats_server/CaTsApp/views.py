from django.shortcuts import render
from django.http import JsonResponse, Http404
# from django.views import View
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
import json

from Api.views import DatabaseCRUD, CustomViewSet, custom_auto_schema_for_create_update, custom_auto_schema_for_list_retrieve_destroy
from . import models
from . import serializers



@csrf_exempt
@action(detail=True, methods=['post'])
def user_profile_login_viewset(request):
    request = json.loads(request.body.decode('utf-8'))
    serializer_class = serializers.UserProfileSerializer  # 시리얼라이저 클래스 지정
    print('UserProfileLoginViewSet')
    user = models.UserProfile.objects.get(StudentId=request['StudentId'])
    print(user)
    provided_password = request['Password']
    if user.check_password(provided_password):
        return JsonResponse(serializer_class(user).data)  # serializer_class 속성 사용
    else:
        return JsonResponse({'detail': '비밀번호 불일치'}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.UserProfileSerializer
    db_crud = DatabaseCRUD(models.UserProfile, serializer_class)

    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 200)
    def list(self, request):
        return JsonResponse(self.db_crud.listAll(request), safe = False)

    @custom_auto_schema_for_create_update(serializer_class, 200)
    def create(self, request):
        _serializers = serializers.UserProfileSerializer(data = request.data)
        _serializers.is_valid(raise_exception = True)
        _serializers.save()
        return JsonResponse(_serializers.data)
    
    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 200)
    def retrieve(self, request, pk=None):
        res = self.db_crud.retrieve(request, pk)
        return JsonResponse(res['data'])

    @custom_auto_schema_for_create_update(serializer_class, 200)
    def update(self, request, pk=None):
        res = self.db_crud.update(request, pk)
        return JsonResponse(res['data'])

    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 204)
    def destroy(self, request, pk=None):
        res = self.db_crud.destroy(request, pk)
        return JsonResponse(res['data'], safe = False)


class PostsViewSet(ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.PostsSerializer
    db_crud = DatabaseCRUD(models.Posts, serializer_class)
        
    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 200)
    def list(self, request):
        return JsonResponse(self.db_crud.listAll(request), safe = False)
    
    @custom_auto_schema_for_create_update(serializer_class, 201)
    def create(self, request):
        res = self.db_crud.create(request)
        return JsonResponse(res['data'], status = res['status'])
    
    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 200)
    def retrieve(self, request, pk=None):
        res = self.db_crud.retrieve(request, pk)
        return JsonResponse(res['data'])

    @custom_auto_schema_for_create_update(serializer_class, 200)
    def update(self, request, pk=None):
        res = self.db_crud.update(request, pk)
        return JsonResponse(res['data'])

    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 204)
    def destroy(self, request, pk=None):
        res = self.db_crud.destroy(request, pk)
        return JsonResponse(res['data'], safe = False)


class CommentsViewSet(ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.CommentsSerializer
    db_crud = DatabaseCRUD(models.Comments, serializer_class)
        
    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 200)
    def list(self, request):
        return JsonResponse(self.db_crud.listAll(request), safe = False)
    
    @custom_auto_schema_for_create_update(serializer_class, 201)
    def create(self, request):
        res = self.db_crud.create(request)
        return JsonResponse(res['data'], status = res['status'])
    
    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 200)
    def retrieve(self, request, pk=None):
        res = self.db_crud.retrieve(request, pk)
        return JsonResponse(res['data'])

    @custom_auto_schema_for_create_update(serializer_class, 200)
    def update(self, request, pk=None):
        res = self.db_crud.update(request, pk)
        return JsonResponse(res['data'])

    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 204)
    def destroy(self, request, pk=None):
        res = self.db_crud.destroy(request, pk)
        return JsonResponse(res['data'], safe = False)


class LikesViewSet(ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.LikesSerializer
    db_crud = DatabaseCRUD(models.Likes, serializer_class)
        
    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 200)
    def list(self, request):
        return JsonResponse(self.db_crud.listAll(request), safe = False)
    
    @custom_auto_schema_for_create_update(serializer_class, 201)
    def create(self, request):
        res = self.db_crud.create(request)
        return JsonResponse(res['data'], status = res['status'])
    
    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 200)
    def retrieve(self, request, pk=None):
        res = self.db_crud.retrieve(request, pk)
        return JsonResponse(res['data'])

    @custom_auto_schema_for_create_update(serializer_class, 200)
    def update(self, request, pk=None):
        res = self.db_crud.update(request, pk)
        return JsonResponse(res['data'])

    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 204)
    def destroy(self, request, pk=None):
        res = self.db_crud.destroy(request, pk)
        return JsonResponse(res['data'], safe = False)


class CommentLikesViewSet(ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.CommentLikesSerializer
    db_crud = DatabaseCRUD(models.CommentLikes, serializer_class)
        
    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 200)
    def list(self, request):
        return JsonResponse(self.db_crud.listAll(request), safe = False)
    
    @custom_auto_schema_for_create_update(serializer_class, 201)
    def create(self, request):
        res = self.db_crud.create(request)
        return JsonResponse(res['data'], status = res['status'])
    
    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 200)
    def retrieve(self, request, pk=None):
        res = self.db_crud.retrieve(request, pk)
        return JsonResponse(res['data'])

    @custom_auto_schema_for_create_update(serializer_class, 200)
    def update(self, request, pk=None):
        res = self.db_crud.update(request, pk)
        return JsonResponse(res['data'])

    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 204)
    def destroy(self, request, pk=None):
        res = self.db_crud.destroy(request, pk)
        return JsonResponse(res['data'], safe = False)
    
    
class AttendanceViewSet(ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.AttendanceSerializer
    db_crud = DatabaseCRUD(models.Attendance, serializer_class)
        
    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 200)
    def list(self, request):
        return JsonResponse(self.db_crud.listAll(request), safe = False)
    
    @custom_auto_schema_for_create_update(serializer_class, 201)
    def create(self, request):
        res = self.db_crud.create(request)
        return JsonResponse(res['data'], status = res['status'])
    
    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 200)
    def retrieve(self, request, pk=None):
        res = self.db_crud.retrieve(request, pk)
        return JsonResponse(res['data'])

    @custom_auto_schema_for_create_update(serializer_class, 200)
    def update(self, request, pk=None):
        res = self.db_crud.update(request, pk)
        return JsonResponse(res['data'])

    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 204)
    def destroy(self, request, pk=None):
        res = self.db_crud.destroy(request, pk)
        return JsonResponse(res['data'], safe = False)
    
    
class FCMLogViewSet(ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.FCMLogSerializer
    db_crud = DatabaseCRUD(models.FCMLog, serializer_class)
        
    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 200)
    def list(self, request):
        return JsonResponse(self.db_crud.listAll(request), safe = False)
    
    @custom_auto_schema_for_create_update(serializer_class, 201)
    def create(self, request):
        res = self.db_crud.create(request)
        return JsonResponse(res['data'], status = res['status'])
    
    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 200)
    def retrieve(self, request, pk=None):
        res = self.db_crud.retrieve(request, pk)
        return JsonResponse(res['data'])

    @custom_auto_schema_for_create_update(serializer_class, 200)
    def update(self, request, pk=None):
        res = self.db_crud.update(request, pk)
        return JsonResponse(res['data'])

    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 204)
    def destroy(self, request, pk=None):
        res = self.db_crud.destroy(request, pk)
        return JsonResponse(res['data'], safe = False)
    
    
class StockStewardViewSet(ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.StockStewardSerializer
    db_crud = DatabaseCRUD(models.StockSteward, serializer_class)
        
    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 200)
    def list(self, request):
        return JsonResponse(self.db_crud.listAll(request), safe = False)
    
    @custom_auto_schema_for_create_update(serializer_class, 201)
    def create(self, request):
        res = self.db_crud.create(request)
        return JsonResponse(res['data'], status = res['status'])
    
    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 200)
    def retrieve(self, request, pk=None):
        res = self.db_crud.retrieve(request, pk)
        return JsonResponse(res['data'])

    @custom_auto_schema_for_create_update(serializer_class, 200)
    def update(self, request, pk=None):
        res = self.db_crud.update(request, pk)
        return JsonResponse(res['data'])

    @custom_auto_schema_for_list_retrieve_destroy(serializer_class, 204)
    def destroy(self, request, pk=None):
        res = self.db_crud.destroy(request, pk)
        return JsonResponse(res['data'], safe = False)

    