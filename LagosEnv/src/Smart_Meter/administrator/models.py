from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Userprofile(models.Model):
    avatar = CloudinaryField('avatar')
    about_me = models.CharField(max_length=255, null=True, blank=True)
