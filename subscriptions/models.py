from django.db import models
from users.models import User


# Create your models here.
class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    plan = models.CharField(max_length=50, choices=[('FREE', 'Free'), ('PREMIUM', 'Premium')])
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    active = models.BooleanField(default=True)
    stripe_subscription_id = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.email} - {self.plan}"
