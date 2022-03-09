from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class ProfileModel(models.Model):
    name_img=  models.ImageField(blank="", default="", upload_to="profile_img")
    id_user= models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)

    