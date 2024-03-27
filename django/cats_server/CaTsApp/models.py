from django.db import models
from django.utils import timezone
from Api.models import User
from django.contrib.auth.hashers import make_password, check_password


import json
# Create your models here.

class UserProfile(models.Model):
    @staticmethod
    def name():
        return 'UserProfile'
    @staticmethod
    def pk_name():
        return 'StudentId'
    def set_password(self, raw_password):
        self.Password = make_password(raw_password)
    def check_password(self, raw_password):
        return check_password(raw_password, self.Password)
    StudentId = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    ProfileImgURL = models.URLField(max_length = 255, null = True)
    PreferredColor = models.CharField(max_length = 20, default = "#409932")
    TimeTableURL = models.URLField(max_length = 255, null = True)
    Password = models.CharField(max_length = 255)

class Posts(models.Model):
    @staticmethod
    def name():
        return 'Posts'
    @staticmethod
    def pk_name():
        return 'PostID'
    PostID = models.AutoField(primary_key=True)
    StudentId = models.ForeignKey(User, on_delete = models.CASCADE)
    Caption = models.TextField()
    ImgURL = models.URLField(max_length = 255, null = True)
    PostDate = models.DateTimeField(default=timezone.now)

class Comments(models.Model):
    @staticmethod
    def name():
        return 'Comments'
    @staticmethod
    def pk_name():
        return 'PostID'
    CommentID = models.AutoField(primary_key=True)
    PostID = models.ForeignKey(Posts, on_delete = models.CASCADE)
    StudentId = models.ForeignKey(User, on_delete = models.CASCADE)
    CommentText = models.TextField()
    CommentDate = models.DateTimeField(default=timezone.now)
    
class Likes(models.Model):
    @staticmethod
    def name():
        return 'Likes'
    @staticmethod
    def pk_name():
        return 'LikeID'
    LikeID = models.AutoField(primary_key=True)
    PostID = models.ForeignKey(Posts, on_delete = models.CASCADE)
    StudentId = models.ForeignKey(User, on_delete = models.CASCADE)

class CommentLikes(models.Model):
    @staticmethod
    def name():
        return 'CommentLikes'
    @staticmethod
    def pk_name():
        return 'CommentLikeID'
    CommentLikeID = models.AutoField(primary_key=True)
    CommentID = models.ForeignKey(Comments, on_delete = models.CASCADE)
    StudentId = models.ForeignKey(User, on_delete = models.CASCADE)

class Attendance(models.Model):
    @staticmethod
    def name():
        return 'Attendance'
    @staticmethod
    def pk_name():
        return 'CheckInDate'
    AttendanceID = models.AutoField(primary_key=True)
    StudentId = models.ForeignKey(User, on_delete = models.CASCADE)
    CheckInDate = models.DateField(default=timezone.now) 
    CheckInTime = models.TimeField(default=timezone.now)

# fcm 알림에 대한 로그 -> pushID (타이틀, 컨텐츠, 수신자 = json(studentsID : FCMToken), 송신자(학번) = fk, pk = auto)
class FCMLog(models.Model):
    @staticmethod
    def name():
        return 'FCMLog'
    @staticmethod
    def pk_name():
        return 'FcmLogID'
    FcmLogID = models.AutoField(primary_key=True)
    Title = models.TextField()
    Contents = models.TextField()
    Sender = models.ForeignKey(User, on_delete = models.CASCADE)
    Receiver = models.TextField()

# StockSteward -> (itemState:[대여중, 대여가능, 대여불가, 준비중], itemCategory = [책, 전자기기, 기타])
#   업데이트 할 때
class StockSteward(models.Model):
    ITEMSTATE_CHOICES = [
        ('OB', 'OnBorrow'),
        ('AFB', 'AvailableForBorrow'),
        ('NAFB', 'NotAvailableForBorrow')
    ]
    ITEMCATEGORY_CHOICES = [
        ('BOOK', 'Book'),
        ('ED', 'ElectronicDevice'),
        ('OI', 'OtherItems')
    ]
    @staticmethod
    def name():
        return 'StockSteward'
    @staticmethod
    def pk_name():
        return 'StockStewardID'
    StockStewardID = models.AutoField(primary_key=True)
    ItemState = models.CharField(max_length = 4, choices = ITEMSTATE_CHOICES)
    ItemCategory = models.CharField(max_length = 4, choices = ITEMCATEGORY_CHOICES)

"""
CREATE TABLE UserProfile (
    StudentId INT PRIMARY KEY,
    ProfileImgURL VARCHAR(255),
    PostsCount INT
    PreferredColor VARCHAR(20),
    TimeTable TEXT
    FOREIGN KEY (StudentId) REFERENCES Users(StudentId)
);

CREATE TABLE Posts (
    PostID INT PRIMARY KEY AUTO_INCREMENT,
    StudentId INT,
    Caption TEXT,
    ImgURL VARCHAR(255),
    PostDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (StudentId) REFERENCES Users(StudentId)
);

CREATE TABLE Comments (
    CommentID INT PRIMARY KEY AUTO_INCREMENT,
    PostID INT,
    StudentId INT,
    CommentText TEXT,
    CommentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (PostID) REFERENCES Posts(PostID),
    FOREIGN KEY (StudentId) REFERENCES Users(StudentId)
);

CREATE TABLE Likes (
    LikeID INT PRIMARY KEY AUTO_INCREMENT,
    PostID INT,
    StudentId INT,
    FOREIGN KEY (PostID) REFERENCES Posts(PostID),
    FOREIGN KEY (StudentId) REFERENCES Users(StudentId)
);

CREATE TABLE CommentLikes (
    CommentLikeID INT PRIMARY KEY AUTO_INCREMENT,
    CommentID INT,
    StudentId INT,
    FOREIGN KEY (CommentID) REFERENCES Comments(CommentID),
    FOREIGN KEY (StudentId) REFERENCES Users(StudentId)
);

-- 출근부 테이블
CREATE TABLE Attendance (
    AttendanceID INT PRIMARY KEY AUTO_INCREMENT,
    StudentId INT,
    CheckInTime DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (StudentId) REFERENCES Users(StudentId)
);
"""