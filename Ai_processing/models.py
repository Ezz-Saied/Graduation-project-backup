from django.db import models

# Create your models here.

class Ai_feature(models.Model):
    name = models.CharField(max_length=100, choices=[
        ('SUPER_RESOLUTION', 'ruper resolution'),
        ('BASIC_FILTER', 'basic filter'),
        ('DE_NOISE', 'dE noise'),
        ('DE_BLUR', 'dE blur'),
        ('SHADOW_REMOVAL', 'Shadow removal'),
    ])
    
    description = models.TextField(blank=True, null=True)

    
    def __str__(self):
        return self.name