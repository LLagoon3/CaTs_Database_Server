from django.db import models

# Create your models here.
class File(models.Model):
    file = models.FileField(upload_to='uploads/')
    upload_datetime = models.DateTimeField()
    file_name = models.CharField(primary_key = True, max_length = 200)
