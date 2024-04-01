from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from rest_framework.viewsets import ViewSet


from .models import Test, User, AttedanceList, ApprovedUser
from .serializers import TestSerializer, UserSerializer, AttendanceListSerializer, ApprovedUserSerializer

import json

def postView(request):
    test_objects = Test.objects.get(uuid = 1234)
    # data = list(test_objects.values())
    # # 가져온 객체를 순회하면서 작업할 수 있습니다.
    serializer = TestSerializer(test_objects)
    print(serializer.data)
    return JsonResponse((serializer.data), safe=False)

def postViewTest(request):
    user = User.objects.get(student_id = '2019037006')
    attendance_lists = AttedanceList.objects.filter(student_id=user)
    serializer = AttendanceListSerializer(attendance_lists, many=True)
    print(serializer.data)
    return JsonResponse(serializer.data, safe=False)
    

def sqlQuery(sql_query: str):
    with connection.cursor() as cursor:
        cursor.execute(sql_query)
    return cursor.fetchall()

class UserViewSet(ViewSet):
    user_tmp = User
    user_serial = UserSerializer
    def list(self, request):
        # GET 리소스 목록을 반환하는 구현
        all_users = self.user_tmp.objects.all()
        user_student_id_list = list()
        for user in all_users:
            user_student_id_list.append(user.student_id)
        user_student_id_dict = {'user_student_id': user_student_id_list}
        print(user_student_id_dict)
        return JsonResponse(json.dumps({"test":"test"}), safe = False)
        pass

    def create(self, request):
        # POST 새로운 리소스를 생성하는 구현
        pass

    def retrieve(self, request, pk=None):
        # GET 특정 ID의 리소스를 반환하는 구현
        print(request.path)
        print("[USER][RETREVE] : ", end = "")
        user = self.user_tmp.objects.get(student_id=pk)
        print(self.user_serial(user).data)
        return JsonResponse(json.dumps({"test":"retrieve"}), safe = False)
        pass

    def update(self, request, pk=None):
        # PUT 특정 ID의 리소스를 업데이트하는 구현
        pass

    def destroy(self, request, pk=None):
        # DELETE 특정 ID의 리소스를 삭제하는 구현
        pass
    
    
from rest_framework import viewsets, mixins

# class MultiModelCRUDViewSet(
#     mixins.ListModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.CreateModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     viewsets.GenericViewSet
# ):
#     queryset1 = User.objects.all()
#     queryset2 = ApprovedUser.objects.all()
    
#     serializer_class1 = UserSerializer
#     serializer_class2 = ApprovedUserSerializer

#     def get_queryset(self):
#         if self.action in ['list', 'retrieve', 'create', 'update', 'partial_update', 'destroy']:
#             if self.request.path.startswith('/TestApp/test/user/'):
#                 return self.queryset1
#             elif self.request.path.startswith('/TestApp/test/approveduser/'):
#                 return self.queryset2
#         return None

#     def get_serializer_class(self):
#         if self.action in ['list', 'retrieve', 'create', 'update', 'partial_update', 'destroy']:
#             if self.request.path.startswith('/TestApp/test/user/'):
#                 return self.serializer_class1
#             elif self.request.path.startswith('/TestApp/test/approveduser/'):
#                 return self.serializer_class2
#         return None
    
from rest_framework import generics, mixins
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import BasePermission
from django.db.models.query import QuerySet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import APIModelSerializer
from .models import APIModel

class APIModelGenericView(generics.ListCreateAPIView,
                        generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = APIModel.objects.all()
    serializer_class = APIModelSerializer
    
import subprocess

def backup_database():
    # 백업 파일 경로 지정
    backup_file_path = './backup.sql'
    user_name = 'cats'
    database_name = 'cats_db'
    # MySQL 백업 명령 실행
    command = f"mysqldump -u [{user_name}] -p [{database_name}] > {backup_file_path}"
    subprocess.run(command, shell=True)

backup_database()
print('backup_database')