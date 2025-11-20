from django.db import models
from users.models import User

# Create your models here.
class User_History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='history')
    image_uploaded = models.ImageField(upload_to='user_history/')
    restored_image = models.ImageField(upload_to='user_history/restored/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"History of {self.user.email} at {self.created_at}"