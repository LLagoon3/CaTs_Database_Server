from rest_framework import serializers
from .models import Test, User, AttedanceList, ApprovedUser, APIModel

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['uuid', 'students_id']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['student_id', 'name', 'fcm_token', 'birth_date']

class AttendanceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttedanceList
        fields = ['student_id', 'date', 'time']

class ApprovedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovedUser
        fields = ['student_id', 'gender', 'interest', 'kakao_id', 'motivation', 'phone_number']

class APIModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIModel
        fields = '__all__'
