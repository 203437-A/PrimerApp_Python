
from django.db import models
from django.utils import timezone
# Create your models here.

class ImageModel(models.Model):
    name_img=  models.ImageField(blank="", default="", upload_to="img/")
    url_image= models.CharField(max_length=100)
    format_img= models.CharField(max_length=100) 
    created= models.DateTimeField(default=timezone.now)
    edited= models.DateTimeField(blank=True, null=True, default=None)
    