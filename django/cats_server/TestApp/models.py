from django.db import models

# Create your models here.

class Test(models.Model):
    uuid = models.IntegerField()
    students_id = models.CharField(max_length = 10, primary_key=True)

class User(models.Model):
    student_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    fcm_token = models.CharField(max_length=100)
    birth_date = models.DateField()
    
class AttedanceList(models.Model):
    student_id = models.ForeignKey(User, related_name = "attedance_list", on_delete = models.CASCADE, primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    
class ApprovedUser(models.Model):
    student_id = models.ForeignKey(User, related_name = "approved_users", on_delete = models.CASCADE, primary_key=True)
    gender = models.CharField(max_length = 1)
    interest = models.TextField()
    kakao_id = models.CharField(max_length = 100)
    motivation = models.TextField()
    phone_number = models.CharField(max_length = 12)
    
    