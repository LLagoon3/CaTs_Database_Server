"""cats_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('userprofile', views.UserProfileViewSet, basename='userprofile')
router.register('posts', views.PostsViewSet, basename='posts')
router.register('comments', views.CommentsViewSet, basename='comments')
router.register('likes', views.LikesViewSet, basename='likes')
router.register('commentlikes', views.CommentLikesViewSet, basename='commentlikes')
router.register('attendance', views.AttendanceViewSet, basename='attendance')
router.register('fcmlog', views.FCMLogViewSet, basename='fcmlog')
router.register('stocksteward', views.StockStewardViewSet, basename='stocksteward')
# router.register('userprofilelogin', views.UserProfileLoginViewSet, basename='userprofilelogin')


urlpatterns = [
    path('', include(router.urls)),
    path('userprofilelogin/', views.user_profile_login_viewset),
]
