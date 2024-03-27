from django.db import models

# Create your models here.
class User(models.Model):
    @staticmethod
    def name():
        return 'User'
    @staticmethod
    def pk_name():
        return 'StudentId'
    GENDER_CHOICES = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other')
    ]
    AUTH_CHOICES = [
        ('ADMIN', 'Admin'),
        ('USER', 'User'),
        ('NONE', 'None')
    ]
    StudentId = models.CharField(max_length = 10, primary_key=True)
    Username = models.CharField(max_length=255)
    Email = models.EmailField(max_length = 255, null = True)
    GitHubEmail = models.EmailField(max_length = 255, null = True)
    PhoneNumber = models.CharField(max_length = 20, null = True)
    Gender = models.CharField(max_length = 6, choices = GENDER_CHOICES, null = True)
    Birthday = models.DateField(null = True)
    Auth = models.CharField(max_length = 5, choices = AUTH_CHOICES)
    # password = models.CharField(max_length = 255)

class UserKakaoInfo(models.Model):
    @staticmethod
    def name():
        return 'UserKakaoInfo'
    @staticmethod
    def pk_name():
        return 'StudentId'
    StudentId = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    KakaoUID = models.CharField(max_length = 255)
    
class UserFCMToken(models.Model):
    @staticmethod
    def name():
        return 'UserFCMToken'
    @staticmethod
    def pk_name():
        return 'StudentId'
    StudentId = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    FCMToken = models.CharField(max_length = 255, null = True)
    



"""
CREATE TABLE Users (
    StudentId INT PRIMARY KEY AUTO_INCREMENT,
    Username VARCHAR(255) UNIQUE,
    Email VARCHAR(255) UNIQUE,
    GitHubEmail VARCHAR(255) UNIQUE,
    PhoneNumber VARCHAR(20) UNIQUE,
    Gender ENUM('Male', 'Female', 'Other'),
    Birthday DATE,
);

CREATE TABLE UserKakaoInfo (
    StudentId INT PRIMARY KEY,
    KakaoUID VARCHAR(255),
    FOREIGN KEY (StudentId) REFERENCES Users(StudentId)
);

CREATE TABLE UserFCMToken (
    StudentId INT PRIMARY KEY,
    FCMToken VARCHAR(255),
    FOREIGN KEY (StudentId) REFERENCES Users(StudentId)
);
"""