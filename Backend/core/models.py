from django.db import models
from django.contrib.auth.models import User

class UploadedImage(models.Model):
    #input_image = models.ForeignKey(UploadedImage, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)