from rest_framework import serializers
from .models import UserProfile, Posts, Comments, Likes, CommentLikes, Attendance, FCMLog, StockSteward

class UserProfileSerializer(serializers.ModelSerializer):
    # Password = serializers.CharField(write_only=True)
    class Meta:
        model = UserProfile
        fields = ['StudentId', 'ProfileImgURL', 'PreferredColor', 'TimeTableURL', 'Password']
    def create(self, vaild_data):
        Password = vaild_data.pop('Password', None)
        instance = self.Meta.model(**vaild_data)
        if Password is not None:
            instance.set_password(Password)
        instance.save()
        return instance

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = '__all__'
        
class CommentLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLikes
        fields = '__all__'
        
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class FCMLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = FCMLog
        fields = '__all__'
        
class StockStewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockSteward
        fields = '__all__'