from rest_framework import serializers
from .models import User, AttendanceList, ApprovedUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['student_id', 'name', 'fcm_token', 'birth_date']

class AttendanceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceList
        fields = ['id', 'student_id', 'date', 'time']

class ApprovedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovedUser
        fields = ['student_id', 'gender', 'interest', 'kakao_id', 'motivation', 'phone_number']

