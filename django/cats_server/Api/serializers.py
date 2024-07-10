from rest_framework import serializers
from .models import User, UserKakaoInfo, UserFCMToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserKakaoInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserKakaoInfo
        fields = '__all__'

class UserFCMTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFCMToken
        fields = '__all__'




# class UserJWTSignupSerializer(serializers.ModelSerializer):
#     id = serializers.CharField(
#         required=True,
#         write_only=True,
#         max_length=20
#     )
#     password = serializers.CharField(
#         required=True,
#         write_only=True,
#         style={'input_type': 'password'}
#     )
#     class Meta(object):
#         model = User
#         fields = ['id', 'password']

#     def save(self, request):
#         user = super().save()
#         user.id = self.validated_data['id']
#         user.set_password(self.validated_data['password'])
#         user.save()
#         return user

#     def validate(self, data):
#         id = data.get('id', None)

#         if User.objects.filter(id=id).exists():
#             raise serializers.ValidationError("user already exists")

#         return data
    

# from rest_framework_simplejwt.tokens import RefreshToken

# class JWTLoginSerializer(serializers.ModelSerializer):
#     id = serializers.CharField(
#         required=True,
#         write_only=True,
#     )
#     password = serializers.CharField(
#         required=True,
#         write_only=True,
#         style={'input_type': 'password'}
#     )
#     class Meta(object):
#         model = User
#         fields = '__all__'
    
#     def validate(self, data):
#         id = data.get('id', None)
#         password = data.get('password', None)
#         if User.objects.filter(id=id).exists():
#             user = User.objects.get(id=id)
#             if not user.check_password(password):
#                 raise serializers.ValidationError("wrong password")
#         else:
#             raise serializers.ValidationError("user account not exist")
#         token = RefreshToken.for_user(user)
#         refresh = str(token)
#         access = str(token.access_token)
#         data = {
#             'user': user,
#             'refresh': refresh,
#             'access': access,
#         }
#         return data