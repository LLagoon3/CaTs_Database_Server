from django.db import models

# Create your models here.
class User(models.Model):
    student_id = models.CharField(max_length = 10, primary_key=True)
    name = models.CharField(max_length=10)
    fcm_token = models.CharField(max_length=200)
    birth_date = models.DateField()
    
class AttendanceList(models.Model):
    # id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(User, related_name = "attedance_list", on_delete = models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    
class ApprovedUser(models.Model):
    student_id = models.ForeignKey(User, related_name = "approved_users", on_delete = models.CASCADE, primary_key=True)
    gender = models.CharField(max_length = 1)
    interest = models.TextField()
    kakao_id = models.CharField(max_length = 100)
    motivation = models.TextField()
    phone_number = models.CharField(max_length = 12)