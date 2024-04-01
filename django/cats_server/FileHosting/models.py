from django.db import models
from django.utils import timezone
from Api.models import User

def dynamic_upload_path(instance, filename):
    print('filename : ', f"user_{filename}")
    # if instance.upload_path is None: return f"{filename}"
    # elif instance.upload_path[-1] == '/': upload_path = instance.upload_path[:-1]
    # else: upload_path = instance.upload_path
    # return f"{upload_path}/{filename}"
    return f"{instance.file_name}"

# Create your models here. 
class File(models.Model):
    @staticmethod
    def name(): 
        return "File"
    def pk_name():
        return 'file_name'
    file_name = models.CharField(primary_key = True, max_length = 200)
    file = models.FileField(upload_to=dynamic_upload_path)
    upload_user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    upload_datetime = models.DateTimeField(default=timezone.now)
    upload_path = models.TextField(null = True)