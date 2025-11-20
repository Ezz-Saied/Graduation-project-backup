from django.db import models
from django.db import models
from django.conf import settings

class UserImage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                             on_delete=models.CASCADE, 
                             related_name='images')
    image = models.ImageField(upload_to='user_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.email} - {self.id}"
